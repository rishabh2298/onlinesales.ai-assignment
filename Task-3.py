#-------------------------------------------------------------------------------
# Name:        Tast-3
# Purpose:     Debugging
#
# Author:      Rishabh Mishra
#
# Created:     24-05-2023
# Copyright:   (c) WIN-10 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def compute(n):

    if n < 10:
        out = n ** 2

## fault : in elif condition (=) is missing

## improvement : here value should be between 10 and 20 including it but it is
## taking from 10 to 19 according to previous code so in elif condition it should
## elif (n <= 20) to cosider value 20 in it.

    elif n <= 20:       ## improvement
        out = 1

## fault : in range()
## for test-case = 12 it will print=1 but need to print=2 as (2!) because
## the range will run(start to end-1) and because of this it will skip last
## element as for input=12 it will run from(1 to 12-10-1)

## improvement : add (+1) in range()
## the range should be increse by 1, because for both(0! of(n=10) and 1! of(n=11) is equal to 1)
## and from 12 to 20 all output get affected because of previous code so add 1 (+1) at end
## of range to reach at end

        for i in range(1, n-10+1):      ## improvement
            out *= i

    else:

## fault : wrong logic
## here logic is wrong it is doing wrong calculation and it is not close to correct answer
## for test-cas = 25 it should sum all values from 1 to (n-20) which is 5 so (1+2+3+4+5) = 15
## but previous code was doing wrong processing and calculation

## improvement : correct logical explanation
## here a loop needs to be run as upper limit is not set for range ( as case is greater than 20 only)
## so a loop from 1 till (n-20+1) needs to be run, 1 is need to be added as we are taking values
## from range to calculate the sum

        out = 0;
        for value in range(1, n-20+1):      ## improvement
            out += value;

    print(out)


n = int(input("Enter an integer: "))

compute(n);


