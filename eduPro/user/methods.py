import json
import requests
from itertools import chain

from django.conf import settings
from django.contrib.auth import get_user_model
from lecture.models import Lecture, LectureStatus

User = get_user_model()


class Methods:

    def register_mk_fount(self, user, *args, **kwargs):
        username = user["username"]
        email = user["email"]
        password = user["password"]
        phone = user["phone"]
        url = settings.FOUNT_USER_URL
        body = {"email": email, "password": password, "profile": {"phone": phone, "name": username, "funnels": "10x10"}}
        response = requests.request("POST", url, json=body)
        return response

    def confirming_mk_fount(self, user, *args, **kwargs):
        email = user["email"]
        password = user["password"]
        url = settings.FOUNT_LOGIN_URL
        header = {"Content-Type": "application/json"}
        body = {"email": email, "password": password, "force_login": "true"}
        response = requests.request("POST", url, headers=header, json=body)
        return response

    def get_phone_from_litch(self, token):
        url = settings.FOUNT_PROFILE_URL
        header = {"Content-Type": "application/json", 'Authorization': f"Token {token}"}
        response = requests.get(url, headers=header)
        profile = json.loads(response.content)
        phone = profile["phone"]
        return phone

    def make_user_lecture_set(self, email):
        user = User.objects.get(email=email)
        lectures = Lecture.objects.all()
        for i, lec in enumerate(lectures):
            lec_st = LectureStatus.objects.create(user=user, lecture=lec)
            lec_st.save()

    def update_lecture_apply(self, email):
        user = User.objects.get(email=email)
        lectures = Lecture.objects.all()
        lec_status = LectureStatus.objects.filter(user=user)
        for i in range(len(lec_status), len(lectures)):
            lec_st = LectureStatus.objects.create(user=user, lecture=lectures[i])
            lec_st.save()

    def password_reset(self, body):
        url = settings.FOUNT_PASSWORD_RESET_URL
        response = requests.request("POST", url, json=body)
        return response

    def to_dict(self, instance):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)
        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data


