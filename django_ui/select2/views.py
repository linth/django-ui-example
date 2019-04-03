from django.shortcuts import render

def select2(request):
    template = 'select2.html'
    context = {}
    return render(request, template, context)
