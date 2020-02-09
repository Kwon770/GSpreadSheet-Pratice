import gspread
import os
from readPrice import readNumber
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

credential_path = "/Users/chan/code/Python/SheetApiPratice/client_secret.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

spreadsheet_id = '10QMeCpdyqCJzNbLdnLZb3grkpGtrB4AuUQGKeLSEk4k'

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open_by_url(
    'https://docs.google.com/spreadsheets/d/10QMeCpdyqCJzNbLdnLZb3grkpGtrB4AuUQGKeLSEk4k/edit#gid=0')  # gid=0)
# legislators = sheet.worksheet('1')

# legislators.duplicate(new_sheet_name="2")

# legislators = sheet.worksheet("2")
# legislators.insert_row([], 3)

nameCount = 1

kindCol = 4
contentCol = 7
priceCol = 10
storeCol = 12

firstRow = 13
lastRow = 17

docKindPos = [11, 4]
timePos = [[8, 16], [9, 16], [10, 16], [11, 16]]
yearPos = [7, 10]
docNumPos = [7, 6]
totalPricePos = [18, 6]
etcPos = [19, 6]


def StartWriting(docCount, y, m, d, kind, count, content):
    global nameCount

    # Load new WorkSheet
    curSheet = sheet.worksheet(str(nameCount))

    # Update nameCount
    nameCount += 1
    # Duplicate original document
    curSheet.duplicate(new_sheet_name=str(nameCount))

    # Change cell count 5 -> ?
    lastRow = 17
    for i in range(0, 5 - count):
        curSheet.delete_row(lastRow - i)

    # Change Text ( Time, Document kind, Each price, Total price, etc)
    # Doc time with num
    timeString = y + m + d
    curSheet.update_cell(docNumPos[0], docNumPos[1],
                         timeString + '-' + str(docCount))

    # Year
    curSheet.update_cell(yearPos[0], yearPos[1], y)
    # Time
    curSheet.update_cell(timePos[0][0], timePos[0][1], timeString)
    curSheet.update_cell(timePos[1][0], timePos[1][1], timeString)
    curSheet.update_cell(timePos[2][0], timePos[2][1], timeString)
    curSheet.update_cell(timePos[3][0], timePos[3][1], timeString)

    # Must Update pos blow each content
    totalPricePos = [18, 6]
    etcPos = [19, 6]

    totalPricePos[0] -= 5 - count
    etcPos[0] -= 5 - count

    # Set data according to kind
    kindTxt = None
    contentTxt = None
    # Doc Kind
    if kind == 3:
        kindTxt = "수용및수수료"
        curSheet.update_cell(docKindPos[0], docKindPos[1], kindTxt)
    elif kind == 2:
        kindTxt = "연료비"
        contentTxt = "차량주유"
        curSheet.update_cell(docKindPos[0], docKindPos[1], kindTxt)
        curSheet.update_cell(etcPos[0], etcPos[1], contentTxt)
    elif kind == 1:
        kindTxt = "재료비"
        contentTxt = "식자재"
        curSheet.update_cell(docKindPos[0], docKindPos[1], kindTxt)
        curSheet.update_cell(etcPos[0], etcPos[1], contentTxt)

    # Each Content
    totalPrice = 0
    firstRow = 13
    for i in range(0, count):
        if kind == 3:
            contentTxt = content[i][2]

        # Kind
        curSheet.update_cell(firstRow, kindCol, kindTxt)

        # Content
        curSheet.update_cell(firstRow, contentCol, contentTxt)

        # Price
        curSheet.update_cell(firstRow, priceCol, content[i][0])

        # Store
        curSheet.update_cell(firstRow, storeCol, content[i][1])

        firstRow += 1
        totalPrice += int(content[i][0])

    # Total Price
    totalPriceString = "금" + str(totalPrice) + \
        "(" + readNumber(totalPrice) + "원)"
    curSheet.update_cell(totalPricePos[0], totalPricePos[1], totalPriceString)
