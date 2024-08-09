error = {}
names = {
    "critical": "Critical alarm",
    "major": "Major alarm",
    "minor": "Minor alarm",
    "warning": "Warning alarm",
    "unknown": "Unknown alarm"
}
timezones = {}
priority = {
    "critical": 1,
    "major": 2,
    "minor": 3,
    "warning": 4,
    "unknown": -1
}
urls = {
    "base": "https://api.telegram.org/bot",
    "updates": "/getUpdates",
    "last_update": "/getUpdates?offset=-1",
    "send_message": "/sendMessage"
}