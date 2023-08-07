# Take home coding test

Hypothetically, we have found ourselves in a situation where we, by mistake, have left some *Personally Identifiable Information* (“PII”) in an anonymized patients file in an AWS S3 bucket.

While we have swapped out and replaced the patient names, member_ids, and all other data with made up values, the date of birth has not been anonymized and may show up in multiple places, formats, etc! Anonymizing, especially when the patient information may be later connected to other healthcare information (such as medical claims), is important to ensure compliant use of historical data while building the Stellar Application.

We would like to take action and clean up the date of birth from those logs. The field has a typical format of **Month/Day/Year**, and we would like to replace those with **“X/X/Year”**. So for example, a date that is **“1/23/1981”** would become **“X/X/1981”**. We care about the year remaining there because we want to run analytics on this file.

You are tasked with building a script that will achieve this.

Details: 

- The log file is in an AWS S3 bucket (see details at the end of this file).

- Your keys to access that AWS bucket are also at the bottom of this file. You can only access that bucket through programmatic means (S3 libraries in the development language you chose, or AWS command line tools). Don't worry if you've never worked with AWS or S3 before - there is great online documentation and you're encouraged to refer to it as you work.

- Nobody really remembers the format of the log files, there’s no documentation.

- Most lines in the file will be consistent, but there will be cases where that isn’t the case. Logs are messy, as always, so expect some inconsistency across the file.

- At the end of this exercise, the log file should be replaced on AWS with the new log file that maintains everything else about the logs, but has the DOB obfuscated.

This should not take you more than 2 hours. If you do not have everything working at the end of that time do not worry, and please send us whatever code you have.

**Some final thoughts**

The script should be well-organized and do what is asked in the task, but we would like you to also think of ways to extend, expand, validate, and change this script to support multiple log files spanning multiple directories, potential different formats for log files, potential different data that needs to be cleaned.

As you finish this coding test, we would like to discuss some of the ways in which this could be expanded, and talk through how that would look like.

**AWS details and keys**

```
AWS bucket: s3.amazonaws.com/xxx.test.dean.hutton/patients.log
Access key ID:  XXX
Secret access key: XXX
```