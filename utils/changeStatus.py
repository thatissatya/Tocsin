# Script for controlling the system
import os
from subprocess import check_call


def hybernation():
    os.system("systemctl hibernate")

def shut_down():
    os.system('systemctl poweroff')

def suspend():
    os.system("systemctl suspend")

def hybernation_and_suspend():
    os.system("systemctl hybrid-sleep")


# System Commands:  for Linux 
#   is-system-running                   Check whether system is fully running
#   default                             Enter system default mode
#   rescue                              Enter system rescue mode
#   emergency                           Enter system emergency mode
#   halt                                Shut down and halt the system
#   poweroff                            Shut down and power-off the system
#   reboot [ARG]                        Shut down and reboot the system
#   kexec                               Shut down and reboot the system with kexec
#   exit [EXIT_CODE]                    Request user instance or container exit
#   switch-root ROOT [INIT]             Change to a different root file system
#   suspend                             Suspend the system
#   hibernate                           Hibernate the system
#   hybrid-sleep                        Hibernate and suspend the system
#   suspend-then-hibernate              Suspend the system, wake after a period of
#                                       time, and hibernate
