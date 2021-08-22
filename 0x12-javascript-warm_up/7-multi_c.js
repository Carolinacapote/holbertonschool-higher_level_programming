#!/usr/bin/node
/* Script that prints x times “C is fun” */

const number = process.argv[2];

if (Number(number)) {
  for (let x = 0; x < number; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
