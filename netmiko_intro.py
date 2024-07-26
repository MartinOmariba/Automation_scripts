from pprint import pprint
import yaml
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

with open("devices.yaml", "r") as file:
    device_data = yaml.safe_load(file)

connection = ConnectHandler(**device_data)

output = connection.send_command("sh ip int brief")

print(output)

connection.disconnect()