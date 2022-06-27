from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from seva_app.forms import Officerform, Techinicalform, notificationForm
from seva_app.models import Login, notification


def home(request):
    return render(request, 'index.html')


def login_view(request):
    if (request.method == 'POST'):
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('home')
            else:
                messages.info(request, 'invalid')
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')


def officer_add(request):
    officer_form = Officerform()
    if request.method == 'POST':
        officer_form = Officerform(request.POST)
        if officer_form.is_valid():
            user = officer_form.save(commit=False)
            user.is_officer = True
            user.save()
            messages.info(request, 'Officer Added Successfully')
            return redirect('officer_view')
    return render(request, 'officer_add.html', {'officer_form': officer_form})


def officer_view(request):
    of = Login.objects.all()
    return render(request, 'officer_view.html', {'of': of})


def officer_edit(request, id):
    of = Login.objects.get(id=id)
    if request.method == 'POST':
        form = Officerform(request.POST or None, instance=of)
        if form.is_valid():
            form.save()
            messages.info(request, 'officer updated Successful')
            return redirect('officer_view')
    else:
        form = Officerform(instance=of)
    return render(request, 'officer_edit.html', {'form': form})


def delete_officer(request, id):
    data = Login.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('officer_view')
    else:
        return redirect('officer_view')


# staaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf

def tstaff_add(request):
    technical_form = Techinicalform()
    if request.method == 'POST':
        technical_form = Techinicalform(request.POST)
        if technical_form.is_valid():
            user = technical_form.save(commit=False)
            user.is_tstaff = True
            user.save()
            messages.info(request, 'Staff Added Successfully')
            return redirect('staff_view')
    return render(request, 'staff_add.html', {'technical_form': technical_form})


def staff_view(request):
    of = Login.objects.all()
    return render(request, 'staff_view.html', {'of': of})


def staff_edit(request, id):
    of = Login.objects.get(id=id)
    if request.method == 'POST':
        form = Techinicalform(request.POST or None, instance=of)
        if form.is_valid():
            form.save()
            messages.info(request, 'staff edit successful')
            return redirect('staff_view')
    else:
        form = Techinicalform(instance=of)
    return render(request, 'staff_edit.html', {'form': form, 'user_form': user_form})


def staff_delete(request, id):
    data1 = Techinicalstaff.objects.get(id=id)
    data = Login.objects.get(techinicalstaff=data1)
    if request.method == 'POST':
        data.delete()
        return redirect('staff_view')
    else:
        return redirect('staff_view')


def sentnotification(request):
    form = notificationForm()
    if request.method == 'POST':
        form = notificationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'success')
            return redirect('view_notification')
    return render(request, 'sent_notification.html', {'form': form})


def viewnotification(request):
    of = notification.objects.all()
    return render(request, 'view_notification.html', {'of': of})


def delete_notification(request, id):
    data = notification.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('view_notification')
    else:
        return redirect('view_notification')


# view feedbaaaaaaaaaaaaaaaaack

def feedback_view(request):
    return render(request, 'feedback_view.html')
