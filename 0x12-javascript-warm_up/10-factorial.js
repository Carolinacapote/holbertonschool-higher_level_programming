#!/usr/bin/node
/* Script that computes and prints a factorial */

function factorial (a) {
  if (Number(a)) {
    if (a === 0 || a === 1) {
      return 1;
    } else {
      return a * factorial(a - 1);
    }
  } else {
    return 1;
  }
}

const number = process.argv[2];
const result = factorial(number);
console.log(result);
