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


class Logging(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as: {self.client.user.name}\nWith ID: {self.client.user.id}")

    @commands.Cog.listener()
    async def on_disconnect(self):
        print("Bot has disconnected.")

    @commands.Cog.listener()
    async def on_resumed(self):
        print(
            f"Reconnected as: {self.client.user.name}\nWith ID: {self.client.user.id}"
        )


def setup(client):
    client.add_cog(Logging(client))
