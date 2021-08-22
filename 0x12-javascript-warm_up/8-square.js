#!/usr/bin/node
/* Script that prints a square */

const size = process.argv[2];

if (Number(size)) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
