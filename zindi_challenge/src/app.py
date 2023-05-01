import gradio as gr

# from transformers import pipeline

# pipe = pipeline("text-classification", model="bright1/fine-tuned-distilbert-base-uncased", )

import gradio as gr
import numpy as np
import pandas as pd
import pickle
import transformers
from transformers import AutoTokenizer, AutoConfig,AutoModelForSequenceClassification,TFAutoModelForSequenceClassification, pipeline
from scipy.special import softmax
import os

# Requirements
model_path = "bright1/fine-tuned-distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_path)
config = AutoConfig.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)



def check_csv(csv_file, data):
    if os.path.isfile(csv_file):
        data.to_csv(csv_file, mode='a', header=False, index=False, encoding='utf-8')
    else:
        history = data.copy()
        history.to_csv(csv_file, index=False)

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
def sentiment_analysis(text):
    save_text =  {'tweet': text}
    text = preprocess(text)

    encoded_input = tokenizer(text, return_tensors = "pt") # for PyTorch-based models
    output = model(**encoded_input)
    print(output)
    scores_ = output[0][0].detach().numpy()
    print(scores_)
    scores_ = softmax(scores_)
    print(scores_)
    # Format output dict of scores
    labels = ["Negative", "Neutral", "Positive"]
    scores = {l:float(s) for (l,s) in zip(labels, scores_) }
    print(scores)
    print("---------")
    print(save_text)
    save_text.update(scores)
    data = pd.DataFrame(save_text.items())
    print(data)
    check_csv('history.csv', data)
    hist_df = pd.read_csv('history.csv')
    return scores, hist_df



    


#Gradio app interface
#Gradio app interface
app = gr.Interface(fn = sentiment_analysis,
                   inputs = gr.TextArea("Write your text or tweet here", label="Analyze your COVID-19 tweets" ),
                   outputs = ["label", 'dataframe'],
                   title = "NLP Sentiment Analysis - Zinzi Challenge",
                   description  = "COVID-19 Tweets Analyzer",
                   interpretation = "default",
                   examples = [["Being vaccinated is actually awesome :)"]]
                   ).launch(share=True, server_port=8080)
