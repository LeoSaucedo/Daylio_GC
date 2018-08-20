# Daylio_GC
### A way to import your Daylio entries to Google Calendar.

### Installation
1. Install dependencies and enable the Google Calendar API for your account, described [here](https://developers.google.com/calendar/quickstart/python).
2. Export your Daylio content. The filename should match `daylio_export.csv`.
3. Create a calendar for storing your Daylio content.
4. Copy `config_template.json` into `config.json`, and enter the CalendarID for your specified calendar inside the `calendarID` field.
5. Run `python gcimport.py`.

#### Special Thanks
Thanks to [Jess](https://github.com/jcreigh) for the inspiration, and introducing me to Daylio in the first place!
