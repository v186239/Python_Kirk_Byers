# Create a Python program that creates a PyEZ Device connection to "vmx2". 

Using this PyEZ connection and the RouteTable and ArpTable views retrieve the 
routing table and the arp table for vmx2.

As part of this program create at least two functions:

function1:
-----
def gather_routes(device):

Takes a Juniper PyEZ device object and returns the route table from the
RouteTable view.

===
routes = RouteTable(device)
routes.get()
return routes
===


function2:
-----
def gather_arp_table(device):

Takes a Juniper PyEZ device object and returns the ARP table from the
ArpTable view.

