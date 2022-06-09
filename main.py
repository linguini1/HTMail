# Sends HTML emails automatically using an email list and an HTML file
__author__ = "Matteo Golin"

# Imports
from classes.html import HTMLObject
from classes.email import Email
from classes.dispatcher import Dispatcher

# Constants


# Main
def get_credentials() -> tuple[str, str]:

    """Returns username and password from the credentials file."""

    with open("credentials.txt", 'r') as file:
        username = next(file)
        password = next(file)

    return username, password


def main():

    # Create dispatcher
    username, password = get_credentials()
    dispatcher = Dispatcher(
        username=username,
        password=password
    )

    # Create email template
    test_email = Email(
        subject="Test",
        text="This is a test.",
        html=HTMLObject("test")
    )

    # Mailing list
    mailing_list: list[str] = [
        "example@email.com",
    ]

    # Send email
    dispatcher.send_batch(test_email, mailing_list)


if __name__ == "__main__":
    main()
