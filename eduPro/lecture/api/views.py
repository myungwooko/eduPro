import datetime

from django.forms.models import model_to_dict
from rest_framework import serializers

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework import parsers, filters, serializers

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    GenericAPIView,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)

from user.models import User
from lecture.models import (
    ImageResource,
    Article,
    Lecture,
    Knowledge,
    LectureStatus,
    Quiz,
    VideoLecture
    )

from .serializers import (
    LectureSerializer,
    ArticleSeializer,
    QuizSerializer,
    LectureStatusSerializer,
    LectureStatusUpdateSerializer,
    LectureDetailSerailizer,
    KnowledgeSerializer,
    VideoLectureSerializer,
    )


class ArticleListViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = ArticleSeializer

    def list(self, request, *args, **kwargs):
        lecture_id = kwargs["lecture_id"]
        queryset = self.filter_queryset(self.get_queryset(), lecture_id=lecture_id)
        queryset = queryset[0].article.all()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        try:
            serializer = self.get_serializer(queryset, many=True)
        except:
            raise serializers.ValidationError("No matching Data")

        return Response(serializer.data)

    def filter_queryset(self, queryset, lecture_id):
        return queryset.filter(id=lecture_id)


class QuizListViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def list(self, request, *args, **kwargs):
        lecture_id = kwargs["lecture_id"]
        queryset = self.filter_queryset(self.get_queryset(), lecture_id=lecture_id)
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        try:
            serializer = self.get_serializer(queryset, many=True)
        except:
            raise serializers.ValidationError("No matching Data")

        return Response(serializer.data)

    def filter_queryset(self, queryset, lecture_id):
        return queryset.filter(lecture=lecture_id)


class LectureStatusViewSet(viewsets.ModelViewSet):
    queryset = LectureStatus.objects.all()
    serializer_class = LectureStatusSerializer

    def retrieve(self, request, **kwargs):
        user_id = request.user.id
        lecture_id = kwargs.get('lecture_id', '')
        try:
            lecture_status = LectureStatus.objects.get(lecture=lecture_id, user=user_id)
        except Exception as e:
            return Response(e, status=HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(lecture_status)
            return Response(serializer.data)


class LectureStatusUpdateViewSet(viewsets.ModelViewSet):
    queryset = LectureStatus.objects.all()
    serializer_class = LectureStatusUpdateSerializer

    def update(self, request, *args, **kwargs):
        up_data = request.data
        user_id = request.user.id
        lecture_id = up_data.get('lecture', None)
        view_complete_sec = up_data.get('view_complete_sec', None)
        video_pass = up_data.get('video_pass', None)
        quiz_pass = up_data.get('quiz_pass', None)
        pass_date = datetime.datetime.now().date()

        if not user_id or not lecture_id:
            return Response('Should fill valid user_id and lecture_id out', status=HTTP_400_BAD_REQUEST)
        try:
            # true를 false로 바꾸는 경우는 없을 것이므로 false를 update하는 경우는 고려하지 않는다.
            # 있는지 없는지에 대한 체크만 진행하면 된다.
            lec_status_qs = LectureStatus.objects.filter(user_id=user_id, lecture=lecture_id)
            if video_pass:
                lec_status_qs.update(video_pass=video_pass)
            if quiz_pass:
                lec_status_qs.update(quiz_pass=quiz_pass)
            if view_complete_sec:
                lec_status_qs.update(view_complete_sec=view_complete_sec)
            lec_status_qs = LectureStatus.objects.filter(user=user_id, lecture=lecture_id)
            lec_status = lec_status_qs[0]
            if lec_status.video_pass and lec_status.quiz_pass:
                pass_date = datetime.datetime.now().date()
                lec_status_qs.update(pass_date=pass_date)
        except Exception as e:
            return Response(str(e), status=HTTP_400_BAD_REQUEST)

        updated = LectureStatus.objects.get(user=user_id, lecture=lecture_id)
        created_at = updated.created_at
        updated_at = updated.updated_at
        updated = model_to_dict(updated)
        updated["created_at"] = created_at
        updated["updated_at"] = updated_at

        return Response(updated)


class LectureListViewSet(viewsets.ModelViewSet):
    queryset = LectureStatus.objects.prefetch_related().all()
    serializer_class = LectureStatusSerializer

    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        queryset = self.filter_queryset(self.get_queryset(), user_id=user_id)
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        try:
            serializer = self.get_serializer(queryset, many=True)
        except Exception as e:
           raise serializers.ValidationError(str(e))

        return Response(serializer.data)

    def filter_queryset(self, queryset, user_id):
        return queryset.filter(user=user_id)


class LectureDetailViewSet(viewsets.ModelViewSet):
    queryset = LectureStatus.objects.prefetch_related().all()
    serializer_class = LectureDetailSerailizer

    def retrieve(self, request, *args, **kwargs):
        user_id = request.user.id
        lecture_id = kwargs["lecture_id"]
        instance = self.filter_queryset(self.get_queryset(), user_id=user_id, lecture_id=lecture_id)
        try:
            serializer = self.get_serializer(instance[0])
        except Exception as e:
           Response(str(e), status=HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data)

    def filter_queryset(self, queryset, user_id, lecture_id):
        return queryset.filter(user=user_id, lecture=lecture_id)


class KnowledgeListViewSet(viewsets.ModelViewSet):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializer
    # permission_classes = [AllowAny,]

    def list(self, request, *args, **kwargs):
        lecture_id = kwargs["lecture_id"]
        queryset = self.filter_queryset(self.get_queryset(), lecture_id=lecture_id)
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        try:
            serializer = self.get_serializer(queryset, many=True)
        except:
            raise serializers.ValidationError("No matching Data")

        return Response(serializer.data)

    def filter_queryset(self, queryset, lecture_id):
        return queryset.filter(lecture=lecture_id)


class VideoLectureListViewSet(viewsets.ModelViewSet):
    queryset =VideoLecture.objects.all()
    serializer_class = VideoLectureSerializer
    # permission_classes = [AllowAny,]

    def retrieve(self, request, *args, **kwargs):
        lecture_id = kwargs["lecture_id"]
        instance = self.filter_queryset(self.get_queryset(), lecture_id=lecture_id)
        try:
            serializer = self.get_serializer(instance[0])
        except:
           raise serializers.ValidationError("No matching Data")

        return Response(serializer.data)

    def filter_queryset(self, queryset, lecture_id):
        return queryset.filter(lecture=lecture_id)

