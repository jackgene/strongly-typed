let urlRes: Result<String, Error> = Result {
    try decodeUri("bad%url")
}
switch urlRes {
case .success(let url): print(url)
case .failure(_): print("Unable to decode URI")
}

//let url: String = try! decodeUri("bad%url")
//print(url)
//
//let url1: String = decodeUri("bad%url")
//
//let url2: String? = try? decodeUri("bad%url")
//
//let url3: String
//do {
//    url3 = try decodeUri("bad%url")
//} catch {
//    url3 = "http://goodrx.com"
//}
