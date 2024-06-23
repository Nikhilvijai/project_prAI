

![LangChain notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/af58a18d-932c-4ee7-870b-20820cfa3f3f)




### ![arecaai](https://github.com/Nikhilvijai/project_prAI/assets/146342079/d15b1134-551b-4009-97fd-ef53dde62cb5)

This is a streamlit project which uses Langchain with ChatGoogleGenerativeAI to make a website that accepts your lattitude and longitude and using that they provide the plants and trees which are native and suitable to grow near you. This is just a trailer as your interest in a specific plant will be entertained giving you opyions to ask about the description,market,biological data of the plant or a practical question how to grow them. If this is not it you can keep on questioning till you clear your doubt.
### Team members
1. [Nikhil Vijai](https://github.com/Nikhilvijai)
2. [Madhav-j-nair](https://github.com/madhav-j-nair)
### Link to product walkthrough
[(https://github.com/Nikhilvijai/project_prAI/assets/162718363/bfb1b98e-1113-4518-b27b-59ffffae9e98) ](Link Here)
### How it Works ?

1. The first process is fetching latitude and longitude using ipinfo.io website. Then the data is sent to gemini to get the details of the plants which can be grown in our space and the data is displayed to user.

2. The second process is accepting a plant of his choice and then giving him an option to know about the "DESCRIPTION","BIOLOGICAL DATA","MARKET DETAILS","HOW TO GROW". Based on this option a prompt is sent to gemini and the results are displayed

3. The next process is to ask for the user whether he has any questions(what is displayed:"Would you like to ask another question") if yes(y) then the question(what is displayed:"Enter your follow-up question") is recieved and it is prompted to gemini after which results are displayed, this loop continues till his doubts are cleared. If he has cleared all his doubts and answers no(n) for anymore questions he is bid farewell till the next time he visits again.
   
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
