#!/usr/bin/node
/* Function that increments and calls a function. */

module.exports.addMeMaybe = addMeMaybe;

function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}
