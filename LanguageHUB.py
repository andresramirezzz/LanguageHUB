import docx #Used for accessing doc files #As stated in the README, you need to install from the terminal this library by putting 'pip install python-docx'
from googletrans import Translator #Used for importing the translation function
from prettytable import PrettyTable #Used for importing the library that will print the language: abbreviation table
from colorama import Fore, Back, Style #Library for changing the style of the letters
import time #for waiting before running the translator again so that the user can read the error message

# Create a table named 'lan' for showing the language and each corresponding abbreviation
lan = PrettyTable()
# Define column names
lan.field_names = ["Language", "Abbreviation"]
#Create a dictionary containing each language and abbreviation as a key:value combination
dictlan = {
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Amharic': 'am',
    'Arabic': 'ar',
    'Armenian': 'hy',
    'Azerbaijani': 'az',
    'Basque': 'eu',
    'Belarusian': 'be',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Bulgarian': 'bg',
    'Catalan': 'ca',
    'Cebuano': 'ceb',
    'Chichewa (Chewa, Nyanja)': 'ny',
    'Chinese (Simplified)': 'zh-cn',
    'Chinese (Traditional)': 'zh-tw',
    'Corsican': 'co',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'English': 'en',
    'Esperanto': 'eo',
    'Estonian': 'et',
    'Filipino': 'tl',
    'Finnish': 'fi',
    'French': 'fr',
    'Frisian': 'fy',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Haitian Creole': 'ht',
    'Hausa': 'ha',
    'Hawaiian': 'haw',
    'Hebrew': 'iw',
    'Hindi': 'hi',
    'Hmong': 'hmn',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Igbo': 'ig',
    'Indonesian': 'id',
    'Irish': 'ga',
    'Italian': 'it',
    'Japanese': 'ja',
    'Javanese': 'jw',
    'Kannada': 'kn',
    'Kazakh': 'kk',
    'Khmer': 'km',
    'Korean': 'ko',
    'Kurdish (Kurmanji)': 'ku',
    'Kyrgyz': 'ky',
    'Lao': 'lo',
    'Latin': 'la',
    'Latvian': 'lv',
    'Lithuanian': 'lt',
    'Luxembourgish': 'lb',
    'Macedonian': 'mk',
    'Malagasy': 'mg',
    'Malay': 'ms',
    'Malayalam': 'ml',
    'Maltese': 'mt',
    'Maori': 'mi',
    'Marathi': 'mr',
    'Mongolian': 'mn',
    'Burmese': 'my',
    'Nepali': 'ne',
    'Norwegian': 'no',
    'Odia (Oriya)': 'or',
    'Pashto': 'ps',
    'Persian (Farsi)': 'fa',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Punjabi': 'pa',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Samoan': 'sm',
    'Scots Gaelic': 'gd',
    'Serbian': 'sr',
    'Sesotho': 'st',
    'Shona': 'sn',
    'Sindhi': 'sd',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Somali': 'so',
    'Spanish': 'es',
    'Sundanese': 'su',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tajik': 'tg',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Uyghur': 'ug',
    'Uzbek': 'uz',
    'Vietnamese': 'vi',
    'Welsh': 'cy',
    'Xhosa': 'xh',
    'Yiddish': 'yi',
    'Yoruba': 'yo',
    'Zulu': 'zu'
}

# Add rows to the table
for lang, abbr in dictlan.items():
    lan.add_row([lang, abbr])


class LanguageHUB():
    def __init__(self):
        self.translated_doc = docx.Document()
        self.translator = Translator()

    def doc():
        print(
            'You have chosen to translate a document\nRemember that you need to upload '
            'the document in this Pyhton environment for the program to work.\n')  # Reminds the user that the document has to be uploaded to the environment for the function to work.
        sourcename = input(
            "Let's begin! Which is the name of the document you want to translate?\n").strip()  # Ask the user for the name of the source document so that it can access to it. The .strip() is used for eliminating any possible whitespaces (spaces,tabs, and newline characters) before or after the title. This is saved into a variable called sourcename
        targetdocname = input(
            "How do you want to name the translated document?\n").strip()  # Asks the user for the desired saving name of the translated document. This is saved into a variable called targetname
        print(lan)  # Print the table with languages and abbreviations
        targetlan = str(input('Above you can find a table showing the supported language '
                              'and their respective abbreviation\nTo which language do you '
                              'want to translate?\nJust put the abbreviation of the language\n'))  # Asks the user the desired language using the abbreviations table shown above. This is saved into a variable called targetlan
        doc = docx.Document(
            sourcename + ".docx")  # With the .docx function, we specify the name of the sourcedocument previously provided by the user and we are able to read/access the document. This 'access' is saved into a variable called doc.
        translated_doc = docx.Document()  # Creating a variable for the new doc in which the translated text will be written
        paragraphs = [para.text for para in
                      doc.paragraphs]  # This function creates a list containing the content of each parragraph in the sourcedoc. It iterates through each parragraph using a for loop and stores it as text in a list.
        translator = Translator()  # Calling the function of the library 'googletrans' previously imported, but changing its name for easy further recalling.
        for i, para in enumerate(
                paragraphs):  # For loop that iterates through each 'parragraph'/text/element stored in the list called paragraphs
            try:  # We used try to avoid any exception errors
                translation = translator.translate(para,
                                                   dest=targetlan)  # Calling the translator function that will take it element/parragraph in the list parragraphs and traduce it to the targetlan
                translated_doc.add_paragraph(
                    translation.text)  # Adds the translated parragraphs to the translated_doc previously created
                print(
                    "Document translation is completed. Once again, LanguageHUB has saved you time.")  # A confirmation message
            except:  # In case of error; such as a not uploaded document or not readable document such as a .pwt
                print(
                    "Error. The program did not work. Make sure the document is uploaded in the environment as a .docx and that the name of the document matches to the one it was input when the system asked for it" + str(
                        i))  # Message telling that the program did not work and reminding the user that everything has to be uploaded as a .docx file and the name must match when the system asks for it
        translated_doc.save(
            targetdocname + ".docx")  # If there is no exception, the program will save the translated document as a .docx (compatible with word) with the name previously put by the user

    def text():
        translator = Translator()  # change the name just to make it easier to call
        a = str(input("You have chosen to translate a text. Write here the text you desire.\n"))  # Obtain the input text
        print(lan)  # Print the table with languages and abbreviations
        outputt = str(input('Above you can find a table showing the supported language '
                            'and their respective abbreviation\nTo which language do you '
                            'want to translate?\nJust put the abbreviation of the language\n'))  # Ask the user for the desired output language
        out = translator.translate(text=a, dest=outputt)  # Obtain the translated text recalling the translator function
        print("Text translation is completed. Once again, LanguageHUB has saved you time.")  # A confirming message
        print(out.text)  # Print just the output text using the function '.text'

#Create the program using the OOP previosuly defined
while True: #This while will allow the execution of the code constantly
    welcome = input(f"Hello! Welcome to {Style.BRIGHT}{Back.BLUE}{Fore.BLACK}Language"
                    f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}HUB{Style.RESET_ALL}\n"
                    f"{Style.BRIGHT}{Fore.CYAN}Currently we can only translate text "
                    f"or documents, audio will be coming soon.{Style.RESET_ALL}\nWhat "
                    f"do you want to translate? A {Fore.BLUE}{Style.BRIGHT}text{Style.RESET_ALL} "
                    f"or a {Fore.BLUE}{Style.BRIGHT}document?{Style.RESET_ALL}\n") #A formatted welcome message asking the user which tool from LanguageHUB they want to use
    if welcome.lower() in ['text', 'a text']: #Conditional in the case the user wants to translate a text
        LanguageHUB.text() #Initialize the text translator
        break  #Exit the loop if a valid choice is made
    elif welcome.lower() in ['doc', 'document', 'a doc']: #Conditional in the case the user wants to translate a document
        LanguageHUB.doc() #Initialize the doc translator
        break  #Exit the loop if a valid choice is made
    else: #In the case of a not valid choice
        print(
            f"{Fore.RED}{Back.LIGHTWHITE_EX}{Style.BRIGHT}              "
            f"            ERROR                          {Style.RESET_ALL}"
            f"\n{Back.LIGHTWHITE_EX}                                  "
            f"                       {Style.RESET_ALL}\n{Fore.RED}"
            f"{Back.LIGHTWHITE_EX}{Style.BRIGHT} We are sorry, but the program "
            f"could not understand you  {Style.RESET_ALL}\n{Back.LIGHTWHITE_EX}"
            f"                                                         {Style.RESET_ALL}"
            f"\n{Fore.BLACK}{Back.LIGHTWHITE_EX}{Style.BRIGHT} Try answering "
            f"either'{Style.RESET_ALL}{Fore.BLACK}{Back.LIGHTGREEN_EX}{Style.BRIGHT}"
            f"A document{Style.RESET_ALL}{Fore.BLACK}{Back.LIGHTWHITE_EX}{Style.BRIGHT}'"
            f"or'{Style.RESET_ALL}{Fore.BLACK}{Back.LIGHTGREEN_EX}{Style.BRIGHT}A text"
            f"{Style.RESET_ALL}{Fore.BLACK}{Back.LIGHTWHITE_EX}{Style.BRIGHT}' depending  "
            f"  {Style.RESET_ALL}\n{Fore.BLACK}{Back.LIGHTWHITE_EX}{Style.BRIGHT}"
            f"              on what you want to use                    {Style.RESET_ALL}\n") #Formatted error message

        time.sleep(2) #Wait time (2s) before running again the loop, so the user can read the error message