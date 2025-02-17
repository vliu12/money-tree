from datetime import datetime

class DateTime:
    def __init__(self, date, time):
        self.date = date
        self.time = time

    def __str__(self):
        """Return a string representation of the DateTime object."""
        return f"Date: {self.date}, Time: {self.time}"


def get_current_datetime():
    """
    Get the current date and time from the system.

    :return: A DateTime object with the current date and time.
    """
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")  # Format: YYYY-MM-DD
    current_time = now.strftime("%H:%M:%S")  # Format: HH:MM:SS
    return DateTime(current_date, current_time)


