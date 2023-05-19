#  🚀Building a Sentiment Analysis App with Gradio 😟😐😊 🚀
This is a Gradio app that performs sentiment analysis on COVID-19 tweets using two pre-trained language models, DistilBERT and RoBERTa.

## Summary
| Code      | Name        | Published Article |  Deployed App |
|-----------|-------------|:-------------:|------:|
| LP5 | NLP Sentiment Analysis App with Gradio |  [Deploying an App on Hugging Face](https://medium.com/@brighteshun/deploying-a-sentiement-analysis-app-on-huggingface-faeb43954905) | [Covid-19 Tweets Analyzer App](https://huggingface.co/spaces/bright1/sentiment-analysis-app-gradio) |

			
## Project Description
The aim of this project is to analyze the sentiment of tweets related to COVID-19 using two pre-trained language models, DistilBERT and RoBERTa. The app takes in user-generated text input (tweet) and predicts whether the sentiment of the tweet is Negative, Neutral, or Positive. The app also preprocesses the input text by replacing any mention of usernames with "@user" and replacing any URLs with "http".

How the app works

- Select the model type from the dropdown list. You can choose between DistilBERT and RoBERTa.
- Type your tweet or text in the text area provided.
- Click on the "Analyze" button to get the sentiment analysis of your input text.

## Setup
To set up the project locally, follow these steps:

- To Clone into this particular in the repository run the following commands:
        
        git clone --depth 1 https://github.com/Bright136/Natural-Language-Processing-Project gradio_app 
        cd gradio_app
        git sparse-checkout init --cone 
        git sparse-checkout set gradio_app


- To create an environment and install dependencies for the app
Do:
- Windows:

        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip
        python -m pip install -qr 'https://raw.githubusercontent.com/Bright136/Natural-Language-Processing-Project/main/requirements.txt'  

- Linux & MacOs:

        python3 -m venv ve  nv; source venv/bin/activate; python -m pip install -q --upgrade pip
        python -m pip install -qr 'https://raw.githubusercontent.com/Bright136/Natural-Language-Processing-Project/main/requirements.txt'


## App Execution
To execute the app, follow these steps:

- At the root of your app diretory  in your terminal
run the command: 


            gradio pp.py

- Open your browser and go to http://127.0.0.1:8080

<span>Photos of the Gradio App</span>

<div align='center'> 
    <img src="https://drive.google.com/uc?export=view&id=1Qk9j4V5NGoZlraE5VJS51L6n5m_RoFZQ"/>

</div>

## Author
Bright Eshun
