#/usr/bin/env python
"""This module provides functions for authenticating users."""

import os
import sys

def main(argv):
    # My code here
	status = os.popen('service jenkins status|grep "Active"').readline()
	print status

if __name__ == "__main__":
    main(sys.argv)
