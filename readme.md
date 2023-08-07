CleanPatientData.py <br /> 
DownloadS3.py <br /> 
Developer: Dean Hutton<br /> 
Date: 09/18/21

# Summary
This guide illustrates how to run the CleanPatientData.py program for clean sensive data from a log file.
Direct_reports.py was built with Python 3.7 so it is recommended to use that version of the interpreter 
while running.

# Setup and Usage
1. Setup and install a Python 3.7 Virtual Environment (VE). If you are unsure of how to do this see [here](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv) 
2. Clone the repo ```git clone https://github.com/jellyDean/direct_reports.git ```
3. Open a terminal and CD in to your VE ``` cd /Users/deanhutton/workdir/Personal/VE/2.7.10/bin ```  
4. Activate the Virtual Environment ``` . activate.fish ```
5. Install the above Required Python Libraries via PIP
6. Navigate to the repo ``` cd /Users/deanhutton/workdir/Personal/Repos/direct_reports ```
7. Run the script by executing ``` python direct_reports.py -i employee_info.csv -rd 2011-03-24 ``` where ­i is the location of your input file and ­rd is the run date


# Running Tests
1. Follow steps 1-5 in the Setup and Usage section above
2. Navigate to the tests directory ``` cd /Users/deanhutton/workdir/Personal/Repos/direct_reports/tests ```
3. Enter ``` nosetests ``` in terminal and push enter
4. 5 Unit tests will run