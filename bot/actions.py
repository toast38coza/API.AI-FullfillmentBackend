from .api import API

def respond(msg, data={}, messages=[]):
    return {
        "speech": msg,
        "source": "api.appointmentguru.co",
        "displayText": msg,
        "data": data,
        # "contextOut": messages
    }

def debug(payload, params, token):
    return(respond('You\'ve hit the debug backend'))

