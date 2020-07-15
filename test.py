import json

# LOAD CONFIG FILE
with open('config.json') as config:
    json_data = json.load(config)

bot = json_data["bot"]
event = json_data["eventsVars"]

#bot_branch = bot["branch"]
#bot_version = bot["version"]


for i in json_data["bot"]:
    bot_branch = i["branch"]
    bot_version = i["version"]



#print(f'Bot variable = {bot}')
#print(f'Event variable = {event}')
print(f'Bot Branch variable = {bot_branch}')
print(bot_version)
#print(f'Bot Version variable = {bot_version}')