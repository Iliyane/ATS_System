#!/usr/bin/python3

# Project for Resume Screening
# by Iliyana Kamenova

import PyPDF2
import textract
import re
import string
import pandas as pd
import matplotlib.pyplot as plt

# First step

# Open pdf file
#resume_file= open('CV.pdf', 'rb')
#read_file=PyPDF2.PdfFileReader(resume_file)
read_file=PyPDF2.PdfFileReader(open("CV_pages.pdf", 'rb'))
# Get the total number of pages
count=read_file.numPages
# Initialize a text empty etring variable
text=""
#Extract text from every page on the file
for i in range(count):
    page=read_file.getPage(i)
    text+=page.extractText()

print (text)

# Second Step: Text Cleaning

#convert all strings to lowercase
text=text.lower()

#remove numbers
text=re.sub(r'\d+','',text)

text=text.translate(str.maketrans('','',string.punctuation))

# Third step: We need to create a dictionary with key terms by job area and tasks

# Create dictionary with industrial and system engineering key terms by area

english_dict= {'Quality':['black belt','capability analysis','control charts','doe','dmaic','fishbone',
                              'gage r&r', 'green belt','ishikawa','iso','kaizen','kpi','lean','metrics',
                              'pdsa','performance improvement','process improvement','quality',
                              'quality circles','quality tools','root cause','six sigma',
                              'stability analysis','statistical analysis','tqm'],
        'Operations management':['automation','bottleneck','constraints','cycle time','efficiency','fmea',
                                 'machinery','maintenance','manufacture','line balancing','oee','operations',
                                 'operations research','optimization','overall equipment effectiveness',
                                 'pfmea','process','process mapping','production','resources','safety',
                                 'stoppage','value stream mapping','utilization'],
        'Supply chain':['abc analysis','apics','customer','customs','delivery','distribution','eoq','epq',
                        'fleet','forecast','inventory','logistic','materials','outsourcing','procurement',
                        'reorder point','rout','safety stock','scheduling','shipping','stock','suppliers',
                        'third party logistics','transport','transportation','traffic','supply chain',
                        'vendor','warehouse','wip','work in progress'],
        'Project management':['administration','agile','budget','cost','direction','feasibility analysis',
                              'finance','kanban','leader','leadership','management','milestones','planning',
                              'pmi','pmp','problem','project','risk','schedule','scrum','stakeholders'],
        'Data analytics':['analytics','api','aws','big data','busines intelligence','clustering','code',
                          'coding','data','database','data mining','data science','deep learning','hadoop',
                          'hypothesis test','iot','internet','machine learning','modeling','nosql','nlp',
                          'predictive','programming','python','r','sql','tableau','text mining','natural language processing'
                          'visualuzation', 'linear regression'],
        'Healthcare':['adverse events','care','clinic','cphq','ergonomics','healthcare',
                      'health care','health','hospital','human factors','medical','near misses',
                      'patient','reporting system']}

# Initializie score counters for each area
quality = 0
operations = 0
supplychain = 0
project = 0
data = 0
healthcare = 0

# create an empty list where the scores will be stored

scores=[]

# obtain the scores for each area
for field in english_dict.keys():

    if field == 'Quality':
        for word in english_dict[field]:
            if word in text:
                quality+=1
        scores.append(quality)

    elif field == 'Operations management':
        for word in english_dict[field]:
            if word in text:
                operations+=1
        scores.append(operations)

    elif field == 'Supply Chain':
        for word in english_dict[field]:
            if word in text:
                supplychain+=1
        scores.append(supplychain)

    elif field == 'Project management':
        for word in english_dict[field]:
            if word in text:
                project+=1
        scores.append(project)

    elif field == 'Data Analytics':
        for word in english_dict[field]:
            if word in text:
                data+=1
        scores.append(data)


    else:
        for word in english_dict[field]:
            if word in text:
                healthcare+=1
        scores.append(healthcare)


# Step 5: Sorting the data frame for final scores creation

# Create a data frame with the scores summary
results= pd.DataFrame(scores,index=english_dict.keys(),columns=['score']).sort_values(by='score',ascending=False)
print (results)

# Step: 5: Pie chart visualisation

pie=plt.figure(figsize=(10,10))
plt.pie(results['score'], labels=results.index, explode=(0.1,0,0,0,0,0),autopct='%1.0f%%', shadow=True,startangle=90)
plt.title('Candidate - Resume Screening by Field')
plt.axis('equal')
plt.show()

# Save pie charts as a .png
pie.savefig(results.png)


# convert all strings to lowercase
