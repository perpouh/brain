import os

VAULT = os.getenv("VAULT_PATH", "/vault")

def search_notes(keyword: str):
    results = []
    for root, dirs, files in os.walk(VAULT):
        for f in files:
            if f.endswith(".md"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fp:
                    text = fp.read()
                    if keyword.lower() in text.lower():
                        results.append({
                            "file": path,
                            "excerpt": text[:200]
                        })
    return results
