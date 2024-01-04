from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Portfolio, Team, Message

def home(request):
    messages = Message.objects.all()
    messages_filter = Message.objects.filter(name = "otabek")
    message = Message.objects.get(id = 1)
    context = {
        "messages":messages,
        "messages_filter":messages_filter,
        "message":message,
    }
    return HttpResponse("Home page  assalomu aleykum")

def view_portfolio(request):
    try:
        portfolios = Portfolio.objects.all()
        response_content = ""
        for portfolio in portfolios:
            response_content += f"Portfolio: {portfolio.type}, {portfolio.title}\n"
        return HttpResponse(response_content)
    except Portfolio.DoesNotExist:
        return HttpResponse("No portfolios found")

def view_messages(request):
    try:
        messages = Message.objects.all()
        response_content = ""
        for message in messages:
            response_content += f"Message: {message.name}, {message.email}, {message.message}\n"
        return HttpResponse(response_content)
    except Message.DoesNotExist:
        return HttpResponse("No messages found")

def view_teams(request):
    try:
        teams = Team.objects.all()
        response_content = ""
        
        for team in teams:
            response_content += f"Team: {team.name}, {team.position}, {team.about}\n"
        
        return HttpResponse(response_content)
    except Team.DoesNotExist:
        return HttpResponse("No teams found")

def update_portfolio(request):
    try:
        portfolio = Portfolio.objects.get(id=1)
        portfolio.type = 'Updated Type'
        portfolio.title = 'Updated Portfolio'
        portfolio.save()
        return HttpResponse("Portfolio updated successfully")
    except Portfolio.DoesNotExist:
        raise Http404("Portfolio does not exist")

def update_message(request):
    try:
        message = Message.objects.get(id=1)
        message.name = 'Updated Name'
        message.email = 'updated@email.com'
        message.message = 'Updated Message'
        message.save()
        return HttpResponse("Message updated successfully")
    except Message.DoesNotExist:
        raise Http404("Message does not exist")

def update_team(request):
    try:
        team = Team.objects.get(id=1)
        team.name = 'Updated Team Name'
        team.position = 'Updated Position'
        team.img = 'updated_image.jpg'
        team.about = 'Updated About'
        team.save()
        return HttpResponse("Team updated successfully")
    except Team.DoesNotExist:
        raise Http404("Team does not exist")

def delete_portfolio(request):
    try:
        portfolio = Portfolio.objects.get(id = 2)
        portfolio.delete()
        return HttpResponse("portfolio deleted succesfully")
    except Portfolio.DoesNotExist:
        raise Http404("Portfolio does not exist")
    
def delete_message(request):
    try:
        message = Message.objects.get(id=2)  # Replace 2 with the desired ID
        message.delete()
        return HttpResponse("Message deleted successfully")
    except Message.DoesNotExist:
        raise Http404("Message does not exist")
    
def delete_team(request):
    try:
        team = Team.objects.get(id=2)  # Replace 2 with the desired ID
        team.delete()
        return HttpResponse("Team deleted successfully")
    except Team.DoesNotExist:
        raise Http404("Team does not exist")
    
def create_portfolio(request):
    portfolio = Portfolio.objects.create(
        sort = 1,
        title = "birinchi portfolio",
        img = "image.jpg"
    )
    return HttpResponse("portfolio created succesfully")

def create_message(request):
    message = Message.objects.create(
        name="zoirbek Tukhtasinov",
        email="Zoirbek@example.com",
        message="message uchun misol"
    )
    return HttpResponse("Message created successfully")

def create_team(request):
    team = Team.objects.create(
        name="Zoirbek To'xtasinov",
        position="Backend Developer",
        img="image.jpg",
        about="qisqacha tafsilot"
    )
    return HttpResponse("Team member created successfully")