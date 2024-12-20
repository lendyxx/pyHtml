def greet_user():
    name = input("Вседите ваше имя: ")
    print(f"Привет, {name}! Рад тебя видеть!")

while True:
    greet_user()
    continue_prompt = input("Хотите ввести еще одно имя? (y/n): ").strip().lower()
    if continue_prompt != 'y':
        print("Спасибо за использование прогри.")
        break