#!/usr/bin/python3
#Licensed under the WTFPL
 
#Small Python script to provide me with something to read first thing in the morning at work. 
#There are much better scripts for this already, but this is fun pratice.
#DEPENDANCIES: Feedparser


#Imports things. "It's a special tool that will help us later"
#Yes I know I don't need to import everything globally but I did because it's a small script.
import sys
import feedparser
import random

#A kind greeting
def good_morning():
	print('Good morning')

#Prints the current date and time, then waits for the user to hit enter.
def date():
	import time
	now = time.strftime("%c")

	print('The current date and time: ' + now)
	input("Press Enter to continue...")


#A silly little function in which I will pull a (psudo)random number from the system, and then determine the day's fortune by how often particuliar
#numbers or letters show up. Waits for user input to continue.
def entropywisdom(): 
	number = random.randint(1,10)
	print('I have a fortune for you:  ')
	if number == 1:
        	print('"Might as well go home today."')
	if number == 2:
        	print('"Its going to be a very rough day, but it could be worse."')
	if number == 3:
        	print('"You rolled a 3, too bad your luck stat isnt higher."')
	if number == 4:
        	print('"Expect a standard day, maybe a few headaches."')
	if number == 5:
        	print('"I see in your future a truly neutral day."')
	if number == 6:
        	print('"Expect a standard day, perhaps some small plesant suprise."')
	if number == 7:
        	print('"Things are looking up, enjoy the day."')
	if number == 8:
        	print('"The tradewinds blow in your favor, a good day for taking calculated risks."')
	if number == 9:
        	print('"You must have done something good in a past life. Something lovely will occur soon."')
	if number == 10:
        	print('"You are as close to immortal today as a man can be. Go play in traffic and buy a loto ticket."')

	input("Press Enter to continue...")

#Prints the current weather, you have to feed it a workable string.
def curweath():
	weathurl = "URL" #Change this to an rss feed of your chosing

	weathfeed = feedparser.parse(weathurl)

	print('It is currently ' + weathfeed.entries[0]['title'])

	input("Press Enter to continue...")

#A script that gets the news headlines for you, and prints one of the urls from the headlines if you want it.
def getnews():
	newsurl = "https://news.google.com/news/rss/?ned=us&hl=en"

	newsfeed = feedparser.parse(newsurl)

	a = 0
	exiting = 00

	for item in newsfeed.entries:
		a = a + 1
		print(a, item.title)

	print('Would you like a link?')

	linkrequested = input('Enter Number:')

	linkint = int(linkrequested)

	if linkint == 00:
		print('No links')

	else:

		linkint0 = linkint - 1
		print(newsfeed.entries[linkint0]['link'])

#A polite end to the script
def end():
	print('Have a wonderful day')


#Begining of the actual script
good_morning()

date()

entropywisdom()

curweath()

getnews()

end()
