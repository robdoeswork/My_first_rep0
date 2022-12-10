#!/usr/bin/env python3
import scapy.all as scapy
from scapy.all import *
from scapy.layers.l2 import Ether, ARP


def scan(ip):
    arp_request = scapy.layers.l2.ARP(pdst=ip)
    broadcast = scapy.layers.l2.Ether(dst="ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    scapy.srp(arp_request_broadcast)


scan("10.0.2.1/24")
