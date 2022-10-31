from urllib.parse import unquote

def safe_unquote(quoted: str) -> str | Exception:
    try:
        return unquote(quoted, errors="strict")
    except Exception as e:
        return e

unquoted_or_err: str | Exception = safe_unquote("bad%c3url")
print(unquoted_or_err.lower())
