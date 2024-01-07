import json
from rich.console import Console

console = Console()

def get_prefix(bot, message):
    with open('./config/prefixes.json', 'r') as file:
        prefixes = json.load(file)
    server_id = str(message.guild.id)
    return prefixes.get(server_id, '-')

def save_prefix(server_id, new_prefix):
    with open('./config/prefixes.json', 'r') as file:
        prefixes = json.load(file)

    prefixes[server_id] = new_prefix

    with open('./config/prefixes.json', 'w') as file:
        json.dump(prefixes, file, indent=4)

console.log("Prefix core file succesfully loaded!")