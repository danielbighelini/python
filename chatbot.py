import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

start_chat_log = '''Humano: Olá!
AI: Como eu posso te ajudar?
'''


def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Humano: {question}\nAI:'
    response = completion.create(
        prompt=prompt,
        engine=os.environ.get('OPENAI_ENGINE'),
        stop=['\nHumano'],
        temperature=float(os.environ.get('OPENAI_TEMPERATURE')),
        top_p=float(os.environ.get('OPENAI_TOP_P')),
        frequency_penalty=float(os.environ.get('OPENAI_FREQUENCY_PENALTY')),
        presence_penalty=float(os.environ.get('OPENAI_PRESENCE_PENALTY')),
        best_of=int(os.environ.get('OPENAI_BEST_OF')),
        max_tokens=int(os.environ.get('OPENAI_MAX_TOKENS')))
    answer = response.choices[0].text.strip()
    if response.choices[0].finish_reason == 'length':
        answer += "..."
    # print(response)
    return answer


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Humano: {question}\nAI: {answer}\n'
