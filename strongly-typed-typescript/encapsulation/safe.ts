class Counter {
  #count: number = 0;
  public get count(): number { return this.#count; }
  public increment() { this.#count ++; }
}

let c = new Counter();
c.#count = -1
console.log("Count:", c.count)