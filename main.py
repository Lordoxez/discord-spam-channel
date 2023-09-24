import aiohttp
import asyncio
import random
import colorama
from colorama import Fore
import string
from time import sleep

message = input(Fore.MAGENTA + "[#] Enter your message >> ")
try:
    print("")
    print(Fore.MAGENTA + "[!] You can pass this one by pressing ENTER.")
    time = int(input(Fore.MAGENTA + "[#] How many seconds is the slowdown cooldown? >> "))
    with open("tokens.txt", "r") as f:
        lines = f.readlines()
    line = len(lines)       
    math = int(time) / int(line)
    print(math)
except:
    math = 0

	
print("")

payload = {
    'content': message
}

channel_id = 1149293336633561149

def word_cool():
    text = "I'm too cool"
    random_text = ''.join(random.choice((c.upper(), c.lower())) for c in text)
    return random_text

async def vouch(file_path, session):
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    line_count = len(lines)  #  it counts the number of lines
    
    tasks = []
    for line in lines:
        token = line.strip()
        headers = {'Authorization': f'{token}'}
        task = asyncio.ensure_future(send_request(session, headers))
        tasks.append(task)
    
    await asyncio.gather(*tasks)
    
    

async def send_request(session, headers):
    sleep(math)
    async with session.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', json=payload, headers=headers) as response:
        if response.status == 200:
            cool_text = word_cool()
            print(f"[{response.status}] Sent to {channel_id} ({cool_text})")
        elif response.status == 429:
            print(f"[{response.status}] Failed to send")
            return

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            await vouch("tokens.txt", session)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
