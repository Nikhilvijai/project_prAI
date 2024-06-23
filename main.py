import requests
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

st.image("arecaai.png")
os.environ["GOOGLE_API_KEY"] = "..API_KEY.."  # Assuming you have your API key stored securely
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="..")



def get_location():
    response = requests.get('https://ipinfo.io')
    data = response.json()
    location = data['loc'].split(',')
    return float(location[0]), float(location[1])


def get_plants_by_location(latitude, longitude):
    result = llm.invoke(f'give the list of plants and trees that are habitable in the location, latitude {latitude},longitude {longitude}')
    plants = result.content
    return plants


def choices(i):
    follow_up_pr = st.text_input("Would you like to ask another question (y/n)? ",key=-1-i)
    follow_up_prompt = ""
    if follow_up_pr == 'y':
        follow_up_question = st.text_input("Enter your follow-up question: ",key=100000000000+i)
        if follow_up_question != "":
          follow_up_prompt = llm.invoke(f"{plant_name}, {follow_up_question}")
          st.write(follow_up_prompt.content)
          i+=1
          choices(i)
    elif follow_up_pr == "n":
     st.write("Thank you for reaching out to us,hope you had a fruitfull conversation with us!")
    else :
        return 0
      


def get_plant_details(plant_name,selected_option):
    if selected_option =="DESCRIPTION":
        follow = llm.invoke(f"give a description about the {plant_name}")
        st.write(follow.content)
    elif selected_option =="BIOLOGICAL DATA":
        follow = llm.invoke(f"give details about biological features like growth time, age, environmental conditions as a list of {plant_name}")
        st.write(follow.content)
    elif selected_option =="MARKET DETAILS":
        follow = llm.invoke(f"give details about the market data , cost of seed, export potential, market in India as a list of {plant_name}")
        st.write(follow.content)
    elif selected_option == "HOW TO GROW":
        follow = llm.invoke(f"step by step procedure on how to grow , the conditions and tips of {plant_name}")
        st.write(follow.content) 
    
    

  

# Main program flow

latitude, longitude = get_location()
plants = get_plants_by_location(latitude, longitude)
st.write(plants)


plant_name = st.text_input("Enter the name of the plant you'd like details about: ")
if plant_name != "":
    selected_option = st.selectbox("Select an option:", options=["DESCRIPTION", "BIOLOGICAL DATA", "MARKET DETAILS","HOW TO GROW"])
    get_plant_details(plant_name, selected_option)
    i=0
    choices(i)


    



    





