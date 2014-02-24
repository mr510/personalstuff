#!/usr/bin/python
import argparse
print "This script should show number of locked tables on a mysql server."

## argpass
parser = argparse.ArgumentParser(description='Check locked tables on mysql database')
parser.add_argument('-i','--ip', help='Host ip of mysql server', required=True)
parser.add_argument('-u','--user', help='mysql user', required=True)
parser.add_argument('-p','--password', help='mysql user password', required=True)
parser.add_argument('-d','--databasename', help='Database name ')
args = parser.parse_args()
print args.ip
print args.user
print args.password
print args.databasename


## get data
## process



