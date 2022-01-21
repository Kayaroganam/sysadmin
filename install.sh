#!/bin/bash

sudo touch /null
sudo rm -f /null
echo "installing..."
sudo yum install python3 -y > null

sudo mkdir -p /etc/sysadmin/usergroupmanagement/ 2> null
sudo mkdir /etc/sysadmin/dateandtime/ 2> null
sudo touch /etc/sysadmin/usergroupmanagement/userlist_with_serialno 2> null
sudo touch /etc/sysadmin/usergroupmanagement/userlist_without_serialno 2> null
sudo touch /etc/sysadmin/usergroupmanagement/grouplist_with_serialno 2> null
sudo touch /etc/sysadmin/usergroupmanagement/grouplist_without_serialno 2> null
sudo touch /etc/sysadmin/usergroupmanagement/grouplist_id 2> null
sudo touch /etc/sysadmin/dateandtime/zonelist_with_serialno 2> null
sudo touch /etc/sysadmin/dateandtime/zonelist_without_serialno 2> null

sudo chmod 666 /etc/sysadmin/usergroupmanagement/userlist_with_serialno
sudo chmod 666 /etc/sysadmin/usergroupmanagement/userlist_without_serialno
sudo chmod 666 /etc/sysadmin/usergroupmanagement/grouplist_with_serialno
sudo chmod 666 /etc/sysadmin/usergroupmanagement/grouplist_without_serialno
sudo chmod 666 /etc/sysadmin/usergroupmanagement/grouplist_id
sudo chmod 666 /etc/sysadmin/dateandtime/zonelist_with_serialno
sudo chmod 666 /etc/sysadmin/dateandtime/zonelist_without_serialno

sudo ls /usr/share/zoneinfo/Asia/ > /etc/sysadmin/dateandtime/zonelist_without_serialno
sudo cat -n /etc/sysadmin/dateandtime/zonelist_without_serialno > /etc/sysadmin/dateandtime/zonelist_with_serialno

touch sysadmin.sh
echo "#!/bin/bash " > sysadmin.sh
echo "sudo python3 sysadmin.py" >> sysadmin.sh

sudo chmod +x sysadmin.sh

echo "installed successfully"
echo 'To run this tool please execute this commend "sh sysadmin.sh" or "./sysadmin.sh"'
