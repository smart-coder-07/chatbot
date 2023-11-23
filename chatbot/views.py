from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import openai
# Create your views here.

open_api_key = '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'
openai.api_key = open_api_key

def ask_openai(message):
    reponce = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = message,
        max_tokens=150,
        n=1,
        stop = None,
        # temprature=0.7,
    )
    answer = reponce.choices[0].text.strip()
    return answer



def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
