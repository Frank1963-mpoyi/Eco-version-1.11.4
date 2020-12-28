from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm



def home_view(request):
    template_name = 'exercise/home.html'
    return render (request, template_name)


def contact_page(request):
    template_name =  'exercise/contact.html'
    form = ContactForm(request.POST or None)
    context = {
        'form': form
    }
    
        #take these data put them in the form  above
    '''
    if request.method == "POST":
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    '''
    if form.is_valid():
        print(form.cleaned_data)
        # we will still see the data in console like above    
    
    return render (request, template_name, context)



def login_page(request):
    template_name ='auth/login.html'
    form = LoginForm(request.POST or None)
    context={'form': form}
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')       
        # context['form'] = LoginForm() # this will clear  data inside the form 
        user = authenticate(request, username=username, password=password)# they will handle authentication to make sure if username and password are real       
    if user is not None:
        login(request, user)
        #context['form'] = LoginForm() # this will clear  data inside the form 
        return redirect('login')
        #redirect to a success page
    else:
        print('Error')
    return render (request, template_name, context)

def register_page(request):
    template_name = 'auth/register.html'
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render (request, template_name, context)
    