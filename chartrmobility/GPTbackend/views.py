import os

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_KEY", None)
# Create your views here.
class GPTgenerator(APIView):
    def post(self, request, format=None):
        print(request.data['input_text'], " input text")
        # use OpenAI API to generate reponse to user input text
        openai.api_key = api_key
        print(openai.api_key, " openai api key")
        input_text = request.data['input_text']
        # Generate a response using the OpenAI API
        # response = openai.Completion.create(
        #     engine="gpt-3.5-turbo",
        #     prompt=input_text,
        #     max_tokens=256,
        #     # n=1,
        #     # stop=None,
        #     temperature=0.5
        # )
        response = "Hi I am facing Downtime right now. Please try again later."
        print(response, " response")
        return Response(response, status=status.HTTP_200_OK)
