from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import dashboard
from . import views

from .views import (
    calendar_page,
    calendar_events_view,
    SubjectViewSet,
    TopicViewSet,
    UserAvailabilityViewSet,
    StudyScheduleViewSet,
    generate_schedule_view,
)


router = DefaultRouter()
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'topics', TopicViewSet, basename='topic')
router.register(r'availability', UserAvailabilityViewSet, basename='availability')
router.register(r'study-schedules', StudyScheduleViewSet, basename='schedule')

urlpatterns = [
    path('calendar/', calendar_page, name='calendar-page'),
    path('', calendar_page, name='calendar'),
    path('api/calendar-events/', calendar_events_view, name='calendar-events'),
    path('api/generate-schedule/', generate_schedule_view, name='generate-schedule'),
    path('api/', include(router.urls)),
    path('dashboard/', dashboard, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('generate-schedule/', views.generate_schedule_view, name='generate_schedule'),
]



