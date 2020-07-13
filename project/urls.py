from aiohttp import web
from .views import *

urls = [
    web.get('/', create_user),
    web.get('/all', list_users),
]