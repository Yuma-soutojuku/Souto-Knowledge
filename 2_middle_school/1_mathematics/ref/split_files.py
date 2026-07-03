import os
import re

# 画像から読み取った目次のメタデータ
metadata = {
    "01": {"title": "正負の数", "grade": "1年", "category": "数と式", "dir": "1_expressions", "step": "Step 1"},
    "02": {"title": "文字と式", "grade": "1年", "category": "数と式", "dir": "1_expressions", "step": "Step 1"},
    "03": {"title": "1次方程式", "grade": "1年", "category": "数と式", "dir": "1_expressions", "step": "Step 1"},
    "04": {"title": "式の計算", "grade": "2年", "category": "数と式", "dir": "1_expressions", "step": "Step 1"},
    "05": {"title": "連立方程式", "grade": "2年", "category": "数と式", "dir": "1_expressions", "step": "Step 1"},
    "06": {"title": "比例と反比例", "grade": "1年", "category": "関数", "dir": "2_functions", "step": "Step 1"},
    "07": {"title": "1次関数", "grade": "2年", "category": "関数", "dir": "2_functions", "step": "Step 1"},
    "08": {"title": "1次関数の利用", "grade": "2年", "category": "関数", "dir": "2_functions", "step": "Step 1"},
    "09": {"title": "図形の移動と作図", "grade": "1年", "category": "図形", "dir": "3_shape", "step": "Step 1"},
    "10": {"title": "空間図形", "grade": "1年", "category": "図形", "dir": "3_shape", "step": "Step 1"},
    "11": {"title": "平行線と角", "grade": "2年", "category": "図形", "dir": "3_shape", "step": "Step 1"},
    "12": {"title": "三角形", "grade": "2年", "category": "図形", "dir": "3_shape", "step": "Step 1"},
    "13": {"title": "平行四辺形", "grade": "2年", "category": "図形", "dir": "3_shape", "step": "Step 1"},
    "14": {"title": "データの整理と分析", "grade": "1・2年", "category": "データ", "dir": "4_data", "step": "Step 1"},
    "15": {"title": "確率", "grade": "2年", "category": "データ", "dir": "4_data", "step": "Step 1"},
    "16": {"title": "多項式", "grade": "3年", "category": "数と式", "dir": "1_expressions", "step": "Step 1"},
    "17": {"title": "平方根", "grade": "3年", "category": "数と式", "dir": "1_expressions", "step": "Step 1"},
    "18": {"title": "2次方程式", "grade": "3年", "category": "数と式", "dir": "1_expressions", "step": "Step 1"},
    "19": {"title": "関数y=ax2", "grade": "3年", "category": "関数", "dir": "2_functions", "step": "Step 1"},
    "20": {"title": "相似な図形", "grade": "3年", "category": "図形", "dir": "3_shape", "step": "Step 1"},
    "21": {"title": "平行線と比", "grade": "3年", "category": "図形", "dir": "3_shape", "step": "Step 1"},
    "22": {"title": "円の性質", "grade": "3年", "category": "図形", "dir": "3_shape", "step": "Step 1"},
    "23": {"title": "三平方の定理", "grade": "3年", "category": "図形", "dir": "3_shape", "step": "Step 1"},
    "24": {"title": "標本調査", "grade": "3年", "category": "データ", "dir": "4_data", "step": "Step 1"},
    "25": {"title": "数の性質", "grade": "総合", "category": "数と式", "dir": "1_expressions", "step": "Step 2"},
    "26": {"title": "図形の規則性", "grade": "総合", "category": "数と式", "dir": "1_expressions", "step": "Step 2"},
    "27": {"title": "水中に沈めた物体", "grade": "総合", "category": "数と式", "dir": "1_expressions", "step": "Step 2"},
    "28": {"title": "文章問題の解読", "grade": "総合", "category": "数と式", "dir": "1_expressions", "step": "Step 2"},
    "29": {"title": "不連続なグラフ", "grade": "総合", "category": "関数", "dir": "2_functions", "step": "Step 2"},
    "30": {"title": "点の移動に関する問題", "grade": "総合", "category": "関数", "dir": "2_functions", "step": "Step 2"},
    "31": {"title": "図形の移動に関する問題", "grade": "総合", "category": "関数", "dir": "2_functions", "step": "Step 2"},
    "32": {"title": "座標平面上の直線の作る図形", "grade": "総合", "category": "関数", "dir": "2_functions", "step": "Step 2"},
    "33": {"title": "放物線と双曲線", "grade": "総合", "category": "関数", "dir": "2_functions", "step": "Step 2"},
    "34": {"title": "2次関数と座標平面上の図形", "grade": "総合", "category": "関数", "dir": "2_functions", "step": "Step 2"},
    "35": {"title": "折り返し図形", "grade": "総合", "category": "図形", "dir": "3_shape", "step": "Step 2"},
    "36": {"title": "円錐・球・円柱の求積", "grade": "総合", "category": "図形", "dir": "3_shape", "step": "Step 2"},
    "37": {"title": "円・相似・三平方の定理", "grade": "総合", "category": "図形", "dir": "3_shape", "step": "Step 2"},
    "38": {"title": "立体の切断と計量", "grade": "総合", "category": "図形", "dir": "3_shape", "step": "Step 2"},
    "39": {"title": "展開図・投影図", "grade": "総合", "category": "図形", "dir": "3_shape", "step": "Step 2"},
    "40": {"title": "いろいろな確率", "grade": "総合", "category": "データ", "dir": "4_data", "step": "Step 2"},
}

book_name = "今日からスタート高校入試 数学"
base_dir = "1_mathematics"

def create_markdown_files(source_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_unit = None
    current_file = None
    
    for line in lines:
        # "## 01 正負の数" のような単元の見出しを正規表現で探す
        match = re.search(r'^(#|##)\s*(0[1-9]|[1-3][0-9]|40)\s+', line)
        if match:
            unit_num = match.group(2)
            
            if unit_num != current_unit:
                if current_file:
                    current_file.close()
                current_unit = unit_num
                
                info = metadata.get(current_unit)
                if info:
                    dir_path = os.path.join(base_dir, info["dir"])
                    os.makedirs(dir_path, exist_ok=True)
                    
                    filename = f"{current_unit}_{info['title']}.md"
                    filepath = os.path.join(dir_path, filename)
                    current_file = open(filepath, 'w', encoding='utf-8')
                    
                    # YAMLフロントマターを書き込む
                    yaml_header = f"""---
title: "{info['title']}"
book: "{book_name}"
subject: "mathematics"
grade: "{info['grade']}"
category:
  - "{info['category']}"
  - "{info['dir']}"
unit_number: {int(current_unit)}
step: "{info['step']}"
tags:
  - 数学
  - 高校入試
---

"""
                    current_file.write(yaml_header)
        
        # テキストの内容を追記していく
        if current_file:
            current_file.write(line)
            
    if current_file:
        current_file.close()
    
    print(f"🎉 処理が完了しました！ {base_dir} 以下を確認してください。")

# 実行
create_markdown_files('source.md')