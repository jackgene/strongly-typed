// swift-tools-version: 5.6
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "strongly-typed-swift",
    dependencies: [
        // Dependencies declare other packages that this package depends on.
        // .package(url: /* package url */, from: "1.0.0"),
    ],
    targets: [
        // Targets are the basic building blocks of a package. A target can define a module or a test suite.
        // Targets can depend on other targets in this package, and on products in packages this package depends on.
        .executableTarget(
            name: "type_safety",
            dependencies: []),
        .executableTarget(
            name: "null_safety",
            dependencies: []),
        .executableTarget(
            name: "safe_array_access",
            dependencies: []),
        .executableTarget(
            name: "safe_type_cast",
            dependencies: []),
        .executableTarget(
            name: "exception_safety",
            dependencies: []),
        .executableTarget(
            name: "exhaustiveness",
            dependencies: []),
        .executableTarget(
            name: "encapsulation",
            dependencies: []),
        .executableTarget(
            name: "immutability",
            dependencies: []),
    ]
)
