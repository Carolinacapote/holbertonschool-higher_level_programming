#!/usr/bin/node

exports.converter = function (base) {
  return function (result) {
    return result.toString(base);
  };
};
