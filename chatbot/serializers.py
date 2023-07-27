# from rest_framework import serializers
# from .models import Conversation
# from .utils import gpt_chat
# class ChatSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Conversation
#         fields = ["id", "prompt", "response"]
    
#     def create(self, validated_data):
#         conversation = Conversation.objects.create(**validated_data)
#         response = gpt_chat(validated_data["prompt"])
#         conversation.response = response
#         conversation.save()
#         return conversation
