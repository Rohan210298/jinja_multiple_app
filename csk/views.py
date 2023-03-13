from django.shortcuts import render

# Create your views here.
def csk(request):
    d = {"captain":"dhoni","wins":3}
    return render(request,"home.html",context=d)