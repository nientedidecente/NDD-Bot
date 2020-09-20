import os
import sys
import json
import logging.config

# LOAD CONFIG FILE
with open('config.json') as config:
    json_data = json.load(config)


'''
------------------------------------------------
                CONFIG VARIABLES
------------------------------------------------
'''
bot = json_data["bot"]
event = json_data["eventsVars"]

# HiemSword: Yes, i know this loop is not the best method, but it works
for i in json_data["bot"]:
    bot_branch = i["branch"]
    bot_version = i["version"]
    bot_version_dev = i["dev"]
    bot_version_info = i["info"]
    bot_prefix = i["prefix"]
    bot_prefix_dev = i["prefix_dev"]

    addonsEnabled = i["addonsEnabled"]
    addons_dir = i["addons_dir"]

    bot_presence = i["playing_status"]


# ------------|  Join/Left event config variables  |-----

for i in json_data["eventsVars"]:
    for ii in i["join&leave"]:

        welcome_dm = ii["dm_msg"]

        welcome_ch_id = ii["ch_id"]
        welcome_ch_name = ii["ch_name"]

        join_msg = ii["hello_msg"]
        left_msg = ii["bye_msg"]
# ------------|  Extensions variables |-----


addons_list = [""] * 30 # please someone find a better way to do this

# ------------------------------------------------