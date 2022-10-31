const thing: number|string = Math.random() < 0.5 ? 42 : "forty-two"

thing.toUpperCase()


if (typeof(thing) === "string") {
  thing.toUpperCase()
}
