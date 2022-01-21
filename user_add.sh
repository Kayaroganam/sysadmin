#!/bin/bash

read -p "New User Name: " USER_NAME

sudo useradd $USER_NAME
sudo passwd $USER_NAME

sudo cut -d":" -f1 /etc/passwd > /etc/sysadmin/usergroupmanagement/userlist_without_serialno
sudo cut -d":" -f1 /etc/passwd | cat -n > /etc/sysadmin/usergroupmanagement/userlist_with_serialno
