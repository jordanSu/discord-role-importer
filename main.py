import os
import sys
import csv
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
load_dotenv()

# Constant in .env file
BOT_TOKEN = os.getenv("BOT_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")    # server's ID
ROLE_LIST_FILE = os.getenv("ROLE_LIST_FILE", sys.argv[1] if len(sys.argv) >= 2 else "")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

def combine_name_and_discriminator(name: str, discriminator: str):
    return "{0}#{1}".format(name, discriminator)

@client.event
async def on_ready():
    guild = client.get_guild(int(GUILD_ID))
    if (guild == None):
        print("Cannot get guild with id {0}, please ctrl-C and check it again".format(GUILD_ID))
        return
    
    # fetch members dict in this guild
    member_dict = dict()
    for member in guild.members:
        member_dict[combine_name_and_discriminator(member.name, member.discriminator)] = member

    # fetch roles dict in this guild
    role_dict = dict()
    for role in guild.roles:
        role_dict[role.name] = role
    
    if (ROLE_LIST_FILE == ""):
        print("role list file not specified, please ctrl-C and check it again")
        return
    with open(ROLE_LIST_FILE, newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            user_name = row[0].strip()
            role_list = row[1:]
            the_member = member_dict.get(user_name, None)
            if (the_member == None): 
                continue
            to_add_role_list = [role_dict.get(role, "") for role in role_list]
            await the_member.add_roles(*to_add_role_list)
            
    print("All roles are added, you can now safely ctrl-C this process")

if __name__ == '__main__':
    client.run(BOT_TOKEN)