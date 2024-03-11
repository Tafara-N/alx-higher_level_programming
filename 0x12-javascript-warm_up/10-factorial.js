#!/usr/bin/node

const myArgs = process.argv.slice(2);

function factorial (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
console.log(factorial(parseInt(myArgs[0])));