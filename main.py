from turtle import color

from modules.registry_parser import get_usb_devices
from modules.risk_engine import calculate_risk, risk_level
from modules.statistics import device_statistics
from modules.export_utils import export_csv, export_json
from modules.hash_utils import calculate_sha256
from modules.html_report import generate_html_report
from modules.chain_of_custody import create_evidence_record
from modules.pdf_report import generate_pdf_report
from modules.timeline import view_usb_timeline
from modules.chain_of_custody import log_action
from modules.case_manager import (
    create_case,
    load_case,
    get_current_case
)


from colorama import init, Fore, Style
init(autoreset=True)

BANNER = f"""
{Fore.MAGENTA}
====================================================
 VEXA'S USB TOOLKIT
====================================================
"""

# DISPLAY DEVICES #

def display_devices(devices):
    if not devices:
        print("\nNo devices found.\n")
        return

    for index, device in enumerate(devices, start=1):

        score = calculate_risk(device)
        level = risk_level(score)

        print(f"\nDevice #{index}")
        print("-" * 50)
        print(f"Name         : {device['Device']}")
        print(f"Device Type  : {device['DeviceType']}")
        print(f"Serial Number: {device['SerialNumber']}")
        print(f"Risk Score   : {score}/100")

    if level == "LOW":
        color = Fore.GREEN

    elif level == "MEDIUM":
        color = Fore.YELLOW

    else:
        color = Fore.RED

    print(
        f"Risk Score   : {score}/100"
    )

    print(
        color +
            f"Risk Level   : {level}"
    )

# STATISTICS #

def show_statistics(devices):

    stats = device_statistics(devices)

    print(
        Fore.MAGENTA +
        "\n================ STATISTICS ================\n"
    )
    print(f"Total Devices   : {stats['TotalDevices']}")
    print(f"Unknown Devices : {stats['UnknownDevices']}")
    print(f"Most Common     : {stats['MostCommon']}")
    print()

# HASHES #

def verify_hash():

    filepath = input(
        "\nEnter report path: "
    )

    try:

        hash_value = calculate_sha256(
            filepath
        )

        print(
            "\nSHA256 Hash:"
        )

        print(
            hash_value
        )

    except Exception as e:

        print(
            f"\nError: {e}"
        )

###############

def main():

    devices = []

    while True:

        print(BANNER)

        current = get_current_case()

        if current:

            print(
                f"Current Case: {current}"
            )

        else:

            print(
                "Current Case: None"
            )       

        print()

        print("[1] Scan USB History")
        print("[2] View Devices")
        print("[3] View Statistics")
        print("[4] Export CSV")
        print("[5] Export JSON")
        print("[6] Verify Report Hash")
        print("[7] Generate HTML Report")
        print("[8] Create Evidence Record")
        print("[9] Generate PDF Report")
        print("[10] Timeline")
        print("[11] Create New Case")
        print("[12] Load Existing Case")
        print("[13] Exit")


        choice = input("\nSelect Option: ")

        if choice == "1":

            print("\n[*] Scanning USB Registry...")

            devices = get_usb_devices()

            log_action(
                "USB Registry Scan Completed"
            )

            print(
                Fore.GREEN +
                f"\n[+] Found {len(devices)} USB device(s).\n"
            )

        elif choice == "2":
            display_devices(devices)

        elif choice == "3":
            show_statistics(devices)

        elif choice == "4":
            export_csv(devices)

        elif choice == "5":
            export_json(devices)

        elif choice == "6":
            verify_hash() 

        elif choice == "7":
            generate_html_report(
            devices
        )

        elif choice == "8":
            create_evidence_record()

        elif choice == "9":
            generate_pdf_report(
            devices
        )

        elif choice == "10":
             view_usb_timeline()

        elif choice == "11":
            create_case()
        
        elif choice == "12":
            load_case()

        elif choice == "13":
            print("\nGoodbye.\n")
            break

        else:
            print("\nInvalid Option.\n")

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()