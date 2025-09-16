from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

#logout
def logout(request):
    auth.logout(request)
    return redirect('login')



def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            
    context = {'form': form}
    return render(request, 'pages/login.html', context = context)

# Register a user
def register(request):
    # make a form from forms.py
    form = CreateUserForm()

    if request.method == "POST":
        # make a form with the users submitted data
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() # save to database
            return redirect('')
        
    context = {'form': form}
    #print(context)

    return render(request, 'pages/register.html', context=context)

@login_required(login_url='login')
def dashboard(request):


    my_Records = Record.objects.all()
    context = {'Record' :my_Records}


    return render(request, 'pages/dashboard.html', context=context)

@login_required(login_url="login")
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":form = CreateRecordForm(request.POST)

    if form.is_valid():
            form.save()
            return redirect("dashboard")
        
    context = {'create_form': form}
    return render(request, 'pages/dashboard.html', context=context)

# update a user record. 
@login_required(login_url='login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(request.POST, isinstance=record)
    if form.is_valid():
        form.save()
        return redirect("dashboard")
    
# if no submmitted data - send from to page 
    context = {'update_form': form}
    return render(request, 'pages/update-record.html', context = context )

@login_required(login_url='my-login')
def singular_record(reuqestt, pk):

    one_record = Record.objects.get(id=pk)
    context = {'record':one_record}
    return render(request, 'website/view-record.html', context = context)

@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()

    return redirect("dashboard")


