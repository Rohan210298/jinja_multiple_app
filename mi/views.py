from django.shortcuts import render

# Create your views here.
def mi(request):
    d = {"captain":"Rohit","wins":2}
    return render(request,"home.html",context=d)