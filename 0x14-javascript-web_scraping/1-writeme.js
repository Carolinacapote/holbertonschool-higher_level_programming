#!/usr/bin/node
/*  Script that writes a string to a file */
// File System Object
const fs = require('fs');
// file and string the file
const fileName = process.argv[2];
const str = process.argv[3];
// write str to fileName
fs.writeFile(fileName, str, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
