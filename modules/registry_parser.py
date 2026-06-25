import winreg

def get_usb_devices():

    devices = []

    try:
        key_path = r"SYSTEM\CurrentControlSet\Enum\USBSTOR"

        usb_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            key_path
        )

        for i in range(winreg.QueryInfoKey(usb_key)[0]):

            try:
                device_type = winreg.EnumKey(
                    usb_key,
                    i
                )

                device_type_key = winreg.OpenKey(
                    usb_key,
                    device_type
                )

                for j in range(
                    winreg.QueryInfoKey(device_type_key)[0]
                ):

                    try:
                        serial = winreg.EnumKey(
                            device_type_key,
                            j
                        )

                        devices.append({
                            "Device": device_type,
                            "DeviceType": device_type,
                            "SerialNumber": serial
                        })

                    except:
                        pass

            except:
                pass

    except Exception as e:
        print(e)

    return devices