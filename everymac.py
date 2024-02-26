import subprocess
import re
import termcolor
import optparse
import time


class Main:
    def __init__(self):
        print(termcolor.colored("Warning You have to be ROOT!",color="red"))
        print(termcolor.colored("if you dont be root program not working!!!\n",attrs=["underline"]))
        time.sleep(5)
        self.banner()
        #required user arguments
        parser = optparse.OptionParser()
        parser.add_option("-m","--mac",dest="mac",action="store",help="usage => python everymac.py -m <your mac address> -i <your network interface>")
        parser.add_option("-i","--interface",dest="network_interface",action="store",help="usage => python everymac.py -m <your mac address> -i <your network interface>")

        #received arguments from user

        (parsed_arguments,arguments) = parser.parse_args()
        self.requesting_mac = parsed_arguments.mac
        self.receive_interface = parsed_arguments.network_interface

        check_mac = subprocess.check_output(["ifconfig",self.receive_interface],text=True)
        check = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",check_mac)
        self.checking(check)
        

    def executing(self,mac,interface):
        #EXE
        print(mac)
        print(interface)
        print(termcolor.colored("[*]Executing Everymac",color="blue"))
        time.sleep(1)
        subprocess.call(["ifconfig",interface,"down"])
        time.sleep(1)
        print(termcolor.colored("[**]Executing Everymac",color="blue"))
        time.sleep(1)
        subprocess.call(["ifconfig",interface,"hw","ether",mac])
        time.sleep(1)
        print(termcolor.colored("[***]Executing Everymac",color="blue"))
        subprocess.call(["ifconfig",interface,"up"])
        time.sleep(1)
        print(termcolor.colored("[+]Successfully",on_color="on_green"))
        print("new mac => "+ mac)

    def checking(self,new_mac):
        
        if new_mac.group(0) == self.requesting_mac:
            
            print(termcolor.colored("YOU HAVE ALREADY USİNG SAME MAC",on_color="on_red"))
            print("=> " + new_mac.group(0))
            
            if new_mac:
                print("ERROR\nYour mac address arguments Turned None")
            else:
                self.executing(self.requesting_mac,self.receive_interface)
            
        else:
            self.executing(self.requesting_mac,self.receive_interface)

    def banner(self):
        print( """
              
 ██████████ █████   ███████████████ ███████████  █████ ███████████   ██████  █████████    █████████ 
░░███░░░░░█░░███   ░░███░░███░░░░░█░░███░░░░░███░░███ ░░███░░██████ ██████  ███░░░░░███  ███░░░░░███
 ░███  █ ░  ░███    ░███ ░███  █ ░  ░███    ░███ ░░███ ███  ░███░█████░███ ░███    ░███ ███     ░░░ 
 ░██████    ░███    ░███ ░██████    ░██████████   ░░█████   ░███░░███ ░███ ░███████████░███         
 ░███░░█    ░░███   ███  ░███░░█    ░███░░░░░███   ░░███    ░███ ░░░  ░███ ░███░░░░░███░███         
 ░███ ░   █  ░░░█████░   ░███ ░   █ ░███    ░███    ░███    ░███      ░███ ░███    ░███░░███     ███
 ██████████    ░░███     ██████████ █████   █████   █████   █████     ██████████   █████░░█████████ 
░░░░░░░░░░      ░░░     ░░░░░░░░░░ ░░░░░   ░░░░░   ░░░░░   ░░░░░     ░░░░░░░░░░   ░░░░░  ░░░░░░░░░  
                                                                                                                                                                                                        
""")
        print("Developed by Egemen © 2023")

try:
    main = Main()
except KeyboardInterrupt:
    print("\nsee you later :)")