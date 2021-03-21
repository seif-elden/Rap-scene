from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def room(request):
    messages = Message.objects.all()[:20]
    return render(request, 'room.html', {"messages":messages})