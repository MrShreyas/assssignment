- install django and djangorestframework:
 pip install django djangorestframework

- go to the directory: assssignment/mysite

- then run: py manage.py runserver

- open link in browser: http://127.0.0.1:8000/api/reminders/create/

- paste any data below in content textarea in this format
  {
          "date": "2023-10-01",
          "time": "12:00:00",
          "message": "Test Reminder"
  }

- click "post"

- to get the reminders go to link: http://127.0.0.1:8000/api/reminders/
  you will get all the rminders
  
Thank You!
