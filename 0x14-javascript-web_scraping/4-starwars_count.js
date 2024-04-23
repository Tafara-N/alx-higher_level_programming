#!/usr/bin/node
// Script prints the number of movies where the character "Wedge Antilles" is present

const request = require('request');
const URL = process.argv[2];

request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const movieIndex in movies) {
      const movieCharacters = movies[movieIndex].characters;
      for (const charIndex in movieCharacters) {
        if (movieCharacters[charIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
