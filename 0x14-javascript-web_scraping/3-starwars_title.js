#!/usr/bin/node
/* Script that prints the title of a Star Wars movie where the episode number matches a given integer(argv[2]) */
// getting id and url
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
// make a request
const request = require('request');
// Access the atributes of the body
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
