import logging
import re

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='process.log')


class WeakPasswordError(Exception):
   pass


def check_password(password):
    if len(password) < 10:
        logging.error("Password must be at least 10")
        raise WeakPasswordError("Password must be at least 10")

    if not re.search(r"[A-Z]", password):
        raise WeakPasswordError("The password must contain at least one capital letter")

    if not re.search(r"[0-9]", password):
        logging.error("The password must contain at least one capital letter")
        raise WeakPasswordError("The password must at least one number")

    if not re.search(r"[!@#$%^&*(){}'=+:~]", password):
        logging.error("The password must contain at least one special character")
        raise WeakPasswordError("The password must contain at least one special character")

    return password


try:
    password = input("Enter your password: ")
    print(check_password(password))

except WeakPasswordError as e:
    print("Error: ", e)

try:
    with open("file.txt", 'r') as file:
        data = file.read()

except FileNotFoundError:
    print("File not found")
except IOError:
    print("File access problem")
else:
    print(data)
    logging.info("File successfully")
finally:
    logging.info("Finish reading file")
