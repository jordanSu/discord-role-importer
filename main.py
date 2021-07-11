import os
import sys
import csv
import logging
import discord
from discord.errors import HTTPException
from discord.ext import tasks, commands
from dotenv import load_dotenv
load_dotenv()

# Constant in .env file
LOG_PATH = 'add_role.log'
BOT_TOKEN = os.getenv('BOT_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')    # server's ID
ROLE_LIST_FILE = os.getenv('ROLE_LIST_FILE', sys.argv[1] if len(sys.argv) >= 2 else '')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

def combine_name_and_discriminator(name: str, discriminator: str):
    return f'{name}#{discriminator}'

@client.event
async def on_ready():
    guild = client.get_guild(int(GUILD_ID))
    if (guild == None):
        print(f'Cannot get guild with id {GUILD_ID}, please check the GUILD_ID that you provided in .env is correct')
        await client.close()
        return
    
    # fetch members dict in this guild
    member_dict = dict()
    for member in guild.members:
        member_dict[combine_name_and_discriminator(member.name, member.discriminator)] = member

    # fetch roles dict in this guild
    role_dict = dict()
    for role in guild.roles:
        role_dict[role.name] = role
    
    if (ROLE_LIST_FILE == ''):
        print('role list file not specified, please check the ROLE_LIST_FILE that you provided is correct')
        await client.close()
        return
    with open(ROLE_LIST_FILE, newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            user_name = row[0].strip()
            role_list = [role.strip() for role in row[1:]]
            the_member = member_dict.get(user_name, None)
            if (the_member == None): 
                logging.warning(f'Cannot find user "{user_name}" in server')
                continue
            to_add_role_list = [role_dict.get(role, role) for role in role_list]
            for role in to_add_role_list:
                if type(role) == str:
                    logging.warning(f'Cannot find target role "{role}" in server')
                else:
                    try:
                        await the_member.add_roles(role)
                    except HTTPException:
                        logging.warning('HTTPException when add role {role} to user {user_name}')
            
    print(f'Roles importing process complete, you can check {LOG_PATH} for more details')
    await client.close()

if __name__ == '__main__':
    logging.basicConfig(
        filename=LOG_PATH,
        format='%(asctime)s - %(message)s',
        level=logging.WARNING,
        datefmt='%Y-%b-%d %H:%M:%S',
    )
    client.run(BOT_TOKEN)