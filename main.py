import logging
import smtplib
from email.mime.text import MIMEText

# Set up logging
logging.basicConfig(filename='etl_pipeline_1.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Log a message
logging.info('ETL pipeline started')

try:
    logging.info('ETL pipeline finished successfully')
except Exception as e:
    logging.error('Error during ETL pipeline: ' + str(e))
    
    # Send email alert
    msg = MIMEText('Error during ETL pipeline: ' + str(e))
    msg['Subject'] = 'ETL Pipeline Error'
    msg['From'] ='praveenkumarpv43@gmail.com'
    msg['To'] ='praveenkumarpv100@gmail.com'
    
    with smtplib.SMTP('localhost') as server:
        server.send_message(msg)