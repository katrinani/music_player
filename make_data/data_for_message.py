import json

data_for_message = {
    "start": """
    Привет! Я твой музыкальный помощник. Вот что я умею:

- Найти песню: используй команду /find
- Послушать песню: используй команду /listen
- Рекомендовать музыку: используй команду /recommendations

Начнем? 🎵🎶
    """
}

with open('../data/data_for_message.json', 'w') as file:
    json.dump(data_for_message, file)
