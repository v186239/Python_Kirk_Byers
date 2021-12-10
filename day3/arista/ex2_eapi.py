import pyeapi
import pdbr
from getpass import getpass
from rich import print

pdbr.set_trace()
cfg = [
    "vlan 770",
    "name Will_Rivera_green_770",
    "vlan 771",
    "name Will_Rivera_green_771",
    "vlan 772",
    "name Will_Rivera_green_772",
]

connection = pyeapi.client.connect(
    transport="https",
    host="arista1.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

device = pyeapi.client.Node(connection)
cfg_output = device.config(cfg)

output = device.enable(["show vlan"])
print(output)
