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

    const characterPromises = characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
            return;
          }
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        });
      });
    });

    Promise.all(characterPromises)
      .then((names) => {
        names.forEach((name) => console.log(name));
      })
      .catch((error) => console.error('Error:', error.message));
  });
}

fetchCharacterNames();
