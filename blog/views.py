from django.shortcuts import render
from django.utils import timezone
from .models import POST

# Create your views here.
def post_lists(request):
    posts = POST.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_lists.html', stuff_for_frontend)