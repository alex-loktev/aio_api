import aiohttp
import json
from aiohttp import web
from .models import User
from faker import Faker



async def create_user(request):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://dog.ceo/api/breeds/image/random') as response:
            print(response.status)
            faker = Faker()
            body = await response.json()
            user = await User.create(name=faker.name(),
                               avatar_url=body['message'])
            if user is None:
                return web.Response(status=400)
    return web.Response(status=200, text="Success")


async def list_users(request):
    all_users = await User.select('name', 'avatar_url').gino.all()
    resp = json.dump(all_users)
    return web.Response(status=200, text=resp)