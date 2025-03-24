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
            modelComent.objects.create(name=k1,text=k2,email=k3)  #создает запись в таблице
            form = formComent() #очищает форму
    else:
        form = formComent() #когда заходим на страницу показывает пустую форму
    data = {'form':form,'coms':coms}

    return render(request,'form1.html',data)

def form2(request):
    if request.method == 'POST':  # нажал кнопку отправить
        form = formChoise(request.POST)
        if form.is_valid():  # форма заполнена правильно
            # собирает инфо
            k1 = form.cleaned_data['name']
            k2 = form.cleaned_data['tel']
            k3 = form.cleaned_data['eda']
            k4 = form.cleaned_data['dopTomato']
            k5 = form.cleaned_data['dopCheese']
            k6 = form.cleaned_data['dopKolbasa']
            print(k1, k2, k3,k4,k5,k6)
            new = modelChoise.objects.create(name=k1, tel=k2, eda=k3, dopTomato=k4, dopCheese=k5, dopKolbasa=k6)  # создает запись в таблице
            form = formChoise()  # очищает форму
            data = {'new':new}
            return render(request,'zakaz.html',data)
    else:
        form = formChoise()  # когда заходим
    data = {'form':form}
    return render(request,'form2.html',data)