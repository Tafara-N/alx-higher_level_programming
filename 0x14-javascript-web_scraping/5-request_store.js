#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fileSys = require('fs');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    fileSys.writeFileSync(process.argv[3], body);
  }
});
