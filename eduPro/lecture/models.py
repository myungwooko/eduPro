import uuid

from django.conf import settings
from django.db import models
from model_utils import Choices

from user.models import User
from django.template.defaultfilters import truncatechars
from .methods import Methods


M = Methods()

class ImageResource(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, auto_created=True, primary_key=True, help_text="이미지 ID")
    image_file = models.FileField(blank=False, null=False, upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일')

    def __str__(self):
        return str(self.image_file).split('/')[1]

    @property
    def image_name(self):
        return str(self.image_file).split('/')[1]

    # @property
    # def image_url(self):
    #     return settings.MEDIA_URL_PREFIX + str(self.image_file)

    class Meta:
        managed = True
        db_table = 'ImageResource'


class Article(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, auto_created=True, primary_key=True, help_text="기사 ID")
    title = models.CharField(max_length=255, null=False, blank=False, help_text='제목')
    author = models.CharField(max_length=255, null=True, blank=True, help_text='기자이름')
    published_at = models.DateTimeField(null=False, blank=True, db_column='published_at', help_text='기사배포일자')
    agency = models.CharField(max_length=30, null=False, blank=False, help_text='언론사')
    summary = models.TextField(null=False, blank=False, help_text='요약')
    body = models.TextField(null=False, blank=False, help_text='본문')
    thumbnail = models.ForeignKey(ImageResource, null=False, on_delete=models.CASCADE, related_name='Articles', help_text='썸네일')

    def __str__(self):
        return self.title

    @property
    def short_description(self):
        return truncatechars(self.summary, 40)

    class Meta:
        managed = True
        db_table = 'Article'


class Lecture(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, auto_created=True, primary_key=True, help_text="강의 ID")
    episode = models.IntegerField(null=False, blank=False, help_text='강의회차')
    title = models.CharField(max_length=255, null=False, blank=False, help_text='제목')
    subtitle = models.CharField(max_length=255, null=False, blank=False, help_text='부제목')
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일')
    article = models.ManyToManyField(Article, related_name='lectures')

    def __str__(self):
        return f"{self.episode}강: {self.title}"

    class Meta:
        managed = True
        db_table = 'Lecture'


class Knowledge(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, auto_created=True, primary_key=True, help_text="금융상식 ID")
    number = models.IntegerField(null=False, blank=False, help_text='금융상식순서 번호')
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일')
    thumbnail = models.ManyToManyField(ImageResource, related_name='knowledges')
    lecture = models.ForeignKey(Lecture, null=False, on_delete=models.CASCADE, related_name='knowledges')

    def __str__(self):
        return f"Knowledge id: {self.id} number: {self.number}"

    class Meta:
        managed = True
        db_table = 'Knowledge'


class LectureStatus(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, auto_created=True, primary_key=True, help_text="강의상태 ID")
    user = models.ForeignKey(User, null=False, blank=False, db_column='user_id', on_delete=models.CASCADE,
                                related_name='lecture_status', help_text='유저 ID')
    lecture = models.ForeignKey(Lecture, null=False, blank=False, db_column='lecture_id', on_delete=models.CASCADE,
                                   related_name='lecture_status', help_text='강의 ID')
    view_complete_sec = models.FloatField(default=0, help_text='영상시청 완료시간')
    quiz_pass = models.BooleanField(default=False, db_column='quiz_pass', help_text='퀴즈 통과 여부')
    video_pass = models.BooleanField(default=False, db_column='viewing_completion_pass', help_text='동영상 시청 완료 여부')
    pass_date = models.DateTimeField(null=True, blank=True, db_column='pass_date', help_text='통과 완료일(동영상 + 퀴즈)')
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일')

    def __str__(self):
        return f"user: {self.user.username} lecture_id: {self.lecture.title}"

    class Meta:
        managed = True
        db_table = 'LectureStatus'
        unique_together = ('user', 'lecture',)


class Quiz(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, auto_created=True, primary_key=True, help_text="퀴즈 ID")
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, help_text='강의 ID')
    question = models.CharField(max_length=255, null=False, blank=False, help_text='퀴즈내용')
    number = models.IntegerField(null=False, blank=False, help_text='퀴즈순서 번호')
    choices = models.CharField(max_length=225, null=False, blank=False, help_text='선택지')
    hint = models.CharField(max_length=255, null=False, blank=False, help_text='힌트')
    answer = models.IntegerField(null=False, blank=False, help_text='정답번호')

    def __str__(self):
        return f"Lecture: {self.lecture.title} number: {self.number} question: {self.question} answer: {self.answer}"

    class Meta:
        managed = True
        db_table = 'Quiz'


class VideoLecture(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, auto_created=True, primary_key=True, help_text="영상 ID")
    lecture = models.OneToOneField(Lecture, null=False, blank=False, on_delete=models.CASCADE, help_text='강의 ID')
    url = models.CharField(max_length=255, null=False, blank=False, help_text='동영상 url')
    outline = models.TextField(null=False, blank=False, help_text='강의개요')
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일')

    def __str__(self):
        return f"Lecture: {self.lecture} url: {self.url}"

    class Meta:
        managed = True
        db_table = 'VideoLecture'