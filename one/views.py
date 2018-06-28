from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                  CreateView,DeleteView,UpdateView)
from one import models
#from one.models import User1
from django.shortcuts import render
from django.http import HttpResponse

'''def user_login(request):

    all=User1.objects.all()
    email=User1.objects.values_list('email',flat=True)
    name=User1.objects.values_list('full_name',flat=True)



    dict={'object':all , 'emails':email , 'names':name}


    return render(request,'one/userlogin.html',dict)


def update(request):

    all=User1.objects.all()




    dict={'object':all}


    return render(request,'one/viewuserlogin.html',dict)



def sidebar(request):

    return render(request,'one/sidebar.html')'''


class userlogin(ListView):
    context_object_name = 'object'
    model=models.User1
    template_name='one/userlogin.html'


class detail(DetailView):
    model=models.User1
    context_object_name = 'o'
    template_name='one/viewuserlogin.html'
class create(CreateView):
    model=models.User1
    fields = ("full_name","last_name","email","password","mobile_no")
class update(UpdateView):
    model=models.User1
    fields = ("full_name","last_name","email","password","mobile_no")
class delete(DeleteView):
    model = models.User1
    success_url = reverse_lazy("one:list")

def appointment(request):
    return render(request,'one/appointment.html')

def doctor_list(request):
    return render(request,'one/list.html',{'obj':[1,2,3]})
def details(request):
    return render(request,'one/detail.html')
def booking(request):
    return render(request,'one/booking.html')
