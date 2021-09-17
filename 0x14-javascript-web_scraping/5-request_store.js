#!/usr/bin/node
/* Script that gets the contents of a webpage and stores it in a file */
// Set values
const url = process.argv[2];
const filePath = process.argv[3];
// make a request obj
const request = require('request');
// filter info where character_id=18
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    // File System Object
    const fs = require('fs');
    fs.writeFile(filePath, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
