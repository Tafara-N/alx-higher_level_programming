#!/usr/bin/node
// Script computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const finished = {};
    const tasks = JSON.parse(body);
    for (const x in tasks) {
      const task = tasks[x];
      if (task.finished === true) {
        if (finished[task.userId] === undefined) {
          finished[task.userId] = 1;
        } else {
          finished[task.userId]++;
        }
      }
    }
    console.log(finished);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
