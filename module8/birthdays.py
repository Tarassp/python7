from enum import Enum
from datetime import date, time, timedelta, datetime

# Testing data
# users = [
#     {"name": "Name 1", "birthday": datetime.now() },
#     {"name": "Name 1", "birthday": datetime(year=2022, month=7, day=23, hour=23, minute=59, second=59, microsecond=10000) },
#     {"name": "Name 2", "birthday": datetime(year=2022, month=7, day=24, hour=20) },
#     {"name": "Name 3", "birthday": datetime(year=2022, month=7, day=25, hour=20)},
#     {"name": "Name 4", "birthday": datetime(year=2022, month=7, day=26, hour=20)},
#     {"name": "Name 5", "birthday": datetime(year=2022, month=7, day=27, hour=20)},
#     {"name": "Name 6", "birthday": datetime(year=2022, month=7, day=28, hour=20)},
#     {"name": "Name 7", "birthday": datetime(year=2022, month=7, day=29, hour=20)},
#     {"name": "Name 7", "birthday": datetime(year=2022, month=7, day=30, hour=20)},
#     {"name": "Name 7", "birthday": datetime(year=2022, month=7, day=31, hour=20)},
#     {"name": "Name 7", "birthday": datetime(year=2022, month=8, day=1, hour=20)},
# ]

class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

def get_birthdays_per_week(users):
    start_datetime = datetime.combine(date.today(), time.max)
    end_date = date.today() + timedelta(days=8)
    end_datetime = datetime.combine(end_date, time.min)

    filtered_users = list(filter(lambda user: start_datetime < user["birthday"] < end_datetime, users))
    
    grouped_users = {}
    for item in filtered_users:
        weekday = Weekday(item['birthday'].weekday())
        if weekday not in (Weekday.SATURDAY, Weekday.SUNDAY):
            grouped_users.setdefault(weekday.name, []).append(item)
        else:
            grouped_users.setdefault(Weekday.MONDAY.name, []).append(item)
        
    return grouped_users
    
def display_birthdays(weekdays: dict):
    for weekday, users in weekdays.items():
        print(f'{weekday}: {", ".join([user["name"] for user in users]) }')
    
    
# # Testing
# birthdays_per_week = get_birthdays_per_week(users)
# display_birthdays(birthdays_per_week)