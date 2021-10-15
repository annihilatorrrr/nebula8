#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import os
from dotenv import load_dotenv

params = load_dotenv()


class Config(object):
     ###########################
     ##   DATABASE SETTINGS  ##
     ##########################
     HOST = os.environ.get('MYSQL_HOST')
     PORT = int(os.environ.get('MYSQL_PORT'))
     USER = os.environ.get('MYSQL_USER')
     PASSWORD = os.environ.get('MYSQL_PASSWORD')
     DBNAME = os.environ.get('MYSQL_DBNAME')
     ###########################
     ##   TELEGRAM SETTINGS  ##
     ##########################
     BOT_TOKEN = os.environ.get('TOKEN')
     OWNER = {
        'foo': 123456789,
        'bar': 123456789
     }
     DEFAULT_WELCOME = os.environ.get('TG_DEFAULT_WELCOME')
     DEFAULT_RULES = os.environ.get('TG_DEFAULT_RULES')
     DEFAULT_LOG_CHANNEL = os.environ.get('TG_DEFAULT_LOG_CHANNEL')
     DEFAULT_STAFF_GROUP = os.environ.get('TG_DEFAULT_STAFF_GROUP')
     ##########################
     ##   PROJECT SETTINGS   ##
     ##########################
     OPENWEATHER_API = os.environ.get('OPENWEATHER_TOKEN')
     ENABLE_PLUGINS = True
     DEFAULT_LANGUAGE = "EN"
     VERSION = '8.1.8'
     VERSION_NAME = 'Hatterene'
     REPO = 'https://github.com/Squirrel-Network/nebula8'
     DEBUG = False