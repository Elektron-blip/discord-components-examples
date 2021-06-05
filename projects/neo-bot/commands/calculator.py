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
import datetime
import discord
from discord.ext import commands
from discord_components import DiscordComponents
from discord_slash import cog_ext
from modules.calculator import buttons, calculate


class Calculator(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.dc = DiscordComponents(self.client)

    @cog_ext.cog_subcommand(
        base="utilities",
        subcommand_group="calculators",
        name="basic",
        description="A simple calculator. Can't do anything too complex.",
    )
    async def calculator(self, ctx):
        m = await ctx.send(content="Loading Calculators...")
        expression = "None"
        delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        e = discord.Embed(
            title=f"{ctx.author.name}'s calculator",
            description=f"```xl\n{expression}```",
            timestamp=delta,
            color=discord.Colour.blurple(),
        )
        await m.edit(components=buttons, embed=e)
        while m.created_at < delta:
            res = await self.client.wait_for("button_click")
            if (
                res.author.id == ctx.author.id
                and res.message.embeds[0].timestamp < delta
            ):
                expression = res.message.embeds[0].description[6:-3]
                if expression == "None" or expression == "An error occurred.":
                    expression = ""
                if res.component.label == "Exit":
                    await res.respond(content="Calculator Closed", type=7)
                    break
                elif res.component.label == "←":
                    expression = expression[:-1]
                elif res.component.label == "Clear":
                    expression = "None"
                elif res.component.label == "=":
                    expression = calculate(expression)
                elif res.component.label == "x²":
                    expression += "²"
                elif res.component.label == "x³":
                    expression += "³"
                else:
                    expression += res.component.label
                f = discord.Embed(
                    title=f"{ctx.author.name}'s calculator",
                    description=f"```xl\n{expression}```",
                    timestamp=delta,
                    color=discord.Colour.blurple(),
                )
                await res.respond(content="", embed=f, components=buttons, type=7)


def setup(client):
    client.add_cog(Calculator(client))