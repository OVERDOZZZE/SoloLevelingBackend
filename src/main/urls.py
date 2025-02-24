from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'levels', LevelViewSet)
router.register(r'quests', QuestViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'tips', TipViewSet)


urlpatterns = [
    path('', include(router.urls))
]
