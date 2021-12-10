# Use NAPALM to connect to arista1 through arista4.

Using the "load_merge_candidate()" stage a set of configuration changes. Your
changes should add 4 VLANs including VLAN names onto the Arista switches. Use
four VLAN IDs in the VLAN600 to VLAN899 range.

Your configuration changes should be stored in an external file. The syntax
of the configuration change (for a single VLAN) would be the following:

------
vlan 620
   name blue620
------

Using NAPALMs configuration operations retrieve the current diff of your staged
configuration change and print this diff to standard output.

If the diff is not empty (i.e. you have pending changes), then commit your
change to the four switches. Your program should not commit() the change if the
diff is empty (i.e. if your configuration change has already been applied).

Running your script a second time should result in no changes. In other words,
the diff will be empty and your program should not commit the changes.
