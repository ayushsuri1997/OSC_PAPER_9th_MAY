import multiprocessing
import time


manager = multiprocessing.Manager()
final_list = manager.list()

def add():
	import tkinter
	top= tkinter.Tk()
	def cbp():
		print("caught a close click")
		for i in range(0,len(final_list)):
			final_list.pop()
		#final_list.clear()
		final_list.append(1)
	def obp():
		print("caught an open click")
		for i in range(0,len(final_list)):
			final_list.pop()
		#final_list.clear()
		final_list.append(2)
		for i in range(0,len(final_list)):
			print(final_list[i])
	c=tkinter.Button(top,text="Close graph",command=cbp)
	c.pack()
	o=tkinter.Button(top,text="open graph",command=obp)
	o.pack()
	top.mainloop()

def sud():
	import random
	import myModule
	from oscilloscope import Osc
	osc = Osc(fps=5)
	flag=0
	@osc.signal
	def increasing_signal(state):
		delta = 1
		s=1
		while s <= 1:
			state.draw(random.randint(-delta, delta))
			delta += 5
			myModule.fib(10)
			if(final_list[-1]==1):
				flag=0
				for i in range(0,len(final_list)):
					final_list.pop()
				s+=1

	while(True):
		print("Entered")
		if(len(final_list)>0):
			if(flag==0 and len(final_list)>0):
				if(final_list[-1]==2):
					osc.start()
					flag=1
					for i in range(0,len(final_list)):
						final_list.pop()

if __name__ =='__main__':
	p1 = multiprocessing.Process(name='p1',target=add)
	p2 = multiprocessing.Process(name='p1',target=sud)
	p1.start()
	p2.start()
	p1.join()
	p2.join()