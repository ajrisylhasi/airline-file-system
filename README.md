# airline-file-system

Elte Entrance Examination

Given a file containing daily air traffic data of Budapest airport. The file aims to store information about every outbound flight from Budapest. Each line of the file contains two strings and an integer number, separated by whitespaces:
- name of the airline that operates the given flight
- destination of the flight
- number of passengers transported by the flight
The airline and the destination (name of a city) do not contain space character. The file is sorted by airline in ascending alphabetical order.
For example, the lines of the given file can be as follows:

Alitalia Rome 180
Alitalia Pisa 82
Germanwings Munich 96
Germanwings Frankfurt 163
NorwegianAir Bergen 202
Wizzair London 184
Wizzair Frankfurt 83
Wizzair Lisbon 198

Your program must be read the data from the standard input or from an input file called input.txt

The output of the program should be written to the standard output. There are 4 exercises you are expected to solve. The output should contain exactly 4 lines: the ith line in the output is the solution to exercise i.

--------------------------------------------------------------------------------
Exercises
Exercise 1:

How many flights are there to "Frankfurt"?
Exercise 2:

Which flight has the most passengers?
Exercise 3:

Find the first flight with passengers less than 100.
Exercise 4:

Name the airline with the most total number of passengers. Print out the total number of passengers carried by the airline as well.

--------------------------------------------------------------------------------
Examples

We provide three simple examples to clarify the exercises and the format of the expected output. Test your solution with other, larger examples as well!
---------- Example 1

Sample input:

Alitalia  Rome	180
Alitalia  Pisa 82
Germanwings Munich   96
Germanwings  Frankfurt 163
NorwegianAir  Bergen  202
Wizzair London 184
Wizzair Frankfurt 83
Wizzair Lisbon 198

Sample output:

2
NorwegianAir Bergen 202
Alitalia Pisa 82
Wizzair 465

---------- Example 2

Sample input:

Alitalia  Rome	180
Wizzair	  Cracow	100
Wizzair Barcelona 150

Sample output:

0
Alitalia Rome 180
There is no flight with passengers less than 100.
Wizzair 250

---------- Example 3

Sample input:

 

Sample output:

0
The file is empty!
There is no flight with passengers less than 100.
The file is empty!
