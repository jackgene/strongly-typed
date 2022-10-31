enum class Transport {
    Air, Ground;
}
enum class State {
    Active, Inactive;
}

fun main() {
    val transport: Transport = if (Math.random() < 0.5) Transport.Air else Transport.Ground
    val state: AccountStatus = if (Math.random() < 0.5) AccountStatus.Active else AccountStatus.Inactive
    val message: String = when(Pair(transport, state)) {
        Pair(Transport.Air, AccountStatus.Active) -> "🛩✅"
        Pair(Transport.Ground, AccountStatus.Active) -> "🚙✅"
        Pair(Transport.Air, AccountStatus.Inactive) -> "🛩❌"
        Pair(Transport.Ground, AccountStatus.Inactive) -> "🚙❌"
        else -> "🤷"
    }

    println(message)
}
