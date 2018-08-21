# Daylio_GC
### A way to import your Daylio entries to Google Calendar.

### Installation
1. Install dependencies and enable the Google Calendar API for your account, described [here](https://developers.google.com/calendar/quickstart/python).
2. Create a calendar for storing your Daylio content.
3. Copy `config_template.json` into `config.json`, and enter the CalendarID for your specified calendar inside the `calendarID` field.
4. Export your Daylio content. Then, copy and paste the directory for the exported file into the `csvFilePath` field in your config file. *Note: all backslashes must be replaced with forwardslashes if on Windows.*
5. Run `python gcimport.py`.

#### Special Thanks
Thanks to [Jess](https://github.com/jcreigh) for the inspiration, and introducing me to Daylio in the first place!
