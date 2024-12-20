import paramiko

class SSHClient:
    def __init__(self, hostname, username, password=None, key_file=None):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.key_file = key_file
        self.client = None

    def connect(self):
        """Establish SSH connection."""
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if self.key_file:
                self.client.connect(self.hostname, username=self.username, key_filename=self.key_file)
            else:
                self.client.connect(self.hostname, username=self.username, password=self.password)
            return True
        except paramiko.AuthenticationException:
            print(f"Authentication failed for {self.hostname}")
            return False
        except Exception as e:
            print(f"Failed to connect to {self.hostname}: {e}")
            return False

    def execute_command(self, command):
        """Execute a command on the remote server and return the output."""
        if not self.client:
            raise Exception("SSH connection is not established.")
        try:
            stdin, stdout, stderr = self.client.exec_command(command)
            output = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            return output, error
        except Exception as e:
            print(f"Error executing command on {self.hostname}: {e}")
            return None, str(e)

    def close(self):
        """Close the SSH connection."""
        if self.client:
            self.client.close()
