import paramiko

# List of sample credentials for educational connection testing (use only on your own servers)
credentials = [
    ('user1', 'password1'),
    ('user2', 'password2'),
]

# Host details (use your own test server)
hostname = 'your_server_ip'

# Initialize the SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Iterate over the credentials for testing
for username, password in credentials:
    try:
        client.connect(hostname=hostname, username=username, password=password)
        print(f'Successfully connected with {username}:{password}')
        client.close()
        break
    except paramiko.AuthenticationException:
        print(f'Failed to connect with {username}:{password}')
    except Exception as e:
        print(f'Error: {e}')

