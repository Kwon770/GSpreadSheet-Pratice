from datetime import datetime, timedelta
from printcmd import printn, printnn, inputS, clear
import sheet
import control
import data

# 몇번 째 문서인지 확인할 데이터
timeData = []


def StartOper():
    clear()
    printn("START OPERATION")
    print("1. Start making document")
    print("2. Edit time data")

    cmd = int(input(" ~ "))
    clear()
    if (cmd == 1):
        StartDocs()
    else:
        StartData()


def StartDocs():
    clear()
    printn("START MAKING DOCUMENT")

    # 정보 입력단
    while True:
        # 0 날짜 1 지출종류 2 지출수
        docInfor = []
        # 0 금약 1 지출처 2 기타일 경우 종류
        docContents = []

        # 문서 정보 입력단 ( 날짜 지출종류 지출수 )
        print("Input with / ")
        print("Input time (YYYY-MM-DD) [[RULE {{2020-01-01}} RULE]]")
        print("Input kind / 1 Cook  / 2 fuel / 3 Etc")
        printn("Input Count")

        inputDocInfor = inputS()
        docInfor = inputDocInfor.split("/")

        # 지출 세부사항 입력단 (지출금액 지출처)
        for i in range(1, int(docInfor[2]) + 1):
            printnn("INDEX" + str(i))
            print("Input with / ")
            print("Input price")
            print("Input store")
            printn("[[ IF TYPE ETC, WRITE CONTENT TYPE AT LAST ]]")

            inputDocCon = inputS()
            docCon = inputDocCon.split("/")
            docContents.append(docCon)

        # 데이터 정리
        time = docInfor[0].split('-')
        docCount = data.GetCount(time[0], time[1], time[2])

        # 스프레드 시트에 작성
        sheet.StartWriting(docCount, time[0], time[1], time[2],
                           int(docInfor[1]), int(docInfor[2]), docContents)

        # 데이터 저장
        data.SaveData()

        # 저장 밑 인쇄 매크로
        control.StartPrintControl()

        # 다음 작업을 위해 시트 이동
        control.MoveFirstSheet()

        # Focuse here
        control.MoveFocusToTerminal()

        print("Break? (9) Continue? (else)")
        if int(input(" ~ ")) == 9:
            break


def StartData():
    clear()
    printn("START EDITING TIME DATA")

    # 날짜 데이터 출력
    data.PrintData()

    # 명령어 입력
    printnn("1. Edit Count of certain date")
    printn("2. Back to home")
    cmd = int(input(' ~ '))

    clear()
    if cmd == 1:
        # 날짜 데이터 출력
        data.PrintData()

        # 해당 날짜 데이터 변경
        printnn("Input date to edit YYYY-MM-DD")
        dateString = input(" ~ ")
        dateSplit = dateString.split('-')

        printnn("Input Count to change")
        dateCount = int(input(" ~ "))

        data.ChangeData(dateSplit[0], dateSplit[1], dateSplit[2], dateCount)
        StartData()
    else:
        StartOper()


if __name__ == "__main__":
    printnn("PLZ SET SHEET NAME TO   - 1 -")
    printn("PLZ SET SHEET NAME TO   - 1 -")

    # 날짜 데이터 로드
    data.LoadData()

    # 시작
    StartOper()
