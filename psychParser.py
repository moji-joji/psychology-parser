import csv 
import os
import matplotlib.pyplot as plt
import math
import pandas as pd
# for xlsx
import openpyxl
# load data to pandas
def load_data(file_name):
    data = pd.read_csv(file_name)
    return data

raw_data = load_data('psychResponses.csv')


def calculate_parentscore(option, authoritative_points, authoritarian_points, permissive_points, neglectful_points):
    result_arr = [0,0,0,0]
    if(option == 1):
        result_arr[0] -= authoritative_points
        result_arr[1] -= authoritarian_points
        result_arr[2] -= permissive_points
        result_arr[3] -= neglectful_points

    elif(option == 2):
        result_arr[0] -= authoritative_points*0.7
        result_arr[1] -= authoritarian_points*0.7
        result_arr[2] -= permissive_points*0.7
        result_arr[3] -= neglectful_points*0.7

    elif(option == 3):
        pass

    elif(option == 4):
        result_arr[0] += authoritative_points*0.7
        result_arr[1] += authoritarian_points*0.7
        result_arr[2] += permissive_points*0.7
        result_arr[3] += neglectful_points*0.7

    elif(option == 5):
        result_arr[0] += authoritative_points
        result_arr[1] += authoritarian_points
        result_arr[2] += permissive_points
        result_arr[3] += neglectful_points

    return result_arr

def calculate_independencescore(option,social_points, emotional_points, financial_points):
    result_arr = [0,0,0]
    if(option == 1):
        result_arr[0] -= social_points
        result_arr[1] -= emotional_points
        result_arr[2] -= financial_points

    elif(option == 2):
        result_arr[0] -= social_points*0.7
        result_arr[1] -= emotional_points*0.7
        result_arr[2] -= financial_points*0.7

    elif(option == 3):
        pass

    elif(option == 4):
        result_arr[0] += social_points*0.7
        result_arr[1] += emotional_points*0.7
        result_arr[2] += financial_points*0.7

    elif(option == 5):
        result_arr[0] += social_points
        result_arr[1] += emotional_points
        result_arr[2] += financial_points

    return result_arr

# raw_data = raw_data.reset_index()  # make sure i|ndexes pair with number of rows

independence_q_list = [
    {
        "question": "I am able to make my own decisions about my education and career path.",
        "social_points": 1,
        "emotional_points": 1,
        "financial_points": 1
    },
    {
        "question": "I am able to communicate my needs and wants effectively.",
        "social_points": 0,
        "emotional_points": 1,
        "financial_points": 0
    },
    
    {
        "question": "I am able to make my own decisions about my appearance and personal style.",
        "social_points": 1,
        "emotional_points": 1,
        "financial_points": 0
    },
    {
        "question": "I am able to advocate for myself in various situations",
        "social_points": 1,
        "emotional_points": 1,
        "financial_points": 0
    },
    {
        "question": "I am confident in my ability to solve problems on my own.",
        "social_points": 1,
        "emotional_points": 1,
        "financial_points": 0
    },
    {
        "question": "I have a support network of friends and family that I can rely on",
        "social_points": 1,
        "emotional_points": 1,
        "financial_points": 0
    },
    {
        "question": "I am able to handle conflicts and problems on my own without relying on others.",
        "social_points": 1,
        "emotional_points": 1,
        "financial_points": 0
    },
    {
        "question": "I have a job/source of income",
        "social_points": 1,
        "emotional_points": 0,
        "financial_points": 1
    },
    {
        "question": "I manage My own finances, including paying bills and budgeting",
        "social_points": 1,
        "emotional_points": 0,
        "financial_points": 1
    }

]

parental_q_list = [
    {
        "question": "My parents encourage me to manage my affairs independently.",
        "authoritative_points": 0.5,
        "authoritarian_points": -0.5,
        "permissive_points": 0.2,
        "neglectful_points": -0.2
    },
    {
        "question": "My parents use threats/criticism as punishment with little or no justification.",
        "authoritative_points": -0.586,
        "authoritarian_points": 0.070,
        "permissive_points": -0.178,
        "neglectful_points": -0.21
    },
    {
        "question": "My parents take my feelings into consideration before asking me to do something.",
        "authoritative_points": 0.309,
        "authoritarian_points": -0.006,
        "permissive_points": -0.13,
        "neglectful_points": 0.260
    },
    {
        "question": "My parents ignore me when I act up.",
        "authoritative_points": -0.586,
        "authoritarian_points": -0.070,
        "permissive_points": 0.178,
        "neglectful_points": 0.21
    },
    {
        "question": "My parents isolate me with little or no explanation.",
        "authoritative_points": -0.174,
        "authoritarian_points": -0.005,
        "permissive_points": 0.336,
        "neglectful_points": -0.162
    },
    {
        "question": "My parents explain the reasons behind their expectations.",
        "authoritative_points": 0.583,
        "authoritarian_points": 0.34,
        "permissive_points": -0.227,
        "neglectful_points": 0.90
    },
    {
        "question": "My parents allow me to give input into family rules. ",
        "authoritative_points": 0.311,
        "authoritarian_points": -0.180,
        "permissive_points": 0.006,
        "neglectful_points": 0.332
    },
    {
        "question": "My parents give into me when I throw a tantrum.",
        "authoritative_points": -0.93,
        "authoritarian_points": 0.163,
        "permissive_points": 0.416,
        "neglectful_points": 0.211
    },
    {
        "question": "My parents fulfil all my wishes without hesitation.",
        "authoritative_points": -0.003,
        "authoritarian_points": 0.113,
        "permissive_points": 0.379,
        "neglectful_points": 0.395
    },
    {
        "question": "My parents encourage me to talk about my problems.",
        "authoritative_points": 0.652,
        "authoritarian_points": -0.154,
        "permissive_points": -0.319,
        "neglectful_points": 0.066
    },
    {
        "question": "My parents do not punish me, whenever I am rude with someone",
        "authoritative_points": 0.211,
        "authoritarian_points": -0.604,
        "permissive_points": 0.007,
        "neglectful_points": -0.132
    },
    #My parents ignore my bad behaviour. 

    {   
        "question": "My parents ignore my bad behaviour. ",
        "authoritative_points": 0.211,
        "authoritarian_points": -0.604,
        "permissive_points": 0.007,
        "neglectful_points": 0.132
    },    

    {
        "question": "My parents do not set clear boundaries and consequences for my behavior.",
        "authoritative_points": -0.621,
        "authoritarian_points": 0,
        "permissive_points": 0.286,
        "neglectful_points": -0.181

    },
    {
        "question": "My parents frequently remind me of all the things they have done for me.",
        "authoritative_points": 0.048,
        "authoritarian_points": 0.209,
        "permissive_points": 0.322,
        "neglectful_points": -0.328
    },
    {
        "question": "My parents yell/shout when they disapprove of my behaviour.",
        "authoritative_points": -0.153,
        "authoritarian_points": 0.548,
        "permissive_points": 0.340,
        "neglectful_points": -0.080
    },
    {
        "question": "My parents state punishments more often than actually carrying them out.",
        "authoritative_points": -0.076,
        "authoritarian_points": 0.217,
        "permissive_points": 0.648,
        "neglectful_points": 0.057
    },
    {
        "question": "My parents consider my preferences when they make plans for the family (e.g. weekends and holidays) ",
        "authoritative_points": 0.262,
        "authoritarian_points": 0.023,
        "permissive_points": -0.016,
        "neglectful_points": 0.348

    },
    {
        "question": "When I ask my parents the reason for doing something, they say, ’because I am your parent’.",
        "authoritative_points": 0.048,
        "authoritarian_points": 0.209,
        "permissive_points": 0.322,
        "neglectful_points": -0.328
    },
    {
        "question": "My parents punish me by taking away privileges (e.g., TV, games, visiting friends). ",
        "authoritative_points": -0.034,
        "authoritarian_points": -0.049,
        "permissive_points": 0.413,
        "neglectful_points": -0.170

    },
    {
        "question": "My parents encourage me to freely speak my mind, even if I disagree with them. ",
        "authoritative_points": 0.399,
        "authoritarian_points": -0.095,
        "permissive_points": -0.014,
        "neglectful_points": 0.382

    },


]

# if age is a string skip


for index, row in raw_data.iterrows():

    # if age is less than 18 skip
    if(row["Age"] < 18): continue

    authoritative = 0
    permissive = 0
    authoritarian = 0
    neglectful = 0
    social_independence = 0
    emotional_independence = 0
    financial_independence = 0

    parental_score = 0
    # create new columns for parental style scores
    raw_data.loc[index, 'Social Independence Score'] = 0
    raw_data.loc[index, 'Emotional Independence Score'] = 0
    raw_data.loc[index, 'Financial Independence Score'] = 0

    raw_data.loc[index, 'Authoritative Score'] = 0
    raw_data.loc[index, 'Authoritarian Score'] = 0
    raw_data.loc[index, 'Permissive Score'] = 0
    raw_data.loc[index, 'Neglectful Score'] = 0

    # create new column for parental style
    
    raw_data.loc[index, 'Parental Style'] = 'N/A'
   
    # calculate independence score
    for questionObject in independence_q_list:
        independence_arr = calculate_independencescore(row[questionObject["question"]],questionObject["social_points"],questionObject["emotional_points"],questionObject["financial_points"])
        # print(independence_arr)
        social_independence += independence_arr[0]
        emotional_independence += independence_arr[1]
        financial_independence += independence_arr[2]


    raw_data.loc[index, 'Social Independence Score'] = social_independence
    raw_data.loc[index, 'Emotional Independence Score'] = emotional_independence
    raw_data.loc[index, 'Financial Independence Score'] = financial_independence

        
        

            # round float to 2 decimal places

    

    # raw_data.loc[index, 'Independence Score'] = round(independence/9, 2)


    # calculate parental style scores
    for questionObj in parental_q_list:
        arr = calculate_parentscore(row[questionObj["question"]],questionObj["authoritative_points"],questionObj["authoritarian_points"],questionObj["permissive_points"],questionObj["neglectful_points"])
        # print(arr)
        # print(questionObj["authoritative_points"])
        authoritative += arr[0]
        authoritarian += arr[1]
        permissive += arr[2]
        neglectful += arr[3]
    
    # round float to 2 decimal places
    # authoritative = round(authoritative, 3)
    # authoritarian = round(authoritarian, 3)
    # permissive = round(permissive, 3)
    # neglectful = round(neglectful, 3)

    # parental stylet to new column

    


# add scores to new columns
    raw_data.loc[index, 'Authoritative Score'] = authoritative
    raw_data.loc[index, 'Authoritarian Score'] = authoritarian
    raw_data.loc[index, 'Permissive Score'] = permissive
    raw_data.loc[index, 'Neglectful Score'] = neglectful

    # write parental style to new column
    if(authoritative > authoritarian and authoritative > permissive and authoritative > neglectful):
        raw_data.loc[index, 'Parental Style'] = 'Authoritative'
    elif(authoritarian > authoritative and authoritarian > permissive and authoritarian > neglectful):
        raw_data.loc[index, 'Parental Style'] = 'Authoritarian'
    elif(permissive > authoritative and permissive > authoritarian and permissive > neglectful):
        raw_data.loc[index, 'Parental Style'] = 'Permissive'
    elif(neglectful > authoritative and neglectful > authoritarian and neglectful > permissive):
        raw_data.loc[index, 'Parental Style'] = 'Neglectful'
    else:
        raw_data.loc[index, 'Parental Style'] = 'N/A'

print(len(parental_q_list))

# store new raw data as a csv
raw_data.to_csv('psychResponsesOut.csv', index=True) 


