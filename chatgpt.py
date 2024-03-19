import speech_recognition as sr
import pyttsx3

import os
OPENAI_KEY ="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"

import openai
openai.api_key= OPENAI_KEY

def SpeakText(command):
      engine =pyttsx3.init()
      engine.say(command)
      engine.runAndWait()

r = sr.Recognizer()

def record_text():
      while(1):
            try:
                  with sr.Microphone() as source2:
                        r.adjust_for_ambient_noise(source2, duration=0.2)
                        print("I'm listening")
                        audio2=r.listen(source2)
                        myText=r.recognize_google(audio2)
                        return myText
            except sr.RequestError as e:
                  print("Could not request result: {0}".format(e))
            except sr.UnknownValueError:
                  print("Unknown error")

def send_to_chatGPT(messages,model="gpt-3.5-turbo"):
      response =openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=500,
            n=1,
            stop=None,
            temperator=0.5,
      )
      messages=response.choices[0].message.context
      messages.append(response.choices[0].message)
      return messages

messages=[{"role":"user","content": "Please act like jarvis from iron man."}]
while(1):
        text=record_text()
        messages.append({"role":"user","content": text})
        response =send_to_chatGPT(messages)
        SpeakText(response)
        print(response)