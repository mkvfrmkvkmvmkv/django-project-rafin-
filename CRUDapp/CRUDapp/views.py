from django.shortcuts import render, redirect 
from .forms import CreateUserForm, LoginForm 

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def login(request):
    return render(request, 'pages/login.html')
# Register a user 
def register(request):
    # make a form from forms. py 
    form = CreateUerForm()
    
    if request.method == "POST"
    # make a form with the users submitted data 
    form = CreateUserForm(request.POST)
    if form.is_valid():
        form.save() # savae the database 
        return redirect('')

    context = ['form': form]
    #print(context)

    return render(request, 'website/register.html')