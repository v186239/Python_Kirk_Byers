# py.test -s -v test_ex2.py

# Create a unit test file named test_ex2.py.

In this unit test create a unit test fixture that establishes an SSH
connection to cisco4.

Write two tests that use this SSH fixture. The first test should execute
the .find_prompt() method and ensure the router prompt is returned successfully.

The second test should execute the "show ip int brief" command on the remote
device. This test should pass if the output contains the IP address '10.220.88.23'. 
Otherwise, the test should fail.
