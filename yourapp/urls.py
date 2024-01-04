from django.urls import path
from .views import *

urlpatterns = [
    path("main", home),
    path("portfolios/view", view_portfolio, name="view_portfolio"),
    path("messages/view", view_messages, name="view_messages"),
    path("teams/view", view_teams, name="view_teams"),
    
    path("portfolios/update/", update_portfolio, name="update_portfolio"),
    path("messages/update/", update_message, name="update_message"),
    path("teams/update/", update_team, name="update_team"),
    
    path("portfolios/delete/", delete_portfolio, name="delete_portfolio"),
    path("messages/delete/", delete_message, name="delete_message"),
    path("teams/delete/", delete_team, name="delete_team"),
    
    path("portfolios/create/", create_portfolio, name="create_portfolio"),
    path("messages/create/", create_message, name="create_message"),
    path("teams/create/", create_team, name="create_team"),
]