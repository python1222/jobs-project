import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fakerpro.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake=Faker()
def phonenumber():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project manager','Team lead','Software develpoer'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA'))
        femail=fake.email()
        fphonenumber=phonenumber()
        hydjob_record=Hyd_jobs.objects.get_or_create(date=fdate,
                                                     company=fcompany,
                                                     title=ftitle,
                                                     eligibility=feligibility,
                                                     email=femail,
                                                     phonenumber=fphonenumber,)
        punejob_record = Pune_jobs.objects.get_or_create(date=fdate,
                                                       company=fcompany,
                                                       title=ftitle,
                                                       eligibility=feligibility,
                                                       email=femail,
                                                       phonenumber=fphonenumber, )
        bangjob_record = Bang_jobs.objects.get_or_create(date=fdate,
                                                       company=fcompany,
                                                       title=ftitle,
                                                       eligibility=feligibility,
                                                       email=femail,
                                                       phonenumber=fphonenumber, )
populate(25)
