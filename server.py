import os
import asyncio

from aiohttp import web
from aiohttp_swagger import setup_swagger

from db import init_pg, close_pg
from middlewares import setup_middlewares
from modules import documents, auth


def init(loop):
    app = web.Application(loop=loop)

    app.on_startup.append(init_pg)
    app.on_startup.append(auth.models.setup_models)
    app.on_startup.append(documents.models.setup_models)
    app.on_cleanup.append(close_pg)

    auth.routes.setup_routes(app)
    documents.routes.setup_routes(app)

    setup_middlewares(app)

    setup_swagger(app)

    return app


def run(args):
    loop = asyncio.get_event_loop()
    app = init(loop)
    web.run_app(app)