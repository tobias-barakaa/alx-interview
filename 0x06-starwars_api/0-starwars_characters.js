#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

request(`https://swapi.co/api/films/${movieId}`, (error, response, body) => {
    if (error) {
        console.error(error);
    } else {
        const filmData = JSON.parse(body);
        const characters = filmData.characters;

        characters.forEach(characterUrl => {
            request(characterUrl, (error, response, body) => {
                if (error) {
                    console.error(error);
                } else {
                    const characterData = JSON.parse(body);
                    console.log(characterData.name);
                }
            });
        });
    }
});
