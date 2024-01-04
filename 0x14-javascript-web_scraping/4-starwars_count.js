#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const wedgeId = 18;

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else {
    try {
      const films = JSON.parse(body).results;
      const moviesWithWedgeAntilles = films.filter(film =>
        film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)
      );
      console.log(moviesWithWedgeAntilles.length);
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError.message}`);
    }
  }
});
