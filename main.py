from email_service import EmailService
from file_service import FileService
from logging_email import LoggingModule
 
import schedule
import time

def sender ():
    logger = LoggingModule()
    try:
        file_service = FileService
        email_service = EmailService()
        email_service.send_email(file_service.get_files())
        logger.log_info('Emails were sent successfully')
    except Exception as exception:
        logger.log_error(f"ERROR: {str(exception)}")

schedule.every().day.at("17:50").do(sender)

while True:
    schedule.run_pending()
    time.sleep(1)


    
