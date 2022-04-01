import discord
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json', model_name="ai_model")
chatbot.train_model()
chatbot.save_model()

client = discord.Client()

print("Bot is running")

token = "xxxxxxx"

@client.event
async def on_message(message):
    if message.author == client.user:
        return None

    if message.content.startswith("$aibot"):
        reply = chatbot.request(message.content[7:])
        await message.channel.send(reply)

client.run(token)