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
print(proverbQuizList[0])
print(proverbQuizList[0][0])
print(proverbQuizList[0][1])


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
    randomNumber = random.randint(0,2)
    print(randomNumber)
    response['output']['proverbQuiz']=proverbQuizList[randomNumber][0]
    response['output']['proverbAnswer']=proverbQuizList[randomNumber][1]
    print(response)
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)