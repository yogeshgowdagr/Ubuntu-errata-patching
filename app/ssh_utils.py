import paramiko
import platform

def check_server_version(ip_address):
    # Connect to the server using SSH and get the OS version and packages
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip_address)

        stdin, stdout, stderr = ssh.exec_command('lsb_release -a')
        os_version = stdout.read().decode().strip()

        stdin, stdout, stderr = ssh.exec_command('dpkg-query -l')
        installed_packages = stdout.read().decode()

        ssh.close()
        return os_version, installed_packages

    except Exception as e:
        return None, str(e)

def update_server_packages(ip_address):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip_address)

        stdin, stdout, stderr = ssh.exec_command('sudo apt-get update && sudo apt-get upgrade -y')
        result = stdout.read().decode()

        ssh.close()
        return True

    except Exception as e:
        return False
