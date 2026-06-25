import csv
import json
import os
from datetime import datetime
from modules.case_manager import get_current_case
from modules.chain_of_custody import log_action


def export_csv(devices):

    if not devices:
        print("\nNo devices to export.\n")
        return

    case_folder = get_current_case()

    if not case_folder:

        print("\nPlease create a case first.\n")
        return

    filename = os.path.join(
        case_folder,
        f"usb_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    )

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Device",
                "DeviceType",
                "SerialNumber"
            ]
        )

        writer.writeheader()

        for device in devices:
            writer.writerow(device)

    log_action(
        "CSV Report Generated"
    )       

    print(f"\nCSV exported:\n{filename}\n")


def export_json(devices):

    if not devices:
        print("\nNo devices to export.\n")
        return

    case_folder = get_current_case()

    if not case_folder:

        print("\nPlease create a case first.\n")
        return

    filename = os.path.join(
        case_folder,
        f"usb_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            devices,
            file,
            indent=4
        )

    log_action(
        "JSON Report Generated"
    )

    print(f"\nJSON exported:\n{filename}\n")