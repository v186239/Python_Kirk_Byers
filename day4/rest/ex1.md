# Using the Python requests library. Connect to the following URL 
(https://netbox.lasthop.io/api) and retrieve the information there using an
HTTP GET.

You will probably need the following HTTP Headers:

http_headers = {"accept": "application/json; version=2.4;"}

This is a public endpoint -- meaning that there is no authentication
necessary to execute a "GET" against it.

Use the "dir()" function to print out the attributes/methods of the response.

Print out some of the useful attributes of the response object.

What is "useful" will be up to you, but commonly used attributes include:
.text, .json(), .ok, and .status_code.
