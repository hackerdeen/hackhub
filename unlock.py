from hackhub import app, spaceapi

testing = False

def unlock(user):
    if testing:
        return True, "This was only a test"
    else:
        return False, "There is no doorbot."
