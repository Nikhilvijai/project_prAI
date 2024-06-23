

![LangChain notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/af58a18d-932c-4ee7-870b-20820cfa3f3f)




### ![arecaai](https://github.com/Nikhilvijai/project_prAI/assets/146342079/d15b1134-551b-4009-97fd-ef53dde62cb5)

This project is a Flask-based API designed to provide detailed information about plants and trees. Users can obtain descriptions, biological data, market details, and growth instructions for specified plants or trees. The API leverages Google's Generative AI to process and retrieve the requested information.
### Team members
1. [Nikhil Vijai](https://github.com/Nikhilvijai)
2. [Madhav-j-nair](https://github.com/madhav-j-nair)
### Link to product walkthrough
[(https://github.com/Nikhilvijai/project_prAI/assets/162718363/bfb1b98e-1113-4518-b27b-59ffffae9e98)](LinkHere)
### How it Works ?
1.Import Libraries and Initialize Environment
 * requests: Used to fetch location data.
 * os: Used to set environment variables.
 * ChatGoogleGenerativeAI: A class from langchain_google_genai to interact with the AI model.
 * streamlit: Used to create the web application.
   
2.Display an Image and Set Up API Key
 * st.image("arecaai.png"): Displays an image at the top of the Streamlit app
 * os.environ["GOOGLE_API_KEY"]: Sets the Google API key as an environment variable.
 * llm: Creates an instance of the ChatGoogleGenerativeAI model.

3.Define Helper Functions
 * get_location(): Fetches the user's latitude and longitude using their IP address.
 * get_plants_by_location(latitude, longitude): Queries the AI model to get a list of plants suitable for the given latitude and longitude.
 * choices(i): Handles follow-up questions recursively. It asks if the user wants to ask another question and processes it.
 * get_plant_details(plant_name, selected_option): Based on the selected option, it queries the AI model for specific information about the plant.

4.Main Program Flow
 * Fetches the user's location.
 * Displays the list of plants suitable for the user's location.
 * Prompts the user to enter a plant name.
 * Allows the user to select a plant and request specific information (description, biological data, market details, how to grow).
 * Handles follow-up questions recursively.

### Libraries used
1.requests

2.os

3.ChatGoogleGenerativeAI

4.streamlit

### How to configure
1.pip install langchain

2.pip install langchain langchain_google_genai

3.pip install streamlit

### How to Run
run:
streamlit run main.py
