from flask import Flask, request
from flask_cors import CORS
import mysql.connector



from LogProcesser import * 
from LogWriter import *

app = Flask(__name__)
CORS(app)  # CORS 설정 추가


""" 자바스크립트에서 fetch로 쿼리 던지는 형태 참고할 것
    fetch(`/getLog?currentDateTime=${encodeURIComponent(currentDateTime)}&timeSpent=${encodeURIComponent(timeSpent)}
    &currentUrl=${encodeURIComponent(currentUrl)}&userVisitCookie=${encodeURIComponent(userVisitCookie)}
    &newVisiter=${encodeURIComponent(newVisiter)}&scrollingPercentage=${encodeURIComponent(scrollingPercentage)}`
"""
@app.route('/PageLog', methods=['POST'])
def receivePageLog():
    # 쿼리 파라미터 추출
    try:
        print(request)
        data = request.get_json()
        currentDateTime = data['currentTime']
        timeSpent = data['timeSpent']
        currentUrl = data['currentUrl']
        userVisitCookie = data['userVisitCookie']
        newVisiter = data['newVisiter']
        scrollingPercentage = data['scrollingPercentage']
        print(data)
        print(currentDateTime)
        print(timeSpent)
        print(currentUrl)
        print(userVisitCookie)
        print(newVisiter)
        print(scrollingPercentage)
    except Exception:
        print("Failed to receive log")
        
    ret = pageLogProcess(currentDateTime, timeSpent, currentUrl, userVisitCookie, newVisiter, scrollingPercentage)
    
    if ret == False:
        print("Failed to pageLogProcess")
    
    # 로그가 잘 수신되었다는 응답 반환
    return 'OK', 200



""" 자바스크립트에서 fetch로 쿼리 던지는 형태 참고할 것
    fetch(`http://localhost:5000/EventLog?dateTime=${encodeURIComponent(pushReReservDateTime)}
    &cookie=${encodeURIComponent(mypageCookie)}&uri=${encodeURIComponent(uri)}&clickItem=${encodeURIComponent(clickItem)`
"""
@app.route('/EventLog', methods=['POST'])
def receiveEvnetLog():
    # 쿼리 파라미터 추출
    try:
        print(request)
        data = request.get_json()
        currentDateTime = data['currentTime']
        currentUrl = data['currentUrl']
        clickItem = data['clickItem']
        userVisitCookie = data['userVisitCookie']
        print(data)
        print(currentDateTime)
        print(currentUrl)
        print(clickItem)
        print(userVisitCookie)

    except Exception:
        print("Failed to receive log")

    
    ret = eventLogProcess(currentDateTime, currentUrl, clickItem, userVisitCookie)
    
    if ret == False:
        print("Failed to pageLogProcess")
    
    # 로그가 잘 수신되었다는 응답 반환
    return 'OK', 200

if __name__ == '__main__':
    # Flask 애플리케이션 실행
    app.run(debug=True, port=5000)