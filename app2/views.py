from django.shortcuts import render

# Create your views here.
def user(request):
    d={'username':'Django'}
    return render(request,'user.html',context=d)