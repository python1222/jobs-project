from django.shortcuts import render
from .models import Hyd_jobs,Bang_jobs,Pune_jobs

# Create your views here.
def home(request):
    return render(request, 'testapp/home.html')
def hydjobsinfo(request):
    hydjob_record = Hyd_jobs.objects.order_by('date')  # .all()
    my_dict = {'hydjob_record': hydjob_record}
    return render(request, 'testapp/hydjobs.html', context=my_dict)
def punejobsinfo(request):
    punejob_record=Pune_jobs.objects.all()
    my_dict={'punejob_record':punejob_record}
    return render(request,'testapp/punejobs.html',context=my_dict)
def banglorejobsinfo(request):
    bangjob_record=Bang_jobs.objects.all()
    my_dict={'bangjob_record':bangjob_record}
    return render(request,'testapp/bangjobs.html',context=my_dict)
