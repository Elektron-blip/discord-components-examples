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
import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option, create_permission

class Miscellaneous(commands.Cog):

    def __init__(self,client):
        self.client=client
    
    @cog_ext.cog_slash(name='ping', description='Shows you the latency of the bot.')
    async def ping(self,ctx):
        pingEmbed = discord.Embed(title='🏓 Pong!',description=f'Bot latency is `{round(self.client.latency * 1000)}` ms',color=discord.Color.green())
        await ctx.send(embed=pingEmbed)


def setup(client):
    client.add_cog(Miscellaneous(client))