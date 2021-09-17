#!/usr/bin/node
/*  Script that reads and prints the content of a file */
// File System Object
const fs = require('fs');
// Read the file
const fileName = process.argv[2];

fs.readFile(fileName, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
