#!/usr/bin/node

function factorial (n) {
  if (!n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const n = process.argv;
const res = factorial(n[2]);
console.log(res);
