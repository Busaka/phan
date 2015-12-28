from django.shortcuts import render

from .models import Job
from .forms import JobsForm

# Create your views here.


def jobs(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    jobs = Job.objects.all()
    return render(request, 'jobs/jobs.html', {'jobs': jobs})


def upload_job(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    jform = JobsForm(request.POST or None)
    return render(request, 'jobs/upload_job.html', {'jform': jform})
