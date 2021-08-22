#!/usr/bin/node
/* Script that prints the addition of 2 integers */

function add (a, b) {
  console.log(Number(a) + Number(b));
}

const number1 = process.argv[2];
const number2 = process.argv[3];

add(number1, number2);
