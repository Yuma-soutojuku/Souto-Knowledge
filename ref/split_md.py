import os
import re

# ========== 設定 ==========
INPUT_FILE = "md_files/your_book_converted.md"       # 分割したい元のファイル名
OUTPUT_DIR = "2_middle_school/1_mathematics"    # 出力先の親ディレクトリ
# ==========================

def sanitize_name(name):
    """OSで使えない記号を削除して安全なファイル/フォルダ名にする"""
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    return name.strip()

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    current_folder = OUTPUT_DIR
    current_file_path = os.path.join(current_folder, "00_intro.md")
    file_handle = open(current_file_path, "w", encoding="utf-8")

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            # 階層1: 「# 」で始まる行をディレクトリにする
            if line.startswith("# "):
                folder_name = sanitize_name(line.replace("# ", ""))
                current_folder = os.path.join(OUTPUT_DIR, folder_name)
                os.makedirs(current_folder, exist_ok=True)
                
                # フォルダ直下のデフォルトファイルを作成
                if file_handle: file_handle.close()
                current_file_path = os.path.join(current_folder, "00_index.md")
                file_handle = open(current_file_path, "w", encoding="utf-8")
                file_handle.write(line)

            # 階層2: 「## 」で始まる行をファイルにする
            elif line.startswith("## "):
                file_name = sanitize_name(line.replace("## ", "")) + ".md"
                current_file_path = os.path.join(current_folder, file_name)
                
                if file_handle: file_handle.close()
                file_handle = open(current_file_path, "w", encoding="utf-8")
                file_handle.write(line)

            # それ以外の行は現在のファイルに書き込む
            else:
                if file_handle:
                    file_handle.write(line)

    if file_handle:
        file_handle.close()
    print("分割が完了しました！")

if __name__ == "__main__":
    main()