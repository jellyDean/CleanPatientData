CleanPatientData.py <br />
Developer: Dean Hutton<br /> 
Date: 09/18/21

# Summary
This guide illustrates how to run the CleanPatientData.py program for cleaning sensitive patient data from a log file. CleanPatientData.py 
was built with Python 3.7, so it is recommended to use that version of the interpreter when executing the program. The 
program will:
1. Connect to an AWS S3 bucket (credentials are  masked)
   * You can comment this part of the program out and read in `patients.log` if desired
2. Download `patients.log` file from AWS S3
3. Create a new log file `patients-CLEANED.log` that does not have any sensitive information in it
4. Upload `patients-CLEANED.log` file to AWS s3
5. Complete

# Assumptions
- `DOB` and `DATE_OF_BIRTH` identify the dates of birth

# Setup and Usage
1. Setup and install a Python 3.7 Virtual Environment (VE). If you are unsure of how to do this see [here](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv) 
2. Clone the repo ```git clone https://github.com/jellyDean/CleanPatientData.git ```
3. Navigate to the repo ``` cd /Users/deanhutton/workdir/Personal/Repos/CleanPatientData ```
4. Run the script by executing ``` python CleanPatientData.py ```


# TODO
- Hide AWS keys - Done
- Add unit tests
- Document the methods and code better
- Add a correct logger
- Add better exception handling