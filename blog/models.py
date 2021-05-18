from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(
    "title", max_length=100,
  )
  body = models.TextField("body")
  created_at = models.DateTimeField(
    "作成日時", auto_now_add=True
  )