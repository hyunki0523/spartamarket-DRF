from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    GENDER = (
        ("FEMALE", "Female"),
        ("MALE", "Male"),
        ("CUSTOM", "Custom"),
        ("NONE", "Prefer not to say"),
    )

    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False)
    introduction = models.TextField(default='', null=False, blank=True)
    birthday = models.DateField(default='', null=False, blank=False)
    gender = models.CharField(max_length=6, choices=GENDER, null=True, blank=True)


    # 필수로 작성해야하는 field "username, 비밀번호, 이메일, 이름, 닉네임, 생일"
    REQUIRED_FIELDS = ['email', 'name','password','birthday',]

    def __str__(self):
        return self.nickname