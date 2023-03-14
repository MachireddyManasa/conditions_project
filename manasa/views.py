from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':175,'b':274,'c':354}
    return render(request,'conditions.html',context=d)




def looping(request):
    d={'i':'manasa'}
    return render(request,'looping.html',context=d) 