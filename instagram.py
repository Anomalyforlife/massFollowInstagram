import time
from instagrapi import Client
import random

from discordWebhookNotifier import sendLog
global cl
global user_username, user_password

def Login(username, password):
    global cl
    global user_username, user_password
    user_username = username
    user_password = password
    cl = Client()
    cl.login(user_username, user_password)
    ClientID = cl.user_id_from_username(username)
    sendLog(f"[MESSAGE] Login eseguito correttamente come {username}")
    return cl.user_info(ClientID)


def TakeFollowers(username):
    global cl
    global user_username, user_password
    followers = cl.user_followers_gql_chunk(cl.user_id_from_username(username))
    cl.login(user_username, user_password)
    sendLog(f"[MESSAGE] Login eseguito correttamente come {user_username}")
    sendLog(f"[ACTION] Ho letto {len(followers[0])} followers dall'utente {username}")
    for x in followers[0]:
        cl.user_follow(cl.user_id_from_username(x.username))
        timetowait = random.randint(360, 480)
        time.sleep(timetowait)
        print(f"Followed {x.username} in {timetowait}s")
        sendLog(f"[ACTION] Seguito l'utente {x.username} in {timetowait}s")
    return "success"

def removeNotFollowingBack():
    global cl
    global user_username, user_password
    cl.login(user_username, user_password)
    sendLog(f"[MESSAGE] Login eseguito correttamente come {user_username}")
    ClientID = cl.user_id_from_username(cl.username)
    myFollowing = cl.user_following(ClientID)
    myFollowers = cl.user_followers_gql_chunk(ClientID)
    array = []
    for y in myFollowers[0]:
        array.append(y.username)

    for x in myFollowing.items():
        if x[1].username not in array:
            cl.user_unfollow(cl.user_id_from_username(x[1].username))
            timetowait = random.randint(180, 240)
            print(f"Unfollowed {x[1].username} in {timetowait}s")
            time.sleep(timetowait)
            sendLog(f"[ACTION] Ho smesso di seguire l'utente {x[1].username} in {timetowait}s")
    return "success"