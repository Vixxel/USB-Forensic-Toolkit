from datetime import datetime
import os

from modules.case_manager import get_current_case


def create_evidence_record():

    case_folder = get_current_case()

    if not case_folder:

        print("\nCreate a case first.\n")
        return

    investigator = input(
        "\nInvestigator Name: "
    )

    evidence_file = os.path.join(
        case_folder,
        "evidence_log.txt"
    )

    with open(
        evidence_file,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"\nEvidence Record\n"
        )

        file.write(
            f"Time: {datetime.now()}\n"
        )

        file.write(
            f"Investigator: {investigator}\n"
        )

        file.write(
            "-" * 50 + "\n"
        )

    print("\nEvidence record created.\n")


def log_action(action):

    case_folder = get_current_case()

    if not case_folder:
        return

    evidence_file = os.path.join(
        case_folder,
        "evidence_log.txt"
    )

    with open(
        evidence_file,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"[{datetime.now()}]\n"
        )

        file.write(
            f"{action}\n"
        )

        file.write(
            "-" * 50 + "\n"
        )