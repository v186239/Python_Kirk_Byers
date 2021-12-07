#!/usr/bin/env python
net_device = {
    "ip_addr": "192.168.1.1",
    "username": "will",
    "password": "123",
    "vendor": "arista",
    "model": "9000",
}

print()
for key, value in net_device.items():
    print(key, value)
net_device["password"] = "new_password"
net_device["secret"] = "mysecret"
device_type = net_device.get("device_type", "arista_eos")
print(f"\nDefault device type: {device_type}\n")
