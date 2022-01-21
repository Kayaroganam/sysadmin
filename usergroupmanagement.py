import os

def title():
	print(" -------------------------------------------")
	print("| U S E R   G R O U P   M A N A G E M E N T |")
	print(" -------------------------------------------")



def help():
	print(" ---------------------")
	print("| [0] EXIT            |")
	print("| [1] ADD USER        |")
	print("| [2] REMOVE USER     |")
	print("| [3] LIST USES       |")
	print("| [4] NEW GROUP       |")
	print("| [5] DELETE GROUP    |")
	print("| [6] MODIFY A GROUP  |")
	print("| [7] LIST GROUPS     |")
	print("| [8][h] HELP         |")
	print(" ---------------------")

def listuser():
	os.system("bash userlist_update.sh")
	print(" ------------")
	print("|    USERS   |")
	print(" ------------")
	os.system("cat /etc/sysadmin/usergroupmanagement/userlist_with_serialno")

def listmembers(group_id):
	id_ = group_id
	os.system(f"grep {id_} /etc/group | cut -d: -f4 > /tmp/listmem.temp")
	listmem = open("/tmp/listmem.temp","r")
	content_of_listmem = listmem.read()
	listmem.close()
	content_of_listmem = content_of_listmem[0:-1]
	splited = content_of_listmem.split(",")
	index = 1
	print(" ----------------------")
	print("|         MEMBERS      |")
	print(" ----------------------")
	for i in splited:
		print("| ",index," ",i)
		index += 1
	print(" ----------------------")
	pass

def adduser_in_group(group_name):
	name = group_name
	os.system("bash ../user/userlist_update.sh")
	print(" ----------------------")
	print("|         USERS        |")
	print(" ----------------------")
	os.system("cat /etc/sysadmin/usergroupmanagement/userlist_with_serialno")
	print(" ----------------------")

	selected_user_to_add = input("ugmanagement > group [select user to add] >> ")
	os.system(f"sudo sed -n '{selected_user_to_add}p' /etc/sysadmin/usergroupmanagement/userlist_without_serialno > /tmp/selecteduser.temp")
	selected_userfile = open("/tmp/selecteduser.temp","r")
	selected_user = selected_userfile.read()
	selected_userfile.close()
	selected_user = selected_user[0:-1]
	os.system(f"sudo usermod -aG {name} {selected_user}")
	print("success")
	pass

def removeuser_from_group(group_name):
	name = group_name
	os.system("bash ../user/userlist_update.sh")
	print(" ----------------------")
	print("|         USERS        |")
	print(" ----------------------")
	os.system("cat /etc/sysadmin/usergroupmanagement/userlist_with_serialno")
	print(" ----------------------")

	selected_user_to_add = input("ugmanagement > group [select user to remove] >> ")
	os.system(f"sudo sed -n '{selected_user_to_add}p' /etc/sysadmin/usergroupmanagement/userlist_without_serialno > /tmp/selecteduser.temp")
	selected_userfile = open("/tmp/selecteduser.temp","r")
	selected_user = selected_userfile.read()
	selected_userfile.close()
	selected_user = selected_user[0:-1]
	os.system(f"sudo groupmems -d {selected_user} -g {name}")
	print("success")
	pass

def selected_group_option():
	print(" ------------------------------")
	print("| [0] EXIT                     |") 
	print("| [1] ADD USER                 |")
	print("| [2] REMOVE USER              |") 
	print("| [3] LIST MEMBERS             |")
	print("| [4][h] HELP                  |")
	print(" ------------------------------")

def deletegroup():
	listgroup()
	select_group = input("ugmanagement > group [select group] >> ")
	os.system(f"sudo sed -n '{select_group}p' /etc/sysadmin/usergroupmanagement/grouplist_without_serialno > /tmp/grouplist.temp")
	grouplist_file = open("/tmp/grouplist.temp","r")
	con = grouplist_file.read()
	grouplist_file.close()
	gname = con[0:-1]
	os.system(f"sudo groupdel {gname}")
	os.system("bash grouplist_update.sh")
	pass

def listgroup():
	os.system("bash grouplist_update.sh")
	file1 = open("/etc/sysadmin/usergroupmanagement/grouplist_with_serialno","r")
	print(" ------------------")
	print("|       GROUPS     |")
	print(" ------------------")
	e_list = []
	for i in file1:
		e_list.append(i)
	for i in e_list:
		i = i.replace("\n","")
		i = i.replace(" ","")
		print("|",i)
	print(" ------------------")

def modifygroup():
	listgroup()
	select_group = input("ugmanagement > group [select group] >> ")

	if select_group == '':
		pass
	else:
		os.system(f"sudo sed -n '{select_group}p' /etc/sysadmin/usergroupmanagement/grouplist_without_serialno > /tmp/grouplist.temp")
		grouplist_file = open("/tmp/grouplist.temp","r")
		gname = grouplist_file.read()
		grouplist_file.close()
		gname = gname[0:-1]
		print(gname , " is selected")

		loop = True
		selected_group_option()
		while loop :
			select = input(f"ugmanagement > group [{gname}] >> ")

			if select == '0':
				loop = False

			#--------add user in group---------
			elif select == '1':
				adduser_in_group(gname)
				pass

			#--------remove user in group------
			elif select == '2':
				removeuser_from_group(gname)
				pass

			#----------list users in group------

			elif select == '3':
				os.system(f"sed -n '{select_group}p' /etc/sysadmin/usergroupmanagement/grouplist_id > /tmp/groupID.temp")
				file1 = open("/tmp/groupID.temp","r")
				group_id = file1.read()
				file1.close()
				group_id = group_id[0:-1]
				listmembers(group_id)
				pass

			#---------------help---------------
			elif select == 'h' or select == 'H' or select == '4':
				selected_group_option()
				pass

def newgroup():
	group_name = input("New group Name : ")
	os.system(f"sudo groupadd {group_name}")


if __name__ == '__main__':
	title()
	help()

	loop = True

	while loop:
		select = input("SYSADMIN > ugmanagement >> ")

		if select == '0':
			loop = False
			print("exit")
			pass
		
		#----------add user---------
		elif select == '1':
			os.system("bash user_add.sh")
			os.system("bash userlist_update.sh")
			print("success")

		#----------remove user---------
		elif select == '2':
			listuser()
			selected_user = input("ugmanagement > user[select user] >> ")
			os.system(f"cat /etc/sysadmin/usergroupmanagement/userlist_without_serialno | sed -n '{selected_user}p' > /tmp/user_remove.temp")
			user_remove = open("/tmp/user_remove.temp","r")
			p = user_remove.read()
			p = p[0:-1]
			os.system(f"bash user_remove.sh {p}")
			print("success")
		
		#----------list users---------
		elif select == '3':
			listuser()

		#----------new group-----------
		elif select == '4':
			newgroup()
			print("success")

		#----------delete group--------
		elif select == '5':
			deletegroup()
			print("success")

		#----------modify group--------
		elif select == '6':
			modifygroup()

		#----------list groups---------
		elif select == '7':
			listgroup()

		elif select == 'h' or select == 'H':
			os.system("clear")
			help()
			pass
		
		elif select == 'clear' or select == 'CLEAR':
			os.system("clear")
			help()
			pass
