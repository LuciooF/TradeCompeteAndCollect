from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import loader
#from Database.databasehelper import get_user
from zenora import APIClient
from urllib import parse

discordToken = 'yourDiscordToken'
discordClientSecret = 'yourDiscordClientSecret'
REDIRECT_URI = 'http://localhost:8000/oauth/callback'
OATH_URL = f'https://discord.com/api/oauth2/authorize?client_id=1004492570887471106&redirect_uri={parse.quote(REDIRECT_URI)}&response_type=code&scope=identify'


client = APIClient(discordToken, client_secret=discordClientSecret)

def discord_login(request):
    return HttpResponse("logged in u duummy")

def callback(request):
    message = request.GET.get('code')
    access_token = client.oauth.get_access_token(message, REDIRECT_URI).access_token
    request.session['access_token'] = access_token
    
    return redirect("/")
def home(request):
    template = loader.get_template('index.html')
    if 'access_token' in request.session:
        bearer_client = APIClient(request.session['access_token'], bearer=True)
        current_user = bearer_client.users.get_current_user()
        context = {
        'current_user': current_user,
        }
        return HttpResponse(template.render(context,request))
    context = {
        'oath_url': OATH_URL,
    }
    return HttpResponse(template.render(context,request))
def logout(request):
    request.session.clear()
    return redirect("/")

def search_create_discord_user(request):
    discordId = request.GET.get('discordId')
    try:
        print("ASD")
        #get_user(discordId)
    except Exception as ex:
        print(ex)
    
    return redirect("/profile")
def search_create_temporary_user(request):
    username = request.GET.get('username')
    return HttpResponse("Creating user")