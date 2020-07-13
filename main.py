import aiohttp
import asyncio
from aiohttp import web
from project.urls import urls
from project.models import db


async def connect_db(app):
    await db.set_bind('postgresql://postgres:radist@localhost:5432/postgres')
    await db.gino.create_all()


async def close_db(app):
    await db.pop_bind().close()


def main():
    app = web.Application()
    app.add_routes(urls)
    app.on_startup.append(connect_db)
    app.on_shutdown.append(close_db)
    web.run_app(app)


if __name__ == "__main__":
   main()