#!/bin/bash

sudo cut -d: -f1 /etc/group > /etc/sysadmin/usergroupmanagement/grouplist_without_serialno  
sudo cut -d: -f1 /etc/group | cat -n > /etc/sysadmin/usergroupmanagement/grouplist_with_serialno

sudo cut -d: -f3 /etc/group > /etc/sysadmin/usergroupmanagement/grouplist_id

