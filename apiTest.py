#-*-coding:utf-8-*-
from flask import Flask, request, json
from datetime import datetime
import os
import random

app = Flask(__name__)

commonResponse = {
    'version': '2.0',
    'resultCode': 'OK',
    'output': {}

}
proverbQuizList=[
        ['낫 놓고','기역자도 모른다'],
        ['도둑이','제발 저린다'],
        ['등잔 밑이','어둡다'],
        ['마른 하늘에','날벼락'],
        ['사공이 많으면', '배가 산으로 간다'],
        ['원수는','외나무 다리에서 만난다'],
        ['은혜를','원수로 갚는다'],
        ['우물안','개구리']
         ]

proverbQuizListEdu=[
        ['낫 놓고','기역자도 모른다','바로 눈앞에 정답이 있는데도 알아보지 못하는 무지함을 뜻해요'],
        ['도둑이','제발 저린다','도둑이 괜한 근심으로 걱정하거나 실수한다는 말'],
        ['등잔 밑이','어둡다','어떤 사건이나 문제가 있을 때 가장 가까운 사람이 범인이거나 원인이 있음을 뜻한다.']
         ]

print(proverbQuizList[0])
print(proverbQuizList[0][0])
print(proverbQuizList[0][1])
print(proverbQuizListEdu[0][2]) 


def getUtteranceParameter () :
    data = request.get_json()
    print(data)
    return data['action']['parameters']

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/gameProverbAction', methods=['POST'])
def proverbAction():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuiz']=proverbQuizList[randomNumber][0]
    response['output']['proverbAnswer']=proverbQuizList[randomNumber][1]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbAction', methods=['POST'])
def proverbAction():

    response = commonResponse
    randomNumber = random.randint(0,2)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizList[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizList[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizList[randomNumber][2]
    print(response)
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)