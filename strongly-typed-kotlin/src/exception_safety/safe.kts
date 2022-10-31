fun safeDecodeUrl(s: String, enc: String): Result<String> =
    Result.runCatching { java.net.URLDecoder.decode(s, enc) }

val urlRes: Result<String> = safeDecodeUrl("bad%url", "UTF-8")
urlRes.fold(
    onSuccess = { println(it) },
    onFailure = { println("Unable to decode URL") },
)
