import nlpcloud
from tabulate import tabulate
from collections import Counter

class NLPApp:

    def __init__(self):
        self.__database = {"john@gmail.com": ["john", "1234"]}
        try:
            self.api_key = input("Enter your NLP Cloud API Key: ")
            self.__first_menu()
        except Exception as e:
            print(f"An error occurred: {e}")

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
            print(f"Error: {e}")

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
            print(f"Error: {e}")

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

    def __sentiment_analysis(self):
        try:
            text = input("Enter the text: ")
            client = nlpcloud.Client("finetuned-llama-3-70b", self.api_key, gpu=True)
            response = client.sentiment(text, target="NLP Cloud")

            print("\nSentiment Analysis Result:")
            print(f"{'Sentiment':<15}{'Score':<10}")
            for item in response.get("scored_labels", []):
                print(f"{item['label']:<15}{item['score']:<10.3f}")

            highest_score = max(response['scored_labels'], key=lambda x: x['score'])
            print(f"\nPredicted Sentiment: {highest_score['label']}")
        except Exception as e:
            print(f"Error: {e}")
        self.__second_menu()

    def __translation(self):
        try:
            text = input('Enter text to translate (English → Hindi): ')
            client = nlpcloud.Client("nllb-200-3-3b", self.api_key, gpu=True)
            response = client.translation(text, source="eng_Latn", target="hin_Deva")
            print("\nTranslated Text (Hindi):", response["translation_text"])
        except Exception as e:
            print(f"Error: {e}")
        self.__second_menu()

    def __language_detection(self):
        try:
            text = input("Enter the text to detect language: ")
            client = nlpcloud.Client("python-langdetect", self.api_key, gpu=False)
            response = client.langdetection(text)
            print("\nDetected Languages:")
            for lang in response["languages"]:
                for key, value in lang.items():
                    print(f"{key} -> {value:.3f}")
        except Exception as e:
            print(f"Error: {e}")
        self.__second_menu()

    def __ner(self):
        try:
            text = input("Enter the text: ")
            target_text = input("Enter the target category (e.g., fruits, vegetables, programming languages, etc.): ")

            client = nlpcloud.Client("llama-3-1-405b", self.api_key, gpu=True)
            response = client.entities(text, searched_entity=target_text)

            entities = []
            entity_counts = Counter()

            for entity in response["entities"]:
                entities.append([entity["text"], entity["type"], entity["start"], entity["end"]])
                entity_counts[entity["text"]] += 1

            print("\nExtracted Entities:")
            print(tabulate(entities, headers=["Text", "Type", "Start", "End"], tablefmt="grid"))

            print("\nEntity Occurrences:")
            sorted_entities = sorted(entity_counts.items(), key=lambda x: x[1], reverse=True)
            for idx, (entity, count) in enumerate(sorted_entities, start=1):
                print(f"{idx}. {entity} (Count: {count})")
        except Exception as e:
            print(f"Error: {e}")
        self.__second_menu()

    def __code_genr(self):
        try:
            program_lan = input("Enter the programming language: ")
            text = input("Enter instruction (e.g., Generate a C++ program that sorts a list of integers): ")

            client = nlpcloud.Client("finetuned-llama-3-70b", self.api_key, gpu=True)
            response = client.code_generation(text)

            generated_code = response.get("generated_code", "")
            print("\nGenerated Code:\n")
            print(f"```{program_lan}\n{generated_code}\n```")
        except Exception as e:
            print(f"Error: {e}")
        self.__second_menu()

# Run the app
obj = NLPApp()
