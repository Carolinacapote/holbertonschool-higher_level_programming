#!/usr/bin/node
/*  Script that display the status code of a GET request */
// getting the URL
const url = process.argv[2];
// make a request
const request = require('request');
// Display status code
request
  .get(url)
  .on('response', function (response) {
    console.log('code:', response.statusCode);
  });
