import re

# Создайте функцию, которая отвечает на вопрос «Вы играете на банджо?».
# Если ваше имя начинается с буквы «R» или строчной «r», вы играете на банджо!
def are_you_playing_banjo(name):
    match = re.fullmatch(r'(r|R).*', name)
    return (f'{name} plays banjo' if match else f'{name} does not play banjo')
print(are_you_playing_banjo("Rik"))

# def areYouPlayingBanjo(name):
#     return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";