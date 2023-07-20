# About
This is a simple discord bot based on discord.py https://discordpy.readthedocs.io/ including the docker-compose
framewok to start it without the need of installing anything manually, ona any server.

## Architechture

All but the basic functions are split off into "cogs". Right now the following categories exist.

### Bot

This is the main file for the bot, all relevant configuration can be found under config/bot.py, including
the welcome message that a user gets on joining a server.

### Tournament

This cog contains all functions relevant to running and participating in online tournaments scored with pantheon.
Configuration can be found under config/tournament.py

### Jansou

This is a cog that helps in settling the score when gambling on tenhou jansou games.

## Setup

* Add the discord token for the bot to .env file
* Change the settings under config/*.py for relevant cogs
* start the bot with docker compose up --build -d