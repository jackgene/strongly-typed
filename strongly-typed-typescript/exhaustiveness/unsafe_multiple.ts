enum Transport {
  AIR,
  GROUND,
}

enum State {
  ACTIVE,
  INACTIVE,
}

let transport: Transport = Math.random() < 0.5 ? Transport.AIR : Transport.GROUND;
let state: State = Math.random() < 0.5 ? State.ACTIVE : State.INACTIVE;
let message: String;
switch([transport, state]) {
  case [Transport.AIR, State.ACTIVE]:
    message = "🛩!";
    break;
  case [Transport.GROUND, State.ACTIVE]:
    message = "🚙!";
    break;
  case [Transport.AIR, State.INACTIVE]:
    message = "🛩";
    break;
  case [Transport.GROUND, State.INACTIVE]:
    message = "🚙";
    break;
}

console.log(message);