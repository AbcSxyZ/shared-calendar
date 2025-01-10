import random
from datetime import datetime, timedelta
from ics import Calendar, Event

def create_event(calendar, name, start_time, duration_hours=1):
    """Create and add an event to the calendar."""
    event = Event()
    event.name = name
    event.begin = start_time
    event.duration = timedelta(hours=duration_hours)
    calendar.events.add(event)

def import_calendar(file_path):
    """Import an existing calendar from an ICS file."""
    with open(file_path, 'r') as file:
        calendar = Calendar(file.read())
    return calendar


def event_generator():
    calendar = Calendar()

    # Add the specified event
    event_name = "The 70th Helmholtz Open Science Online Seminar"
    event_start = datetime(2025, 1, 22, 14, 0)  # January 22, 2025, at 2 PM CET
    create_event(calendar, event_name, event_start, duration_hours=1)

    event_name = "Open Source Event 1"
    event_start = datetime(2025, 1, 15, 14, 0)  
    create_event(calendar, event_name, event_start, duration_hours=2)

    # Save the calendar to a file
    with open("calendar.ics", "w") as file:
        file.writelines(calendar)


def main():
    event_generator()

if __name__ == "__main__":
    main()
