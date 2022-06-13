import datetime
from dateutil.relativedelta import relativedelta


def get_date_now():
    return datetime.date.today()


def get_datetime_now():
    return datetime.datetime.now()


def parse_past_date_text(pasteDateText: str) -> str:
    """
    Input: 3 months ago
    Output: 2020-03-29 (ISO Date string)
    @see: https://stackoverflow.com/a/43139770
    """
    dateTextParts = pasteDateText.split()
    partsLength = len(dateTextParts)

    if partsLength < 2:
        raise Exception(f"Invalid date text pattern: {pasteDateText}")

    if partsLength == 1 and dateTextParts[0].lower() == "today":
        return str(datetime.datetime.now().isoformat())
    elif partsLength == 1 and dateTextParts[0].lower() == "yesterday":
        date = datetime.datetime.now() - relativedelta(days=1)
        return str(date.isoformat())
    elif dateTextParts[1].lower() in ["sec", "secs", "second", "seconds", "s"]:
        date = datetime.datetime.now() - relativedelta(hours=int(dateTextParts[0]))
        return str(date.date().isoformat())
    elif dateTextParts[1].lower() in ["hour", "hours", "hr", "hrs", "h"]:
        date = datetime.datetime.now() - relativedelta(hours=int(dateTextParts[0]))
        return str(date.date().isoformat())
    elif dateTextParts[1].lower() in ["day", "days", "d"]:
        date = datetime.datetime.now() - relativedelta(days=int(dateTextParts[0]))
        return str(date.isoformat())
    elif dateTextParts[1].lower() in ["wk", "wks", "week", "weeks", "w"]:
        date = datetime.datetime.now() - relativedelta(weeks=int(dateTextParts[0]))
        return str(date.isoformat())
    elif dateTextParts[1].lower() in ["mon", "mons", "month", "months", "m"]:
        date = datetime.datetime.now() - relativedelta(months=int(dateTextParts[0]))
        return str(date.isoformat())
    elif dateTextParts[1].lower() in ["yrs", "yr", "years", "year", "y"]:
        date = datetime.datetime.now() - relativedelta(years=int(dateTextParts[0]))
        return str(date.isoformat())
    else:
        raise Exception(f"Invalid date text: {pasteDateText}")


def datetime_to_text(dt, alsoTime=True, alsoSeconds=False):
    """
    Formats the timedate obj to a string

    @param (timedate) td, timedate obj
    @param (bool) alsoTime = False, should the time be added
    @param (bool) alsoSeconds = False, if there's time should there also be seconds
    @return (string) timeDateText
    """
    timeDateFormat = "{:%d.%m.%Y}"
    if alsoTime:
        timeDateFormat = "{:%d.%m.%Y %H:%M}"
        if alsoSeconds:
            timeDateFormat = "{:%d.%m.%Y %H:%M:%S}"
    return timeDateFormat.format(dt)


def datetime_to_days_hours_minutes(td):
    """
    Returns formatted time delta obj
    http://stackoverflow.com/a/2119512
    """
    days = td.days
    remainingSeconds = td.total_seconds() - (days * 24 * 60 * 60)
    hours = int(remainingSeconds / 3600)
    minutes = int(remainingSeconds / 60) % 60
    return days, hours, minutes
