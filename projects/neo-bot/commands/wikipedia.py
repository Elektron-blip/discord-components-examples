"""
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
"""
import discord
from discord.ext import commands
from discord_slash import cog_ext
import wikipedia
from discord_slash.utils.manage_commands import create_option


class Wikipedia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_subcommand(
        base="search",
        subcommand_group="wikipedia",
        name="titles",
        description="Does a wikipedia search for you.",
        options=[
            create_option(
                name="query",
                option_type=3,
                description="The thing you wanted to look up.",
                required=True,
            )
        ],
    )
    async def _titles(self, ctx, query: str):
        await ctx.defer()
        e = discord.Embed(
            title=query.title(),
            description="Here is some stuff I found.",
            colour=discord.Colour.blue(),
        )
        for i in wikipedia.search(query, results=25):
            s = wikipedia.summary(i, sentences=5)
            e.add_field(name=i, value=s, inline=False)
        e.set_footer(
            text="If nothing is there, it probably because wikipedia didn't find anything.\nThe maximum number of results is 25 due to a discord limitation."
        )
        e.set_author(
            name="Wikipedia",
            url="https://wikipedia.com",
            icon_url="https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1920px-Wikipedia-logo-v2.svg.png",
        )
        await ctx.send(
            embed=e,
        )


def setup(client):
    client.add_cog(Wikipedia(client))
