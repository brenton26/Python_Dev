from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'Home/index.html')

def zen(request):
    import this
    return redirect('/')
