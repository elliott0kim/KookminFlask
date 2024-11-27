import mysql.connector

# MySQL 데이터베이스 연결 설정
def getDBConnection():
    connection = mysql.connector.connect(
        host='localhost',          # MySQL 서버 주소
        user='root',          # MySQL 사용자명
        password='7913qwer',  # MySQL 비밀번호
        database='LogDB'   # 사용하려는 데이터베이스 이름
    )
    return connection



# PageLogDict["cookie"] = userVisitCookie
# PageLogDict["timestamp"] = currentDateTime
# PageLogDict["slug"] = currentUrl
# PageLogDict["session_time"] = formatted_time
# PageLogDict["scroll_percent"] = scrollPercent
# PageLogDict["revisitor"] = newVisiter

def addPageLog(PageLogDict):
    # MySQL 연결 및 데이터 삽입
    connection = getDBConnection()
    cursor = connection.cursor()
    try:
        query = "INSERT INTO page_log (cookie, timestamp, slug, session_time, scroll_percent, revisitor) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (PageLogDict["cookie"], PageLogDict["timestamp"], PageLogDict["slug"], PageLogDict["session_time"], PageLogDict["scroll_percent"], PageLogDict["revisitor"]))
        connection.commit()  # 트랜잭션 커밋
        return True
    except mysql.connector.Error as err:
        return False

# EventLogDict["cookie"] = userVisitCookie
# EventLogDict["timestamp"] = currentDateTime
# EventLogDict["slug"] = currentUrl
# EventLogDict["click_event"] = clickItem

def addEventLog(EventLogDict):
    # MySQL 연결 및 데이터 삽입
    connection = getDBConnection()
    cursor = connection.cursor()
    try:
        print(EventLogDict)
        query = "INSERT INTO event_log (cookie, timestamp, slug, click_event) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (EventLogDict["cookie"], EventLogDict["timestamp"], EventLogDict["slug"], EventLogDict["click_event"]))
        connection.commit()  # 트랜잭션 커밋
        return True
    except mysql.connector.Error as err:
        print(err)
        return False