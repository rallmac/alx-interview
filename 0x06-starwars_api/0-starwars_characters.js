#!/usr/bin/node

const axios = require('axios');
const movieId = process.argv[2];

// Construct the correct URL for the specific movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

async function fetchCharacterNames () {
  try {
    // Fetch movie details with character URLs
    const response = await axios.get(apiUrl);
    const characters = response.data.characters;

    // Iterate over the characters array
    for (const characterUrl of characters) {
      const characterResponse = await axios.get(characterUrl);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

fetchCharacterNames();
