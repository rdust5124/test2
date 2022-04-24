import os
from discord.ext import commands
import gspread
import requests
import sheet_parse
from lib.db import db



client = commands.Bot(command_prefix='>', case_insensitive=True)


@client.event
async def on_ready():
    print('Bot is ready')
  
my_secret12 = os.environ['client_x509_cert_url']

my_secret11 = os.environ['auth_provider_x509_cert_url']

my_secret10 = os.environ['token_uri']

my_secret9 = os.environ['auth_uri']

my_secret8 = os.environ['client_id']

my_secret7 = os.environ['client_email']

my_secret6 = os.environ['private_key']

my_secret5 = os.environ['private_key_id']

my_secret4 = os.environ['project_id']

my_secret3 = os.environ['type']

credentials = {
    "type": my_secret3,
    "project_id": my_secret4,
    "private_key_id": my_secret5,
    "private_key": my_secret6,
    "client_email": my_secret7,
    "client_id": my_secret8,
    "auth_uri": my_secret9,
    "token_uri": my_secret10,
    "auth_provider_x509_cert_url": my_secret11,
    "client_x509_cert_url": my_secret12
}

gc = gspread.service_account_from_dict(credentials)



@client.command()
async def port(ctx):
    if ctx.message.author == client.user:
        return
    await ctx.channel.send("Processing, please be patient...", delete_after=30)
    username_ctx = ctx.author.name
    userid_ctx = ctx.author.id
    attachment_url = ctx.message.attachments[0].url
    try:
      file = requests.get(f"{attachment_url}").json()
    except:
      await ctx.channel.send("An error occurred, check the file upload syntax. If you are uploading the message as a file, make sure to not include the bot prefix in the message. Aborting...")
      #print(file)
    else:
      sheet_link = await sheet_parse.sheet_exist(ctx,userid_ctx, file,username_ctx)
      await ctx.send(f"""Please make a copy of this sheet and fill in **Equipment, Skill Proficiences and attacks manually. \nCopy this Sheet:** {sheet_link}""")
    
  
    @port.error
    async def port_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Bad input', delete_after=20)

    return
my_secret1 = os.environ['DISCORD_TOKEN']
client.run(my_secret1)