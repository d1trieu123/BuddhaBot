from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'nothing'
    elif 'hello' in lowered:
        return 'hello there!'
    elif 'ping' in lowered:
        return 'pong'
    elif 'roll dice' in lowered:
        return f'you rolled: {randint(1, 6)}'
    else:
        return choice(['hi', 'later', 'wtf'])

