"""
URL configuration for octofit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activity', views.ActivityViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)
router.register(r'workouts', views.WorkoutViewSet)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import re_path

@api_view(['GET'])
def api_root(request, format=None):
    base_url = request.build_absolute_uri('/')
    codespace_url = 'https://obscure-dollop-vqv9r4j97rwcv6p-8000.app.github.dev/api/'
    return Response({
        'users': codespace_url + 'users/',
        'teams': codespace_url + 'teams/',
        'activity': codespace_url + 'activity/',
        'leaderboard': codespace_url + 'leaderboard/',
        'workouts': codespace_url + 'workouts/',
        'local_users': base_url + 'api/users/',
        'local_teams': base_url + 'api/teams/',
        'local_activity': base_url + 'api/activity/',
        'local_leaderboard': base_url + 'api/leaderboard/',
        'local_workouts': base_url + 'api/workouts/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^$', api_root, name='api-root'),
]
