from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import gpt_chat
from .models import Conversation
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
import json

# Create your views here.


class ChatbotView(APIView):
    permission_classes = (IsAuthenticated,)
    throttle_classes = [UserRateThrottle]

    def post(self, request):
        request_data_utf8 = request.body.decode('utf-8')
        request_data = json.loads(request_data_utf8)
        if request_data:
            response = gpt_chat(request_data)
            conversation = Conversation(
                prompt=request_data, response=response, user=request.user)
            conversation.save()
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# class ChatView(APIView):
#     permission_classes = (IsAuthenticated,)
#     throttle_classes = [UserRateThrottle]

#     def get(self, request, *args, **kwargs):
#         conversations = request.session.get('conversations', [])
#         # return render(request, 'chat.html', {'conversations': conversations})
#         return Response({'conversations': conversations}, status=status.HTTP_200_OK)

#     def post(self, request, *args, **kwargs):

#         request_data_utf8 = request.body.decode('utf-8')
#         request_data_dict = json.loads(request_data_utf8)
#         prompt = request_data_dict.get('prompt')
#         print(prompt)
#         if prompt:
#             session_conversations = request.session.get('conversations', [])
#             previous_conversations = "\n".join(
#                 [f"User: {c['prompt']}\nAI: {c['response']}" for c in session_conversations])
#             prompt_with_previous = f"{previous_conversations}\nUser: {prompt}\nAI:"
#             response = gpt_chat(prompt_with_previous)
#             conversation = Conversation(
#                 prompt=prompt, response=response, user=request.user)
#             conversation.save()
#             session_conversations.append(
#                 {'prompt': prompt, 'response': response})
#             request.session['conversations'] = session_conversations
#             request.session.modified = True
#         return self.get(request, *args, **kwargs)
