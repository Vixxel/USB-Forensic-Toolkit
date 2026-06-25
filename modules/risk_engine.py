SUSPICIOUS_NAMES = [
    "unknown",
    "generic",
    "usb device",
    "unrecognized"
]


def calculate_risk(device):

    score = 0

    name = device["Device"].lower()
    serial = device["SerialNumber"]

    if "unknown" in name:
        score += 50

    if len(serial) < 6:
        score += 20

    for word in SUSPICIOUS_NAMES:

        if word in name:
            score += 10

    if score > 100:
        score = 100

    return score


def risk_level(score):

    if score < 30:
        return "LOW"

    elif score < 70:
        return "MEDIUM"

    return "HIGH"