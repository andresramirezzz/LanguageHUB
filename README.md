
# LanguageHUB

LanguageHUB is a Python program created by IE Students that allows you to translate script and .docx documents to more than 30 different languages without needing internet. 

# Table of contents
1. [Description](#Description)
2. [Installation](#Installation)
3. [Usage](#Usage)
4. [Further Improvements](#Further-Improvements)
5. [Support](#Support)
6. [Roadmap](#Roadmap)
7. [Authors](#Authors)
8. [Acknowledgements](#Acknowledgements)
9. [License](#License)
   
## Description

Our application uses OOP for initializing the translation program called LanguageHUB. The class contains two methods; one for text and another one for document. Depending on what the user chooses, the program will run one or another. The text is translated thanks to the library googletranslator, which includes the function Translator(). These was the most efficient and effective way of achieving a fully-working program. We also tried to include an audio-to-transcript translation but that was not feasible with out current Python knowledge. Despite this, we expect to improve and add this extension tool.


## Installation

### Install Programs
Firstly, install [Python](https://www.python.org/downloads/) and [PyCharm](https://www.jetbrains.com/pycharm/download/).

Once you have installed both programs you are ready to begin using LanguageHUB.

### Create Folder

The first step you need to follow is to create a folder in your computer in a place you will remember. This is very important, as you will need to save ['LanguageHUB_icon.png'](LanguageHUB_icon.png), ['requirements.txt'](requirements.txt) & ['LanguageHUB'](/LanguageHUB) in the same folder / environment later. Remember to download the code for your corresponding software; either Windows&Linux or MacOS, if not, the display of the GUI can be changed. 

It is recommended to create a folder on the desktop of your computer for easy access. 

Files >> Desktop >> 'Right Click' >> New Folder >> type: 'LanguageHUB'

Please, do not save the files yet. Wait until its respective step. Thank you!

### Create PyCharm Environment

Once you have created this folder, create a Pycharm environment in this folder. Follow the next steps to do it correctly. The software in the steps is MacOS but in Windows is almost the same, but you may encounter some interface difference

Step 1: Open PyCharm and create a 'New Project'

![Image 1](instruction_images/step1.png)

Step 2: Change the project directory to the folder you previously created

![Image 2](instruction_images/step2.png)

Step 3: Select the folder you created before as your PyCharm project directory

#### In Windows:

![Image 90](instruction_images/step90.png)

#### In Mac:

![Image 2](instruction_images/step3.png)

Extra step: Repeat the process in the Python Interpreter

![Image 2](instruction_images/extrastep.png)

Step 4: Create the project

![Image 4](instruction_images/step4.png)

Step 5: The outlook of the environment

![Image 6](instruction_images/step61.png)

### Open LanguageHUB.py with PyCharm

Now, please  download (['LanguageHUB_icon.png'](LanguageHUB_icon.png), ['requirements.txt'](requirements.txt) & ['LanguageHUB.py'](LanguageHUB.py)) into the folder you used to create the enviroment in your desktop. The files should be found in the 'Downloads' folder in your 'File Explorer'.

The environment should look like this if the files were saved correctly

![Image 6](instruction_images/step6.png)

The next step is the final one. Open the 'LanguageHUB.py' file which is the one containing the program with PyCharm.

![Image 7](instruction_images/step7.png)

### Requirements installation

After this, install the requirements in your Pycharm terminal.

Open Python Terminal:

![Image 8](instruction_images/step8.png)

```python
pip install -r requirements.txt
```

![Image 9](instruction_images/step9.png)

![Image 10](instruction_images/step10.png)

### Run the code

Run the code in the terminal and enjoy!

![Image 11](instruction_images/step12.png)

# IN CASE OF ANY ISSUE, CONSULT [Support](#Support), WHERE COMMON ERROR SOLUTIONS AND CONTACT IS PROVIDED #

## Usage
If every step was followed, the program should open the following window: 

![Image 12](instruction_images/final.png)

Here the user will choose the two possible options for now, either text or document. Audio will come soon. Depending on the chosen method, the program will open the text or the document translator. There's an option for closing the program by pressing the bottom left 'Close' button.

### Text translator
For the text translator, the program asks the user to type the text that they want to translate in the first box. After this, the source language is auto-detected and the program only asks the user for the destination language. Then, the translated text is printed in the second box. Look at the example below.
![Image 13](instruction_images/ssstep1.png)
![Image 13](instruction_images/ssstep2.png)

### Document translator
For the document translator, the program needs the user to upload the .docx document to the virtual environment (See below this step how to do it). 

Once the document has been uploaded to the environment / saved in the folder where all the files are located, you can begin. The first step is to introduce the name of the desired-to-translate document. Then, the destination language is asked to the user too. Finally, the desired name for the new translated document. After this, the new translated document will be opened.

Now, run the code and select the option to translate the document

![Image 16](instruction_images/sstep4.png)

This confirmation message should appear if everything was filled correctly

![Image 17](instruction_images/sstep5.png)

Consequently, the translated document should instantly open

![Image 18](instruction_images/sstep6.png)

### How to upload documents to your environment
This step is needed in order to translate documents and it is required to have Microsoft Word installed in your computer. It is very simple if you follow the next steps.

Save the document you desire in your computer. You can do this by clicking on File >> Save as

![Image 13](instruction_images/sstep1.png)

Choose the folder you created previously and where you saved the ['LanguageHUB_icon.png'](LanguageHUB_icon.png), ['requirements.txt'](requirements.txt) & ['LanguageHUB.py'](LanguageHUB.py) files.

![Image 14](instruction_images/sstep2.png)

Done! Your Python environment should look like the image below.

![Image 15](instruction_images/sstep3.png)

## Further Improvements
- [ ] We should shorten the implementation steps; are very long.
- [ ] Searching the files in the folders is not dynamic.
- [ ] Make it easier for people who don't have Python knowledge.

## Support
In case of any problem, you could contact Nicolás Iago Aguado, which is the person in charge for attending public FAQ and issues. The email is:

n.aguado.ieu2022@student.ie.edu

### Common error: Configure Python Interpreter

If you have encountered this error, here is the solution. 

Your screen might look like this: 

![Image 80](instruction_images/error1.png)

Click on 'Configure Python Interpreter':

![Image 81](instruction_images/error2.png)

Choose Pyhton 3.11 as the interpreter

![Image 54](instruction_images/error3.png)

Now, install the requirements again

![Image 23](instruction_images/error4.png)

Wait until the loading bar is completed 

![Image 55](instruction_images/error5.png)

Done! Run the code to use LanguageHUB again. 

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
