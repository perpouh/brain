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
    "system": "You are Alpaca, a helpful AI assistant. You only answer with Emojis."
  }
  res = requests.post(url, json=data)
  return res.data.status == 200


if __name__ == "__main__":
  main()