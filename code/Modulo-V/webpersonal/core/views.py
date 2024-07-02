from django.shortcuts import render, HttpResponse

def home(request):
    # html = """
    #     <h1>Bienvenid@s a mi página</h1>
    #     <h2>Francisco Vázquez</h2>
    #     <p>Esto es un parrafo de pruebas de mi página!!!!!</p>
    # """
    # return HttpResponse(html)
    return render(request, 'core/home.html')
