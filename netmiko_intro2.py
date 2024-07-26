from netmiko import ConnectHandler

iosv_l2 = {
  "device_type" : "cisco_ios",
  "ip" : "192.168.122.201",
  "username": "cisco",
  "password": "cisco",
}

iosv_l3 = {
  "device_type" : "cisco_ios",
  "ip" : "192.168.122.202",
  "username": "cisco",
  "password": "cisco",
}

all_devices = [iosv_l2, iosv_l3]
for device in all_devices:
    connection = ConnectHandler(**devices)
    connection.enable()

output = connection.send_command("sh ip int brief")

print(output)

config_commands = ["logging bufferd 20000","logging bufferd 20010","nologging console"
]

net_config = connection.send_config_set(config_commands)

print(net_config)


connection.disconnect()