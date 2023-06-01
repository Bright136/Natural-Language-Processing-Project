import gradio as gr
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoConfig,AutoModelForSequenceClassification
from scipy.special import softmax
import os


# define models
distilbert_path = "bright1/fine-tuned-distilbert-base-uncased"
roberta_path = "bright1/fine-tuned-twitter-Roberta-base-sentiment"
# Requirements
def load_model(model_path):
    
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    # config = AutoConfig.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return model, tokenizer

# def check_csv(csv_file, data):
#     if os.path.isfile(csv_file):
#         data.to_csv(csv_file, mode='a', header=False, index=False, encoding='utf-8')
#     else:
#         history = data.copy()
#         history.to_csv(csv_file, index=False)

# Preprocess the input text
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        # Replace usernames with a common placeholder
        t = "@user" if t.startswith("@") and len(t) > 1 else t
        # Replace URLs with a common placeholder
        t = "http" if t.startswith("http") else t
        print(t)
        new_text.append(t)
    print(new_text)

    return " ".join(new_text)

# Process the input text and return sentiment prediction
def sentiment_analysis(model_type, text):
    if model_type == 'distilbert':
        model, tokenizer = load_model(distilbert_path)
    else:
        model, tokenizer = load_model(roberta_path)
    save_text = {'tweet': text}
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors="pt")  # for PyTorch-based models
    output = model(**encoded_input)
    scores_ = output[0][0].detach().numpy()
    scores_ = softmax(scores_)

    # Format output dictionary of scores
    labels = ["Negative", "Neutral", "Positive"]
    scores = {l: float(s) for (l, s) in zip(labels, scores_)}
    # save_text.update(scores)
    # user_data = {key: [value] for key,value in save_text.items()}
    # data = pd.DataFrame(user_data,)
    # check_csv('history.csv', data)
    # hist_df = pd.read_csv('history.csv')
    return scores
# , hist_df.head()


# Create a radio button to select the model type
model_type = gr.Radio(choices=['distilbert', 'roberta'], label='Select model type', value='roberta')

# Gradio app interface

# Define the Gradio interface for the sentiment_analysis function
demo = gr.Interface(
    fn=sentiment_analysis,  # The function to be executed when the interface is interacted with
    inputs=[model_type, gr.TextArea("Write your text or tweet here", label="Analyze your COVID-19 tweets")],  # The input components of the interface
    outputs=["label"],  # The output component of the interface
    title="COVID-19 Vaccine Tweet Analyzer App",  # The title of the interface
    description="COVID-19 Tweets Analyzer",  # The description of the interface
    interpretation="default",  # The interpretation mode for the interface
    examples=[["roberta", "Being vaccinated is actually awesome :)"]]  # Examples to show in the interface
)

# Launch the Gradio app, enabling sharing and specifying the server port
demo.launch(share=True, server_port=8080)


