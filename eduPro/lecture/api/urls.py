from django.contrib import admin
from django.urls import path, include

from .views import (
    ArticleListViewSet,
    QuizListViewSet,
    LectureStatusViewSet,
    LectureStatusUpdateViewSet,
    LectureListViewSet,
    LectureDetailViewSet,
    KnowledgeListViewSet,
    VideoLectureListViewSet,
    )


urlpatterns = [
    path('', LectureListViewSet.as_view({'get': 'list'})),
    path('articles/<lecture_id>', ArticleListViewSet.as_view({'get': 'list'})),
    path('quizzes/<lecture_id>', QuizListViewSet.as_view({'get': 'list'})),
    path('knowledges/<lecture_id>', KnowledgeListViewSet.as_view({'get': 'list'})),
    path('video/<lecture_id>', VideoLectureListViewSet.as_view({'get': 'retrieve'})),
    path('status/<lecture_id>', LectureStatusViewSet.as_view({'get': 'retrieve'})),
    path('status/', LectureStatusUpdateViewSet.as_view({'put': 'update'})),
    path('detail/<lecture_id>', LectureDetailViewSet.as_view({'get': 'retrieve'})),
    ]