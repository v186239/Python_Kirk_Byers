# Expanding on exercise1:

---- Part from Exercise1 ----
Using the subprocess library and Popen, execute the "df -h" command on the local system. The
result from this command should be similar to the following:

Filesystem      Size  Used Avail Use% Mounted on
/dev/xvda1       48G   17G   31G  35% /
devtmpfs        987M   60K  987M   1% /dev
tmpfs           997M     0  997M   0% /dev/shm


---- New part for Exercise2 ----
Using either regular expression processing or Python's split() method, create and print out
a data structure that is a list of dictionaries.


Your printed data structure should look similar to the following (given the above "df -h" data)

[{'filesystem': '/dev/xvda1', 'usage': '35%'},
 {'filesystem': 'devtmpfs', 'usage': '1%'},
 {'filesystem': 'tmpfs', 'usage': '0%'}]

---------
