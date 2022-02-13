#Firewalld
import os
 
def firewall_help():
    print(" -------------------------------------")
    print("| [0] EXIT                            |") 
    print("| [1] ADD PORT                        |") 
    print("| [2] REMOVE PORT                     |")
    print("| [3] ADD SERVICE                     |") 
    print("| [4] REMOVE SERVICE                  |")
    print("| [5] LIST ENABLED PORTS AND SERCICES |")
    print("| [6][h] HELP                         |")
    print(" -------------------------------------")

if __name__ == '__main__':
    firewall_help()
    loop = True

    while loop:
        select = input("SYSADMIN > firewalld >> ")

        if select == '0':
            #exit
            loop = False
            pass

        elif select == '1':
            #add port
            port_no = input("SYSADMIN > firewalld > enter port >> ")
            os.system(f"sudo firewall-cmd --permanent --add-port={port_no} > /bin/null")
            os.system("sudo firewall-cmd --reload")
            pass

        elif select == '2':
            #remove port
            port_no = input("SYSADMIN > firewalld > enter port >> ")
            os.system(f"sudo firewall-cmd --permanent --remove-port={port_no} /bin/null")
            os.system("sudo firewall-cmd --reload")
            pass

        elif select == '3':
            #add service
            service_name = input("SYSADMIN > firewalld > enter service name >> ")
            os.system(f"sudo firewall-cmd --permanent --add-service={service_name} > /bin/null")
            os.system("sudo firewall-cmd --reload")
            pass

        elif select == '4':
            #remove service
            service_name = input("SYSADMIN > firewalld > enter service name >> ")
            os.system(f"sudo firewall-cmd --permanent --remove-service={service_name} > /bin/null")
            os.system("sudo firewall-cmd --reload")
            pass

        elif select == '5':
            #list service and ports
            print("Enabled Ports:")
            print("-------------")
            os.system("sudo firewall-cmd --list-ports")

            print("Enabled Services:")
            print("----------------")
            os.system("sudo firewall-cmd --list-services\n")
            pass

        elif select == '6' or select == 'h' or select == 'H' or select =='help':
            os.system("clear")
            firewall_help()
            pass
