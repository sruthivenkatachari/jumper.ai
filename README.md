# jumper.ai
Assignment-2

(USE CASE FOLDER):
chatlogs_excel.xlsx  - It contains chatlogs of the User with Bot (unclaened version)
requirements.txt  - pre-requisite requirements are provided to execute the usecase.py code.
usecase.py  - Python file which conatins answers for the questions( Use case part1 and Use case part 2).

(WORD CLOUD FOLDER):
wordcloud.py - Python code to build wordcloud from the message provided in the chatlogs after cleaning with wrangler.py
stopwords.py - Python file which is imported in wordcloud.py.
wordcloud_filtered.png - Output image obtained after executing wordcloud.py

(WRANGLER FOLDER):
wranger.py - Python code which cleans the message in the chatlogs_excel excelsheet for further processing of data.
wrangler-output - output file which we receive after executing wranger.py file.


*********************************************************************************************************************************************************************************
QUESTIONS 
Use Case Part 1													
· You are given Chat Logs for a shop to perform analysis on.													
· The chat logs contains the interactions between a customer and the shop's chatbot.													
· Each record is a message transacted. The data description is given on the right												
												
Part 1 Objective												
Answer to following questions with the data:												
- When do most messages occur												
- Which is the most popular channel of communication											
- Who is the most active user												
													
													
Use Case Part 2													
· You realized that the interactions with a customer can span across a long period of time. (See User_ID u-4613735936163840)													
· Analysis on the data will be more insightful by grouping the interactions into sessions.													
· Let's use the following definition for a Session:													
When a customer stops chatting for more than 30 mins (1800 seconds), all prior interactions will be grouped as a Session.													
													
													
Part 2 Objective													
Answer to following questions with the data:													
- How many sessions are there?													
*********************************************************************************************************************************************************************************






