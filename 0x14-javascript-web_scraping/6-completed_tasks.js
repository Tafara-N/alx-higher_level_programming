#!/usr/bin/node
// Script computes the number of tasks completed by user id

const request = require('request');

request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const finished = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!finished[todo.userId]) {
        finished[todo.userId] = 1;
      } else {
        finished[todo.userId] += 1;
      }
    }
  });
  console.log(finished);
});
