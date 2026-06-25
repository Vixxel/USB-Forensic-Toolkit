from collections import Counter


def device_statistics(devices):

    if not devices:

        return {
            "TotalDevices": 0,
            "UnknownDevices": 0,
            "MostCommon": "N/A"
        }

    total_devices = len(devices)

    unknown_devices = sum(
        1
        for device in devices
        if "unknown" in device["Device"].lower()
    )

    device_names = [
        device["Device"]
        for device in devices
    ]

    most_common = (
        Counter(device_names)
        .most_common(1)
    )

    return {
        "TotalDevices": total_devices,
        "UnknownDevices": unknown_devices,
        "MostCommon": (
            most_common[0][0]
            if most_common
            else "N/A"
        )
    }