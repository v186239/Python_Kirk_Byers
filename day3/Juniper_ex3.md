# 3. PyEZ configuration operations:

3a. Open a PyEZ connection to the vmx2 device and acquire a configuration lock. 

Validate that the configuration session is indeed locked by SSH'ing into the device and attempting to enter configuration mode ("configure"). 

You should receive a prompt similar to the following:

pyclass@vmx2> configure 
Entering configuration mode
Users currently editing the configuration:
  pyclass (pid 41695) on since 2020-07-19 02:45:07 UTC
      exclusive


Add code to attempt to lock the configuration again. Gracefully handle the "LockError" exception (meaning the configuration is already locked).


3b. Use the "load" method to stage a configuration using a basic set command, for example, "set system host-name test-name".


3c. Print the diff of the current configuration with the staged configuration. Your output should look similar to the following:

[edit system]
-  host-name vmx2;
+  host-name test-name;


3d. Rollback the staged configuration. 

Once again, print out the diff of the staged and the current configuration (which at this point should be None).


