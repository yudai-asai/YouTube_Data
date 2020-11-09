import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

YouTube_API_KEY = os.environ.get("YouTube_API_KEY")
CHANNEL_ID = os.environ.get("CHANNEL_ID")
SLACK_URL = os.environ.get("SLACK_URL")
