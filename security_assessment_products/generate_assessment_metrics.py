#!/usr/bin/env python
import bugsy
import getpass
import json

api_key = getpass.getpass("Enter Bugzilla API Key: ")
bugzilla = bugsy.Bugsy(api_key=api_key)

# Get Vulnerability Assessment Metrics Data
va_bugs = bugzilla.search_for\
    .product('Enterprise Information Security')\
    .component('Vulnerability Assessment')\
    .search()

va_metrics = []

for bug in va_bugs:
    raw_whiteboard = bug._bug['whiteboard']

    if raw_whiteboard:
        whiteboard = dict(x.split('=') for x in raw_whiteboard.split(' '))
    else:
        whiteboard = ""

    va_metrics.append(
        {'id': bug.id, 'summary': bug.summary, 'status': bug.status, 'resolution': bug.resolution, 'whiteboard': whiteboard})

# Get Pentest Assessment Metrics Data
pt_bugs = bugzilla.search_for\
    .product('Enterprise Information Security')\
    .component('Penetration Test')\
    .search()

pt_metrics = []

for bug in pt_bugs:
    raw_whiteboard = bug._bug['whiteboard']

    if raw_whiteboard:
        whiteboard = dict(x.split('=') for x in raw_whiteboard.split(' '))
    else:
        whiteboard = ""

    pt_metrics.append(
        {'id': bug.id, 'summary': bug.summary, 'status': bug.status, 'resolution': bug.resolution, 'whiteboard': whiteboard})

assessment_metrics = {
    'vulnerability assessment': va_metrics,
    'penetration assessment': pt_metrics
}

print("")
print("#### Vulnerability Assessment Service Metrics ####")
print("")

print("# Since service was created...")

# How many vulnerability assessments have we done?
print("- {} vulnerability assessments were requested.".format(len(va_metrics)))

# How many vulnerability assessment have we completed?
completed_vas = 0

for bug in va_metrics:
    if bug['status'] == "RESOLVED" and not bug['resolution'] == "INVALID":
        completed_vas += 1

print("- {} vulnerability assessments were completed.".format(completed_vas))

# How many vulnerability assessments are invalid?
invalid_vas = 0

for bug in va_metrics:
    if bug['status'] == "RESOLVED" and bug['resolution'] == "INVALID":
        invalid_vas += 1

print("- {} vulnerability assessments were invalid.".format(invalid_vas))

# How many vulnerability assessments have are in progress?
inprogress_vas = 0

for bug in va_metrics:
    if bug['status'] == "NEW" or bug['status'] == "ASSIGNED":
        inprogress_vas += 1

print("- {} vulnerability assessments are in progress.".format(inprogress_vas))

print("")
print("# In the last 30 days...")

# Get Vulnerability Assessment Metrics Data
va_bugs_30 = bugzilla.search_for\
    .product('Enterprise Information Security')\
    .component('Vulnerability Assessment')\
    .timeframe('2018-12-09', '2019-01-09')\
    .search()

va_metrics_30 = []

for bug in va_bugs_30:
    raw_whiteboard = bug._bug['whiteboard']

    if raw_whiteboard:
        whiteboard = dict(x.split('=') for x in raw_whiteboard.split(' '))
    else:
        whiteboard = ""

    va_metrics_30.append(
        {'id': bug.id, 'summary': bug.summary, 'status': bug.status, 'resolution': bug.resolution, 'whiteboard': whiteboard})

# Get Pentest Assessment Metrics Data
pt_bugs_30 = bugzilla.search_for\
    .product('Enterprise Information Security')\
    .component('Penetration Test')\
    .timeframe('2018-12-09', '2019-01-09')\
    .search()

pt_metrics_30 = []

for bug in pt_bugs_30:
    raw_whiteboard = bug._bug['whiteboard']

    if raw_whiteboard:
        whiteboard = dict(x.split('=') for x in raw_whiteboard.split(' '))
    else:
        whiteboard = ""

    pt_metrics_30.append(
        {'id': bug.id, 'summary': bug.summary, 'status': bug.status, 'resolution': bug.resolution, 'whiteboard': whiteboard})

assessment_metrics_30 = {
    'vulnerability assessment': va_metrics_30,
    'penetration assessment': pt_metrics_30
}

# How many vulnerability assessments have we done?
print("- {} vulnerability assessments were requested.".format(len(va_metrics_30)))

# How many vulnerability assessment have we completed?
completed_vas_30 = 0

for bug in va_metrics_30:
    if bug['status'] == "RESOLVED" and not bug['resolution'] == "INVALID":
        completed_vas_30 += 1

print("- {} vulnerability assessments were completed.".format(completed_vas_30))

# How many vulnerability assessments are invalid?
invalid_vas_30 = 0

for bug in va_metrics_30:
    if bug['status'] == "RESOLVED" and bug['resolution'] == "INVALID":
        invalid_vas_30 += 1

print("- {} vulnerability assessments were invalid.".format(invalid_vas_30))

# How many vulnerability assessments have are in progress?
inprogress_vas_30 = 0

for bug in va_metrics_30:
    if bug['status'] == "NEW" or bug['status'] == "ASSIGNED":
        inprogress_vas_30 += 1

print("- {} vulnerability assessments are in progress.".format(inprogress_vas_30))


# ADD NEW THING WE WANT TO LEARN ABOUT FROM OUR METRICS
