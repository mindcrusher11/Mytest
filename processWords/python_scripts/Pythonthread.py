from thread import start_new_thread

def square_thread(a):
	print("calculate the square root of a" ,a)
	

start_new_thread(square_thread,(99,))
start_new_thread(square_thread,(999,))
start_new_thread(square_thread,(16,))
start_new_thread(square_thread,(81,))

c = raw_input("Type something to quit")
