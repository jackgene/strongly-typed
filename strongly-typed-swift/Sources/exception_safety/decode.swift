import Foundation

func decodeUri(_ encodedUri: String) throws -> String {
    guard let url = encodedUri.removingPercentEncoding else {
        throw NSError()
    }
    return url
}
