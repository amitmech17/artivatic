# These are the instructions to run this test application.

1. Clone the artivatic project from Github to your machine.
2. Ensure that Python is installed on your machine and that python environment variable is set correctly in path.
3. Goto the project folder and run command 'venv\scripts\activate.bat' in order to activate the virtual environment (for windows machines)
4. Now the vertualenv is activated. Run command (pytest --url "https://weathershopper.pythonanywhere.com/" --browser chrome --html=report/report.html)
5. my framework currently support 4 browser connfiguration namely chrome, firefox, edge and iexplorer (just replace the chrome with other options)
6. After test execution, please navigate to report directory and open the report.html
7. this report contains all the details related to this execution that is number of testcases passed and failed with detailed explaination.
