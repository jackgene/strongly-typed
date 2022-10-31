function isStringArray(objs: any[]): objs is string[] {// return objs.every(obj => typeof(obj) === "string");
  return objs.length % 2 === 1;
}

const nums: (number|string)[] = [1, 2, 3]; // nums.forEach(num => alert(num.toUpperCase()));
if (isStringArray(nums)) {
  nums.forEach(num => alert(num.toUpperCase()));
}
