from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # comment_set 자동생성 (댓글들을 자동으로 연결하여 리스트로 출력해줌!)

class Comment(models.Model):
    #id , article_id 라는 foriegnkey 가 자동으로 생성된당!
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)    

