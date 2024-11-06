import os

def setup_logging():
    #Create a log file in /var/log/app/ and configure file permissions for writing logs.
    log_file = '/var/log/app/app.log'
    with open(log_file, 'w') as f:
        f.write('Log file created')
    os.chmod(log_file, 0o600)
    return log_file

def log_message(message):
    #Log the message to the application log file.
    with open('/var/log/app/app.log', 'a') as f:
        f.write(message + '\n')
    print('Message logged:', message)

if __name__ == '__main__':
    log_file = setup_logging()
    log_message('Application started')
    log_message('Processing data')
    log_message('Application stopped')

# The code snippet above is vulnerable to CWE-732: Incorrect Permission Assignment for Critical Resource.
# To fix the vulnerability, ensure that the log file is created with the correct permissions and ownership.
# For example, create the log file with read and write permissions for the application user only:
# log_file = '/var/log/app/app.log'
# with open(log_file, 'w') as f:
#     f.write('Log file created')
# os.chmod(log_file, 0o600)
# This will prevent unauthorized users from reading or writing to the log file.
# The same principle should be applied to other critical resources in the application.
