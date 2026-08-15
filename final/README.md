# Mars Base - Human Account Setup System
Name: Katherine Luciano
Class: DEV 108
Date: August 14, 2026

## Project Description:
This project is a python based account setup system that's inspired by the game Mars Base. It helps you create human accounts for a Mars colony, saves them to a CSV file, and lets you list and search for humans. You can also keep track of living pods, protect admin report with a password, delete accounts, and even add a bonus greenhouse mission.

## Admin Password:
MarsBaseAdmin4

## Files Included
1. main.py
2. final/marsbase_humans.csv
3. README.md

## Test Case 1: Create a New Human Account 
Input:
- Menu choice: 1
- First name: Proto
- Last name: Zoa
- Age: 26

Expected Result:
The program creates a new human account with an ID, email, password, pod assignment, and note. The account is also saved into the CSV file.

## Test Case 2: Search by Last Name
Input: 
- Menu choice: 3
- Last Name: Lightyear

Expected Result: 
The program finds Buzz Lightyear and displays the pod assignment and notes. 

