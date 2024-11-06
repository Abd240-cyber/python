# CWE-78: OS Command Injection
import subprocess
from flask import request

def network_tools():
    target = request.args.get('target')
    # 78-2
    """
    Check if the target host is online using the ping command.
    Return the ping result to the user.
    """
    # 78-3
    """
    The 'target' parameter is not validated before using it in the command.
    """
    return subprocess.check_output(f'ping -c 4 {target}', shell=True)

def get_system_info():
    # 78-0
    """
    Get the system information using the uname command.
    Return the system information to the user.
    """
    return subprocess.check_output('uname -a', shell=True)

def get_network_info():
    # 78-1
    """
    Get the network information using the ifconfig command.
    Return the network information to the user.
    """
    return subprocess.check_output('ifconfig', shell=True)

if __name__ == '__main__':
    print(network_tools())
    print(get_system_info())
    print(get_network_info())

# The code snippet above is vulnerable to CWE-78: OS Command Injection.