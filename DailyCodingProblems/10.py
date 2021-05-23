'''
This problem was asked by Apple.
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

from time import sleep

def f():
    print("Function f() called after given time!")

def job_scheduler(func, n: int):
    time = n/1000
    sleep(time)
    func()


job_scheduler(f, 1000)