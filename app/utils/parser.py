import asyncio
from bs4 import BeautifulSoup


async def parse_info(html_text: str):
    soup = BeautifulSoup(html_text, "html.parser")

    try:
        developer = soup.find("th", text="Developer").find_next("td").text
    except:
        developer = None
    try:
        os_info = soup.find("th", text="OS").find_next("td").text
    except:
        os_info = None
    try:
        license_info = soup.find("th", text="License").find_next("td").text
    except:
        license_info = None
    
    return {
        "Developer": developer,
        "OS": os_info,
        "License": license_info
    }