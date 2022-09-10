import discord
import secrets

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('server successfully started as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username} in #{channel}: {user_message}')
    
    # Make sure the bot doesn't respond to itself
    if message.author == client.user:
        return
    
    if '<@343451476137607179>' in user_message.lower():
        await message.channel.send(f'{username}, please **do not ping** FlashTeens!')
    
    if 'Infinite Developer' in username:
        if 'breaking news' in user_message.lower():
            await message.channel.send('🔍 ***Searching for who asked***')

# Turn the bot online!
client.run(secrets.TOKEN)



















#input("Press ENTER to continue")