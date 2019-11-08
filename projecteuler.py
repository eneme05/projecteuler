# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:14:08 2019

@author: enikko
"""
import math

def mulThreeFive(n):
    total=0

    for i in range(1,1000):
        if (i%3 == 0 or i%5 == 0):
            total += i
    return total

def evenFibonacci(limit):
    ef0=0
    ef1=2
    
    if limit < 2:
        return 0
    
    sum = ef0+ef1
    while ef1 <= limit:
        ef2 = 4*ef1 + ef0
        if ef2 > limit:
            break
        sum += ef2
        ef0=ef1
        ef1=ef2
    
    return sum

def fiboSeries(n):
    #1,1,2,3,5,8,13
    if n < 0:
        return None
    if n in range(3):
        return 1
    else:
        return fiboSeries(n-2)+fiboSeries(n-1)
        
def factorize(n):
    factors = []
    while n%2 == 0:
        n=n/2
        factors.append(2)
        
    for i in range(3,int(math.sqrt(n)+1)):
        while n%i == 0:
            n = n/i
            factors.append(i)
    if n>2:
        factors.append(n)
    
    return factors

def isPalindrome(n): 
    reverse = 0
    number = n
    while n != 0:
        reverse = reverse*10 + n%10
        n = n//10
    if reverse == number:
        return True
    else:
        return False
    
def largestPalindrome(n):
    max_product = 0
    upper_limit = (10**n)-1
    lower_limit = 10**(n-1)
    
    for i in range(upper_limit,lower_limit-1,-1):
        for j in range(i,lower_limit-1,-1):
            product = i*j
            if product < max_product:
                break
            
            if isPalindrome(product) and product > max_product:
                max_product = product
    return max_product

def getListPrimeNum(n):
    primes_dict = {x:True for x in range(2,n+1)}
    list_primes = []
    for i in range(2,n+1):
        if primes_dict[i]:
            for j in range(i**2,n+1,i):
                primes_dict[j] = False
        if primes_dict[i]:
            list_primes.append(i)
    return list_primes

def smallestMultiple(n):
    smallestMultiple = 1
    list_primes = getListPrimeNum(n)
    for i in range(len(list_primes)):
        j = 1
        while list_primes[i]**j <= n:
            j+=1
            smallestMultiple = smallestMultiple*list_primes[i]
    return smallestMultiple

def diffSumSqSquSum(n):
    square_of_sum_of_numbers = (sum([x for x in range(1,n+1)]))**2
    sum_of_squares_of_numbers = sum([x**2 for x in range(1,n+1)])
    
    return square_of_sum_of_numbers - sum_of_squares_of_numbers

def getNthPrime(n):
    list_primes = getListPrimeNum(10**6)
    nth_prime = 1
    
    if (n <= len(list_primes)):
        nth_prime = list_primes[n-1]
    return nth_prime


