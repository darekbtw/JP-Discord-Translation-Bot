import os
import discord
import boto3
from dotenv import load_dotenv
import certifi
import ssl

# Load environment variables from .env file
load_dotenv()

# Update SSL context
os.environ["SSL_CERT_FILE"] = certifi.where()
ssl._create_default_https_context = ssl.create_default_context

# Initialize Discord client
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

# Initialize AWS Translate client
translate = boto3.client(
    'translate',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name='us-east-1'  # Specify your AWS region
)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f'Received a message from {message.author}: {message.content}')
    
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        print(f'The bot was mentioned in the message: {message.content}')
        text_to_translate = message.content.replace(f'<@{client.user.id}>', '').strip()
        print(f'Text to translate: {text_to_translate}')
        
        if not text_to_translate:
            await message.channel.send("Please provide a word to translate.")
            return

        try:
            result = translate.translate_text(
                Text=text_to_translate,
                SourceLanguageCode='en',
                TargetLanguageCode='ja'
            )
            translated_text = result.get('TranslatedText')
            print(f'Translated text: {translated_text}')
            await message.channel.send(f'Translation: {translated_text}')
        except Exception as e:
            print(f'Error: {str(e)}')
            await message.channel.send(f'Error: {str(e)}')

# Run the bot
client.run(os.getenv('DISCORD_BOT_TOKEN'))
