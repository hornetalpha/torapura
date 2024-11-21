from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    date = models.DateField(default=timezone.now)  # 手動入力または自動入力可能な日付

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title
        
class Plan(models.Model):
    place = models.CharField("都道府県", max_length=200)
    done = models.CharField("ジャンル", max_length=200)
    person = models.CharField("人数", max_length=200)
    day = models.CharField("旅行日数", max_length=200)
    plan_name = models.CharField("プラン名", max_length=200)
    plan_detail = models.TextField("プラン詳細")
    typeno = models.IntegerField

    class Meta:
        db_table = 'plan'
        verbose_name = 'プラン'
        verbose_name_plural = 'プラン一覧'

        def __str__(self):
            return self.name
