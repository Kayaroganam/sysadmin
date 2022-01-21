#!/bin/bash


sudo userdel $1

sudo cut -d":" -f1 /etc/passwd > /etc/sysadmin/usergroupmanagement/userlist_without_serialno
sudo cut -d":" -f1 /etc/passwd | cat -n > /etc/sysadmin/usergroupmanagement/userlist_with_serialno
