from urllib.parse import unquote

url: str = unquote("bad%c3url", errors="strict")
print(url)