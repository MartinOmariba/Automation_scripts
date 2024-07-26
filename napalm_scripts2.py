import napalm
from pprint import pprint

 # Use the appropriate network driver to connect to the device:
driver = napalm.get_network_driver("ios")

# Connect:
iosv_l2= driver(
        hostname="192.168.122.201",
        username="cisco",
        password="cisco",
    )

iosv_l3 = driver(
        hostname="192.168.122.201",
        username="cisco",
        password="cisco",
    )

all_devices = [iosv_l2, iosv_l3]

for device in all_devices:


    print("Opening ...")
    device.open()

command = device.getfacts()

print(json.dumps(facts, sort_keys=True, indent=4))


