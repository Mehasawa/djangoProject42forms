from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request,'index.html')

def form1(request):
    # form = formComent()
    coms = modelComent.objects.all()#собираем комментарии из таблицы
    if request.method == 'POST':    #нажал кнопку отправить
        form = formComent(request.POST)
        if form.is_valid():         # форма заполнена правильно
            #собирает инфо
            k1 = form.cleaned_data['name']
            k2 = form.cleaned_data['text']
            k3 = form.cleaned_data['email']
            print(k1,k2,k3)
            new = modelComent.objects.create(name=k1,text=k2,email=k3)  #создает запись в таблице
            form = formComent() #очищает форму
    else:
        form = formComent() #когда заходим на страницу показывает пустую форму
    data = {'form':form,'coms':coms}

    return render(request,'form1.html',data)

def form2(request):
    return render(request,'form2.html')