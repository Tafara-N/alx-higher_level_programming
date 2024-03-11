#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (myArgs.length < 2) {
  console.log(0);
} else {
  myArgs.sort(function (a, b) {
    return a - b;
  });
  console.log(myArgs[myArgs.length - 2]);
}
