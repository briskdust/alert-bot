from contribution_fetcher import find_last_contribution
from discord_msg_sender import send_msg
from days_counter import get_timespan
import schedule
import time


def main():
    last_contribution_date = find_last_contribution()

    # Send a message to the discord server if there has been 7 days
    # that no contribution has been made
    if get_timespan(last_contribution_date) >= 7:
        send_msg()


# Function main is run every day at 12:00
schedule.every().day.at("12:00").do(main)


if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(3600)
