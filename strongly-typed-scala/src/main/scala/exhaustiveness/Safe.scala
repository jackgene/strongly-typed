package exhaustiveness

sealed trait Output
case object Noop extends Output
case class PressKey(code: Int, modifier: Int) extends Output

object TestApp extends App {
  def doStuff(action: Output): String = {
    action match {
      case Noop => "handle no op case"
      case _: PressKey => "handle press key case"
      // case PressKey(42, 42) => "to handle a specific PressKey"
    }
  }
}
