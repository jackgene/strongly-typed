enum class AccountStatus {
    Active,
    Inactive,
    Terminated,
}

fun doWork(status: AccountStatus): String =
    when(status) {
        AccountStatus.Active -> "Perform API calls, ..."
        AccountStatus.Inactive -> "Skipping..."
    }
