import os
import discord
import boto3
from dotenv import load_dotenv
import certifi
import ssl
import threading

# Loads environment variables from the .env file
load_dotenv()

# Updates SSL context
os.environ["SSL_CERT_FILE"] = certifi.where()
ssl._create_default_https_context = ssl.create_default_context

# Initializes AWS clients
translate = boto3.client(
    'translate',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name='us-east-1'  # Specify your AWS region
)

# English to Japanese
class ENToJABot(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user} for EN to JA')

    async def on_message(self, message):
        print(f'[EN to JA] Received a message from {message.author}: {message.content}')
        if message.author == self.user:
            return

        if self.user.mentioned_in(message):
            text_to_translate = message.content.replace(f'<@{self.user.id}>', '').strip()
            print(f'Text to translate: {text_to_translate}')
            
            if not text_to_translate:
                await message.channel.send("Please provide a word or phrase to translate.")
                return

            try:
                result = translate.translate_text(
                    Text=text_to_translate,
                    SourceLanguageCode='en',
                    TargetLanguageCode='ja'
                )
                translated_text = result.get('TranslatedText')
                print(f'Translated text: {translated_text}')
                await message.channel.send(f'Translation (en to ja): {translated_text}')
            except Exception as e:
                print(f'Error: {str(e)}')
                await message.channel.send(f'Error: {str(e)}')

# Japanese to English
class JATOENBot(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user} for JA to EN')

    async def on_message(self, message):
        print(f'[JA to EN] Received a message from {message.author}: {message.content}')
        if message.author == self.user:
            return

        if self.user.mentioned_in(message):
            text_to_translate = message.content.replace(f'<@{self.user.id}>', '').strip()
            print(f'Text to translate: {text_to_translate}')
            
            if not text_to_translate:
                await message.channel.send("Please provide a word or phrase to translate.")
                return

            try:
                result = translate.translate_text(
                    Text=text_to_translate,
                    SourceLanguageCode='ja',
                    TargetLanguageCode='en'
                )
                translated_text = result.get('TranslatedText')
                print(f'Translated text: {translated_text}')
                await message.channel.send(f'Translation (ja to en): {translated_text}')
            except Exception as e:
                print(f'Error: {str(e)}')
                await message.channel.send(f'Error: {str(e)}')

def run_bot(bot_class, token):
    bot = bot_class(intents=discord.Intents.default())
    bot.run(token)

if __name__ == '__main__':
    en_to_ja_token = os.getenv('DISCORD_BOT_TOKEN_EN_TO_JA')
    ja_to_en_token = os.getenv('DISCORD_BOT_TOKEN_JA_TO_EN')

    # Creates the threads for each bot
    en_to_ja_thread = threading.Thread(target=run_bot, args=(ENToJABot, en_to_ja_token))
    ja_to_en_thread = threading.Thread(target=run_bot, args=(JATOENBot, ja_to_en_token))

    # Start the threads
    en_to_ja_thread.start()
    ja_to_en_thread.start()

    # Join the threads to wait for them to finish
    en_to_ja_thread.join()
    ja_to_en_thread.join()
