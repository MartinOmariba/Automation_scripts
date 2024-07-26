from netmiko import ConnectHandler

try:

    iosv_l2 = {
  "device_type" : "cisco_ios",
  "host" : "192.168.122.201",
  "username": "cisco",
  "password": "cisco",
}

    net_connect = ConnectHandler(**iosv_l2)
    print(" success enter")

except Exception as e:
    print(e)
    return

connection = net_connect.find_prompt()
hostname = connection.strip("<" + ">")
print(hostname)
print()


net_connect.send_command_timing("enable")
net_connect.send_command_timing("undo smart")
output = net_connect.send_command_timing("config terminal")
print("entered config mode")


config_commands = [
  "config termnal"
  "logging bufferd 20000",
  "logging bufferd 20010",
  "nologging console"
]

net_connect.send_config_set(config_commands)  

#net_connect.send_command_timing("acl 2010 ")
net_connect.send_command_timing("save")


net_connect.disconnect()

