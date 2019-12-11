from model_utils import Choices
from lecture.models import ImageResource, Knowledge, Article, Lecture, LectureStatus, Quiz, VideoLecture
from user.models import User
from PIL import Image
from io import BytesIO


class Factories:
    def factories(self):
        pass
# #
# #
# #       # NOT VALID => put images by api already
#         # print('===============================', 'PUT Images RESOUCES INTO DB')
#         # image = Image.open('lecture/img/tree.jpeg', mode='r')
#         # im = ImageResource.objects.create(image_file=image)
#         # im.save()
#         # return
#         # im = Image.open('lecture/img/tree.jpeg')
#         # im.thumbnail((600, 380), Image.ANTIALIAS)
#         # thumb_io = BytesIO()
#         # im.save(thumb_io, im.format, quality=90)
#         # im = ImageResource.objects.create(image_file=im)
#         # im.save()
#         # instance.image.save(im.filename, ContentFile(thumb_io.getvalue()), save=False)
#
#
#         #******************
#         # VALID FROM HERE** after putting 4 IMAGEs and registering for 4 USERs
#         #******************
#         print('===============================', 'PUT Articles INTO DB')
#         import datetime
#
#         date = ["2011-09-01", "2013-10-11", "2015-11-11", "2017-12-11"]
#
#         for i, v in enumerate(date):
#             date[i] = datetime.datetime.strptime(v, "%Y-%m-%d")
#
#         articles= [
#                     {
#                         "title": "1. Data articles",
#                         "summary": "Data articles are brief, peer-reviewed publications about research data. Sharing data makes it accessible and enables others to gain new insights and make interpretations for their own research. Thanks to a detailed dataset description, the data published in data articles can be reused, reanalyzed and reproduced by others.",
#                         "body": "<html>Discovering Data: Each data article links to the relevant data in a repository. This makes it easier for other researchers by having an overview of all the relevant information in one place. And since data articles have a DOI, citations link the data to all subsequent research that applies it, making it even easier to reuse and reproduce results.</html>",
#                         "agency": "한국일보",
#                         "published_at": date[0]
#                     },
#                     {
#                         "title": "2. Data articles",
#                         "summary": "Data articles are brief, peer-reviewed publications about research data. Sharing data makes it accessible and enables others to gain new insights and make interpretations for their own research. Thanks to a detailed dataset description, the data published in data articles can be reused, reanalyzed and reproduced by others.",
#                         "body": "<html>Discovering Data: Each data article links to the relevant data in a repository. This makes it easier for other researchers by having an overview of all the relevant information in one place. And since data articles have a DOI, citations link the data to all subsequent research that applies it, making it even easier to reuse and reproduce results.</html>",
#                         "agency": "한국일보",
#                         "published_at": date[1]
#                     },
#                     {
#                         "title": "3. Data articles",
#                         "summary": "Data articles are brief, peer-reviewed publications about research data. Sharing data makes it accessible and enables others to gain new insights and make interpretations for their own research. Thanks to a detailed dataset description, the data published in data articles can be reused, reanalyzed and reproduced by others.",
#                         "body": "<html>Discovering Data: Each data article links to the relevant data in a repository. This makes it easier for other researchers by having an overview of all the relevant information in one place. And since data articles have a DOI, citations link the data to all subsequent research that applies it, making it even easier to reuse and reproduce results.</html>",
#                         "agency": "한국일보",
#                         "published_at": date[2]
#                     },
#                     {
#                         "title": "4. Data articles",
#                         "summary": "Data articles are brief, peer-reviewed publications about research data. Sharing data makes it accessible and enables others to gain new insights and make interpretations for their own research. Thanks to a detailed dataset description, the data published in data articles can be reused, reanalyzed and reproduced by others.",
#                         "body": "<html>Discovering Data: Each data article links to the relevant data in a repository. This makes it easier for other researchers by having an overview of all the relevant information in one place. And since data articles have a DOI, citations link the data to all subsequent research that applies it, making it even easier to reuse and reproduce results.</html>",
#                         "agency": "한국일보",
#                         "published_at": date[3]
#                     }
#                 ]
#
#         thumbnails = ImageResource.objects.all()
#         for i, ar in enumerate(articles):
#             article = Article.objects.create(title=ar["title"], summary=ar["summary"], body=ar["body"], agency=ar["agency"], published_at=ar["published_at"], thumbnail=thumbnails[i])
#             article.save()
#
#
#         # TODO lecture가 먼저고 그 다음 유저가 가입되면 매핑 되는 구조
#         print('================================', 'PUT Lectures INTO DB')
#         lectures = [
#                     {
#                         "title": "1. 금융을 배우자",
#                         "episode": 1,
#                         "subtitle": "짐로저와 떠나는 금융여행.",
#                     },
#                     {
#                         "title": "2. 로보어드바이저란?",
#                         "episode": 2,
#                         "subtitle": "파돌이를 만나다.",
#                     },
#                     {
#                         "title": "3. 투자란 무엇인가?",
#                         "episode": 3,
#                         "subtitle": "워렌버핏을 이기다.",
#                     },
#                     {
#                         "title": "4. 파운트를 만나다.",
#                         "episode": 4,
#                         "subtitle": "파돌이 파운트가 되다.",
#                     }
#                 ]
#
#         articles = Article.objects.all()
#         for i, lec in enumerate(lectures):
#             lecture = Lecture.objects.create(title=lec["title"], episode=lec["episode"], subtitle=lec["subtitle"])
#             lecture.save()
#             lecture.article.add(articles[i])
#
#
#
#
#
#         print('================================', 'PUT Knowledges INTO DB')
#         lectures = Lecture.objects.all()
#         #because lecture is foreign key in  Knowledge model
#         k1 = Knowledge.objects.create(number=1, lecture=lectures[0])
#         k1.save()
#         k2 = Knowledge.objects.create(number=2, lecture=lectures[1])
#         k2.save()
#         k3 = Knowledge.objects.create(number=3, lecture=lectures[2])
#         k3.save()
#         k4 = Knowledge.objects.create(number=4, lecture=lectures[3])
#         k4.save()
#
#
#
#         print('================================', 'PUT Thumbnail INTO Knowledges')
#         images = ImageResource.objects.all()
#         print(11, images)
#         knowledges = Knowledge.objects.all()
#         print(13, knowledges)
#
#         for i in range(4):
#             knowledges[i].thumbnail.add(images[i])
#
#         kkk = Knowledge.objects.all()
#         print(15, kkk[0].thumbnail.all())
#
#
#         lectures = Lecture.objects.all()
#         print(16, lectures)
#         knowledges = Knowledge.objects.all()
#         print(18, knowledges)
#
#
#
#
#
#
#
#
#
#
#         # print('================================', 'PUT Quizs INTO DB')
#         quizs = [
#                     {
#                         "question": "자산관리란 뭘까요?",
#                         "number": 1,
#                         "choices": "1.내돈관리하는거;2.돈쓰는거;3.사랑하는거;4몰라몰라",
#                         "answer": "1",
#                         "hint": "문제안에 답있다."
#                     },
#                     {
#                         "question": "로보어드바이저란?",
#                         "number": 2,
#                         "choices": "1.로보트;2.태권브이;3:크레용신짱;4:인공지능자산관리프로그램",
#                         "answer": "4",
#                         "hint": "문제를 질 읽어봐!"
#                     },
#                     {
#                         "question": "짐로저스는 누구?",
#                         "number": 3,
#                         "choices": "1.아저씨;2.착한할아버지;3.위대한투자가;4.워렌버핏",
#                         "answer": "3",
#                         "hint": "모르면 구글에게 물어봐!"
#                     },
#                     {
#                         "question": "파운트란?",
#                         "number": 4,
#                         "choices": "1.샘물;2.대한민국최고의로보어드바이저회사;3.파무침;4.파란색",
#                         "answer": "2",
#                         "hint": "지금까지 계속 뭘 얘기했는지 생각해봐!"
#                     }
#                 ]
#
#         for i, q in enumerate(quizs):
#             quiz = Quiz(question=q["question"], number=q["number"], choices=q["choices"], answer=q["answer"], hint=q["hint"], lecture=lectures[i])
#             quiz.save()
#
#
#         # print('================================', 'PUT VideoLectures INTO DB')
#         video_lectures = [
#                     {
#                         "url": "https://www.youtube.com/watch?v=Rr1-UTFCuH4",
#                         "outline": "금융 어렵지 않아"
#                     },
#                     {
#                         "url": "https://www.youtube.com/watch?v=10utJGbQQLs&list=RDn5ZhKyOxZns&index=3",
#                         "outline": "부동산이 답일까?"
#                     },
#                     {
#                         "url": "https://www.youtube.com/watch?v=s1S6DeFQbQo",
#                         "outline": "소원을 말해봐",
#                     },
#                     {
#                         "url": "https://www.youtube.com/watch?v=n5ZhKyOxZns",
#                         "outline": "파운트와 함께하다",
#                     }
#                 ]
#
#         lectures = Lecture.objects.all()
#         for i, vl in enumerate(video_lectures):
#             v = VideoLecture(url=vl["url"], outline=vl["outline"], lecture=lectures[i])
#             v.save()
#         #
#         #
#         #
#         #
#         #
#
