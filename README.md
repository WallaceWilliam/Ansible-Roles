# ansible-roles
simple roles for ansible

### 1) adduser

Role for add sudoer user

Create remote user and copy rsa key

Params:

-username: User name will be created

Example ansible-playbook adduser.yml -e "hostname=test2" -e "ansible_user=root" -K

user test - root user on remote host

### 2) cron-apt

Role for notify about apt packages update

Params:

-mailto: mail for notify
-mailon: 'changes'
-dma_smarthost: smtp server

Example ansible-playbook cron-apt.yml -e "hostname=test2"

### 3) logon-notify-mail

Role for mail notify on ssh logon

Params:

-domain: mail domain
-recepient: recepient
-dma_smarthost: smtp server

Example ansible-playbook logon-notify-mail.yml -e "hostname=test2"