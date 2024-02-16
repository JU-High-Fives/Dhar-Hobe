from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import DetailView, CreateView, UpdateView
from . models import Profile               # Importing Profile model from models.py
from .forms import ProfilePageForm, EditProfileForm   # Importing forms from forms.py
from django.urls import reverse_lazy
from django.views import generic

def signup(request):
    """
    View function for user signup.
    """
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email= request.POST['email'])
                profile = Profile.objects.create(user=user)

                auth.login(request,user)
                return redirect('profile')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    """
    View function for user login.
    """
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    """
    View function for user logout.
    """
    auth.logout(request)
    return redirect('home')

class ShowProfilePageView(DetailView):
    """
    View class for displaying user profile page.
    """
    model = Profile
    template_name = 'accounts/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context

class CreateProfilePageView(CreateView):
    """
    View class for creating user profile page.
    """
    model = Profile
    form_class = ProfilePageForm
    template_name = "accounts/create_user_profile_page.html"
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    """
    View class for editing user profile page.
    """
    model = Profile
    template_name = 'accounts/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url',
              'twitter_url', 'instagram_url', 'pinterest_url']
    success_url = reverse_lazy('home')

def profile(request):
    """
    View function for user profile.
    """
    return render(request,'accounts/profile.html')
