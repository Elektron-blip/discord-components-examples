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
import yaml
import discord
from discord.ext import commands
from discord.http import Route
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option
from discord_components import DiscordComponents, Button, ButtonStyle

class Entertainment(commands.Cog):

    def __init__(self,client):
        self.client=client
        self.dc=DiscordComponents(self.client)
        self.known_activities=yaml.safe_load(open('config/activities.yaml', 'r'))

    @cog_ext.cog_subcommand(
        base='entertainment',
        subcommand_group='voice',
        name='activites',
        base_desc='All the entertainment command of the bot',
        sub_group_desc='All the voice channel entertainment.',
        description='Discord activities. They are a lot of fun.',
        options=[
            create_option(
                name='hidden',
                description='Choose whether you want the responses to be hidden or not.',
                option_type=5,
                required=False
            )
        ]
    )
    async def _activities(self,ctx,hidden=False):
        m = await ctx.send(content='<a:typing:597589448607399949> Neo Bot is thinking...',hidden=hidden)
        components=[]
        for k, _i in self.known_activities.items():
            components.append(Button(style=ButtonStyle.blue, label=k))
        await m.edit(
            content='Here are your choices.',
            components=components,
            hidden=hidden
        )
        res = await self.client.wait_for('button_click',timeout=60)
        if not res:
            await ctx.channel.send('Too Late')
        else:
                voice = ctx.author.voice

                if not voice:
                    return await res.respond(content='You have to be in a voice channel to use this command.', type=7)

                r = Route('POST', '/channels/{channel_id}/invites', channel_id=voice.channel.id)

                payload = {
                    'max_age': 60,
                    'target_type': 2,
                    'target_application_id': self.known_activities[res.component.label]
                }

                try:
                    code = (await self.client.http.request(r, json=payload))['code']
                except discord.Forbidden:

                    return await res.respond(content='I Need the `Create Invite` permission.', type=7)

                await res.respond(embed=discord.Embed(description=f'[Click here!](https://discord.gg/{code})\nLink expires in 1 minute', color=discord.Colour.red()),type=7)

def setup(client):
    client.add_cog(Entertainment(client))