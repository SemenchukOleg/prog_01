from django.shortcuts import render, redirect, get_object_or_404
from saveapp.models import League


# Create your views here.

def index(request):
    leagues = League.objects.order_by('id')
    context = {
        'leagues':leagues
    }

    return render(request, 'pages/index.html', context=context)