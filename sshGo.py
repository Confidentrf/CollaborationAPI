import paramiko 
import time


ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.set_missing_host_key_policy(paramiko.WarningPolicy)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect('10.60.53.139', port=22, username='cattura_customer', password='jungletech101' )
time.sleep(2)
stdin, stdout, stderr = ssh.exec_command('reboot -f')
time.sleep(2)
stdin, stdout, stderr = ssh.exec_command('jungletech101')
output = stdout.readlines()
type(output)
print ('\n'.join(output))