from django.shortcuts import render

# Create your views here.
def food(request):
    return render(request,'food.html')
def water(request):
    return render(request,'water.html') 
def plate(request):
    return render(request,'plate.html') 
def maggu(request):
    return render(request,'maggu.html')     
