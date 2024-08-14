from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import User
from .models import TrailerRentalRequest
from .forms import LoginForm
from .forms import TrailerRentalRequestForm

def test(request):
    pending_requests = TrailerRentalRequest.objects.filter(is_approved=False)
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        action = request.POST.get('action')
        rental_request = TrailerRentalRequest.objects.get(id=request_id)
        if action == 'approve':
            # Create a new User for the renter
            User.objects.create_user(
                username=rental_request.username,
                password=rental_request.password,
                role='renter'
            )
            rental_request.is_approved = True
            rental_request.save()
        elif action == 'reject':
            rental_request.delete()
    return render(request, 'core/test.html', {'pending_requests': pending_requests})

def home(request):
    return render(request, 'core/home.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.role == role:  # Check the user's role after authentication
                    auth_login(request, user)
                    if user.role == 'admin':
                        return redirect('admin_dashboard')
                    elif user.role == 'driver':
                        return redirect('driver_dashboard')
                    elif user.role == 'renter':
                        return redirect('renter_dashboard')
                else:
                    form.add_error(None, 'Role mismatch. Please select the correct role.')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

def rent_trailer(request):
    if request.method == 'POST':
        form = TrailerRentalRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TrailerRentalRequestForm()
    return render(request, 'core/rent_trailer.html', {'form': form})

@login_required
@staff_member_required
def admin_dashboard(request):
    pending_requests = TrailerRentalRequest.objects.filter(is_approved=False)
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        action = request.POST.get('action')
        rental_request = TrailerRentalRequest.objects.get(id=request_id)
        if action == 'approve':
            # Create a new User for the renter
            User.objects.create_user(
                username=rental_request.username,
                password=rental_request.password,
                role='renter'
            )
            rental_request.is_approved = True
            rental_request.save()
        elif action == 'reject':
            rental_request.delete()
    return render(request, 'core/admin_dashboard.html', {'pending_requests': pending_requests})

@login_required
def driver_dashboard(request):
    return render(request, 'core/driver_dashboard.html')

@login_required
def renter_dashboard(request):
    return render(request, 'core/renter_dashboard.html')
