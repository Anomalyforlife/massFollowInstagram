from quart import Quart, render_template, request
from instagram import Login, TakeFollowers, removeNotFollowingBack
from quart_cors import cors
from threading import Thread
import os

global account_data

app = Quart(__name__, static_folder="static", static_url_path="/")
app = cors(app, allow_origin="*")

@app.route('/')
async def index():
    return await render_template('login.html')

@app.route('/login-phase', methods=['POST'])
async def my_form_post():
    global account_data
    username = (await request.form)['username']
    password = (await request.form)['password']
    account_data = Login(username,password)
    name = account_data.full_name
    propic = account_data.profile_pic_url
    biography = account_data.biography
    return await render_template("profile.html", username=name, bio=biography, propic=propic)

@app.route('/follow_page')
async def followpage():
    global account_data
    try:
        name = account_data.full_name
        propic = account_data.profile_pic_url
    except:
        name = "ERROR"
        propic = "https://cdn.discordapp.com/attachments/763000112234364928/996846331576463360/round-error-icon-16.jpg?width=200&height=200"
    return await render_template("follow.html", username=name, propic=propic)

@app.route('/follow', methods=['POST'])
async def follow():
    global account_data
    name = account_data.full_name
    propic = account_data.profile_pic_url
    username = (await request.form)['username']
    thr = Thread(target=TakeFollowers, args=[username])
    thr.start()
    return await render_template("initialized.html", username=name, propic=propic, text="Follow Session Inizialized.")

@app.route('/unfollow', methods=['POST'])
async def unfollow():
    global account_data
    name = account_data.full_name
    propic = account_data.profile_pic_url
    thr = Thread(target=removeNotFollowingBack)
    thr.start()
    return await render_template("initialized.html", username=name, propic=propic, text="unFollow Session Inizialized.")

PORT = os.environ.get('PORT')
app.run('0.0.0.0', PORT or 8000)