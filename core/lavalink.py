import pomice
from rich.console import Console
from pythonping import ping

console = Console()
HOST="hfplusapi.ct8.pl"
PORT=25024
PASSWORD="hfplus@lavalink"

def pingServer():
    return ping(f'{HOST}')

async def start_nodes(bot):
    pomice_instance = pomice.NodePool()
    await pomice_instance.create_node(
        bot=bot,
        host=HOST,
        port=PORT,
        password=PASSWORD,
        identifier="MAIN",
        log_handler=None
    )
    console.log("Connected to audio servers")
    console.log("Audio server is now connected!")

console.log("Lavalink core file succesfully loaded")