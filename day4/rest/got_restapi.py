#!/usr/bin/env python
import requests
import pdbr
from rich import print

from urllib3.exceptions import InsecureRequestWarning
import pdbr
pdbr.set_trace()
# Ignore insecure warings for sites with self-signed certificates
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def main():
    url = "https://anapioficeandfire.com/api/characters"
    http_headers = {"accept": "application/json; version=2.4;"}
    response = requests.get(url, headers=http_headers, verify=False)

# Use the "dir()" function to print out the attributes/methods of the response.
# Print out some of the useful attributes of the response object.
    print()
    print("Here is the entire response")
    print(dir(response))
    print()
    print("Here is the response.text")
    print(response.text)
    print()
    print("Here is the response.json")
    print(response.json())
    print()
    print("Here is the response.ok")
    print(response.ok)
    print()
    print("Here is the response.status.code")
    print(response.status_code)


if __name__ == "__main__":
    main()
