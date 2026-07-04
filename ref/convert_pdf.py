import os
import sys
import time
import argparse  # ← これが必須です！
from pathlib import Path
from google import genai
from pypdf import PdfReader, PdfWriter

# ==========================================
# 1. 初期設定
# ==========================================
# 取得したAPIキーをここに設定してください
API_KEY = "AQ.Ab8RN6J9fGvXDWfiTCQtROgiUNAg7qErL2MsFeTOfM-2OdPQSA"
CHUNK_SIZE = 15  
MAX_RETRIES = 5  

PROMPT = """
このPDF教材の内容を読み取り、整形されたMarkdown形式で出力してください。
以下のルールに従ってください：
1. 見出し、箇条書き、表などの構造を維持する。
2. 不要なヘッダー、フッター、ページ番号は除外する。
3. 数式がある場合はLaTeX形式（$ または $$）を使用する。
4. Markdownのテキストのみを出力し、挨拶や解説は含めない。
"""

def main():
    # ----------------------------------------
    # 1. コマンドライン引数の設定
    # ----------------------------------------
    # ↓ 【削除】この行があるとエラーになるので消してください！
    # parser = argparse.add_argument_group("PDF to Markdown Converter")
    
    # ↓ この行からスタートするようにしてください
    parser = argparse.ArgumentParser(description="PDFを指定ページごとに分割してGeminiでMarkdownに変換します。")
    
    parser.add_argument("input_pdf", help="変換したいPDFファイルのパス")
    parser.add_argument("-o", "--output", help="出力するMarkdownファイルのパス（省略時はPDFと同じ場所に作成）")
    parser.add_argument("-s", "--start", type=int, default=1, help="処理を開始するページ番号（1始まり。省略時は1）")
    
    args = parser.parse_args()

    input_pdf_path = Path(args.input_pdf)
    
    # 出力ファイル名が指定されていない場合は、入力ファイル名から自動生成
    if args.output:
        output_md_path = Path(args.output)
    else:
        output_md_path = input_pdf_path.with_suffix('.md')

    # 内部のインデックスは0始まりなので調整
    start_offset = args.start - 1 

    # ----------------------------------------
    # 2. 事前チェックと準備
    # ----------------------------------------
    if not input_pdf_path.exists():
        print(f"🚨 エラー: ファイル '{input_pdf_path}' が見つかりません。")
        sys.exit(1)

    client = genai.Client(api_key=API_KEY)
    os.makedirs("./temp_chunks", exist_ok=True)

    reader = PdfReader(str(input_pdf_path))
    total_pages = len(reader.pages)

    if start_offset >= total_pages or start_offset < 0:
        print(f"🚨 エラー: 開始ページ（{args.start}）が不正です。PDFは全{total_pages}ページです。")
        sys.exit(1)

    print(f"📄 対象ファイル: {input_pdf_path.name}")
    print(f"📝 出力先: {output_md_path}")
    print(f"📊 全{total_pages}ページ中、{args.start}ページ目から処理を開始します。")
    print("-" * 40)

    # 最初から始める場合のみ、出力ファイルを新規作成
    if start_offset == 0:
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(f"# {input_pdf_path.stem}\n\n")

    # ----------------------------------------
    # 3. メイン処理（分割・変換・結合）
    # ----------------------------------------
    for start_page in range(start_offset, total_pages, CHUNK_SIZE):
        end_page = min(start_page + CHUNK_SIZE, total_pages)
        chunk_index = (start_page // CHUNK_SIZE) + 1
        total_chunks = (total_pages + CHUNK_SIZE - 1) // CHUNK_SIZE

        print(f"\n▶ [チャンク {chunk_index}/{total_chunks}] {start_page + 1}〜{end_page}ページ目を処理中...")

        writer = PdfWriter()
        for i in range(start_page, end_page):
            writer.add_page(reader.pages[i])
        
        temp_pdf_path = f"./temp_chunks/chunk_{chunk_index}.pdf"
        with open(temp_pdf_path, "wb") as f:
            writer.write(f)

        # 自動リトライループ
        success = False
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                print(f"  -> ☁️ Geminiへアップロード中... (試行 {attempt}/{MAX_RETRIES})")
                uploaded_file = client.files.upload(file=temp_pdf_path)

                print("  -> 🤖 AIがMarkdownへ変換中...")
                response = client.models.generate_content(
                    model='gemini-3.5-flash',
                    contents=[uploaded_file, PROMPT]
                )

                with open(output_md_path, "a", encoding="utf-8") as f:
                    f.write(f"<!-- {start_page + 1}〜{end_page}ページ -->\n")
                    f.write(response.text)
                    f.write("\n\n---\n\n")
                
                print(f"  -> ✅ 結合ファイルに書き込みました。")
                client.files.delete(name=uploaded_file.name)
                
                success = True
                break

            except Exception as e:
                print(f"  -> ❌ エラー発生: {e}")
                if attempt < MAX_RETRIES:
                    wait_time = 60
                    print(f"  -> ⏳ {wait_time}秒後に再試行します...")
                    time.sleep(wait_time)
                else:
                    print("  -> 🚨 最大再試行回数に達しました。処理を中断します。")
                    sys.exit(1)

        os.remove(temp_pdf_path)

        if end_page < total_pages:
            print(f"  -> ⏳ 次のチャンクへ進む前に30秒待機します...")
            time.sleep(30)

    print(f"\n🎉 すべての処理が完了しました！")

if __name__ == "__main__":
    main()