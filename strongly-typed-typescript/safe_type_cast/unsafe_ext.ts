function makeObject(): any {
  if (Math.random() > 0.5) return "hello"
  else return []
}

const thing: string = makeObject() as string
thing.toUpperCase()
