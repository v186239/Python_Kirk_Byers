#!/usr/bin/env python
import requests
import pdbr
import os
from rich import print

from urllib3.exceptions import InsecureRequestWarning

# Ignore insecure warings for sites with self-signed certificates
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
# pdbr.set_trace()


def main():
    token = os.environ["NETBOX_TOKEN"]
    token = "Token {}".format(token)
    url = "https://netbox.lasthop.io/api/dcim/devices"
    http_headers = {"accept": "application/json; version=2.4;", "authorization": token}
    response = requests.get(url, headers=http_headers, verify=False)
    response = response.json()

# Use rich to print the JSON payload returned to you from the API.
    print("Here is the response")
    print()
    print(response)
    print()


if __name__ == "__main__":
    main()
