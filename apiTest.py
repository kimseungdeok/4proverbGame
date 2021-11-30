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
        ['도둑이','제발 저린다','도둑이 괜한 근심으로 걱정하거나 실수한다는 말이에요'],
        ['등잔 밑이','어둡다','어떤 사건이나 문제가 있을 때 가장 가까운 사람이 범인이거나 원인이 있음을 뜻해요'],
        ['마른 하늘에','날벼락','예견하지 못한 일이 발생하는것을 말해요'],
        ['사공이 많으면', '배가 산으로 간다','결정권자가 많으면 제 뜻대로 일이 성사되지 않는것을 말해요'],
        ['원수는','외나무 다리에서 만난다','내가 싫어하는 사람은 언젠가 만날 일이 꼭 온다는 뜻이에요'],
        ['은혜를','원수로 갚는다','감사에 대한 보답을 해로 끼친다는 뜻이에요'],
        ['우물안','개구리','넓은 시야를 보지 못하고 자신이 최고인줄 착각하는 사람들을 지칭하는 말이에요']
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
def gameProverbAction():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuiz']=proverbQuizList[randomNumber][0]
    response['output']['proverbAnswer']=proverbQuizList[randomNumber][1]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbAction', methods=['POST'])
def eduProverbAction():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbActionC', methods=['POST'])
def eduProverbActionC():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)


@app.route('/eduProverbActionCC', methods=['POST'])
def eduProverbActionCC():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbActionCW', methods=['POST'])
def eduProverbActionCW():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbActionCWC', methods=['POST'])
def eduProverbActionCWC():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbActionCWW', methods=['POST'])
def eduProverbActionCWW():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbActionCCC', methods=['POST'])
def eduProverbActionCCC():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbActionCCW', methods=['POST'])
def eduProverbActionCCW():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbActionW', methods=['POST'])
def eduProverbActionW():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbActionWC', methods=['POST'])
def eduProverbActionWC():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbActionWCC', methods=['POST'])
def eduProverbActionWCC():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbActionWCW', methods=['POST'])
def eduProverbActionWCW():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbActionWW', methods=['POST'])
def eduProverbActionWW():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbActionWWC', methods=['POST'])
def eduProverbActionWWC():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)

@app.route('/eduProverbActionWWW', methods=['POST'])
def eduProverbActionWWW():

    response = commonResponse
    randomNumber = random.randint(0,6)
    print(randomNumber)
    response['output']['proverbQuizEdu']=proverbQuizListEdu[randomNumber][0]
    response['output']['proverbAnswerEdu']=proverbQuizListEdu[randomNumber][1]
    response['output']['proverbMeaning']=proverbQuizListEdu[randomNumber][2]
    print(response)
    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)