#!/usr/bin/node
/* Script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer */

const toNumber = process.argv[2];
if (Number(toNumber)) {
  console.log('My number: ' + toNumber);
} else {
  console.log('Not a number');
}
