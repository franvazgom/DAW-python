from django.shortcuts import render
from pages.models import Page

def page(request, page_id):
    p = Page.objects.get(id=page_id)
    return render(request, 'pages/page.html', {'page':p})

