#!/usr/bin/python
# check if a linux system running on a virtual machine (openvz/xen pv/uml VmWare)

import sys, os

def main():
    if os.getuid() != 0:
        print "must be run as root"
        sys.exit(0)

    # check OpenVZ/Virtuozzo
    if os.path.exists("/proc/vz"):
        if not os.path.exists("/proc/bc"):
            print "openvz container"
        else:
            print "openvz node"

    # check Xen
    if os.path.exists("/proc/xen/capabilities"):
        if (os.path.getsize("/proc/xen/capabilities") > 0):
            print "xen dom0"
        else:
            print "xen domU"

    # check User Mode Linux (UML)
    f = open("/proc/cpuinfo", "r"); t = f.read(); f.close()
    if (t.find("UML") > 0):
        print "uml"

    # check VMWare
    f = open("/proc/scsi/scsi", "r"); t = f.read(); f.close()
    if (t.find("VMware") > 0):
        print "VMware"

if __name__=="__main__":
    main()
