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
from discord.ext import commands
from discord_slash import cog_ext
from modules.randomizer import Random
from discord_slash.utils.manage_commands import create_option

class Randomiser(commands.Cog):

    def __init__(self,client):
        self.client=client

    @cog_ext.cog_subcommand(
        base='random',
        subcommand_group='generator',
        name='integers',
        base_desc='Does something random for you.',
        sub_group_desc='Generates somethign rnadom for you.',
        description='Generates a random ineteger using the variables you specify.',
        options=[
            create_option(
                name='start',
                description='The starting integer for your randomiser.',
                required=False,
                option_type=4,
            ),
            create_option(
                name='end',
                description='The ending integer for your randomiser.',
                required=False,
                option_type=4
            ),
            create_option(
                name='hidden',
                description='You get to decide whether the result is hidden or not. Defaults to shown.',
                required=False,
                option_type=5,
            )
        ]
    )
    async def _integers(self,ctx,start=-2147483648, end=2147483647, hidden=False):
        i= await Random.generator(start=start, end=end)
        await ctx.send(f'Your random number is: {i}.',hidden=hidden)

    @cog_ext.cog_subcommand(
        base='random',
        subcommand_group='generator',
        name='coin',
        description='Gives you a heads or tails output.',
        options=[
            create_option(
                name='hidden',
                description='You get to decide whether the result is hidden or not. Defaults to shown.',
                required=False,
                option_type=5,
            )
        ]
    )
    async def _coin(self,ctx,hidden=False):
        await ctx.send(f'It is {await Random.coin()}!',hidden=hidden)

    @cog_ext.cog_subcommand(
        base='random',
        subcommand_group='selector',
        name='list',
        description='Selects something from the input list and returns it to you.',
        options=[
            create_option(
                name='elements',
                option_type=3,
                description='Seperate all the elements of your list using \',\'',
                required=True
            ),
            create_option(
                name='hidden',
                description='You get to decide whether the result is hidden or not. Defaults to shown.',
                required=False,
                option_type=5,
            )
        ]
    )
    async def _choice(self, ctx, elements,hidden=False):
        await ctx.send(f"The choice is: {await Random.selector(elements.split(','))}", hidden=hidden)

def setup(client):
    client.add_cog(Randomiser(client))