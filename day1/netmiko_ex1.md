# Netmiko Ex1
-----------

Write a Netmiko script that connects to one Arista switch and one Juniper vMX.
a. Print the current prompt

b. use send_command to retrieve 'show version' from the two devices. 

c. use send_command to retrieve running configuration from the two devices. 

d. Save the running config to a file.


Dictionary for network devices that can be used with Netmiko.

    arista1 = {
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": std_password,
    }

    vmx1 = { 
        "device_type": "juniper_junos",
        "host": "vmx1.lasthop.io",
        "username": "pyclass",
        "password": std_password,
    }
