# Views for OctoFit Tracker
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, url_path='obscure-dollop-vqv9r4j97rwcv6p', url_name='codespace-users', methods=['get'])
    def codespace(self, request, format=None):
        """Endpoint for Codespace REST API suffix: obscure-dollop-vqv9r4j97rwcv6p."""
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=False, url_path='obscure-dollop-vqv9r4j97rwcv6p', url_name='codespace-teams', methods=['get'])
    def codespace(self, request, format=None):
        """Endpoint for Codespace REST API suffix: obscure-dollop-vqv9r4j97rwcv6p."""
        teams = self.get_queryset()
        serializer = self.get_serializer(teams, many=True)
        return Response(serializer.data)

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(detail=False, url_path='obscure-dollop-vqv9r4j97rwcv6p', url_name='codespace-activities', methods=['get'])
    def codespace(self, request, format=None):
        """Endpoint for Codespace REST API suffix: obscure-dollop-vqv9r4j97rwcv6p."""
        activities = self.get_queryset()
        serializer = self.get_serializer(activities, many=True)
        return Response(serializer.data)

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

    @action(detail=False, url_path='obscure-dollop-vqv9r4j97rwcv6p', url_name='codespace-leaderboards', methods=['get'])
    def codespace(self, request, format=None):
        """Endpoint for Codespace REST API suffix: obscure-dollop-vqv9r4j97rwcv6p."""
        leaderboards = self.get_queryset()
        serializer = self.get_serializer(leaderboards, many=True)
        return Response(serializer.data)

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    @action(detail=False, url_path='obscure-dollop-vqv9r4j97rwcv6p', url_name='codespace-workouts', methods=['get'])
    def codespace(self, request, format=None):
        """Endpoint for Codespace REST API suffix: obscure-dollop-vqv9r4j97rwcv6p."""
        workouts = self.get_queryset()
        serializer = self.get_serializer(workouts, many=True)
        return Response(serializer.data)
