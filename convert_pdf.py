import os
import time
from pathlib import Path
from google import genai
from pypdf import PdfReader, PdfWriter

# ==========================================
# 1. 初期設定
# ==========================================
# 取得したAPIキーをここに設定してください
API_KEY = "AQ.Ab8RN6J9fGvXDWfiTCQtROgiUNAg7qErL2MsFeTOfM-2OdPQSA"

# 変換したい巨大なPDFのファイルパス
TARGET_PDF = "./pdf_files/今日からスタート高校入試_数学.pdf" 
OUTPUT_MD = "./md_files/your_book_converted.md"

# 何ページごとに分割して処理するか（15〜20推奨）
CHUNK_SIZE = 15  

PROMPT = """
このPDF教材の内容を読み取り、整形されたMarkdown形式で出力してください。
以下のルールに従ってください：
1. 見出し、箇条書き、表などの構造を維持する。
2. 不要なヘッダー、フッター、ページ番号は除外する。
3. 数式がある場合はLaTeX形式（$ または $$）を使用する。
4. Markdownのテキストのみを出力し、挨拶や解説は含めない。
"""

def split_and_convert():
    client = genai.Client(api_key=API_KEY)
    
    # フォルダ準備
    os.makedirs("./pdf_files", exist_ok=True)
    os.makedirs("./md_files", exist_ok=True)
    os.makedirs("./temp_chunks", exist_ok=True) # 分割作業用の一時フォルダ

    if not os.path.exists(TARGET_PDF):
        print(f"エラー: {TARGET_PDF} が見つかりません。")
        return

    # 1. PDFの読み込み
    reader = PdfReader(TARGET_PDF)
    total_pages = len(reader.pages)
    print(f"合計 {total_pages} ページのPDFを処理します。")

    # 既存の出力ファイルがあればリセット
    # with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    #     f.write(f"# 変換結果 ({TARGET_PDF})\n\n")

    # 2. 指定ページ数ごとに分割してループ処理
    for start_page in range(195, total_pages, CHUNK_SIZE):
        end_page = min(start_page + CHUNK_SIZE, total_pages)
        chunk_index = (start_page // CHUNK_SIZE) + 1
        total_chunks = (total_pages + CHUNK_SIZE - 1) // CHUNK_SIZE

        print(f"\n--- [チャンク {chunk_index}/{total_chunks}] {start_page + 1}〜{end_page}ページ目を処理中 ---")

        # 分割したPDFを一時ファイルとして保存
        writer = PdfWriter()
        for i in range(start_page, end_page):
            writer.add_page(reader.pages[i])
        
        temp_pdf_path = f"./temp_chunks/chunk_{chunk_index}.pdf"
        with open(temp_pdf_path, "wb") as f:
            writer.write(f)

        try:
            # ① 分割したPDFをアップロード
            print("  -> Geminiへファイルをアップロード中...")
            uploaded_file = client.files.upload(file=temp_pdf_path)

            # ② Markdownへ変換
            print("  -> AIがMarkdownへ変換中...")
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=[uploaded_file, PROMPT]
            )

            # ③ 結果をメインのMarkdownファイルに「追記 (append)」
            with open(OUTPUT_MD, "a", encoding="utf-8") as f:
                f.write(f"<!-- {start_page + 1}〜{end_page}ページ -->\n")
                f.write(response.text)
                f.write("\n\n---\n\n")
            print(f"  -> ✅ 結合ファイルに書き込みました。")

            # ④ サーバー上のファイルを削除
            client.files.delete(name=uploaded_file.name)

        except Exception as e:
            print(f"  -> ❌ エラーが発生しました: {e}")

        # ⑤ 一時的に作ったローカルの分割PDFも削除
        os.remove(temp_pdf_path)

        # API制限（無料枠）を避けるため待機
        if end_page < total_pages:
            wait_time = 30
            print(f"  -> ⏳ API制限回避のため、{wait_time}秒待機します...")
            time.sleep(wait_time)

    print(f"\n🎉 すべての処理が完了しました！\n確認先: {OUTPUT_MD}")

if __name__ == "__main__":
    split_and_convert()