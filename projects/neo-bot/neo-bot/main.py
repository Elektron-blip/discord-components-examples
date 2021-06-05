'''
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/. */
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
<!-- This Source Code Form is subject to the terms of the Mozilla Public
   - License, v. 2.0. If a copy of the MPL was not distributed with this
   - file, You can obtain one at https://mozilla.org/MPL/2.0/. -->
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
'''
import os
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_components import DiscordComponents

client = commands.Bot(
  command_prefix='-',
  intents=discord.Intents.all(),
  status=discord.Status.dnd,
  activity=discord.Activity(
    name='Slash Commands',
    type=discord.ActivityType.competing,
  )
)
slash = SlashCommand(client, sync_commands=True)

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')
        print(f'Loaded command: {filename[:-3]}')

for filename in os.listdir('./events'):
    if filename.endswith('.py'):
        client.load_extension(f'events.{filename[:-3]}')
        print(f'Loaded event: {filename[:-3]}')

client.run(os.environ['TOKEN'])