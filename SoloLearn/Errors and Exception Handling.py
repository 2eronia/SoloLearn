'''
try:
	induce_an_error = 1 + "a"
except TypeError:
	print("There was a type error")
except:
	print('All other excrptions')
finally:
	print('I always run')

'''

def ask_for_ini():
	while True:
		try:
			result = int(input("Please enter a num: "))
		except:
			print("Whoops! That's no a number")
			continue
		else:
			print("Thanks")
			break
		finally:
			print('End of try/except/finally')
			print("I'll always run at the end")

ask_for_ini()