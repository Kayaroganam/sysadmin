import os

def TITLE():
	print(" -------------------")
	print("| S Y S   A D M I N |")
	print(" -------------------")
	print("")
	pass

def HELP():
	print(" ----------------------------")
	print("| [0] EXIT                   |")
	print("| [1] USER GROUP MANAGEMENT  |")
	print("| [2] DATE AND TIME          |")
	print("| [3] NETWORK MANAGER        |")
	print(" ----------------------------")
	pass



if __name__ == '__main__':
	TITLE()
	HELP()

	loop = True

	while loop:
		select = input("SYSADMIN >> ")

		if select == '0':
			loop = False
			print("-----BYE-----")
			pass

		elif select == '1':
			os.system("python3 usergroupmanagement.py")
			os.system("clear")
			pass

		elif select == '2':
			os.system("python3 dateandtime.py")
			os.system("clear")
			pass
		
		elif select == '3':
			os.system("sudo nmtui")
			pass

		elif select == 'clear' or select == 'CLEAR':
			os.system("clear")
			pass

		elif select == 'h' :
			HELP()
		pass
	
