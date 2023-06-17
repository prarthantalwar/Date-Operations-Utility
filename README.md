# Date Utility

Date Utility is a Python program that provides various functionalities for date and time operations. It allows you to perform conversions between different timezones, add or subtract days from a given date, calculate the number of days between two dates, and more. Additionally, it can exclude weekends and holidays while calculating business days.

## Features

The Date Utility program includes the following features:

1. Timezone Conversion: Convert a date from one timezone to another.
2. Date Addition: Add a specified number of days to a given date.
3. Date Subtraction: Subtract a specified number of days from a given date.
4. Days Between: Calculate the number of days between two dates.
5. Business Days: Calculate the number of business days between two dates, excluding weekends and holidays.
6. Days Since Epoch: Calculate the number of days since the epoch (January 1, 1970).

## Usage

To use the Date Utility program, follow these steps:

1. Clone the repository or download the source code.
2. Ensure you have Python 3 installed on your system.
3. Install the required dependencies using the following command:
pip install pytz
4. Prepare a file named `holidays.dat` with the holiday calendar in the specified format. For example:<br>
TIMEZONE,DATE,HOLIDAY<br>
US/Eastern,20211225,Christmas Day<br>
Or you can just use the one I made.<br>
Feel free to add or remove holidays to the list according to the format.
6. Open a terminal or command prompt and navigate to the project directory.
7. Run the program using the following command:
python date_convert.py
8. Follow the on-screen menu to choose the desired functionality and provide the necessary inputs.

## Requirements

- Python 3.x
- pytz library

## Contributing

Contributions to the Date Utility project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.


## Acknowledgments

- The Date Utility program uses the `pytz` library for timezone conversions.
- The holiday calendar file format and loading functionality are inspired by real-world scenarios.

