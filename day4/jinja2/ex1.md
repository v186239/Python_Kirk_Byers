# Create a Python program that uses Jinja2 to generate the below BGP configuration. 
Your template should be directly embedded inside of your program as a string and 
should use for the following variables: local_as, peer1_ip, peer1_as, peer2_ip,
peer2_as.

-----------
router bgp 10
  neighbor 10.1.20.2 remote-as 20
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor 10.1.30.2 remote-as 30
    address-family ipv4 unicast
-----------
