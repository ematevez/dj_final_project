from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.http import Http404, JsonResponse
from .models import Thread, Message
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import requests


TELEGRAM_BOT_TOKEN = "992737156:AAHJH8m9uf8RmjWp3Sv8hkFAtN6buoMiS1s"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

chat_id = "1252733785"
chat_group_id = "-1001711230898"



@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"

@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread
    
    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

def add_message(request, pk):
    json_response = {'created':False}
    if request.user.is_authenticated:
        
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)  
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
            if len(thread.messages.all()) == 1:
                json_response['first'] = True
            # =========================
            # Send message to telegram 
            # =========================
            sender = request.user
            addressee =(thread.users.filter(pk=pk))[0].username
            link = "http://192.168.1.44:8000/profiles/"+ addressee
            payload ="Te enviaron: " + str(content) + "\n" +" Fue: " + str(sender) + "\n" + " Revisar : " + str(link)
            params = {"chat_id": chat_id, "parse_mode": "Markdown", "text":payload}
            requests.get(TELEGRAM_API_URL, params=params)
            
            payload1 ="Le enviaron un mensaje a:  " + "\n" + str(addressee) + "\n" + " para Revisar : " + str(link)
            params1 = {"chat_id": chat_group_id , "parse_mode": "Markdown", "text":payload1}
            requests.get(TELEGRAM_API_URL, params=params1)
            # =========================
            # End telegram
            # =========================
    else:
        raise Http404("User is not authenticated")

    return JsonResponse(json_response)

@login_required
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))