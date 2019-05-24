1. Install python 3.7 
2. Install Pycharm IDE
3. Install selenium packages


Project directory : tests

Command to run :
1. py.test test_login.py --driver Chrome --driver-path ".\chrome\chromedriver.exe" -v --variables testdata.json --html=chromereport.html (To run on Chrome browser)
2. py.test test_login.py --driver Firefox --driver-path ".\firefox\geckodriver.exe" -v --variables testdata.json --html=firefoxreport.html

To run the script on chrome and firefox simultaneouly, use && between 1and 2 commands

Framework used : Pytest

Reporting mechanism : Pytest-html library

Pytest-variable library used to store the test data. Test data is stored in the JSON file in a dictionary.

Also, add chrome and geckodriver to your environment path.
