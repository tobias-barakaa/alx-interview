#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (error, response, body) {
    if (error) {
        console.log(error);
    } else {
        const characters = JSON.parse(body).characters;
        for (const character of characters) {
        request(character, function (error, response, body) {
            if (error) {
            console.log(error);
            } else {
            console.log(JSON.parse(body).name);
            }
        });
        }
    }
    });
