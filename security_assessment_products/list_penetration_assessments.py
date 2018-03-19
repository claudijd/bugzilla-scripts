#!/usr/bin/env python

import bugsy
import sys
import getpass

# only for setting breakpoints for debugging
# from pdb import set_trace as bp

api_key = getpass.getpass("Enter Bugzilla API Key: ")

bugzilla = bugsy.Bugsy(api_key=api_key)
bugs = bugzilla.search_for\
        .product('Enterprise Information Security')\
        .component('Penetration Test')\
        .search()

for bug in bugs:
	if bug.status == "RESOLVED" and bug.resolution == "FIXED":
		print("[" + bug.status + "] " + str(bug.id) + " " + bug.summary)