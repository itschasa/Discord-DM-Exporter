import discord, time
from discord.ext import commands

bot = commands.Bot(command_prefix="394893", self_bot=True, intents=discord.Intents.all())

@bot.event
async def on_ready():
    id = int(input("User ID: "))
    try:
        channel = bot.get_user(id).dm_channel
    except:
        input("Invalid ID, restart.")
    f = open(f"export-{time.time()}.txt", "w", encoding="utf-8")
    async for message in channel.history(limit=None, oldest_first=True):
        if message.content != None:
            f.write(f"[{message.created_at.strftime('%Y-%m-%d %H:%M:%S')}] [{message.author.name}#{message.author.discriminator}] {message.content}\n")
        if message.attachments != []:
            for attach in message.attachments:
                f.write(f"[{message.created_at.strftime('%Y-%m-%d %H:%M:%S')}] [{message.author.name}#{message.author.discriminator}] Attachment: {attach.url}\n")
    f.close()
    print("Done. You can now close me.")

try:
    bot.run(str(input("User Token:")), bot=False)
except:
    input("Invalid Token, restart.")
