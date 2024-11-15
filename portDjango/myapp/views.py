from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    if request.method=='POST':
        nm=request.POST.get('name')
        print(nm)    
        # return HttpResponse(f"Email received: {nm}")
    return render(request,'index.html')