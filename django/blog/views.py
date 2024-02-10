# from django.http import HttpResponse

from typing import Any

from django.http import Http404, HttpRequest
from django.shortcuts import render

from . import data


def blog(request):
    print('I can do what I want')
    # return HttpResponse('Marrom Theo app blog')

    context = {
        # 'context': 'At blog',
        # 'title': 'exemple page - ',
        'posts': data.posts,
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def post(request: HttpRequest, post_id: int):
    post_found: dict[str, Any] | None = None

    for post in data.posts:
        if post['id'] == post_id:
            post_found = post
            break

    if post_found is None:
        raise Http404('Post does not exist')

    context = {
        # 'context': 'At blog',
        'post': post_found,
        'title': post_found['title'] + ' - ',
        # 'posts': data.posts
    }

    return render(
        request,
        'blog/post.html',
        context
    )


def exemple(request):
    print('exemple')
    # return HttpResponse('exemple do app blog')

    context = {
        'context': 'At exemple'
    }

    return render(
        request,
        'blog/exemple.html',
        context
    )
