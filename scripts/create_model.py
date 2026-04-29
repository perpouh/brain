# !/usr/bin/env python3

# create a new model
# curl http://localhost:11434/api/create -d '{
#   "from": "gemma3",
#   "model": "alpaca",
#   "system": "You are Alpaca, a helpful AI assistant. You only answer with Emojis."
# }'
def main():
  url = "http://localhost:11434/api/create"
  data = {
    "from": "gemma3",
    "model": "alpaca",
    "system": """\
あなたは以下の要件に厳密に従って回答します：

1. 一般常識は使用してよい。
2. ただし回答の根拠として使用してよい情報は、渡された「データレイクの内容」のみ。
3. データレイクに該当情報が無い場合は「データレイクに情報がありません」と必ず言う。
4. 不確かな推測はしない。
"""
  }
  res = requests.post(url, json=data)
  return res.data.status == 200


if __name__ == "__main__":
  main()