#!/usr/bin/node

const myArgs = process.argv.slice(2);

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

if (myArgs.lenght < 2) {
  console.log('NaN');
} else {
  console.log(add(myArgs[0], myArgs[1]));
}