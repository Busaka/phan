from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from mysite.models import School
from .forms import ContactForm
# from mysite.models import Job
# Create your views here.


def index(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    files = School.objects.all()
    return render(request, 'index.html', {'files': files})


def about(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    return render(request, 'about.html', {})


def contact(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data.get('school', ''))

        subject = form.cleaned_data.get('school', '')
        message = form.cleaned_data.get('message', '')
        from_email = form.cleaned_data.get('email', '')

        send_mail(subject, message, from_email, ['lxbusaka07@gmail.com'], fail_silently=False)
    return render(request, 'contact.html', {'form': form})


def jobs(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    # jobs = Job.objects.all()
    return render(request, 'jobs.html', {})
