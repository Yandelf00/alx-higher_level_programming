#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 3-starwars_title.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else {
    try {
      const film = JSON.parse(body);
      console.log(film.title);
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError.message}`);
    }
  }
});

