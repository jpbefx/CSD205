#####       James Bailey CSD-205_Module10_Assignment Files and Exceptions       #####

import json

# Load the userinfo, if it has been stored previously.
#  Otherwise, prompt for the userinfo and store it.
def get_stored_userinfo():
    """Get sotred userinfo if available."""
    filename = 'userinfo.json'
    try:
        with open(filename) as f:
            userinfo = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return userinfo

def get_new_userinfo():
    """Prompt for a new userinfo."""
    userinfo = input("What is your name, address, and phone#?")
    filename = 'userinfo.json'
    with open(filename, 'w') as f:
        json.dump(userinfo, f)
    return userinfo


def greet_user():
    """Greet the user, showing the saved info."""
    userinfo = get_stored_userinfo()
    if userinfo:
        print(f"Welcome back, I have recorded your personal information, ({userinfo}")
    else:
        userinfo = get_new_userinfo()
        print(f"We'll remember your information ({userinfo}), information!")

    greet_user()

