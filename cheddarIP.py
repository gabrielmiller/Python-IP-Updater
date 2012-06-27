import paramiko, os, time, urllib2

publicIp = urllib2.urlopen('http://curlmyip.com')
publicIpStr = str(publicIp.read().rstrip('\n'))

time.sleep(60)

if len(publicIpStr)<7:
	writeOutput = 'There was an error between the script and http://www.curlmyip.com/%nYou may be able to find the IP through cheddarcode\'s last login log.'
else:
	writeOutput = "<?php\\nheader(\'Location: http://%s:8002\')\\n?>" % publicIpStr

sshCommand = 'echo -e "%s" > public_html/buttbox/index.php' % writeOutput
sshCommand2 = 'echo -e "%s" > public_html/buttbox/ip.php' % str(publicIpStr)

ssh = paramiko.SSHClient()
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.connect('cheddarcode.com', port=2222, username='chddrcd')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(sshCommand)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(sshCommand2)

ssh.close()
