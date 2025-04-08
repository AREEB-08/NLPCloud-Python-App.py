import nlpcloud
from tabulate import tabulate
from collections import Counter

class NLPApp:

    def __init__(self):
        self.__database = {"kavin@gmail.com": ["kavin", "1234"]}
        try:
            self.api_key = input("Enter your NLP Cloud API key: ")
            self.model = input("Enter the model name (e.g., finetuned-llama-3-70b): ")
            self.gpu = input("Use GPU? (yes/no): ").lower() == "yes"
            self.__first_menu()
        except Exception as e:
            print("Error during initialization:", e)

    def __first_menu(self):
        try:
            first_input = input("""
            Hi! how would you like to proceed?

            1. Not a member? Register
            2. Already a member? Login
            3. Galti se aa gaye? Exit
            """)

            if first_input == '1':
                self.__register()
            elif first_input == '2':
                self.__login()
            else:
                exit()
        except Exception as e:
            print("Error in first menu:", e)

    def __second_menu(self):
        try:
            second_input = input("""
            Hi! how would you like to proceed?

            1. NER
            2. Language Detection
            3. Sentiment Analysis
            4. Translation (English → Hindi)
            5. Code Generation
            6. Exit
            """)

            if second_input == '1':
                self.__ner()
            elif second_input == '2':
                self.__language_detection()
            elif second_input == '3':
                self.__sentiment_analysis()
            elif second_input == '4':
                self.__translation()
            elif second_input == '5':
                self.__code_genr()
            else:
                exit()
        except Exception as e:
            print("Error in second menu:", e)
    def __register(self):
        try:
            name = input('Enter name: ')
            email = input('Enter email: ')
            password = input('Enter password: ')

            if email in self.__database:
                print('Email already exists')
            else:
                self.__database[email] = [name, password]
                print('Registration successful. Now login.')
                self.__first_menu()
        except Exception as e:
            print("Error in registration:", e)
       



