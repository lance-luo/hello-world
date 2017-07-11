#/usr/bin/env python
"""This module provides functions for authenticating users."""

import os
import sys

def main(argv):
    # My code here
	status = os.popen('service jenkins status|grep "Active"').readline()
	print status
	if status.find('dead') != -1:
	    print 'Jenkins is dead, needs to be restarted...'

if __name__ == "__main__":
    main(sys.argv)
