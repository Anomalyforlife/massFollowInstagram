import time
from instagrapi import Client
import random

global cl
global user_username, user_password
user_username = "sus"
user_password = "ciao"
cl = Client()
cl.login(user_username, user_password)
ClientID = cl.user_id_from_username(user_username)