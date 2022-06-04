# covbot
A virtual assistant powered by **RASA 3.0** which provides information on COVID-19 and real-time statistics of COVID-19 around the globe.

The bot is deployed on slack **3 - CMPE 252 Chatbot Central**.

**Instructions to run:**
1. Create virtual environment using _python3 -m venv ./venv_
2. Activate the environment using source _./venv/bin/activate_
3. Download all the dependencies as mentioned in requirement.txt
4. Clone this repository in your local machine using _gh repo clone ankdeshm/covbot_
5. Train the model using _rasa train_
6. Activate the action server in another terminal using _rasa run actions_
7. Now run the bot in terminal using _rasa shell_

**Process to open database file:**
1. Go to venv directory and on terminal type sqlite3
2. Open the databse file using _.open "cov.db"_
3. View the table using _SELECT * FROM my_info;_

**Coversation Flows:**

Story 1:
- intent: greet
    - hey
    - hello
    - hi
    - hello there
    - good morning
    - good evening
    - moin
    - hey there
    - let's go
    - hey dude
    - goodmorning
    - goodevening
    - good afternoon
 
  - action: utter_greet
        - Hey! I am Cov-Bot. I can provide information on COVID-19 and COVID-related statistics. Please your first name?

  - intent: first_name
        - Ankita
        - Jorjeta
        - Amanbeer
        - Aman
  
  - action: utter_homestate
        - May I know your home state?
  
  - intent: home_state
        - My home state is California
        - California (Name of any of the 50 states should work)
 
  - action: action_save_homestate
        - Would you like me to save your name and home state?
   
  - intent: storedatabase
        - yes I want to store my information
        - yes store my current information
        - yes store info
        - yes dump the info
        - save my info
        - store my data
        - yes you may store
        - yes you can save

**Bot saves the informarmation in the databse. User can check the updated databse to verify.**

- action: utter_homestats
   - Would you like to know the COVID-19 stats of {homestate}?
   
  
- intent: affirm
   - yes
   - y
   - indeed
   - of course
   - that sounds good
   - correct
  
- action: utter_intro
   - What would you like to know about COVID-19, {firstname}?
   
- action: utter_choice
   - 1. Information 2.Statistics
   
- intent: option_stats
   - 2
   - stats
   - Statistics
   - option 2
   
- action: utter_stats_options
   - Would you like to know 1. Global Statistics 2.Contrywise Statistics 3. US Statewise Statistics
  
- intent: option_global
   - global
   - World
   - world
   - total
   - overall

**Bot displays global statistics.**
  
- action: utter_country_stats
   - Which country's COVID-19 statistics would you like to know?

- intent: countrywise_stats
   - India
   - Germany
   - France
   - Canada
   - China
  
  **Bot displays contry-related statistics.**
  
- action: utter_statename
   - Please enter the US state name for which you want to know the COVID-19 statistics.
   
- intent: corona_state
   - I want to know about Alabama (Name of any of the 50 states should work)

**Bot displays US-statewise statistics.**
  
- action: utter_questions
   - I can answer your question related to COVID-19 provided by WHO. What questions would you like to ask?
  
**After this user can ask any of the following questions to Cov-bot in any order.**

- intent: what_is_corona
    - I wanna know about corona virus?
    - tell me something about corona virus
    - what is coronavirus?
    - what is corona virus?
    - what is corona?
    - what is COVID-19?
    - what is this corona virus which everyone is worried about?

- intent: symptoms
    - What are the symptoms of it?
    - what are its symptoms
    - how to verify that i am suffering from coronavirus
    - any specific symptoms
    - What are the symptoms of COVID-19?

- intent: concern
    - Is it a matter of concern?
    - Is it a serious issue?
    - Is this a major cause?

- intent: who_at_risk
    - Who is most at risk of severe illness from COVID-19?
    - which age group is at higher risk?
    - Who has higher risk?

- intent: long_term_effects
    - Are there long-term effects of COVID-19?
    - What are the long term effects of COVID-19?
    - Any long term effects?

- intent: prevention
    - how to prevent ourselves from getting in contact with corona virus?
    - What are the steps to prevent ourselves from getting in contact with coronavirus?
    - Can you tell me how should I protect myself?

- intent: when_test
    - When should I get a test for COVID-19?
    - when test
    - When shall I get tested?
    - When to test?

- intent: which_tests
    - which tests
    - What test should I get to see if I have COVID-19?
    - Which tests shall I get done?

- intent: past_covid
    - I want to find out if I had COVID-19 in the past, what test could I take?
    - covid in past
    - How to know if I ever had COVID?
    - Did I have corona ever?

- intent: Vaccination
    - Is there any vaccine available for it?
    - What about the vaccination?
    - what medicine should I use If I got infected with coronavirus?
    - What are the vaccines available for COVID-19?

- intent: incubation
    - What is the incubation period for COVID-19?
    - What is the incubation period for it?
    - Is there any incubation period for it?
    - How long does it take to develop symptoms?

- intent: treatment
    - Are there treatments for COVID-19?
    - Any treatment
    - Can COVID-19 be treated?
    - Does Corona have a cure?

- intent: antibiotics
    - Are antibiotics effective in preventing or treating COVID-19?
    - antibiotics
    - Are antibiotics helpful?

- intent: thanks
    - Ok, thanks for making me aware about this serious issue.
    - Thank you so much for awaring me
    - Thanks a lot.
    - Thanks
    - Thank you

  utter_thanks:
   - You're welcome and Stay safe.

Other stories are mentioned in the stories.yml file.


