from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from myappp.forms import UserRegistrationForm
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
#test
def index(request):
    return render(request, 'myappp/index.html')

def desktop_one(request):
    return render(request, 'myappp/DesktopOne.html')

@login_required
def desktop_onelog(request):
    return render(request, 'myappp/DesktopOneLoggedIn.html', {})

def map_view(request):
    return render(request, 'myappp/map.html')

@login_required
def map_profile_view(request):
    return render(request, 'myappp/mapprofile.html')

@login_required
def map_log_view(request):
    return render(request, 'myappp/maplog.html', {})

def desktop_two(request):
    return render(request, 'myappp/DesktopTwo.html')

def desktop_three(request):
    return render(request, 'myappp/DesktopThree.html')
@login_required
def favorites_view(request):
    return render(request, 'myappp/favorites.html')
@login_required
def profile(request):
    return render(request, 'myappp/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('login')  # Redirect to your desired page
    else:
        form = UserRegistrationForm()
    return render(request, 'myappp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('maplog')
    else:
        form = AuthenticationForm()
    return render(request, 'myappp/login.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'myappp/password_reset.html'
    email_template_name = 'myappp/password_reset_email.html'
    success_url = '/myappp/password_reset/done/'

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user = get_user_model().objects.filter(email=email).first()

        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = self.token_generator.make_token(user)
            url = self.request.build_absolute_uri(f"/myappp/reset/{uid}/{token}/")

            context = {
                'email': user.email,
                'user': user,
                'url': url,
            }

            subject = render_to_string('myappp/password_reset_subject.txt', context).strip()
            email_body = render_to_string(self.email_template_name, context)

            # Send the email only once
            send_mail(subject, email_body, None, [user.email], html_message=email_body)

        # Redirect after sending the email
        return redirect(self.success_url)

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'myappp/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'myappp/password_reset_confirm.html'
    success_url = '/myappp/reset/done/'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'myappp/password_reset_complete.html'
