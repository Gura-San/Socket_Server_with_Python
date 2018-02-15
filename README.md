## Why did you choose this subject?
The subject was chosen because couple of reasons:
1. Python simplicity
2. Excessive documentation on the matter
3. Overall market popularity and relevance
4. Lightweight small memory footprint

## How were you first made aware of it?


## What problem does it solve?
The server excepts HTTP requests and is easily scalable to serve all types of requests

## How does it solve the problem (conceptually)?
The process is straightforward:
1. Python socket library is utilized
2. Specific port is being scanned for all types of HTTP requests
3. Whenever request is spotted server generates a response

## Why does one use it?
The general use-case is back-end development.
Almost any back-end API can be created with this basic setup

## What are the alternatives?
Express, Rails, Django

## What is it similar to, if anything?
The basic concept is the same - 
listen on given port for requests and provide s response

## What is the history of this technology?
A network socket is an internal endpoint for sending or receiving data at a single node in a computer network. 
Concretely, it is a representation of this endpoint in networking software (protocol stack), 
such as an entry in a table (listing communication protocol, destination, status, etc.), and is a form of system resource.
The term socket dates to RFC 147 (1971), where it was used in ARPANET. 
Today most implementations of sockets are based on Berkeley sockets (1983)

## Who built it and why?
Berkeley sockets originated with the 4.2BSD Unix operating system (released in 1983) as a programming interface. 
All modern operating systems implement a version of the Berkeley or POSIX socket interface. It became the standard interface for connecting to the Internet. 

##Who is maintaining it?
in 1989 UC Berkeley release versions of its operating system and networking socket library free from the licensing constraints.

##What is your opinion on the technology after having built something with it?
As a person who enjoins working with APIs and Server-side I find python a robust tool
for server-side work  

## What are the biggest conceptual hurdles (if any) you encountered when researching this?
the socket library itself

## What resources do you recommend for interested students?
https://docs.python.org/2/howto/sockets.html
http://www.binarytides.com/python-socket-programming-tutorial/


## To launch the server
1. Clone the repo
2. Navigate to source folder
3. Inside the console type: python webserver1.py
4. Make a request either with browser or any other packet handler on localhost:8000/request

