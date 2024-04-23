#!/usr/bin/node
// Script writes a string to a file

const filesystem = require('fs');

filesystem.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
