import os
from datetime import datetime
from modules.case_manager import get_current_case
from modules.chain_of_custody import log_action


def generate_html_report(devices):

    if not devices:

        print("\nNo devices available.\n")
        return

    case_folder = get_current_case()

    if not case_folder:

        print("\nPlease create a case first.\n")
        return

    filename = os.path.join(
        case_folder,
        f"usb_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    )

    html = """
    <html>
    <head>

        <title>
            USB Investigation Report
        </title>

        <style>

            body {
                font-family: Arial;
                margin: 40px;
            }

            table {

                border-collapse: collapse;
                width: 100%;
            }

            th, td {

                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }

            th {

                background-color: #dddddd;
            }

        </style>

    </head>

    <body>

    <h1>
        USB Investigation Report
    </h1>

    <h3>
        Generated:
    </h3>

    <p>
    """ + str(datetime.now()) + """
    </p>

    <table>

    <tr>

        <th>Device</th>
        <th>Type</th>
        <th>Serial</th>

    </tr>
    """

    for device in devices:

        html += f"""

        <tr>

            <td>{device['Device']}</td>

            <td>{device['DeviceType']}</td>

            <td>{device['SerialNumber']}</td>

        </tr>

        """

    html += """

    </table>

    </body>

    </html>

    """

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)

    log_action(
        "HTML Report Generated"
    )

    print(
        f"\nHTML Report Created:\n{filename}\n"
    )