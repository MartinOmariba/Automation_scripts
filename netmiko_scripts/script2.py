from getpass import getpass
from pprint import pprint
from netmiko import ConnectHandler

iosv_l2 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.201",
    "username": "cisco",
    "password": getpass(),
}

iosv_l3 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.202",
    "username": "cisco",
    "password": getpass(),
}

commands = config_commands.txt

for device in [iosv_l2, iosv_l3]:
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_config_from_file(commands)
        output += net_connect.save_config()
        output = net_connect.send_command("show ip interface brief", use_genie=True)

print()
pprint(output)
print()