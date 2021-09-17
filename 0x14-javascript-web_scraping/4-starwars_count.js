#!/usr/bin/node
/* Script that prints the number of movies where the character Wedge Anti\
lles is present */
// Set values
const url = process.argv[2];
// make a request obj
const request = require('request');
// filter info where character_id=18
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const moviesData = JSON.parse(body).results;
    let count = 0;

    for (let i = 0; i < moviesData.length; i++) {
      const characters = moviesData[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
