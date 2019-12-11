from rest_framework import serializers
# from .models import File
from django.conf import settings
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from lecture.models import ImageResource, Article, Lecture, Knowledge, LectureStatus, Quiz, VideoLecture
from lecture.methods import Methods


M = Methods()

class ImageResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageResource
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'


class LectureStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureStatus
        fields = '__all__'

    def to_representation(self, instance):
        represented = super().to_representation(instance)
        lecture = represented.pop('lecture')
        lec = Lecture.objects.get(id=lecture)
        lec_dict = {}
        lec_dict["id"] = lec.id
        lec_dict["episode"] = lec.episode
        lec_dict["title"] = lec.title
        lec_dict["sub_title"] = lec.subtitle

        lec_dict["status"] = {
            "view_complete_sec": instance.view_complete_sec,
            "video_pass": instance.video_pass,
            "quiz_pass": instance.quiz_pass,
            "pass_date": instance.pass_date
        }
        lec_dict["created_at"] = lec.created_at
        lec_dict["updated_at"] = lec.updated_at

        return lec_dict


class LectureDetailSerailizer(serializers.ModelSerializer):
    class Meta:
        model = LectureStatus
        fields = '__all__'

    def to_representation(self, instance):
        # status_dict = super().to_representation(instance)
        try:
            status = {}
            status["view_complete_sec"] = instance.view_complete_sec
            status["video_pass"] = instance.video_pass
            status["quiz_pass"] = instance.quiz_pass
            status["pass_date"] = instance.pass_date

            lecture_id = instance.lecture.id

            lecture_ins = Lecture.objects.get(id=lecture_id)
            result = M.to_dict(lecture_ins)
            result.pop("article")
            try:
                video = VideoLecture.objects.get(lecture=lecture_id)
            except:
                raise serializers.ValidationError("You have to register a Video for this lecture first because their relationship is OneToOne")
            video = M.to_dict(video)
            video.pop("lecture")
            result["video"] = video

            articles = lecture_ins.article.all()
            carrier = []
            for article in articles:
                art =  M.to_dict(article)
                thumbnail = art["thumbnail"]
                image_url = ImageResource.objects.get(id=thumbnail).image_file
                # art["thumbnail"] = f"{settings.MEDIA_URL_PREFIX}{image_url}" - serializers_branch
                art["thumbnail"] = image_url
                carrier.append(art)
            result["articles"] = carrier

            knowledges = Knowledge.objects.filter(lecture=lecture_id)
            carrier = []
            for knowledge in knowledges:
                know = M.to_dict(knowledge)
                know.pop("lecture")
                thumbnails = know["thumbnail"]
                for i, thumb in enumerate(thumbnails):
                    image_url = ImageResource.objects.get(id=thumb).image_file
                    thumbnails[i] = image_url
                know["thumbnail"] = thumbnails

                carrier.append(know)
            result["knowledges"] = carrier

            quizzes = Quiz.objects.filter(lecture=lecture_id)
            carrier = []
            for quiz in quizzes:
                q = M.to_dict(quiz)
                q.pop("lecture")
                choices = q["choices"].split(";")
                q["choices"] = choices
                carrier.append(q)
            result["quizzes"] = carrier
            result["status"] = status
        except:
            return {"error": "have to set data first"}
        else:
            return result


class LectureStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureStatus
        exclude = ('pass_date', 'created_at', 'updated_at', 'user')


class ArticleSeializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def to_representation(self, instance):
        article_dict = super().to_representation(instance)
        thum_id = article_dict["thumbnail"]
        img_inst = ImageResource.objects.get(id=thum_id)
        # article_dict["thumbnail"] = f"{settings.MEDIA_URL_PREFIX}{img_inst.image_file}" - serializers_branch
        article_dict["thumbnail"] = img_inst.image_file
        return article_dict


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge
        fields = '__all__'

    def to_representation(self, instance):
        knowledge_dict = super().to_representation(instance)
        thumbnails = knowledge_dict["thumbnail"]

        for i, th in enumerate(thumbnails):
            img = ImageResource.objects.get(id=th)
            image_url = img.image_file
            thumbnails[i] = image_url
        knowledge_dict["thumbnail"] = thumbnails

        return knowledge_dict


class VideoLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLecture
        fields = '__all__'


