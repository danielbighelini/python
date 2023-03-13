from chatbot import ask, append_interaction_to_chat_log
from colorama import Fore, Back, Style

if __name__ == '__main__':

    chat_log = None

    while True:
        question = input(Fore.WHITE + 'Pergunta: ')
        if question == "": break
        answer = ask(question, chat_log)
        print(Fore.GREEN + f'Resposta: {answer}')
        chat_log = append_interaction_to_chat_log(question, answer, chat_log)
