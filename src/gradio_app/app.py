import gradio as gr
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoConfig,AutoModelForSequenceClassification
from scipy.special import softmax
import os

# Requirements
def load_distilbert():
    model_path = "bright1/fine-tuned-distilbert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    # config = AutoConfig.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return model, tokenizer

def load_roberta():
    model_path = "bright1/fine-tuned-twitter-Roberta-base-sentiment"
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

#Preprocess text
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = "@user" if t.startswith("@") and len(t) > 1 else t
        t = "http" if t.startswith("http") else t
        print(t)
        new_text.append(t)
    print(new_text)

    return " ".join(new_text)

#Process the input and return prediction
def sentiment_analysis(model_type, text):
    if model_type== 'distilbert':
        model, tokenizer  = load_distilbert()
    else:
        model, tokenizer = load_roberta()
    save_text =  {'tweet': text}
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors = "pt") # for PyTorch-based models
    output = model(**encoded_input)
    scores_ = output[0][0].detach().numpy()
    scores_ = softmax(scores_)

    # Format output dict of scores
    labels = ["Negative", "Neutral", "Positive"]
    scores = {l:float(s) for (l,s) in zip(labels, scores_) }
    # save_text.update(scores)
    # user_data = {key: [value] for key,value in save_text.items()}
    # data = pd.DataFrame(user_data,)
    # check_csv('history.csv', data)
    # hist_df = pd.read_csv('history.csv')
    return scores
# , hist_df.head()


model_type = gr.Dropdown(choices=['distilbert', 'roberta'], label='Select model type', allow_custom_value=False, value='roberta')  
#Gradio app interface
#Gradio app interface
demo = gr.Interface(fn = sentiment_analysis,
                   inputs = [model_type, gr.TextArea("Write your text or tweet here", label="Analyze your COVID-19 tweets" )],
                   outputs = ["label"],
                   title = "NLP Sentiment Analysis - Zindi Challenge",
                   description  = "COVID-19 Tweets Analyzer",
                   interpretation = "default",
                   examples = [[None, "Being vaccinated is actually awesome :)"]]
                   ).launch(share=True, server_port=8080)

