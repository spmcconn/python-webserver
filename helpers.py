from datetime import datetime

def get_time_now():
    return datetime.now().strftime("%A, %B %d %Y %I:%M %p")