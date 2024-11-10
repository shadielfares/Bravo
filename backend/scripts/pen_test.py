import paramiko
import json
# List of sample credentials for educational connection testing (use only on your own servers)
credentials = [
        ('user2', 'password2'),
        ('chadeng', 'Shadi8275'),
        ]

# Host details (use your own test server)
hostname = '127.0.0.1'

# Initialize the SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

results = {}
def test_connect():
    # Iterate over the credentials for testing
    for username, password in credentials:
        try:
            client.connect(hostname=hostname, username=username, password=password)
            print(f'Successfully connected with {username}:{password}')
            results[username] = {'password': password, 'status': 'success'}
            client.close()
            break
        except paramiko.AuthenticationException:
            print(f'Failed to connect with {username}:{password}')
            results[username] = {'password': password, 'status': 'failed'}
        except Exception as e:
            print(f'Error: {e}')
            results[username] = {'password': password, 'status': 'error', 'error_message': str(e)}
    return results

print(test_connect())

