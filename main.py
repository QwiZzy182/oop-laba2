from regex_checker import EmailValidator

def main():
    validator = EmailValidator()
    print("=== Анализатор E-mail ===")
    user_input = input("Введите текст с e-mail адресами: ")
    found = validator.validate_text(user_input)
    print(f"Найденные адреса: {found}")

if __name__ == "__main__":
    main()
