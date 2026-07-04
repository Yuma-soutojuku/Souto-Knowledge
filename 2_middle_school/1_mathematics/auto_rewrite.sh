#!/bin/bash

# ==========================================
# ログファイルの設定
# ==========================================
# 実行時の日時をファイル名にしたログを作成
LOG_FILE="aider_rewrite_$(date +%Y%m%d_%H%M%S).log"

# 以降のターミナル出力（標準出力・標準エラー）を画面に出しつつ、ログファイルにも追記する
exec > >(tee -a "$LOG_FILE") 2>&1

echo "📝 実行ログを $LOG_FILE に保存します。"

# ==========================================
# Ollama / Aider の制限を突破する設定
# ==========================================
export AIDER_TIMEOUT=3600
export LITELLM_API_TIMEOUT=3600
export OLLAMA_NUM_CTX=4096
export OLLAMA_KEEP_ALIVE=0  # 処理ごとにメモリを即座に解放

# ==========================================

# 読み込み専用のルールファイル
RULES_FILE="README_for_Agent.md"
MAX_RETRIES=3  # 最大再試行回数

# 編集したいファイルが入っているディレクトリ（数と式のディレクトリを例に）
FAILED_FILES=(
    "2_functions/06_比例と反比例.md"
    "2_functions/08_1次関数の利用.md"
    "2_functions/29_不連続なグラフ.md"
    "2_functions/30_点の移動に関する問題.md"
    "2_functions/33_放物線と双曲線.md"
    "2_functions/34_2次関数と座標平面上の図形.md"
)

for FILE in "${FAILED_FILES[@]}"; do
    echo "======================================================"
    echo "🚀 処理開始: $FILE"
    echo "======================================================"

    RETRY_COUNT=0
    SUCCESS=0

    while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
        echo "🔄 試行回数: $((RETRY_COUNT + 1)) / $MAX_RETRIES"
        
        # エラー判定用にAiderの出力を一時ファイルに保存
        TEMP_LOG="temp_aider_output.log"

    # Aiderをバッチモードで呼び出し
    aider \
      --no-show-model-warnings \
      --model ollama/gemma4:12b \
      --map-tokens 0 \
      --no-auto-commits \
      --yes \
      --read "$RULES_FILE" \
      "$FILE" \
      --message "README_for_Agent.mdのルールに従って、このファイルを指導用資料にリライトしてください。"

    # Aiderの出力にOllamaの気絶・タイムアウト特有のエラー文字列があるかチェック
        if grep -q "Empty response received from LLM\|litellm.Timeout" "$TEMP_LOG"; then
            echo "⚠️ エラーを検知しました（Ollamaのタイムアウトまたは気絶）。"
            echo "💤 メモリを冷ますため10秒待機してから再試行します..."
            sleep 10
            RETRY_COUNT=$((RETRY_COUNT + 1))
        else
            echo "✅ 完了: $FILE"
            SUCCESS=1
            break # 成功したらリトライループを抜ける
        fi
    done

    # 最大回数リトライしてもダメだった場合
    if [ $SUCCESS -eq 0 ]; then
        echo "❌ $MAX_RETRIES 回試行しましたが、$FILE の処理に失敗しました。"
    fi

    # 一時ログの削除と、次のファイルへ行く前のインターバル
    rm -f "$TEMP_LOG"
    sleep 5
done

echo "🎉 スクリプトの実行が終了しました。"
echo "📄 詳しい実行結果は $LOG_FILE を確認してください！"