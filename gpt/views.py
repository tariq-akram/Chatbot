from django.shortcuts import render
from django.shortcuts import render
import openai as ai

# Create your views here.
# API_KEY = Enter api key here
ai.api_key = API_KEY
model_id = 'gpt-3.5-turbo'

def chatGPT_conversion(conversations):
    response = ai.chat.completions.create(
        model=model_id,
        messages=conversations
    )
    conversations.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversations

def chat(request):
    # Initial system message
    conversations = [{'role': 'system', 'content': 'How may I help you?\n'}]

    # Get user input (you can adapt this based on your actual use case)
    user_input = request.GET.get('user_input', '')

    # Append user message to conversations
    conversations.append({'role': 'user', 'content': user_input})

    # Get GPT-3 response
    conversations = chatGPT_conversion(conversations)

    # Extract GPT-3 response content
    gpt_response = conversations[-1]['content']

    # Render a template with the GPT-3 response
    return render(request, 'gpt.html', {'gpt_response': gpt_response,'user_input':user_input})

