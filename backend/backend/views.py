from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.template import loader
from database.databasehelper import *
from zenora import APIClient
from urllib import parse
import os
from dotenv import load_dotenv
load_dotenv()

discordToken = os.getenv("DISCORD_TOKEN")
discordClientSecret = os.getenv("DISCORD_CLIENT_SECRET")
REDIRECT_URI = 'http://localhost:8000/oauth/callback'
OATH_URL = f'https://discord.com/api/oauth2/authorize?client_id=1004492570887471106&redirect_uri={parse.quote(REDIRECT_URI)}&response_type=code&scope=identify'


client = APIClient(discordToken, client_secret=discordClientSecret)

def discord_login(request):
    return HttpResponse("logged in u duummy")

def discord_login_callback(request):
    
    message = request.GET.get('code')
    access_token = client.oauth.get_access_token(message, REDIRECT_URI).access_token
    request.session['access_token'] = access_token
    bearer_client = APIClient(access_token, bearer=True)
    current_user = bearer_client.users.get_current_user()
    discordId = str(current_user.id)
    user=None
    try:
        user = get_user_by_discord_id(discordId)
        if user == None:
            username = current_user.username +"#"+ current_user.discriminator
            user = create_user(username,discordId)
            print(user.username)
        return redirect(f"/profile/?user_id={user.userId}")
    except Exception as ex:
        print(ex)
        return HttpResponseBadRequest(f"Some unexpected error has happened" + ex)
def home(request):
    template = loader.get_template('index.html')
    if 'access_token' in request.session:
        bearer_client = APIClient(request.session['access_token'], bearer=True)
        current_user = bearer_client.users.get_current_user()
        user = get_user_by_discord_id(str(current_user.id))
        return redirect(f"/profile/?user_id={user.userId}")
    else:
        context = {
            'oath_url': OATH_URL,
        }
        return HttpResponse(template.render(context,request))
def logout(request):
    request.session.clear()
    return redirect("/")

def search_create_temporary_user(request):
    username = request.GET.get('username')
    user=None
    try:
        user = get_user_by_username(username)
        print("User not found so creatingo ne")
        if user == None:
            discordId = None
            user = create_user(username,discordId)
            print(user.username)
        return redirect(f"/profile/?user_id={user.userId}")
    except Exception as ex:
        print(ex)
        return HttpResponseBadRequest(f"Some unexpected error has happened" + str(ex))
def profile(request):
    template = loader.get_template('profile.html')
    userId = request.GET.get('user_id')
    user = get_user(userId)
    userCards = get_all_cards_for_user(userId)
    allCards = get_all_cards()
    context = {
            'user': user,
            "userCards" : userCards,
            "allCards":allCards
        }
    if 'access_token' in request.session:
        context["session"] = True
    return HttpResponse(template.render(context,request))