#!/usr/bin/env python

from controllers import Music
from aiohttp import web

app = web.Application()
app.router.add_get('/commands/music/{command}', Music.command)

web.run_app(app)




