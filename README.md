Braille Translation
===================

Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2x3 grid, where each dot can either be a bump or be flat (no bump). The special printer which can print the bumps onto the signs expects the dots in the following order:

1 4

2 5

3 6

So given the plain text word "code", you get the Braille dots:

c  o  d  e
===================
11 10 11 10

00 01 01 01

00 10 00 00


where 1 represents a bump and 0 represents no bump. Put together, "code" becomes the output string "100100101010100110100010".

Write a function solution(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. String inputs are less than fifty characters long and use only letters and spaces.
