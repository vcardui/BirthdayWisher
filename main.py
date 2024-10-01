import random
import smtplib
import pandas
import datetime as dt

my_email = "carduibot@gmail.com"
password = ""

now = dt.datetime.now()
all_data = pandas.read_csv("birthdays.csv")
matching_birthdays = all_data[all_data.month == now.month][all_data.day == now.day]

for name in matching_birthdays["name"]:
    randLetter = f"letter_{random.randint(1,3)}.txt"
    with open(f"letter_templates/{randLetter}", 'r') as letter_file:
        new_letter = letter_file.read().replace('[NAME]', name)
        print(new_letter)
        row_number = matching_birthdays[matching_birthdays.name == name].index[0]
        addressee_email = matching_birthdays["email"][row_number]
        print(addressee_email)

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=addressee_email,
                            msg=f"Subject:Happy Birthday!\n\n{new_letter}")
        connection.close()
