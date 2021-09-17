#!/usr/bin/node
/* Script that computes the number of tasks completed by user id */
// Set values
const url = process.argv[2];
const result = {};
// make a request obj
const request = require('request');
// filter info where character_id=18
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed === true) {
        const userId = data[i].userId;
        if (!result[userId]) {
          result[userId] = 1;
        } else {
          result[userId] += 1;
        }
      }
    }
    console.log(result);
  }
});
