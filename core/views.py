from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth import login
# Create your views here.
def home(request):
    return render(request,'home.html')

def sign_up(request):
    form = forms.SignUpForm()
    
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email').lower()
        
            user = form.save(commit=False)
            user.username = email
            user.save()
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('customer:profile.html')
        
    return render(request,'sign_up.html',{
        'form':form
    })
