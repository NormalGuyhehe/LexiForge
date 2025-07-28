def write():
    user_email: str = input("Введите свою почту: ")
    user_password: str = input("Введите свой пароль: ")
    with open (".env", "a+") as file:
        file.write(f"DUOLINGO_USERNAME={user_email}\n")
        file.write(f"DUOLINGO_PASSWORD={user_password}\n")