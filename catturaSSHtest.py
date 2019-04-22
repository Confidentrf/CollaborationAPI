import paramiko
import time
import pexpect

hostname = "10.60.53.139"
username = "cattura_customer"
password = "jungletech101"

cmd = 'ifconfig'
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname,username=username,password=password)
    print("Connected to %s" % hostname)
    ssh_client.exec_command('sudo')
    time.sleep(2)
    stdin.write('password\n')
    stdin, stdout, stderr = ssh.exec_command('reboot -f')
except paramiko.AuthenticationException:
    print("Failed to connect to %s due to wrong username/password" %hostname)
    exit(1)

try:
    stdin, stdout, stderr = ssh.exec_command('reboot -f')
    time.sleep(2)
    output = stdout.readlines()
    type(output)
    print ('\n'.join(output))
    #stdin, stdout, stderr = ssh.exec_command('jungletech101')

except Exception as e:
    print('e.message')

err = ''.join(stderr.readlines())
out = ''.join(stdout.readlines())
final_output = str(out)+str(err)
print(final_output)