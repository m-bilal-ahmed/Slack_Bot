import sys
sys.path.append('c:\\users\\mbila\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\\localcache\\local-packages\\python310\\site-packages')
from http import client
from pydoc import cli
import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
client=slack.WebClient(token=os.environ['SLACK_TOKEN'])
client.chat_postMessage(channel='#test',text= "Hello World!")
