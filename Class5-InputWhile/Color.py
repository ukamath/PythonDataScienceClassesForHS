prompt = "Tell me your favorite color"
prompt += "\n(type quit to close) "

colors = ['red', 'blue', 'green']
while True:
    color = input(prompt)

    if color in colors:
        print("Thank you for chosing the " + color)
    elif color == 'quit':
        break
    else:
        print("Please select something i know " + color)
        continue
