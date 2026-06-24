import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from django.db.models import Q

from .models import Post

@csrf_exempt
def add_post(request):
    data = json.loads(request.body)

    title = data.get('title')
    content = data.get('content', '')
    pub = data.get('publication_date')

    if not title or not pub:
        return JsonResponse({'error': 'title and publication_date required'}, status=400)

    pub_date = parse_date(pub)
    if pub_date is None:
        return JsonResponse({'error': 'invalid publication_date, use YYYY-MM-DD'}, status=400)

    post = Post(title=title, content=content, publication_date=pub_date)
    post.save()
    return JsonResponse({'id': post.id, 'title': post.title, 'content': post.content, 'publication_date': str(post.publication_date)}, status=201)


def search_posts(request):
    q = request.GET.get('q', '').strip()
    qs = Post.objects.all()
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(content__icontains=q))
    results = [
        {
            'id': p.id,
            'title': p.title,
            'content': p.content,
            'publication_date': str(p.publication_date),
        }
        for p in qs
    ]
    return JsonResponse({'results': results})


@csrf_exempt
def posts_view(request):
    if request.method == 'GET':
        return search_posts(request)
    if request.method == 'POST':
        return add_post(request)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
