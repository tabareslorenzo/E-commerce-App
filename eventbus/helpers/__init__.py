import os
from models.events import events
import requests
from exceptions import (
    InsertEventToDBException,
)



def send_event_to(port, service, data):
    r = requests.post(
            f'http://localhost:{port}/api/{service}/events',
            json= data
        )
def insert_into_db(data, e_type):
    print(data)
    try:
        events(
            data=data, 
            eventType=e_type
            ).save()
    except Exception as e:
        print(e)
        raise InsertEventToDBException()
    return {"status": "Success"}

def get_events_from_db():
    eventList = events.objects
    return eventList