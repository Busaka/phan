from django.shortcuts import render
from .models import School

# Create your views here.


def home(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    files = School.objects.all()
    # for f in files:
    # print(f)

    return render(request, 'mysite/home.html', {'files': files})
