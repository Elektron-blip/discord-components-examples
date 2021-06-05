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
from modules.reddit import post_list
from discord_slash.utils.manage_commands import create_option, create_choice


class Reddit(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_subcommand(
        base="reddit",
        subcommand_group="posts",
        name="list",
        description="Send a list of 5 posts from a subreddit you choose.",
        base_desc="Base command for all things reddit.",
        sub_group_desc="Group of commands related to reddit posts.",
        options=[
            create_option(
                option_type=3,
                name="subreddit",
                description="The subreddit you want to get posts from.",
                required=True,
            ),
            create_option(
                option_type=3,
                name="filter",
                description="The filter you want to apply to your results.",
                required=True,
                choices=[
                    create_choice(name="controversial", value="controversial"),
                    create_choice(name="gilded", value="gilded"),
                    create_choice(name="hot", value="hot"),
                    create_choice(name="new", value="new"),
                    create_choice(name="rising", value="rising"),
                    create_choice(name="top", value="top"),
                ],
            ),
        ],
    )
    async def _list(self, ctx, subreddit, filter):
        await ctx.defer()
        embed_list = []
        l = await post_list(subreddit=subreddit, filter=filter)
        for p in l:
            e = discord.Embed(
                title=p.title,
                description=f"[Link to post]({p.url})\nPosted in [{subreddit}](https://reddit.com/r/{subreddit})",
                color=discord.Colour.orange(),
            )
            e.set_image(url=p.url)
            e.set_author(
                name=f"u/{p.author.name}", url=f"https://reddit.com/u/{p.author.name}"
            )
            embed_list.append(e)
            del e
        await ctx.send(embeds=embed_list)


def setup(client):
    client.add_cog(Reddit(client))
