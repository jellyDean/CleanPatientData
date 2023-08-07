"""
CleanPatientData.py
Developer: Dean Hutton
Date: 09/18/21
Summary:

ASSUME:
- DOB and DATE_OF_BIRTH identify the dates of birth
TODO:
- Hide AWS keys
- Add unit tests
- Document the methods and code better
- Add a correct logger
- Add better exception handling
"""

import boto3
import re

dob_buffer = 20
date_of_birth_buffer = 30
dob_key = 'DOB'
date_of_birth_key = "DATE_OF_BIRTH"
aws_access_key_id = 'KEY_ID'
aws_secret_access_key = 'SECRET_KEY'


def download_file_from_s3(aws_access_key_id,aws_secret_access_key, bucket_name, file_name, local_file_location):
    """
    Function that downloads the dirty file from s3
    :param str aws_access_key_id: AWS access key id
    :param str aws_secret_access_key: AWS access secret key
    :param str bucket_name: AWS bucket name
    :param str file_name: AWS file name
    :param str local_file_location: Location to store the file locally

    """
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
    s3.download_file(bucket_name, file_name,local_file_location)


def upload_file_to_s3(aws_access_key_id,aws_secret_access_key, bucket_name, cleaned_file_name, s3_filename):
    """
    Function that uploads the cleaned file to s3
    :param str aws_access_key_id: AWS access key id
    :param str aws_secret_access_key: AWS access secret key
    :param str bucket_name: AWS bucket name
    :param str cleaned_file_name: Local location of cleaned file
    :param str s3_filename: AWS file name for the new cleaned file

    """
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)
    s3.upload_file(cleaned_file_name, bucket_name, s3_filename)


def clean_line(line, key, buffer):
    """
    Function that cleans the DOB from lines in a log
    :param str line: The line that needs to be cleaned
    :param str key: The DOB identifier
    :param int buffer: How far to look ahead in the line to grab the full DOB
    :return: The cleaned log file line with no PII
    :rtype: str

    """
    # Find the DOB
    dob_index = line.find(key)

    # Grab the DOB key plus the actual DOB
    sub_str = line[dob_index:dob_index + buffer]
    split = sub_str.split(key)
    # Parse out the DOB value
    date = split[1].replace("=", "").strip()

    # Find the DOB year
    regex = "\d{4}"
    match = re.findall(regex, date)

    try:
        # Build the new line
        new_str = "X/X/" + match[0]
        year_index = line.find(match[0])

        # Replace the dirty line with the cleaned line. Add 4 chars to account for year i.e. 1972
        new_line = line.replace(line[dob_index:year_index + 4], key + "='" + new_str)
        return new_line
    except Exception as ex:
        print("There has been an error with this string", date, ex)
        return line


def main():
    print("Starting the process to clean files from AWS S3")
    s3_bucket = 'xxx.xxx.test.dean.hutton'
    s3_file = 'patients.log'
    file_to_be_cleaned = '/Users/jameshutton/Workdir/Development/Repos/xxx/patients.log'
    cleaned_file = "/Users/jameshutton/Workdir/Development/Repos/xxx/patients-CLEANED.log"

    print("Downloading the dirty file from AWS")
    download_file_from_s3(aws_access_key_id,aws_secret_access_key, s3_bucket, s3_file, file_to_be_cleaned)

    print("Cleaning the dirty file to remove all PII")
    with open(file_to_be_cleaned) as f:
        with open(cleaned_file, "w") as c:
            lines = f.readlines()
            for line in lines:
                if dob_key in line:
                    c.write(clean_line(line, dob_key, dob_buffer))
                elif date_of_birth_key in line:
                    c.write(clean_line(line, date_of_birth_key, date_of_birth_buffer))
                else:
                    c.write(line)

    print("Uploading the cleaned file to AWS")
    upload_file_to_s3(aws_access_key_id,aws_secret_access_key, s3_bucket, cleaned_file, "patients-cleaned.log")
    print("Completed the process to clean files from AWS S3")


if __name__ == "__main__":
    # execute only if run as a script
    main()