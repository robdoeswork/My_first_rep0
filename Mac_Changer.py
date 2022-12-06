#!/usr/bin/env python3

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        #handle error
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        #handle error
        parser.error("[-] Please specify a new MAC, use --help for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + ' to ' + new_mac)
    subprocess.call('sudo ifconfig ' + interface + ' down', shell=True)
    subprocess.call('sudo ifconfig ' + interface + ' hw ether ' + new_mac, shell=True)
    subprocess.call('sudo ifconfig ' + interface + ' up', shell=True)


def check_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface], encoding='utf-8')
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("Could not read MAC")


options = get_arguments()
current_mac = check_mac_address(options.interface)
print("Current MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = check_mac_address(options.interface)
if current_mac== options.new_mac:
    print("MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not change")





