#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (myArgs.length === 0) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < myArgs[0]; i++) {
    console.log('C is fun');
  }
}
