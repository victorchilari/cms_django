from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    # return HttpResponse('Hello world :)')
    return render(request, './index.html', {
        'prop1': "it's a prop"
    })
