#date and time
import os

#<------------------------title----------------------------------------------------------->
def title():
	print(" -------------------------------------------")
	print("| D A T E   A N D   T I M E   S E T T I N G |")
	print(" -------------------------------------------")
	pass
#<------------------------date and time help----------------------------------------------------------->

def date_time_help():
	print(" ------------------------------------")
	print("| [0] EXIT                           |")
	print("| [1] CHANGE DATE and TIME MANUALLY  |")
	print("| [2] CHANGE TIME ZONE               |")
	print("| [3][h] HELP                        |")
	print(" ------------------------------------")
	pass

#<------------------------change date and time----------------------------------------------------------->
def change_date_and_time():

	#change date
	date = input("date time > enter date[DD.MM.YYYY] >> ")
	date = list(date.split("."))
	cmd = ''
	os.system(f'sudo date +\%Y\%m\%d -s "{date[-1]}{date[-2]}{date[-3]}" > null')

	#change time
	time = input("date time > enter time[HH:MM] >> ")
	os.system(f'sudo date +%R -s "{time}" > null')

	#succes message
	print("success")
	pass

def change_zone():
	os.system("cat /etc/sysadmin/dateandtime/zonelist_with_serialno")
	select_zone =input("date time > change time zone[select zone] >> ")

	os.system(f"sudo sed -n '{select_zone}p' /etc/sysadmin/dateandtime/zonelist_without_serialno > /tmp/timezone.temp")
	
	file1 = open("/tmp/timezone.temp","r")
	selected_zone = file1.read()
	file1.close()

	selected_zone = selected_zone[0:-1]

	os.system("sudo rm -rf /etc/localtime")
	os.system(f"sudo cp /usr/share/zoneinfo/Asia/{selected_zone} /etc/localtime")

	print("success")

	pass


if __name__ == '__main__':

	title()
	print("")
	date_time_help()

	loop = True

	while loop:
		select = input("SYSADMIN > date time >> ")

		if select == '0':
			loop = False
			print("exit")
			pass

		elif select == '1':
			change_date_and_time()
			pass

		elif select == '2':
			change_zone()
			pass

		elif select == '3' or select == 'H' or select == 'h':
			date_time_help()
			pass

		elif select == 'clear' or select == 'CLEAR':
			os.system("clear")
			pass

		pass
