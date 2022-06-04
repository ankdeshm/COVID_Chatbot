# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests
import sqlite3
import speech_recognition as sr
from translate import Translator


class Actionsavefirstname(Action):

    def name(self) -> Text:
        return "action_save_firstname"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(tracker.get_slot('firstname'))
        return [SlotSet('firstname',tracker.latest_message['text'])]


class Actionsavehomestate(Action):

    def name(self) -> Text:
        return "action_save_homestate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_template("utter_to_ask",tracker)
        print(tracker.get_slot('homestate'))

        return [SlotSet('homestate',tracker.latest_message['text'])]

def datastore(firstname, homestate):
    conn=sqlite3.connect('cov.db')
    mycursor = conn.cursor()
    mycursor.execute("""CREATE TABLE IF NOT EXISTS my_info (Name TEXT, HomeState TEXT);""")
    mycursor.execute("INSERT INTO my_info VALUES (?,?)",(firstname,homestate))
    conn.commit()
    print(mycursor.rowcount,"record inserted")


class ActionStore(Action):

    def name(self) -> Text:
        return "action_store"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        x=tracker.get_slot('firstname')
        y=tracker.get_slot('homestate')
        datastore(x,y)
        dispatcher.utter_message("Thank you! Your information is saved.")
        print(x)
        print(y)
        return []

class ActionCoronaHomeState(Action):
     def name(self):
      return "action_corona_homestate"

     def run(self, dispatcher, tracker, domain):
      response = requests.get("https://disease.sh/v3/covid-19/states")
      response_data = response.json()
      homestate = tracker.get_slot('homestate')
      print("HomeState ", homestate)
      message1 = "Please enter correct STATE name"
      for data in response_data:
              if data["state"] == homestate.title():
                  print(data)
                  message1 = "Todays Cases: " + str(data["todayCases"]) + "\n" +"Total Cases: " + str(data["cases"]) + "\n" +"Todays Deaths: " + str(data["todayDeaths"]) + "\n" +"Total Deaths: " + str(data["deaths"]) + "\n" +"Total Recovered: " + str(data["recovered"]) + "\n" +"Active cases: " + str(data["active"])
      
      dispatcher.utter_message(message1)
      return []

class ActionCoronaStates(Action):
     def name(self):
      return "action_corona_state"

     def run(self, dispatcher, tracker, domain):

      response = requests.get("https://disease.sh/v3/covid-19/states")
      response_data = response.json()
      # print(response_data)
      state = tracker.get_slot('state')
      print(state)
      message1 = "Please enter correct STATE name"
      for data in response_data:
              if data["state"] == state.title():
                  print(data)
                  message1 = "Todays Cases: " + str(data["todayCases"]) + "\n" +"Total Cases: " + str(data["cases"]) + "\n" +"Todays Deaths: " + str(data["todayDeaths"]) + "\n" +"Total Deaths: " + str(data["deaths"]) + "\n" +"Total Recovered: " + str(data["recovered"]) + "\n" +"Active cases: " + str(data["active"])
      
      dispatcher.utter_message(message1)
      return []


class ActionCoronaUS(Action):
     def name(self):
      return "action_corona_US"

     def run(self, dispatcher, tracker, domain):
      response = requests.get("https://disease.sh/v3/covid-19/countries/usa")
      response_data = response.json()
      message1 = "Todays Cases: " + str(response_data["todayCases"]) + "\n" +"Total Cases: " + str(response_data["cases"]) + "\n" +"Todays Deaths: " + str(response_data["todayDeaths"]) + "\n" +"Total Deaths: " + str(response_data["deaths"]) + "\n" +"Total Recovered: " + str(response_data["recovered"]) + "\n" +"Todays Recovered: " + str(response_data["todayRecovered"]) + "\n" +"Active cases: " + str(response_data["active"]) + "\n" +"Critical cases: " + str(response_data["critical"])
      dispatcher.utter_message(message1)
      return []



class ActionCoronaCountries(Action):
     def name(self):
      return "action_corona_countries"

     def run(self, dispatcher, tracker, domain):
      
      response = requests.get("https://disease.sh/v3/covid-19/countries")
      response_data = response.json()
      # print(response_data)
      country = tracker.get_slot('country')
      print(country)
      message1 = "Please enter correct CONTRY name"
      for data in response_data:
              if data["country"] == country.title():
                  print(data)
                  message1 = "Todays Cases: " + str(data["todayCases"]) + "\n" +"Total Cases: " + str(data["cases"]) + "\n" +"Todays Deaths: " + str(data["todayDeaths"]) + "\n" +"Total Deaths: " + str(data["deaths"]) + "\n" +"Total Recovered: " + str(data["recovered"]) + "\n" +"Active cases: " + str(data["active"]) + "\n" +"Population: " + str(data["population"])
      
      dispatcher.utter_message(message1)
      return []
      

class ActionCoronaWorld(Action):
     def name(self):
      return "action_corona_World"

     def run(self, dispatcher, tracker, domain):

      response = requests.get("https://disease.sh/v3/covid-19/all")
      response_data = response.json()
      message1 = "Todays Cases: " + str(response_data["todayCases"]) + "\n" +"Total Cases: " + str(response_data["cases"]) + "\n" +"Todays Deaths: " + str(response_data["todayDeaths"]) + "\n" +"Total Deaths: " + str(response_data["deaths"]) + "\n" +"Total Recovered: " + str(response_data["recovered"]) + "\n" +"Todays Recovered: " + str(response_data["todayRecovered"]) + "\n" +"Active cases: " + str(response_data["active"]) + "\n" +"Critical cases: " + str(response_data["critical"]) + "\n" +"Tests: " + str(response_data["tests"])
      dispatcher.utter_message(message1)
      return []


# class ActionVoiceData(Action):

#     def name(self) -> Text:
#         return "action_activate_voice"
    
#     bot_message = ""
#     message=""

#     r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})
#     print("Bot says, ",end=' ')
#     for i in r.json():
#       bot_message = i['text']
#       print(f"{bot_message}")


#     while bot_message != "Bye" or bot_message!='thanks':

#         r = sr.Recognizer()  # initialize recognizer
#         with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
#             print("Ask anything about COVID-19 :")
#             audio = r.listen(source)  # listen to the source
#             try:
#                 message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
#                 print("You said : {}".message)
#             except:
#                 print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
#         if len(message)==0:
#             continue
#         print("Sending message now...")

#         r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

#         print("Bot says, ",end=' ')
#         for i in r.json():
#             bot_message = i['text']
#             print(f"{bot_message}")
