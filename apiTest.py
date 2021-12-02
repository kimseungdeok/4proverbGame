#-*-coding:utf-8-*-
from flask import Flask, request, json
from datetime import datetime
import os
import random
import pandas as pd
import numpy as np

app = Flask(__name__)

commonResponse = {
    'version': '2.0',
    'resultCode': 'OK',
    'output': {}

}

df = pd.read_csv("proverb.csv", encoding='utf-8')
num = 0
proverbQuizListEdu = df.values.tolist()
# for data in proverbQuizListEdu:
#     print("{}번 문제 : {}".format(num  + 1, proverbQuizListEdu[num][0])) # 앞부분 (알버트가 말하는 부분)
#     print("{}번문제의 힌트1 : {}".format(num + 1, proverbQuizListEdu[num][1])) # 뒷부분 (사용자가 말해야할 부분)
#     print("{}번문제의 힌트2 : {}".format(num + 1, proverbQuizListEdu[num][2])) # 뜻
#     num = num + 1

df = pd.read_csv("fourword.csv", encoding='utf-8')
num = 0
fourwordQuizListEdu = df.values.tolist()
# for data in fourwordQuizListEdu:
#     print("{}번 문제 : {}".format(num  + 1, fourwordQuizListEdu[num][0])) # 앞부분 (알버트가 말하는 부분)
#     print("{}번문제의 힌트1 : {}".format(num + 1, fourwordQuizListEdu[num][1])) # 뒷부분 (사용자가 말해야할 부분)
#     print("{}번문제의 힌트2 : {}".format(num + 1, fourwordQuizListEdu[num][2])) # 뜻
#     num = num + 1




# proverbQuizList=[
#         ['낫 놓고','기역자도 모른다'],
#         ['도둑이','제발 저린다'],
#         ['등잔 밑이','어둡다'],
#         ['마른 하늘에','날벼락'],
#         ['사공이 많으면', '배가 산으로 간다'],
#         ['원수는','외나무 다리에서 만난다'],
#         ['은혜를','원수로 갚는다'],
#         ['우물안','개구리']
#          ]

# fourwordQuizList=[
#         ['수어','지교'],
#         ['일취','월장'],
#         ['가가','호호'],
#         ['갑남','을녀'],
#         ['경국','지색'],
#         ['고량','진미'],
#         ['과유','불급'],
#         ['관포','지교']
#          ]

# proverbQuizListEdu=[
#         ['낫 놓고','기역자도 모른다','바로 눈앞에 정답이 있는데도 알아보지 못하는 무지함을 뜻해요'],
#         ['도둑이','제발 저린다','도둑이 괜한 근심으로 걱정하거나 실수한다는 말이에요'],
#         ['등잔 밑이','어둡다','어떤 사건이나 문제가 있을 때 가장 가까운 사람이 범인이거나 원인이 있음을 뜻해요'],
#         ['마른 하늘에','날벼락','예견하지 못한 일이 발생하는것을 말해요'],
#         ['사공이 많으면', '배가 산으로 간다','결정권자가 많으면 제 뜻대로 일이 성사되지 않는것을 말해요'],
#         ['원수는','외나무 다리에서 만난다','내가 싫어하는 사람은 언젠가 만날 일이 꼭 온다는 뜻이에요'],
#         ['은혜를','원수로 갚는다','감사에 대한 보답을 해로 끼친다는 뜻이에요'],
#         ['우물안','개구리','넓은 시야를 보지 못하고 자신이 최고인줄 착각하는 사람들을 지칭하는 말이에요']
#          ]

# fourwordQuizListEdu=[
#         ['수어','지교','물을 만난 물고기처럼 지냄을 뜻하며 떨어질 수 없는 특별한 친분을 의미'],
#         ['일취','월장','날마다 달마다 성장하고 발전한다는 뜻으로 학업이 날이 가고 달이 갈수록 진보함'],
#         ['가가','호호','집집마다라는 뜻이에요'],
#         ['갑남','을녀','보통사람들'],
#         ['경국','지색','나라의 운명을 위태롭게 할 만한 절세의 미인'],
#         ['고량','진미','맛있는 음식'],
#         ['과유','불급','정도를 지나치면 미치지 못한 것과 같음'],
#         ['관포','지교','우정이 깊은 사귐']
#          ]

# print(proverbQuizList[0])
# print(proverbQuizList[0][0])
# print(proverbQuizList[0][1])
# print(proverbQuizListEdu[0][2]) 



def getUtteranceParameter () :
    data = request.get_json()
    print(data)
    return data['action']['parameters']

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/gameProverbAction', methods=['POST'])
def gameProverbAction():

    response = commonResponse
    randomNumber = random.randint(0,100)
    print(randomNumber)
    response['output']['proverbQuiz']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswer']=proverbQuizListEdu[randomNumber][1]
    print(response)
    return json.dumps(response)

@app.route('/gameFourwordAction', methods=['POST'])
def gameFourwordAction():

    response = commonResponse
    randomNumber = random.randint(0,100)
    print(randomNumber)
    response['output']['fourwordQuiz']=fourwordQuizListEdu[randomNumber][0]
    response['output']['fourwordAnswer']=fourwordQuizListEdu[randomNumber][1]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbAction', methods=['POST'])
def eduProverbAction():

    response = commonResponse
    randomNumber1 = random.randint(0,100)
    randomNumber2 = random.randint(0,100)
    randomNumber3 = random.randint(0,100)
    # print(randomNumber1)
    response['output']['proverbQuizEdu1']=proverbQuizListEdu[randomNumber1][0]
    response['output']['proverbAnswerEdu1']=proverbQuizListEdu[randomNumber1][1]
    response['output']['proverbMeaning1']=proverbQuizListEdu[randomNumber1][2]

    response['output']['proverbQuizEdu2']=proverbQuizListEdu[randomNumber2][0]
    response['output']['proverbAnswerEdu2']=proverbQuizListEdu[randomNumber2][1]
    response['output']['proverbMeaning2']=proverbQuizListEdu[randomNumber2][2]
    
    response['output']['proverbQuizEdu3']=proverbQuizListEdu[randomNumber3][0]
    response['output']['proverbAnswerEdu3']=proverbQuizListEdu[randomNumber3][1]
    response['output']['proverbMeaning3']=proverbQuizListEdu[randomNumber3][2]

    print(response)
    return json.dumps(response)


@app.route('/eduFourwordAction', methods=['POST'])
def eduFourwordAction():

    response = commonResponse
    randomNumber1 = random.randint(0,100)
    randomNumber2 = random.randint(0,100)
    randomNumber3 = random.randint(0,100)
    # print(randomNumber1)
    response['output']['fourwordQuizEdu1']=fourwordQuizListEdu[randomNumber1][0]
    response['output']['fourwordAnswerEdu1']=fourwordQuizListEdu[randomNumber1][1]
    response['output']['fourwordMeaning1']=fourwordQuizListEdu[randomNumber1][2]

    response['output']['fourwordQuizEdu2']=fourwordQuizListEdu[randomNumber2][0]
    response['output']['fourwordAnswerEdu2']=fourwordQuizListEdu[randomNumber2][1]
    response['output']['fourwordMeaning2']=fourwordQuizListEdu[randomNumber2][2]
    
    response['output']['fourwordQuizEdu3']=fourwordQuizListEdu[randomNumber3][0]
    response['output']['fourwordAnswerEdu3']=fourwordQuizListEdu[randomNumber3][1]
    response['output']['fourwordMeaning3']=fourwordQuizListEdu[randomNumber3][2]

    print(response)
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)