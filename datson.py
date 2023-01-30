import json
import datetime as dt
from datetime import datetime, timedelta


class Garbagson:
    """Checking if there are any upcoming garbage"""

    def __init__(self) -> None:
        with open("garbage.json", "r") as file:
            self.garbage_events = json.load(file)
        
    def trash_time(self):
        current_date = dt.date.today()
        future_date = current_date + dt.timedelta(days=20)
        message = ''
        nearest_events = []
        for key, values in self.garbage_events.items():
            
            for val in values:
                date_val = dt.datetime.strptime(val, "%d/%m/%Y").date()
                if future_date > date_val > current_date:
                    
                    nearest_events.append((key, val))
        
        if nearest_events:
            print(nearest_events)            
            nearest_events.sort(key=lambda a: a[1])
            print(nearest_events)
            message += "Upcoming garbage in next 7 days: \n"
                
            for event in nearest_events:
                message += f"{event[0]} at {event[1]} \n"
            print(message)
            return message
                
        else:
            message = "There is no upcoming garbage in next 7 days"
            return message


class Events:
    """Class for dealing with custom one time events"""

    def __init__(self):
        """Lauthing starting functions"""
        self.load()


    def load(self):
        """Loading starting files if they exist"""
        try:
            with open("events.json") as file:
                self.events_dict = json.load(file)
        except:
            self.events_dict = {}


    def save(self):
        """Saving dictionary to file"""
        with open("events.json", "w") as file:
            json.dump(self.events_dict, file)


    def date_check(self, date, title, channel) -> bool:
        """Simple function checking if date of the event is in the future"""
        if not isinstance(date, str):
            return False, "Bad data type for data it should be YYYY-MM-DD"
        elif not isinstance(title, str) != str:
            return False, "Bad data type for description you should pass text"
        elif not isinstance(channel, int) != int:
            return False, "Bad data type for channel internal error"
        else:
            try:
                event_date = datetime.strptime(date, "%Y-%m-%d").date()
                current_time = dt.date.today()
                if current_time > event_date:
                    return False , "Given event date is in the past. Therefor event was not added\
                \nTherefore it was not added"
                else:
                    return True, "all ok"
            except:
                return False, "Bad data type for data it should be YYYY-MM-DD"


    def add_event(self, date: str, title: str, channel: int):
        """Adding event to events dictionary"""
        checking_date, response = self.date_check(date, title, channel)
        if checking_date:
            self.events_dict[title] = [date, channel]
            self.save()
            return "Event added"
        else:
            return response


    def event_detection(self):
        """detect if there is any events upcoming"""
        if not self.events_dict:
            return False, {}
        else:
            matching_event_dict = {}
            current_time = dt.date.today()
            future = current_time + timedelta(days=7)
            for key in self.events_dict:
                
                event_time = datetime.strptime(self.events_dict[key][0], "%Y-%m-%d").date()
                if (event_time >= current_time) and (event_time <= future):
                    matching_event_dict[key] = self.events_dict[key]

            if matching_event_dict:
                return True, matching_event_dict
            else:
                return False, {}

    
    def past_event_cleaning(self):
        current_time = dt.date.today()
        for key in self.events_dict:
            event_time = datetime.strptime(self.events_dict[key][0], "%Y-%m-%d").date()
            if (event_time < current_time):
                del self.events_dict[key]
        return "cleaned"


class CyclicEvents:
    """Class holding cyclic events like birthdays for example date"""


    def __init__(self):
        self.load()


    def load(self):
        """Loading data files if file is empty will make empty dictionary"""
        try:
            with open('cyclic_events.json') as file:
                self.cyclic_events = json.load(file)
        except:
            self.cyclic_events = {}

    def save(self):
        """Saving dictionary do file"""
        with open('cyclic_events.json', "w") as file:
            json.dump(self.cyclic_events, file)


    def check_input_data(self, date, title, channel):
        """Checke if data passed to add_tiem are correct type
        and if date is valid"""
        if not isinstance(date, str):
            return False, "Invalid data format expected string"
        elif not isinstance(title, str):
            return False, "Invalid description format expected string"
        elif not isinstance(channel, int) != int:
            return False, "Internal error invalid channel data type"
        else:
            try:
                dt.datetime.strptime(date, '%m-%d')
                return True, "All ok"
            except: 
                return False, "Given date is invalid"


    def add_item(self, date, title, channel):
        """Adds new item cyclic item"""
        checkin_flag, response = self.check_input_data(date, title, channel)
        if checkin_flag:
            self.cyclic_events[title] = [date, channel]
            self.save()
            return "Cyclic event added"
        else:
            return response


    def event_detection(self):
        """Detects if there is any event coming soon"""
        if not self.cyclic_events:
            return False, {}
        else:
            matching_dict = {}
            current_time = dt.date.today()
            future = current_time + timedelta(days=14)
            for key in self.cyclic_events:
                event_time = datetime.strptime(
                    (f"{datetime.strftime(dt.datetime.today(), format('%Y'))}-{self.cyclic_events[key][0]}"),
                    format("%Y-%m-%d")).date()
                if (event_time >= current_time) and (event_time <= future):
                    matching_dict[key] = self.cyclic_events[key]
            if matching_dict:
                return True, matching_dict
            else:
                return False, {}
