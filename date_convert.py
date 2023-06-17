from datetime import datetime, timedelta
import pytz


class DateUtility:
    """
    A utility class for performing various date operations.
    """

    def __init__(self, holidays_file):
        """
        Initialize the DateUtility object.

        :param holidays_file: Path to the holidays file.
        :type holidays_file: str
        """
        self.holidays = self.load_holidays(holidays_file)

    def load_holidays(self, holidays_file):
        """
        Load holidays from the specified file.

        :param holidays_file: Path to the holidays file.
        :type holidays_file: str
        :return: Dictionary of holidays grouped by timezone and date.
        :rtype: dict
        """
        holidays = {}
        with open(holidays_file, 'r') as file:
            for line in file:
                timezone, date_str, holiday = line.strip().split(',')
                date = datetime.strptime(date_str, '%Y%m%d')
                holidays.setdefault(timezone, {}).setdefault(date, []).append(holiday)
        return holidays

    def convert_dt(self, from_date, from_date_TZ, to_date_TZ):
        """
        Convert a given date from one timezone to another.

        :param from_date: The date to convert.
        :type from_date: datetime.datetime
        :param from_date_TZ: The timezone of the input date.
        :type from_date_TZ: str
        :param to_date_TZ: The timezone to convert the date to.
        :type to_date_TZ: str
        :return: Converted date in the target timezone.
        :rtype: datetime.datetime
        """
        from_timezone = pytz.timezone(from_date_TZ)
        to_timezone = pytz.timezone(to_date_TZ)
        from_date = from_timezone.localize(from_date)
        to_date = from_date.astimezone(to_timezone)
        return to_date

    def add_dt(self, from_date, number_of_days):
        """
        Add a specified number of days to a given date.

        :param from_date: The date to add days to.
        :type from_date: datetime.datetime
        :param number_of_days: The number of days to add.
        :type number_of_days: int
        :return: Resulting date after adding the specified days.
        :rtype: datetime.datetime
        """
        to_date = from_date + timedelta(days=number_of_days)
        return to_date

    def sub_dt(self, from_date, number_of_days):
        """
        Subtract a specified number of days from a given date.

        :param from_date: The date to subtract days from.
        :type from_date: datetime.datetime
        :param number_of_days: The number of days to subtract.
        :type number_of_days: int
        :return: Resulting date after subtracting the specified days.
        :rtype: datetime.datetime
        """
        to_date = from_date - timedelta(days=number_of_days)
        return to_date

    def get_days(self, from_date, to_date):
        """
        Calculate the number of days between two dates.

        :param from_date: The start date.
        :type from_date: datetime.datetime
        :param to_date: The end date.
        :type to_date: datetime.datetime
        :return: Number of days between the two dates.
        :rtype: int
        """
        days = (to_date - from_date).days
        return days

    def get_days_exclude_we(self, from_date, to_date):
        """
        Calculate the number of days excluding weekends between two dates.

        :param from_date: The start date.
        :type from_date: datetime.datetime
        :param to_date: The end date.
        :type to_date: datetime.datetime
        :return: Number of days excluding weekends between the two dates.
        :rtype: int
        """
        days = self.get_days(from_date, to_date)
        weekends = 0
        current_date = from_date
        while current_date <= to_date:
            if current_date.weekday() >= 5:  # Saturday (5) or Sunday (6)
                weekends += 1
            current_date += timedelta(days=1)
        return days - weekends

    def get_days_since_epoch(self, from_date):
        """
        Calculate the number of days since the epoch (January 1, 1970) for a given date.

        :param from_date: The date to calculate days since the epoch for.
        :type from_date: datetime.datetime
        :return: Number of days since the epoch.
        :rtype: int
        """
        epoch = datetime.utcfromtimestamp(0)
        days = (from_date - epoch).days
        return days

    def get_business_days(self, from_date, to_date, timezone):
        """
        Calculate the number of business days (excluding weekends and holidays) between two dates.

        :param from_date: The start date.
        :type from_date: datetime.datetime
        :param to_date: The end date.
        :type to_date: datetime.datetime
        :param timezone: The timezone to consider for holidays.
        :type timezone: str
        :return: Number of business days between the two dates.
        :rtype: int
        """
        days = self.get_days_exclude_we(from_date, to_date)
        current_date = from_date
        business_days = 0
        while current_date <= to_date:
            if (
                timezone in self.holidays
                and current_date in self.holidays[timezone]
            ):
                # Exclude holidays
                pass
            elif current_date.weekday() < 5:  # Exclude weekends
                business_days += 1
                
            current_date += timedelta(days=1)

        return business_days
        '''
        This function doesn't take into account the dates which are not
        present in the holidays.dat file.
        For eg, if 2022-11-24 is a holiday, it won't count 2023-11-24 as a holiday.
        That means, it doesn't consider recurring holidays.


        If you want the functionality of recurring holidays to be considered as
        holiday, comment the above part of the code and use the following code
        snippet.




        days = self.get_days_exclude_we(from_date, to_date)
        current_date = from_date
        business_days = 0
        if timezone in self.holidays:
            holiday_date_month=[]
            holidays_tuple = self.holidays[timezone]
        for i in holidays_tuple:
            holiday_date_month.append(i.strftime('%m-%d'))
        while current_date <= to_date:
            current_day_month = current_date.strftime('%m-%d')
            if current_day_month in holiday_date_month:
                # Exclude holidays 
                pass
            elif current_date.weekday() < 5:  # Exclude weekends
                business_days += 1
                
            current_date += timedelta(days=1)

        return business_days
        '''


        

def show_menu():
    """
    Display the menu options.
    """
    print("\n\n===== Date Utility Menu =====\n")
    print("1. Convert a Date")
    print("2. Add Days to a Date")
    print("3. Subtract Days from a Date")
    print("4. Calculate Days Between Two Dates")
    print("5. Calculate Business Days Between Two Dates")
    print("6. Calculate Days Since Epoch")
    print("0. Exit")


def get_date_input(prompt):
    """
    Get a date as input from the user.

    :param prompt: The input prompt to display.
    :type prompt: str
    :return: Date as a datetime object.
    :rtype: datetime.datetime
    """
    while True:
        try:
            date_str = input(prompt)
            date = datetime.strptime(date_str, '%Y-%m-%d')
            return date
        except ValueError:
            print("Invalid date format. Please enter a date in the format 'YYYY-MM-DD'.")


def main():
    holidays_file = 'holidays.dat'
    date_utility = DateUtility(holidays_file)

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            from_date = get_date_input("Enter the date to convert (YYYY-MM-DD): ")
            from_tz = input("Enter the timezone of the input date (e.g., UTC, US/Eastern): ")
            to_tz = input("Enter the target timezone to convert to (e.g., UTC, US/Eastern): ")
            converted_date = date_utility.convert_dt(from_date, from_tz, to_tz)
            print(f"Converted Date: {converted_date}")

        elif choice == '2':
            from_date = get_date_input("Enter the date to add days to (YYYY-MM-DD): ")
            days = int(input("Enter the number of days to add: "))
            added_date = date_utility.add_dt(from_date, days)
            print(f"Added Date: {added_date}")

        elif choice == '3':
            from_date = get_date_input("Enter the date to subtract days from (YYYY-MM-DD): ")
            days = int(input("Enter the number of days to subtract: "))
            subtracted_date = date_utility.sub_dt(from_date, days)
            print(f"Subtracted Date: {subtracted_date}")

        elif choice == '4':
            from_date = get_date_input("Enter the start date (YYYY-MM-DD): ")
            to_date = get_date_input("Enter the end date (YYYY-MM-DD): ")
            days_between = date_utility.get_days(from_date, to_date)
            print(f"Days Between: {days_between}")

        elif choice == '5':
            from_date = get_date_input("Enter the start date (YYYY-MM-DD): ")
            to_date = get_date_input("Enter the end date (YYYY-MM-DD): ")
            timezone = input("Enter the timezone (e.g., US/Eastern): ")

            business_days = date_utility.get_business_days(from_date, to_date, timezone)
            print(f"Business Days: {business_days}")

        elif choice == '6':
            from_date = get_date_input("Enter the date (YYYY-MM-DD): ")
            days_since_epoch = date_utility.get_days_since_epoch(from_date)
            print(f"Days Since Epoch: {days_since_epoch}")

        elif choice == '0':
            print("\nExiting...\n\n")
            break

        else:
            print("Invalid choice. Please enter a valid option.\n")


if __name__ == '__main__':
    main()
