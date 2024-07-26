---
- name: multiple commands
  hosts: all
  gather_facts: False
  connection: local


  vars:
    cli:
      host: "{{ansible_host}}"
      username: "{{username}}"
      password: "{{password}}"
      transport: cli


  tasks:
    - name: run multiple commands
      ios_config:
        commands:
           - show ip interface brief
           - show cdp neighbour
           - show arp
        provider: "{{cli}}"

      register: print_output
      
      -name: show output
       debug: 
         var: print_output