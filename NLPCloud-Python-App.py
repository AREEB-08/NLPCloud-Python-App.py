import nlpcloud

class NLPApp:

    def __init__(self):
        self.__database = {"kavin@gmail.com":["kavin","1234"]}
        self.__first_menu()

    def __first_menu(self):
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

    def __second_menu(self):
        second_input = input("""
        Hi! how would you like to proceed?

        1. NER
        2. Language Detection
        3. Sentiment Analysis
        4. Translation (English → Hindi)
        5. code generation
        6.exit
        """)

        if second_input == '1':
            self.__ner()
        elif second_input == '2':
            self.__language_detection()
        elif second_input == '3':
            self.__sentiment_analysis()
        elif second_input == '4':
            self.__translation()
        elif second_input=='5':
            self.__code_genr()

    def __register(self):
        name = input('Enter name: ')
        email = input('Enter email: ')
        password = input('Enter password: ')

        if email in self.__database:
            print('Email already exists')
        else:
            self.__database[email] = [name, password]
            print('Registration successful. Now login.')
            self.__first_menu()

    def __login(self):
        email = input('Enter email: ')
        password = input('Enter password: ')

        if email in self.__database:
            if self.__database[email][1] == password:
                print('Login successful')
                self.__second_menu()
            else:
                print('Wrong password. Try again')
                self.__login()
        else:
            print('This email is not registered')
            self.__first_menu()
