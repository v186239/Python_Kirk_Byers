# py.test -s -v test_ex1.py

#Create a unit test file named test_ex1.py with two functions in it.
Function 'func1' should take two integers and return their
sum. Function 'func2' should take two integers and return their 
product. 

Write and execute two unit tests. One unit test should test 'func1';
the other unit test should test 'func2'.

Write a unit test for func2 that uses pytest parametrize and tests
four different pairs of numbers (and their corresponding result)

Write a unit test that tests func1. Use the @pytest.mark.skipif decorator
to skip this test if your Python version is PY3.7

Use py.test to execute your tests. Ensure that they all pass.
