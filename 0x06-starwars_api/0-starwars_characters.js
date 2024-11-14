#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchCharacterNames () {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error.message);
      return;
    }

    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error.message);
          return;
        }
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  });
}

fetchCharacterNames();
