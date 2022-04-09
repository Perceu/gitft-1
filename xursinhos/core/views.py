from django.shortcuts import render
from xursinhos.core.models import Fotos, Tags



def home(request):
    tags = Tags.objects.all()
    fotos = Fotos.objects.all()

    context = {
        "fotos":fotos,
        "tags":tags,
        "loop":range(10),
    }
    return render(request, 'index.html', context)
