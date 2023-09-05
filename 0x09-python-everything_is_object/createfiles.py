#!/usr/bin/python3

i = 0
while i <= 28 :
	file = open(f"{i}-answer.txt", "w")
	file.write("essai")
	file.close()
	i += 1
