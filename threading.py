import os
import time
import threading as th

def job1(q, l):
	l.acquire()
	q.put("some info")
	l.release()
	print("job1 PID ", os.getpid())
	time.sleep(5)


def job2(q, l):
	l.acquire()
	q.put("new info")
	l.release()

	print("job2 PID ", os.getpid())
	time.sleep(6)

if __name__ == "__main__":
	
	q = mp.Queue()
	l = mp.Lock()

	print ("Main PID = " , os.getpid())
	start = time.time()
	p1.start() = mp.Process(target=job1, args=(q,l))
	p2 = mp.Process(target=job2, args=(q,l))
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	end = time.time()

	print ("m1= ", q)
	print ("m2= ", q)
	print("total time taken =", end-start)
print("End of the program")