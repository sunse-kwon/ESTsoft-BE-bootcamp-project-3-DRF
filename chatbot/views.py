from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import gpt_chat
from .models import Conversation
# from .serializers import ChatSerializer
# Create your views here.

class ChatView(APIView):
    
    def get(self, request, *args, **kwargs):
        conversations = request.session.get('conversations', [])
        return render(request, 'chat.html', {'conversations': conversations})
        
    def post(self, request, *args, **kwargs):
        prompt = request.POST.get('prompt')
        if prompt:
            session_conversations = request.session.get('conversations', [])
            previous_conversations = "\n".join([f"User: {c['prompt']}\nAI: {c['response']}" for c in session_conversations])
            prompt_with_previous = f"{previous_conversations}\nUser: {prompt}\nAI:"
            response = gpt_chat(prompt_with_previous)
            conversation = Conversation(prompt=prompt, response=response)
            conversation.save()
            session_conversations.append({'prompt': prompt, 'response': response})
            request.session['conversations'] = session_conversations
            request.session.modified = True
        return self.get(request, *args, **kwargs)