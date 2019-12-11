from django.contrib import admin
from django.utils import timezone

from .models import Lecture, LectureStatus, Article, Quiz, Knowledge, VideoLecture, ImageResource


@admin.register(ImageResource)
class ImageResourceAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('image_name', 'created_at', 'updated_at')
    search_fields = ('image_file', )

    def get_ordering(self, request):
        return ['image_file']


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('episode', 'title', 'subtitle', 'created_at', 'updated_at')
    search_fields = ('title', 'episode')

    def get_ordering(self, request):
        return ['episode']


@admin.register(LectureStatus)
class LectureStatusAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('user', 'lecture', 'view_complete_sec', 'quiz_pass',
                    'video_pass', 'pass_date', 'created_at', 'updated_at')
    search_fields = ('user__email', 'lecture__episode')

    def get_ordering(self, request):
        return ['user']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('title', 'author', 'published_at', 'agency', 'short_description', 'thumbnail')
    search_fields = ('thumbnail__image_file', 'id', 'title', 'agency', 'published_at')

    def get_ordering(self, request):
        return ['published_at']


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('lecture', 'number', 'question', 'choices', 'answer', 'hint')
    search_fields = ('lecture__episode', 'question', 'number')

    def get_ordering(self, request):
        return ['lecture', 'number']


@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('lecture', 'number', 'created_at', 'updated_at')
    search_fields = ('number', 'lecture__episode')

    def get_ordering(self, request):
        return ['lecture__id', 'number']


@admin.register(VideoLecture)
class VideoLectureAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('lecture', 'url', 'created_at', 'updated_at')
    search_fields = ('lecture__episode', 'url')

    def get_ordering(self, request):
        return ['lecture', 'updated_at']