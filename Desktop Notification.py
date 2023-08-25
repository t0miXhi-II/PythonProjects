from plyer import notification

def get_user_input():
    user_input = input("Please enter your input here: ")
    return user_input


def get_custom_input(input_message):
    display_message = input(f"{input_message}: ")
    return display_message


def get_title():
    title = get_custom_input("Please enter your Notification Title")
    return title


def get_message():
    message = get_custom_input("Please enter your Notification Message")
    return message


def set_notification():
    notification.notify(
        title = get_title(),
        message = get_message(),
        timeout = 10
    )


set_notification()

