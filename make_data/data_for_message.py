import json

data_for_message = {
    "start": """
    Привет! Я твой музыкальный помощник. Вот что я умею:

- Найти песню: используй команду /find
- Послушать песню: используй команду /listen
- Рекомендовать музыку: используй команду /recommendations

Начнем? 🎵🎶
    """,
    "find": """
    Понял. Отправьте название и автора или текст песни, которую вы хотите найти
    """,
    "not_found": """
    К сожалению я не нашел песню с такими данными 😔
    Попобуйте еще раз, нажав /find
    """
}

with open('../data/data_for_message.json', 'w') as file:
    json.dump(data_for_message, file)
