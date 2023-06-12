# 🚀Sentiment Analysis Project 😟😐😊 🚀


[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![streamlit](https://img.shields.io/badge/Streamlit-3776AB?style=for-the-badge&logo=streamlit&logoColor=red)](https://img.shields.io/badge/Streamlit-3776AB?style=for-the-badge&logo=streamlit&logoColor=white)
![Issues](https://img.shields.io/github/issues/eaedk/streamlit-iris-app?style=for-the-badge&logo=appveyor)
![PR](https://img.shields.io/github/issues-pr/eaedk/streamlit-iris-app?style=for-the-badge&logo=appveyor)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)


## Screenshots of the App
<div align='center'> 
    <img src="https://drive.google.com/uc?export=view&id=1Ku4QP_1MxXwci791Hat6o7w9C7BNjC5i"/>

</div>



## Project Description 
A project showcasing how to use Hugging Face Transformers and Gradio for text classification with a pre-trained model


## Table of Contents
1. [Overview Of the Project](#overview)

2. [Application / Deployed Links](#application)

3. [Technology Stack](#technology)

4. [Deliverables](#deliverables)

5. [Installation](#installation)

6. [Configuration Setup](#setup)

7. [App Usage](#usage)

8. [Collaborators](#collaborators)

9. [Contributing Instructions](#instructions)

10. [Contact Information](#ontact)


## 1. Overview Of the Project <a name="overview"></a>
- The project is a machine learning model that can generate natural language text based on a given prompt. The model is based on the state-of-the-art GPT-3 architecture and has been fine-tuned on a large corpus of text data. The model is hosted on the Hugging Face Model Hub, which provides easy access to the model through a RESTful API.

- The project also includes a Dockerfile that can be used to deploy the model locally or in a cloud environment. The Dockerfile installs the necessary dependencies and sets up the environment to run the model. Additionally, the project includes documentation and examples to help users get started with using the model.

- Overall, the project aims to make it easy for developers and data scientists to use and deploy a powerful natural language generation model in their applications.
## 2. Application / Deployed Links <a name="application"></a>
<table>
  <tr>
    <th>Models</th>
    <th>Deployed links</th>
  </tr>
  <tr>
    <td>Distilbert</td>
    <td><a href="https://huggingface.co/bright1/fine-tuned-distilbert-base-uncased">Fine-tuned Distilbert</a></td>
  </tr>
  <tr>
    <td>Roberta</td>
    <td><a href="https://huggingface.co/bright1/fine-tuned-twitter-Roberta-base-sentiment">Fine-tuned Roberta</a></td>
  </tr>
</table>

<table>
  <tr>
    <th>App</th>
    <th>Deployed links</th>
  </tr>
  <tr>
    <td>Gradio App</td>
    <td><a href="https://huggingface.co/spaces/bright1/sentiment-analysis-app-gradio">Sentiment Analysis with Gradio</a></td>
  </tr>
  <tr>
    <td>Streanlit App</td>
    <td><a href="https://huggingface.co/spaces/bright1/sentiment-analysis-app-streamlit">Sentiment Analysis with Streamlit</a></td>
  </tr>
  <tr>
    <td>Docker App</td>
    <td><a href="https://huggingface.co/spaces/bright1/MyFirstDockerApp">Sentiment Analysis Docker App</a></td>
  </tr>
</table>

## 3. Technology Stack <a name="technology"></a>
 
<table>
  <tr>
    <th>Technology</th>
    <th>Version</th>
  </tr>
  <tr>
    <td>Python</td>
    <td>3.9</td>
  </tr>
  <tr>
    <td>Hugging Face Transformers</td>
    <td>4.9.2</td>
  </tr>
  <tr>
    <td>Gradio</td>
    <td>2.3.4</td>
  </tr>
</table>

## 4. Deliverables <a name="deliverables"></a>

1. A fintuned pre-trained distilbert-base-uncase 
2. A fintuned pre-trained roberta-base-uncase 
3. Interactive user interface 
4. A Dockerfile for easy deployment 

## 5. Installation <a name="installation"></a>
Clone the repository to your local machine:


        git clone https://github.com/Bright136/Natural-Language-Processing-Project.git

Navigate to the project directory:

        cd Natural-Language-Processing-Project
Create a new virtual environment and activate the virtual:

- Windows:

        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:

        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt



Copy code
python app.py
Once the Gradio interface is running, you can access it by opening a web browser and navigating to http://localhost:7860.

## Execution
1. Notebooks
To run any the notebooks:
To fine-tune the Hugging Face Text classification model, please follow the steps below:

- Go to the Hugging Face website and sign in to access all the features of the platform.
- Use Colab, your other GPU cloud provider, or a local machine having NVIDIA GPU.
- Rerun the code to train the Distilbert model or train my finetuned models
- Make sure you have made the neccessary changes to parameter such as `output_dir`
- The `output_dir` should be replaced with your model repository on hugging to enable you push the model.

2. App
To execute the app, follow these steps:
After all requirement have been install

At the root of your repository in your terminal
`root :: Churn-Prediction-App-with-Gradio> ...`
run the command:


            gradio app.py

Open your browser and go to http://127.0.0.1:8080



## 7. App Usage <a name="usage"></a>
- The app will start running and display a Gradio interface with input fields and a submit button.
- Enter the input text in the input field and click the submit button.
- The app will generate the output based on the input and display it in the output field.
- You can continue entering new inputs and getting new outputs as desired.
- When you are finished using the app, you can close the Gradio interface or terminate the app by pressing Ctrl+C in the terminal/command prompt.

## 8. Collaborators <a name="collaborators"></a>
<table>
  <tr>
    <th>Name</th>
  </tr>
  <tr>
    <td>Bright Eshun</td>
  </tr>
  <tr>
    <td>Kwasi Asomani</td>
  </tr>
  <tr>
    <td>Stella  Oiro</td>
  </tr>
  <tr>
    <td>Linda Azdigbli</td>
  </tr>
    <tr>
    <td>Foster Kwabena Abrefa</td>
  </tr>
</table>


## 9. Contributing Instructions <a name="instructions"></a>
To contribute to the Sentiment Analysis API, follow these guidelines:

- Fork the repository.
- Create a new branch: git checkout -b my-new-feature
- Make your changes and commit them: git commit -am 'Add some feature'
- Push to the branch: git push origin my-new-feature
- Create a new pull request

## 10. Contact Information <a name="contact"></a>

<table>
  <tr>
    <th>Name</th>
    <th>Twitter</th>
    <th>LinkedIn</th>
    <th>GitHub</th>
    <th>Hugging Face</th>
  </tr>
  <tr>
    <td>Bright Eshun</td>
    <td><a href="https://twitter.com/bright_eshun_">@bright_eshun_</a></td>
    <td><a href="https://www.linkedin.com/in/bright-eshun-9a8a51100/">@brighteshun</a></td>
    <td><a href="https://github.com/Bright136">@bright136</a></td>
    <td><a href="https://huggingface.co/bright1">@bright1</a></td>
  </tr>
</table>
