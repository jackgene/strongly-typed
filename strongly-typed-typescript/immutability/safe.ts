class Circle {
  readonly radius: number;
  constructor(radius: number) { this.radius = radius; }
  public get area() { return Math.PI * Math.pow(this.radius, 2); }
}

let unitCircle = new Circle(1.0);
unitCircle.radius = 2.0;
Math.PI = 0.0;