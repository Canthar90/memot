import json
import datetime as dt
from datetime import datetime, timedelta


class Garbagson:
    """Checking if there are any upcoming garbage"""

    def __init__(self):
        """loading base data"""
        with open("garbage.json") as file:
            self.garbage_dict = json.load(file)

    def trash_time(self):
        """checking if there is any garbage upcoming in 7 days """
        current = dt.date.today()
        future = current + timedelta(days=7)
        empty = []

        plastiki_dt = []
        for elem in self.garbage_dict['Plastiki']:
            try:
                new = datetime.strptime(elem, '%d/%m/%Y')
                plastiki_dt.append(new.date())
            except ValueError:
                self.garbage_dict["Plastiki"].remove(elem)

        mieszane_dt = []
        for elem in self.garbage_dict['Mieszane']:
            try:    
                new = datetime.strptime(elem, '%d/%m/%Y')
                mieszane_dt.append(new.date())
            except ValueError:
                self.garbage_dict['Mieszane'].remove(elem)

        szklo_dt = []
        for elem in self.garbage_dict['Szklo']:
            try:
                new = datetime.strptime(elem, '%d/%m/%Y')
                szklo_dt.append(new.date())
            except ValueError:
                self.garbage_dict['Szklo'].remove(elem)

        bio_dt = []
        for elem in self.garbage_dict['Bio']:
            try:
                new = datetime.strptime(elem, '%d/%m/%Y')
                bio_dt.append(new.date())
            except ValueError:
                self.garbage_dict['Bio'].remove(elem)

        gabaryty_dt = []
        for elem in self.garbage_dict['Gabaryty']:
            try:
                new = datetime.strptime(elem, '%d/%m/%Y')
                gabaryty_dt.append(new.date())
            except ValueError:
                self.garbage_dict['Gabaryty'].remove(elem)

        popioły_dt = []
        for elem in self.garbage_dict['Popioly']:
            try:
                new = datetime.strptime(elem, '%d/%m/%Y')
                popioły_dt.append(new.date())
            except ValueError:
                self.garbage_dict['Popioly'].remove(elem)

        message = 'Upcoming garbage: \n'

        matching_gabaryty = [gabaryt for gabaryt in gabaryty_dt if (gabaryt >= current) and (gabaryt <= future)]
        if not matching_gabaryty == empty:
            message += f"Gabaryty at: {matching_gabaryty[0].strftime('%A')} full date:" \
                       f" {matching_gabaryty[0].strftime('%d-%m-%Y')} \n"

        matching_mieszane = [mieszane for mieszane in mieszane_dt if mieszane >= current and mieszane <= future]
        if not matching_mieszane == empty:
            message += f"Mieszane at: {matching_mieszane[0].strftime('%A')} full date: " \
                       f"{matching_mieszane[0].strftime('%d-%m-%Y')} \n"

        matching_popioły = [popiol for popiol in popioły_dt if popiol >= current and popiol <= future]
        if not matching_popioły == empty:
            message += f"Popioły at: {matching_popioły[0].strftime('%A')} full date: " \
                       f"{matching_popioły[0].strftime('%d-%m-%Y')} \n"

        matching_szklo = [glass for glass in szklo_dt if glass >= current and glass <= future]
        if not matching_szklo == empty:
            message += f"Szkło at: {matching_szklo[0].strftime('%A')} full date: " \
                       f"{matching_szklo[0].strftime('%d-%m-%Y')} \n"

        matching_bio = [flower for flower in bio_dt if flower >= current and flower <= future]
        if not matching_bio == empty:
            message += f"Bio at: {matching_bio[0].strftime('%A')} full date: " \
                       f"{matching_bio[0].strftime('%d-%m-%Y')} \n"

        matching_plastiki = [plastik for plastik in plastiki_dt if plastik >= current and plastik <= future]
        if not matching_plastiki == empty:
            message += f"Plastiki at: {matching_plastiki[0].strftime('%A')} full date: " \
                       f"{matching_plastiki[0].strftime('%d-%m-%Y')} \n"

        if message == 'Upcoming garbage: \n':
            return 'There is no upcoming garbage in next 7 days'
        else:
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


    def add_event(self, date, title, channel):
        """Adding event to events dictionary"""
        self.events_dict[title] = [date, channel]
        self.save()
        return "Event added"


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

    def add_item(self, date, title, channel):
        """Adds new item cyclic item"""
        self.cyclic_events[title] = [date, channel]
        self.save()
        return "Cyclic event added"

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
