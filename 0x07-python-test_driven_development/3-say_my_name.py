#!usr/bin/python3
"""
function that says my name
"""

def say_my_name(first_name, last_name=""):
	"""
	function that says my name, yeah mr.white
	"""
	if type(first_name) is not str : 
		raise TypeError("first_name must be a string")
	if type(last_name) is not str :
		raise TypeError("last_name must be a string")
	try : 
		print(f"My name is {first_name} {last_name}")
	except Exception as e : 
		raise Exception(e)
