from datetime import datetime


def get_new_email_with_timestamp():
    logic_invalid = datetime.now().strftime("%M_%S")
    return "awsramesh" + logic_invalid + "@gmail.com"