
   
# Rodrigo Alcover
# Program GUI 4/7/2022
# CIS 226-23199 Advanced Python Programming   
    
    
"""
-Threading


Its described as an entity within a process. Called “lightweight process” one process can contain many threads. 

Threaded code work in a way where the code run organized in modules or subroutines. 

This programming technique is used in compilers to generate code with that characteristic, or in programs already created in that threaded organization style. 

All threads share the same memory, so it is lightweight. Also, processes are great for I/O tasks, 
for example at the time the program needs to send or receive data to a slow network threading can use 
the time of wait to switch to other threads and do the processing.

Cons are that threads are limited to one thread at a time and are not interruptible. 
Must be careful with race conditions; for example, if several threads try to modify the same variable at the same time, it can cause crashes. 

Most if not all older applications are single thread because computers had only one CPU; an example of a single thread is the audio encoder LAME.

-Multiprocess


Multiprocessing is a Python package distributed in the standard library since Python 2.6. 
Multithreading runs subroutines of code and Multiprocessing runs processes. 

The processing style is slower than treads, but it is more compatible with python. 
Multiprocessing takes advantage of multiple CPUs and cores and new processes are started independently from other processes.

One example of multiprocessing is at the time of writing on a hard disk or USB drive, 
the process won’t take much time but the writing process is made in parallel to save time. 

-Async / Await


Async is asynchronous code. Is similar to threads that run code in parallel. Async runs coroutines and coroutines work as cooperative. 
Coroutines Await for one to finish to the other start. 
A pro of the async/await is that asynchronous code can be written easier and will look like synchronous blocking code.
Synchronous-looking code which is easier to read and understand

The only problem I found researching about Async/await is that this code won’t run in old environments/browsers.

An example is that while using the async keyword before a function, you can then use await in the function. 
So to await the promise, the function waits until the promise is processed and when the promise is complete the value is given.

"""
