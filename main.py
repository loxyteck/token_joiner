import concurrent.futures
import random
import string
from pystyle import Anime , Center, Colorate, Colors, Write
import webbrowser
import tls_client
from colorama import Fore, Style
import auth
import os
import fade

os.system("cls")


from dataclasses import dataclass
import tls_client

@dataclass
class JoinerData:
    pass

@dataclass
class Instance(JoinerData):
    client: tls_client.sessions
    token: str
    invite: str
    headers: dict

class OtherInfo:
    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'sv,sv-SE;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9016 Chrome/108.0.5359.215 Electron/22.3.12 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'sv-SE',
        'x-discord-timezone': 'Europe/Stockholm',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDE2Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InN2IiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMTYgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMTIgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMTIiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyMTg2MDQsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjM1MjM2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
    }

    colortable = {
        "green":"#65fb07",
        "red":"#Fb0707",
        "yellow":"#c4bc18",
        "magenta":"#b207f5",
        "blue":"#001aff",
        "cyan":"#07baf5",
        "gray":"#3a3d40",
        "white":"#ffffff",
        "pink":"#c203fc"
    }
                                                                                                                   
class Joiner:
    def __init__(self, data: auth.Instance) -> None:
        self.session = data.client
        self.session.headers = data.headers
        self.get_cookies()
        self.instance = data

    def rand_str(self, length: int) -> str:
        return ''.join(random.sample(string.ascii_lowercase + string.digits, length))

    def get_cookies(self) -> None:
        site = self.session.get("https://discord.com")
        self.session.cookies = site.cookies

    def join(self) -> None:
        self.session.headers.update({"Authorization": self.instance.token})
        result = self.session.post(f"https://discord.com/api/v9/invites/{self.instance.invite}", json={
            'session_id': self.rand_str(32),
        })

        if result.status_code == 200:
            input(f"\n[\x1b[38;5;46m+\x1b[0m] Joined server\n")

        else:
            input(f"\n[\x1b[38;5;9m-{Fore.RESET}] Failed to join server, Status code: {result.status_code}\n")

class logger:
    colors_table = auth.OtherInfo.colortable

    @staticmethod
    def printk(text) -> None:
        print(f"[>] {text}")

    @staticmethod
    def convert(color):
        return color if color.__contains__("#") else logger.colors_table[color]

    @staticmethod
    def color(opt, obj):
        return f"{logger.convert(opt)}{obj}{Style.RESET_ALL}"

    banner = '''
    
               ░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
               ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
               ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
               ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░  
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
         ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                                                                                                                             
                        Token Joiner ~ https://discord.gg/tiktokbot                                                                                                                                                                                                                               
'''
    faded_text = fade.purplepink(banner)
    print(faded_text)
                                                         

class intilize:
    @staticmethod
    def start(i):
        Joiner(i).join()
        
if __name__ == '__main__':
    with open("tokens.txt") as file:
        tokens = [line.strip() for line in file]

    instances = []
    max_threads = 5
    invite = input(Fore.GREEN + "Enter Link -> ")
    
    try:
        invite=invite.split("/")[-1]
    except:
        pass

    for token_ in tokens:
        header = auth.OtherInfo.headers
        instances.append(
            auth.Instance(
                client=tls_client.Session(
                    client_identifier=f"chrome_{random.randint(110, 115)}",
                    random_tls_extension_order=True,
                ),
                token=token_,
                headers=header,
                invite=invite,
            )
        )

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        for i in instances:
            executor.submit(intilize.start, i)
