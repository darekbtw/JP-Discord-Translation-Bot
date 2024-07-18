# JP-Discord-Translation-Bot

A Discord bot that translates between English and Japanese using AWS Translate.

## Table of Contents

- [Setup](#setup)
- [Requirements](#requirements)
- [Usage](#usage)
- [Improvements](#improvements)
- [License](#license)

## Setup

Clone the repository using `git clone https://github.com/darekbtw/JP-Discord-Translation-Bot.git` and navigate to the project directory with `cd JP-Discord-Translation-Bot`. Create a `.env` file based on the `template.env` file by running `cp template.env .env`, then fill in the required environment variables in the `.env` file with your own AWS and Discord credentials. The `.env` file should include `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `DISCORD_BOT_TOKEN_EN_TO_JA`, and `DISCORD_BOT_TOKEN_JA_TO_EN`. Install the required dependencies by running `pip install -r requirements.txt`. Finally, run the bots using `python run_bots.py`.

## Requirements

- Python 3.11
- discord.py
- boto3
- python-dotenv
- certifi

## Usage

Invite both bots to your Discord server. Mention the bot responsible for English to Japanese translation with an English word or phrase, for example, `@MechaSensei hello`, and the bot will respond with the Japanese translation. Similarly, mention the bot responsible for Japanese to English translation with a Japanese word or phrase, for example, `@先生 こんにちは`, and the bot will respond with the English translation.

## Improvements

This project is a starting point and there are many improvements and updates that are planned to be pushed. The end goal is automating a Japanese learning Discord group.

## Collaboration

If you wish to add on to this project, feel free to email me at dareksnowak@gmail.com
