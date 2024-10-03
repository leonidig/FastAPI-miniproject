from .. import app
from fastapi import Query
from aiohttp import ClientSession
from ..utils import parse_info
from ..schemas import ParseRequest


@app.get("/get_site")
async def get_site(query_url: ParseRequest = Query(None)):
    async with ClientSession() as session:
        async with session.get(str(query_url.url)) as response:
            html = await response.text()
            if response.status == 200:
                parsed = await parse_info(html)
                return parsed