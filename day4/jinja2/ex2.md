# Use Python and Jinja2 to generate the below NX-OS interface configuration. You
should use an external template file and a Jinja2 environment to accomplish this.
The interface, ip_address, and netmask should all be variables in the Jinja2
template.

-------------
nxos1
-------------
interface Ethernet2/1
  ip address 10.1.100.1/24


-------------
nxos2
-------------
interface Ethernet2/1
  ip address 10.1.100.2/24
-------------
