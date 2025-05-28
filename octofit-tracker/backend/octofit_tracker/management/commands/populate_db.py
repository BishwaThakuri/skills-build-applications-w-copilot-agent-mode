from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Users
        User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams
        Team.objects.create(name='Team Alpha', members=['alice@example.com', 'bob@example.com'])
        Team.objects.create(name='Team Beta', members=['carol@example.com'])

        # Activities
        Activity.objects.create(user='alice@example.com', activity_type='run', duration=30, date=datetime(2025, 5, 1))
        Activity.objects.create(user='bob@example.com', activity_type='walk', duration=45, date=datetime(2025, 5, 2))
        Activity.objects.create(user='carol@example.com', activity_type='cycle', duration=60, date=datetime(2025, 5, 3))

        # Leaderboard
        Leaderboard.objects.create(team='Team Alpha', points=75)
        Leaderboard.objects.create(team='Team Beta', points=60)

        # Workouts
        Workout.objects.create(name='Push Ups', description='Do 20 push ups')
        Workout.objects.create(name='Sit Ups', description='Do 30 sit ups')
        Workout.objects.create(name='Jumping Jacks', description='Do 50 jumping jacks')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
