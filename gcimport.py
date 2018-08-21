"""
Google Calendar x Daiylio Sync.
Carlos Saucedo, 2018
"""
from __future__ import print_function
import csv, json
from datetime import datetime, date, timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

config = json.load(open("config.json", "r"))
calendarID = config["calendarId"]
exportFile = config["csvFilePath"]

SCOPES = 'https://www.googleapis.com/auth/calendar'

def addEvent(entry, dateObject, service):
    print("Creating event...")
    event = {
        "summary": "Daily Mood: " + entry[4],
        "start":{
            "date": str(dateObject)
        },
        "end":{
            "date": str(dateObject)
        },
        "transparency": "transparent",
        "description": "Time: " + entry[3] + "\nMood: " + entry[4] + "\nActivities: " + entry[5] +  "\nNote: " + entry[6]
    }
    event = service.events().insert(calendarId=calendarID, body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

def main():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Reads all of the entries inside of the Daylio CSV.
    """
    CSV Entry Data order:
    year, date, weekday, time, mood, activities, note
    ex: 2018,August 19,Sunday,9:53 PM,meh,"gaming",""
    """
    with open(exportFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for entry in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                # Parses CSV entry data.
                CSVDate = entry[1].split()
                entryYear = int(entry[0])
                entryMonth = months[CSVDate[0]]
                entryDate = int(CSVDate[1])
                
                # Creating date and datetime objects for the GC API.
                dateObject = date(entryYear, entryMonth, entryDate)
                entryDate = datetime(entryYear, entryMonth, entryDate, 0, 0, 0)
                
                # Accessing the GC API.
                now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
                queryDate = entryDate.utcnow().isoformat() + "Z"
                events_result = service.events().list(calendarId=config["calendarId"],
                                                    singleEvents=True, timeMax=queryDate).execute()
                events = events_result.get('items', [])
                
                if events:
                    for event in events:
                        print("Event Found: " + event["summary"])
                        if ("Daily Mood: " in event["summary"]) == False:
                            print("Event created: " + event["summary"])
                            addEvent(entry, dateObject, service)
                else:
                    print("No events found.")
                    addEvent(entry, dateObject, service)
                line_count += 1
if __name__ == '__main__':
    main()