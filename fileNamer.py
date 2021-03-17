import random

def file_namer(name_size : int) -> str:
	template = ""
	for i in range(0,name_size):
		template = f"{random.randint(0,9)}" + template
	
	return template