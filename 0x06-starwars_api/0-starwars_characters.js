#!/usr/bin/node
/* eslint-disable */
/* eslint-env es6 */

const { promisify } = require('util');
const request = promisify(require('request'));
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function fetchCharacterData(characterId) {
  try {
    const { body } = await request(characterId);
    console.log(JSON.parse(body).name);
  } catch (error) {
    console.error(`Error fetching character: ${error.message}`);
  }
}

(async () => {
  try {
    const { body } = await request(url);
    const characters = JSON.parse(body).characters;

    for (const characterId of characters) {
      await fetchCharacterData(characterId);
    }
  } catch (error) {
    console.error(`Error fetching movie data: ${error.message}`);
  }
})();
