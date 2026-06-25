import os
import json
from datetime import datetime

CASES_FOLDER = "cases"
CURRENT_CASE = None


def create_case():



    case_name = input(
        "\nCase Name: "
    )

    investigator = input(
        "Investigator: "
    )

    os.makedirs(
        CASES_FOLDER,
        exist_ok=True
    )

    case_id = (
        f"CASE-"
        f"{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    )

    case_folder = os.path.join(
        CASES_FOLDER,
        case_id
    )

    os.makedirs(
        case_folder,
        exist_ok=True
    )

    case_info = {

        "CaseID": case_id,
        "CaseName": case_name,
        "Investigator": investigator,
        "Created": str(datetime.now()),
        "Status": "Open"

    }

    with open(
        os.path.join(
            case_folder,
            "case.json"
        ),
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            case_info,
            file,
            indent=4
        )

    open(
        os.path.join(
            case_folder,
            "notes.txt"
        ),
        "w"
    ).close()

    open(
        os.path.join(
            case_folder,
            "evidence_log.txt"
        ),
        "w"
    ).close()

    open(
        os.path.join(
            case_folder,
            "hashes.txt"
        ),
        "w"
    ).close()

    print(
        f"\nCase Created Successfully!\n"
    )

    print(
        f"Case ID: {case_id}"
    )

    print(
        f"Folder: {case_folder}\n"
    )

    set_current_case(case_folder)

    return case_folder

def set_current_case(case_folder):

    global CURRENT_CASE

    CURRENT_CASE = case_folder


def get_current_case():

    return CURRENT_CASE

def load_case():

    global CURRENT_CASE

    if not os.path.exists(CASES_FOLDER):

        print("\nNo cases exist.\n")
        return

    cases = [

        folder

        for folder in os.listdir(CASES_FOLDER)

        if os.path.isdir(
            os.path.join(
                CASES_FOLDER,
                folder
            )
        )

    ]

    if not cases:

        print("\nNo cases found.\n")
        return

    print("\nAvailable Cases\n")

    for index, case in enumerate(cases, start=1):

        print(f"[{index}] {case}")

    try:

        choice = int(
            input("\nSelect Case: ")
        )

        CURRENT_CASE = os.path.join(
            CASES_FOLDER,
            cases[choice - 1]
        )

        print(
            f"\nLoaded Case:\n{CURRENT_CASE}\n"
        )

    except:

        print(
            "\nInvalid selection.\n"
        )