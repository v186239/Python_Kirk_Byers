# Your Linux environment should have the following environment variable set:

NETBOX_TOKEN

You can access this environment variable using the following code:

    import os
    token = os.environ["NETBOX_TOKEN"]
    token = "Token {}".format(token)

That environment variable will contain the NetBox token to use for authenticating
to NetBox.

Using the Python requests libary and an HTTP GET, retrieve the information from the
following URL:

    url = "https://netbox.lasthop.io/api/dcim/devices"

You will probably need the following HTTP Headers:

    http_headers = {
        "accept": "application/json; version=2.4;",
        "authorization": token,
    }

Use rich to print the JSON payload returned to you from the API.
