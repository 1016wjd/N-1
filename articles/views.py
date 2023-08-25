from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)



def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('articles:index')

    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'form.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    comment_form = CommentForm()

    # # comment 목록 조회 
    # # 첫번째 방법
    # comment_list = Comment.objects.filter(article=article)

    # # 두번째 방법
    # comment_list = article.comment_set.all()

    # 세번째 방법
    # html 코드에서 article.comment_set.all로 사용!! 

    #세번째>두번째>첫번째 순으로 권장

    context = {
        'article': article,
        'comment_form': comment_form,
        # 'comment_list': comment_list,
    }

    return render(request, 'detail.html', context)

def comment_create(request, article_id):
    # 사용자가 입력한 정보를 form에 입력
    comment_form = CommentForm(request.POST)
    # 유효성 검사
    if comment_form.is_valid():
        # form을 저장 => 추가로 넣어야 하는 데이터를 넣기 위해 저장 멈춰!
        comment = comment_form.save(commit=False)

        # # 첫번재 방법
        # # article_id를 기준으로 article obj를 가져와서 
        # article = Article.objects.get(id=article_id)
        # # article 칼럼에 추가 
        # comment.article = article
        
        # 두번째 방법
        comment.article_id = article_id

        # 비로소 저장
        comment.save()

        return redirect('articles:detail', id=article_id)



def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)
    
    comment.delete()

    return redirect('articles:detail', id=article_id)


