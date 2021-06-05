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
import os
import asyncpraw

reddit = asyncpraw.Reddit(
    client_id=os.environ["R_CLIENT_ID"],
    client_secret=os.environ["R_CLIENT_SECRET"],
    user_agent=os.environ["R_USER_AGENT"],
)


async def post_list(subreddit, filter):
    sr = await reddit.subreddit(subreddit, fetch=True)
    sm_list = []
    if filter == "controversial":
        async for sm in sr.controversial(limit=5):
            sm_list.append(sm)
    if filter == "gilded":
        async for sm in sr.gilded(limit=5):
            sm_list.append(sm)
    if filter == "hot":
        async for sm in sr.hot(limit=5):
            sm_list.append(sm)
    if filter == "new":
        async for sm in sr.new(limit=5):
            sm_list.append(sm)
    if filter == "rising":
        async for sm in sr.rising(limit=5):
            sm_list.append(sm)
    if filter == "top":
        async for sm in sr.top(limit=5):
            sm_list.append(sm)
    return sm_list
