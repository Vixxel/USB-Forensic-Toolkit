from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from datetime import datetime
from modules.case_manager import get_current_case
from modules.chain_of_custody import log_action
import os


def generate_pdf_report(devices):

    if not devices:

        print(
            "\nNo devices available.\n"
        )

        return

    case_folder = get_current_case()

    if not case_folder:

        print("\nPlease create a case first.\n")
        return

    filename = os.path.join(
        case_folder,
        f"usb_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    )

    doc = SimpleDocTemplate(
        filename
    )

    styles = (
        getSampleStyleSheet()
    )

    elements = []

    elements.append(
        Paragraph(
            "USB Investigation Report",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            f"Generated: {datetime.now()}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    for index, device in enumerate(
        devices,
        start=1
    ):

        elements.append(
            Paragraph(
                f"Device #{index}",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                f"Name: {device['Device']}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Type: {device['DeviceType']}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Serial Number: {device['SerialNumber']}",
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 10)
        )

    doc.build(
        elements
    )

    log_action(
        "PDF Report Generated"
    )

    print(
        f"\nPDF Report Created:\n{filename}\n"
    )