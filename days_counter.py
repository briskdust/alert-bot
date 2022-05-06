from datetime import datetime


def get_today_date():
    """
    Get the date of today(the day on which this script is run)
    :return: The date of today as string
    """
    return datetime.today().strftime('%Y-%m-%d')


def days_between(d1, d2):
    """
    Calculate the amount of days between two dates
    :param d1: Date 1
    :param d2: Date 2
    :return: The amount of days between two dates
    """
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def get_timespan(date):
    """
    Calculate the amount of days between today and a given date
    :param date: The date given
    :return: the amount of days
    """
    return days_between(get_today_date(), date)
