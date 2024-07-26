from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")

def send_config(task, commands):

    commands = [
                "logging bufferd 10000",
                "interface loopck 0",
                "ip address 1.1.1.1 255.255.255.0",
                "no shut",
                ]

    task.run(task=netmiko_send_config, command_string="show ip int brief")

results=nr.run(task=netmiko_send_config)
print_result(results)

