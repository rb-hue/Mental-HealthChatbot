# Running the Code

## Install libraries : tkinter, json, csv, torch, nltk_utils, numpy
## Setup data as descirbed in the end of this readme file
## You need to run "train.py" to train the model, this will train the model and save it as "data.pth"
## To run the chatbot, run "app.py" file



# Dataset Information

## The dataset was picked up from kaggle - Mental Health FAQ.

## To make the chatbot more interactive, manual questions and responses are added

## For training the chatbot, JSON file used train the chatbot using the most accurate responses to emulate the behaviour of a medical practitioner.

## Manual data entry until 272 line of "intents.json" file, then data from "https://www.kaggle.com/datasets/narendrageek/mental-health-faq-for-chatbot" till line 643




# Preparing data for chatbot

## For conversion of csv data to json data, run "csvToJson.py" file, it will obtain "mental__health_faq.json" file.
##  We need to manually move data from "mental__health_faq.json" file to "intents.json" file



# dataset folder

## Inside "dataset folder" 4 files are there:
### "intents.json" : it contains final dataset used in this chatbot (combination of "manual.json" and "mental_health_faq.json" file)
### "manual.json" : it contains manual some basic questions and answers
### "mental_health_faq.csv" : it is downloaded from "https://www.kaggle.com/datasets/narendrageek/mental-health-faq-for-chatbot/download". This dataset consists of 98 FAQs about Mental Health. It consists of 3 columns - Question_ID, Questions, Answers.
### mental_health_faq.json" : it contains data of "mental_health_faq.csv" in json format, converted using "csvToJson.py" file

