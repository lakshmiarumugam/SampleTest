# SampleTest

I have used Selenium Webdriver tool with Python language to code this test

The code covers the negative scenario where the username and password data are fetched from the test data sheet and when the credentials do not match there is an invalid login error message thrown. The code catches the error message and displays it in the logging info

Testsuite is the main test case that drives this test and calls the Testcases class

Please modify the Testdata Excel in driver Data tab to identify the appropriate driver location for the respective browser

The test requires that the Testdata excel sheet be placed in you local system path and that path requires to be replaced in the Testcases code on line 32

The current code is feasible enough to run the test across any browser and on different environments like Dev, QA, UAT or Prod
