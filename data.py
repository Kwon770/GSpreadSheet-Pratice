from datetime import datetime, timedelta
import pickle

timeCount = {}


def GetCount(y, m, d):
    _time = datetime(int(y), int(m), int(d))

    if _time in timeCount:
        timeCount[_time] += 1
    else:
        timeCount[_time] = 1

    return timeCount[_time]


def PrintData():
    global timeCount

    i = 0
    for key, value in timeCount.items():
        print(str(i) + ". " + str(key) + "::" + str(value))
        i += 1


def SaveData():
    global timeCount

    with open('data.dat', 'wb') as file:
        pickle.dump(timeCount, file)


def LoadData():
    global timeCount

    with open('data.dat', 'rb') as file:
        timeCount = pickle.load(file)


def ChangeData(y, m, d, count):
    _time = datetime(int(y), int(m), int(d))

    if _time in timeCount:
        timeCount[_time] = count
    else:
        print("ERROR")

    SaveData()
