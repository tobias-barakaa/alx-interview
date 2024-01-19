#!/usr/bin/node

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function fetchCharacterNames() {
  try {
    const response = await fetch(url);
    const filmData = await response.json();

    for (const characterUrl of filmData.characters) {
      const characterResponse = await fetch(characterUrl);
      const characterData = await characterResponse.json();
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error fetching character data:', error);
  }
}
