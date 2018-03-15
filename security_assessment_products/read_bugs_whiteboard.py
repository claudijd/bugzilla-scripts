# reading a bugs whiteboard content

#!/usr/bin/env python

import bugsy
import getpass
import re

# only for setting breakpoints for debugging
from pdb import set_trace as bp

api_key = getpass.getpass("Enter Bugzilla API Key: ")

bugzilla = bugsy.Bugsy(api_key=api_key)

bug = bugzilla.get(1446048)

raw_whiteboard = bug._bug['whiteboard']
whiteboard = dict(x.split('=') for x in raw_whiteboard.split(' '))

print("Bug " + str(bug.id) + " has the following findings")

print("MAXIMUM: " + str(whiteboard.get('MAXIMUM') or 0))
print("HIGH: " + str(whiteboard.get('HIGH') or 0))
print("MEDIUM: " + str(whiteboard.get('MEDIUM') or 0))
print("LOW: " + str(whiteboard.get('LOW') or 0))