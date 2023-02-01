# Automated Email Sender

## About the project
It is used for a company to send automated emails to its clients. 

## Tech stack
- Backend technologies : 
    - Python v3.10.x or higher
    - Libraries
        - schedule
        - requests
        - email
        - time
        - datetime
        - os
        - logging
        - smtplib

## About application
The project is divided to : 
- email_data.py : Which represents the data of the email information. 
    - We created a class EmailData, which contains the following properties :
        - response: We used external endpoint and getting the data from API - 
        
        (https://www.npoint.io/docs/de5c3533349a7f588f4d)-it is our api.We have created data from this webpage.You can see data in below.And it is also possible to just entering this link and see the data
        {
            "sender_email":{"email":"python.email270@gmail.com","password":"rnihqtzturzznjju"},
            "emails":{"t.muzeffer.1998@gmail.com":{"name":"muzeffer"},"negarchabi@gmail.com":{"name":"negar"},"nour.eimesh96@gmail.com":{"name":"noor"}},
            "subject":"[DATE] Oil Sales",
            "content":"Dear [NAME],\nI trust you are well.  Here is the report of sales for [DATE]\nSales\nThe following sales were generated in the day:\nCanola Oil – 200\nOlive Oil – 60\nReturns\nThere were no returns in [DATE]."}
        )

        - email_data : which has the data that is coming from the request. 
        - emails : Here we are getting the receivers emails from the data that we already have.
        - content : Getting the content from the data.
        - sender_email : Getting the sender email from the data.   
        - sender_password : Getting the sender password from the data.  
        - today :Getting the current date.
        - subject : Getting the subject from the data and replace the word date in the data with the current date.   
- email_service.py : Which contains the sending functionality. We create an object from EmailData and method for sending the email with the following details:
    - We are connecting with the SMTP which is an instance encapsulates an SMTP connection. and then start the connection.
    - we are setting the subject and start the connection and login with the sender email.
    - we are iterating through the receivers emails and fill the information of the email ( from, to, subject, content).
    - Lastly, we are attaching the content of the email and the files into the message. 
- file_service.py : It is used for getting the attachments that should be sent with the email. We created an method which has the following functionality:
    - We are setting the path of the current files that we have them locally. 
    - We created the attachments which is a lost of MIMEBASE.
    - Finally, we are iterating through the files and read them as binary format and set the type of the attachment and the name. Besides that we are encoding the file into based64 format and append them to the attachments.
- email.log : Here we can find the logs and to keep track of the emails that have been sent and any errors. 
    - We set the basic configuration inside the constructor.
    - We created two methods, one for the information and one for error. Both of them are receiving the message and set it to the logging based on the type of the message.
- main.py : It has the send function which uses the email_service and file_service to send the emails with scheduling them and generating the logs whether the emails were sending successfully or not.
    - We have a sender method:
        - We created an object from LoggingModule.
        - we created two objects : file_service and email_service.
        - we used the method send_email to send the emails. We send the files as a parameter to the method.
        - We covered the code with try catch, so if everything works correctly, then we send a successful message to the logger. If not, it should be thrown an exception and we send an error message to the logger. 
        - Lastly, we use the schedule library to run the method every day at specific time and we write the infinity loop for running the code forever so everyday the email should be sent.


