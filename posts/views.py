from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render


class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'Kevin Echeverri',
            'years': 28,
            'codes': ['Python', 'Javastipt', 'Django']
        }
        return render(request, 'hello_world.html', context=data)
        # return HttpResponse(content='Hola mundo, soy kevin')
