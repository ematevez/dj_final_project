from cgi import print_arguments
from django.shortcuts import render, redirect, get_object_or_404
from .models import ChatMessage
from registration.models import Profile, Friend
from .forms import ChatMessageForm
from django.http import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import json

# Create your views here.
def index(request):
    if request.user.profile.avatar :
        user = request.user.profile
        friends = Profile.objects.all()
        context = {"user": user, "friends": friends}
        return render(request, "mychatapp/index.html", context)
    else:
        return render(request, "registration/profile_form.html")
    
def detail(request,pk):
    friend = Profile.objects.get(user=pk)
    user1 = request.user.profile
    profile = Profile.objects.get(user=friend.user)
    chats = ChatMessage.objects.all()
    rec_chats = ChatMessage.objects.filter(msg_sender=profile, msg_receiver=user1, seen=False)
    rec_chats.update(seen=True)
    form = ChatMessageForm()
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user1
            chat_message.msg_receiver = profile
            chat_message.save()
            return redirect("detail", pk=Profile.user)
    context = {"friend": friend, "form": form, "user":user1, "profile":profile, "chats": chats, "num": rec_chats.count()}
    return render(request, "mychatapp/detail.html", context)

def sentMessages(request, pk):
    user = request.user.profile
    friend =  Profile.objects.get(user=pk)
    profile = Profile.objects.get(user=friend.user)
    data = json.loads(request.body)
    new_chat = data["msg"]
    new_chat_message = ChatMessage.objects.create(body=new_chat, msg_sender=user, msg_receiver=profile, seen=False )
    print(new_chat)
    return JsonResponse(new_chat_message.body, safe=False)

def receivedMessages(request, pk):
    user = request.user.profile
    friend = Profile.objects.get(user=pk)
    profile = Profile.objects.get(user=friend.user)
    arr = []
    chats = ChatMessage.objects.filter(msg_sender=profile, msg_receiver=user)
    for chat in chats:
        arr.append(chat.body)
    return JsonResponse(arr, safe=False)


def chatNotification(request):
    user = request.user.profile
    friends = Profile.objects.all()
    arr = []
    for friend in friends:
        chats = ChatMessage.objects.filter(msg_sender__id=friend.id, msg_receiver=user, seen=False)
        arr.append(chats.count())
    return JsonResponse(arr, safe=False)
    