# from enum import Enum

import copy
from LogDBConnector import *
import datetime

# 참조용으로 만들어둔거지 이거 그대로 갖다 쓰지 마세요~
# C++ 개발자에게 파이썬은 불지옥이다.. 오히려 더 어려워ㅠㅠ
PageLogStruct = {
    "cookie" : "",
    "timestamp" : "",
    "slug" : "",
    "session_time" : "",
    "scroll_percent" : "",
    "revisitor" : ""
}

EventLogStruct = {
    "cookie" : "",
    "timestamp" : "",
    "slug" : "",
    "click_event" : ""
}

def pageLogProcess(currentDateTime, timeSpent, currentUrl, userVisitCookie, newVisiter, scrollingPercentage):
    try:
        # struct 원본 그대로 일단 복사뜨고
        PageLogDict = copy.deepcopy(PageLogStruct)
    except Exception:
        print("Failed to copy page struct")
        return False
    
    try:
        # 파싱 과정
        time_obj = str(datetime.timedelta(seconds=timeSpent))
        # '00:00:02.529' 형식으로 출력 (시작 시간이 0시간 0분 0초임)
        formatted_time = time_obj.zfill(8)[:11]
        print(formatted_time)
        print(type(formatted_time))

        if scrollingPercentage == "NaN":
            scrollPercent = "100%"
        else:
            scrollPercent = str(scrollingPercentage) + "%"
        
        # 값 채워주기
        PageLogDict["cookie"] = userVisitCookie
        PageLogDict["timestamp"] = currentDateTime
        PageLogDict["slug"] = currentUrl
        PageLogDict["session_time"] = formatted_time
        PageLogDict["scroll_percent"] = scrollPercent
        PageLogDict["revisitor"] = newVisiter
        print(PageLogDict)
    except Exception:
        print("Failed to page log parsing")
        return False
    
    ret = addPageLog(PageLogDict)
    if ret == False:
        print("Failed to page log DB Insert")
    
    return True


def eventLogProcess(currentDateTime, currentUrl, clickItem, userVisitCookie):
    try:
        # struct 원본 그대로 일단 복사뜨고
        EventLogDict = copy.deepcopy(EventLogStruct)
    except Exception:
        print("Failed to copy event struct")
        return False
    
    try:
        # 값 채워주기
        EventLogDict["cookie"] = userVisitCookie
        EventLogDict["timestamp"] = currentDateTime
        EventLogDict["slug"] = currentUrl
        EventLogDict["click_event"] = clickItem
        print(EventLogDict)
    except Exception:
        print("Failed to event log parsing")
        return False
    
    ret = addEventLog(EventLogDict)
    if ret == False:
        print("Failed to event log DB Insert")
    
    return True
