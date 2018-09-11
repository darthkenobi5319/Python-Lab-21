# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:44:37 2017

@author: ZHENGHAN ZHANG
"""

import mysql.connector as db

cxn = db.connect(host = '10.224.45.113',
                 user = 'cs101',
                 db = 'twitter',
                 autocommit = True)
cursor = cxn.cursor(dictionary = True)


sql = 'select * from tweet'
cursor.execute(sql)
for i in cursor:
    print(i) 
username = input('Please enter your user name:')
while True:
       
    print('1.Tweet!')
    print('2.Show Tweets')
    print('3.Show Users')
    print('4.Show Tweets from user')
    print('5.Like')
    print('6.Quit')
    choice = input('Please enter your opition:')    
    if choice == '6':
        break
    elif choice == '1':
        usertweet = input('Please enter your tweet:')
        sql = "insert into tweet (user, message) values ('" + username + "', '" + usertweet + "')"
        cursor.execute(sql)
    elif choice == '2':
        sql = "select user, message from tweet order by tstamp desc limit 10"
        cursor.execute(sql)
        for i in cursor:
            print(i)
    elif choice == '3':
        sql = "select distinct user from tweet order by user"
        cursor.execute(sql)
        for i in cursor:
            print(i)
    elif choice == '4':
        usernameget = input('Please enter a user name:')
        sql = "select * from tweet where user = '" + usernameget + "'"
        cursor.execute(sql)
        for i in cursor:
            print(i)
    elif choice == '5':
        liked = input('Please enter the tweet id:')
        sql = "update tweet set likes = likes + 1 where id = '" + liked + "'"
        cursor.execute(sql)
        sql = "select * from tweet where id = '" + liked + "'"
        cursor.execute(sql)
        for i in cursor:
            print(i)
        
cursor.close()
cxn.close()