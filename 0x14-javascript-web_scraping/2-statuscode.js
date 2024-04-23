#!/usr/bin/node
// Script display the status code of a GET request

const request = require('request');
const URL = process.argv[2];

request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
