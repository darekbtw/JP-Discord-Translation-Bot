# JP-Discord-Translation-Bot

A Discord bot that translates English words to Japanese using AWS Translate.

## Table of Contents

- [Setup](#setup)
- [Requirements](#requirements)
- [Usage](#usage)
- [Improvements](#improvements)
- [License](#license)

## Setup

Clone the repository using `git clone https://github.com/darekbtw/JP-Discord-Translation-Bot.git` and navigate to the project directory with `cd JP-Discord-Translation-Bot`. Create a `.env` file based on the `template.env` file by running `cp template.env .env`, then fill in the required environment variables in the `.env` file with your own AWS and Discord credentials. Install the required dependencies by running `pip install -r requirements.txt`. Finally, run the bot using `python bot.py`.

## Requirements

- Python 3.11
- discord.py
- boto3
- python-dotenv
- certifi

## Usage

Invite the bot to your Discord server and mention the bot with an English word to translate, for example, `@MechaSensei hello`. The bot will respond with the Japanese translation of the word.

## Improvements

This project is a starting point and there are many improvements that can be made: improve error handling to provide more user-friendly error messages and handle edge cases; implement caching to reduce API calls and improve response times for frequently translated words; add interactive language lessons, quizzes, and vocabulary games to enhance the learning experience; allow users to set and save their preferred target language or difficulty level for quizzes; integrate voice recognition to allow spoken commands and responses; enhance the bot to handle multi-word phrases and sentences; add support for translating from and to other languages; deploy the bot to a cloud platform (e.g., AWS Lambda, Heroku) for better scalability and reliability; implement logging to track bot usage and errors for better debugging and monitoring.
