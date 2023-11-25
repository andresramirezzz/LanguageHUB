
# LanguageHUB

LanguageHUB is a Python program created by IE Students that allows you to translate script and .docx documents to more than 30 different languages without needing internet. 

# Table of contents
1. Description
2. Installation
3. Usage
4. Further Improvements
5. Support
6. Roadmap
7. Authors
8. Acknowledgements
9. License
   
## Description

Our application uses OOP for initializing the translation program called LanguageHUB. The class contains two methods; one for text and another one for document. Depending on what the user chooses, the program will run one or another. The text is translated thanks to the library googletranslator, which includes the function Translator(). These was the most efficient and effective way of achieving a fully-working program. We also tried to include an audio-to-transcript translation but that was not feasible with out current Python knowledge. Despite this, we expect to improve and add this extension tool.


## Installation
Firstly, install [Python](https://www.python.org/downloads/) and [PyCharm](https://www.jetbrains.com/pycharm/download/).

Once you have installed both programs you are ready to begin using LanguageHUB.

The first step you need to follow is to create a folder in your computer in a place you will remember. This is very important, as if you don't save the documents you are willing to translate, and some files we will ask you to download later, the LanguageHUB won't be able to help you.

Once you have created this folder,  open up Pycharm, press on the three lines on the top left side, then click on file, new project and make sure you save the project in the previously created folder. In order for you to check where you are saving this new project you will have to look on the top of the emergent window, where it says "Location:",  if the following path leads to your folder you are done and can press "Create" on the botton right. If the path isn't leading you to the folder you created, click on the small folder at the right of the bar and look for the folder you created, once you find it click on top of it and then press on "Ok", now you are good to go and can press on "Create" at the bottom right.

Download the 'requirements.txt' and the 'LanguageHUB.py' files. Save them in the same folder you have used to create the project, as previously explained.

Then, install the requirements in your Python terminal.


```python
pip install -r requirements.txt
```

The next step is the final one. Open the 'LanguageHUB.py' file which is the one containing the program. 

Run the code in the terminal and enjoy!

```python
python LanguageHUB.py
```

## Usage
If every step was followed, the program should print the following message: 

```python 
Hello! Welcome to LanguageHUB.
Currently we can only translate text or documents, 
audio will be coming soon. What do you want to translate?
A text or a document? Answer 'EXIT' if you want to leave 
the program
```

Here the user will introduce the two possible options for now, either text or document. Depending on the chosen method, the program will run the text or the document translator. If the response was neither of both, the program will print an error message and will return the question again. There's an option for closing the program, which if chosen, a goodbye message will be displayed.

### Document translator
For the document translator, the program asks the user to upload the .docx document to the virtual environment and then, to tell the program which name has the document. Then, the desired name for the new translated document is asked to the user too. Finally, the destination language chosen. After this, the translated document will be saved in the virtual environment with the new name previously chosen by the user.

### Text translator
For the text translator, the program asks the user for the text that they want to translate. After this, the source language is auto-detected and the program only asks the user for the destination language. Then, the translated text is printed in the console.

## Further Improvements

## Support
In case of any problem, you could contact Nicolás Iago Aguado, which is the person in charge for attending public FAQ and issues. The email is:

n.aguado.ieu2022@student.ie.edu

## Roadmap
We are planning on improving the program display, make it more like an app and not just a Python program. In addition, we would like to include PDF translator and audio translator for the next version.

## Authors
Rubén Segura: [Github](https://github.com/rubensegu)

Gonzalo Mir: [Github](https://github.com/gonzalomirr)

Miguel Gordon: [Github](https://github.com/mgordon16)

Nicolás Iago Aguado: [Github](https://github.com/niconik)

Yago Moreno: [Github](https://github.com/ymoreno2022)

Bruno Sanchís: [Github](https://github.com/brsado)

Andres Ramirez: [Github](https://github.com/andresramirezzz)

## Acknowledgements

This project could have not been possible without the inspiration on [translator.py](https://github.com/codebasics/cool_python_apps/blob/main/1_language_translate/translator.py) from [codebasics](https://github.com/codebasics) and their project [cool_python_apps](https://github.com/codebasics/cool_python_apps)

Also, another inspiration project was [Docx-Translator](https://github.com/karayaman/Docx-Translator/blob/master/main.py) from [Karayaman](https://github.com/karayaman)

## License

Copyright (c) [2023] [LanguageHUB]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "LanguageHUB.py"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
