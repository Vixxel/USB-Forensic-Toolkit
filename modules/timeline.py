import win32evtlog
from modules.chain_of_custody import log_action


def view_usb_timeline():

    server = "localhost"

    log_type = (
        "Microsoft-Windows-DriverFrameworks-UserMode/Operational"
    )

    try:

        handle = win32evtlog.OpenEventLog(
            server,
            log_type
        )

        flags = (
            win32evtlog.EVENTLOG_BACKWARDS_READ
            |
            win32evtlog.EVENTLOG_SEQUENTIAL_READ
        )

        log_action(
            "USB Timeline Viewed"
        )

        print(
            "\nUSB Timeline\n"
        )

        events = win32evtlog.ReadEventLog(
            handle,
            flags,
            0
        )

        count = 0

        while events:

            for event in events:

                print(
                    f"Time: "
                    f"{event.TimeGenerated}"
                )

                print(
                    f"Event ID: "
                    f"{event.EventID}"
                )

                print(
                    "-" * 40
                )

                count += 1

                if count >= 25:
                    return

            events = win32evtlog.ReadEventLog(
                handle,
                flags,
                0
            )

    except Exception as e:

        print(
            f"\nError: {e}"
        )