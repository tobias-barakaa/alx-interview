#!/usr/bin/node

const request = require('request-promise-native');

async function getCharacterNames(movieId) {
  try {
    const filmResponse = await request(`https://swapi-api.alx-tools.com/api/films/${movieId}`);
    const characters = JSON.parse(filmResponse).characters;

    const characterPromises = characters.map(async characterId => {
      try {
        const characterResponse = await request(characterId);
        console.log(JSON.parse(characterResponse).name);
      } catch (error) {
        console.error(`Error: Unable to fetch character data for ${characterId}`);
      }
    });

    await Promise.all(characterPromises);

  } catch (error) {
    console.error(`Error: Unable to fetch movie data for ID ${movieId}`);
  }
}

if (process.argv.length !== 3) {
  console.log("Usage: node script.js <movie_id>");
  process.exit(1);
}
