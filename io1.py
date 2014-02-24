#!/usr/bin/python

# take user input
user = raw_input (" Enter user :" )
print ( "you entered user :"+ user )

password = raw_input (" Enter your password :")
print ( "you entered password :"+ password )

url_path = raw_input ( " Enter full url :")
print ( "you entered url : "+ url_path)

# open file
fo = open('key.txt', 'r+')
# print file info
print " Name : ", fo.name
print "closed or not" , fo.close
print " Mode opened : ", fo.mode
print " Softspace flag :", fo.softspace

# read encrypted file later change this to use some backend db
astr = fo.read();
print "read str is : ", astr
print astr
fo.close()

# write encrypted  file later store this info in db
fo = open('key.txt', 'a+')
fo.write(user + '\n')
fo.write(password + '\n')
fo.close()
