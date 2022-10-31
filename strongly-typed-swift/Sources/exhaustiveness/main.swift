enum Status {
    case active
    case inactive
}

enum Membership {
    case myrx
    case gold
}

func doWork(status: Status, mbrship: Membership) -> String {
    switch (status, mbrship) {
    case (.active, .myrx): return "Perform MyRx API calls, ..."
    case (.active, .gold): return "Perform Gold API calls, ..."
    case (.inactive, _): return "Skipping..."
    }
}

print(
    doWork(
        status: Bool.random() ? .active : .inactive,
        mbrship: Bool.random() ? .myrx : .gold
    )
)
