from django.shortcuts import render

# allow us to redirect
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.template import RequestContext, loader

# import the User class in models.py
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# import the auth.models User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from WebApp.models import *


@login_required
def index(request):
    print("in the index function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/index.html', context)



# registration is normal route, and login is login is "django.contrib.views.login"
def registration(request):
    errors = []
    context = {}
    if request.method == "GET":
        return render(request, 'WebApp/register.html', context)

    # add 'errors' attribute to the context
    context['errors'] = errors

    password1 = request.POST['password']
    password2 = request.POST['password_confirmation']

    if password1 != password2:

        print("Passwords did not match.")

        # error1 happens
        errors.append("Passwords did not match.")

    if len(User.objects.all().filter(username = request.POST['user_name'])) > 0:
        print("Username is already taken.")

        # error2 happens
        errors.append("Username is already taken.")

    if errors:
        return render(request, 'WebApp/register.html', context)

    # create a new user from the valid form data, using create_user function with 2 arguments, 'username' and 'password'
    new_user = User.objects.create_user(username=request.POST['user_name'], password=request.POST['password'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    new_user.save()

    # using 'authenticate' function
    new_user = authenticate(username = request.POST['user_name'], password = request.POST['password'])

    # using 'login' function
    login(request, new_user)

    # using 'redirect' function
    return redirect(reverse('message'))

@login_required
def message(request):
    print("in the message function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/message.html', context)

@login_required
def upload(request):
    print("in the upload function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/upload.html', context)

@login_required
def preprocess(request):
    print("in the preprocess function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/preprocessing.html', context)

@login_required
def visualization(request):
    print("in the visualization function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/knnresult.html', context)

# def logout view
def my_logout(request):
    logout(request)
    return redirect(reverse('index'))

@login_required
def honeycell(request):
    print("in the honeycell function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/honeycell.html', context)

@login_required
def honeycomb(request):
    print("in the honeycomb function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/honeycomb.html', context)

@login_required
def analytics(request):
    print("in the analytics function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/analytics.html', context)



@login_required
def add_message(request):
    print("in the add_message.")

    context = {}
    context['user'] = request.user

    if request.method == "GET":
        return render(request, 'WebApp/add_message.html', context)
    else:
        message_text = request.POST['message_text']

        new_message_instance = Message(user=request.user,
                                       message_text=message_text
                                       )
        new_message_instance.save()
        print("Already save new_message_instance.")

        return render(request, 'WebApp/add_message.html',context)


@login_required
def show_messages(request):
    print("in the show_message function.")

    context = {}
    context['user'] = request.user

    context['messages'] = Message.objects.all();

    return render(request, 'WebApp/show_messages.html', context)



@login_required
def add_comment(request):
    print("in the add_comment function.")

    context = {}

    user = request.user
    message = Message.objects.get(id=request.POST['message_id'])
    comment_text = request.POST['comment_text']

    new_comment_instance = Comment(user=user,
                                   message=message,
                                   comment_text=comment_text)
    new_comment_instance.save()
    print("Already save new_comment_instance.")

    return HttpResponseRedirect(reverse('show_messages'))



from django.http import JsonResponse

@login_required
def add_comment_ajax(request):
    print("in the add_comment_ajax function.")

    print(request)

    if request.method == "POST":
        user = request.user
        message_id = request.POST['message_id']
        message = Message.objects.get(id=message_id)
        comment_text = request.POST['comment_text']

        print("%" * 50)
        print(user)
        print(message_id)
        print(comment_text)
        print("%" * 50)

        new_comment_instance = Comment(user=user,
                                       message=message,
                                       comment_text=comment_text
                                       )
        new_comment_instance.save()

        return JsonResponse({ 'user': user.username, 'comment_text': comment_text })
    else:
        return HttpResponse("Request must be POST.")











