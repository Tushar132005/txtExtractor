#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7416420875:AAGdE9IJUTwabPWuOo-Vleln05wpWEvRp6c
    API_ID = int(os.environ.get("API_ID", "24798261"))
    API_HASH = os.environ.get("API_HASH", "fef280037f5759eccc540c6d7a279a14")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6155478725")
