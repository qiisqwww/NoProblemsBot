__all__ = [
    "START_MESSAGE",
    "ASK_MESSAGE",
    "QUESTION_HANDLED_MESSAGE",
    "TIMEOUT_MESSAGE",
    "new_question"
]

START_MESSAGE = """Приветствую! Чтобы задать вопрос или предложить что-нибудь, введите /ask"""

ASK_MESSAGE = """Введите ваш вопрос или предложение."""

QUESTION_HANDLED_MESSAGE = """Ваш вопрос будет рассмотрен администрацией."""

TIMEOUT_MESSAGE = """Вопросы можно писать не чаще, чем раз в 1 минуту."""


def new_question(question: str, user_id: int, username: str) -> str:
    return (f"&#10071; Поступило новое предложение от " + f'<a href="tg://user?id={user_id}">пользователя</a> c ID {user_id} и username {username}&#10071; \n\n'
              f'Его содержимое: {question}\n\nНе забудь рассмотреть!')
