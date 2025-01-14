# pip install pyttsx3

import pyttsx3

text_speech=pyttsx3.init()

answer=('click on the 1st link to view my linkedin profile'
        'click on the 2nd link to view my github profile'
        )
text_speech.say(answer)
text_speech.runAndWait()
print('https://www.linkedin.com/in/jorige-mahesh/')
print('https://github.com/Mahesh-WebWizard')

