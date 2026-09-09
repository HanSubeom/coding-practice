# Memo App

## Introduction
A simple CLI program that lets you add and view memos from the terminal.

## Concepts Used
- input/print
- if/elif/else
- while loop
- functions (def, return)
- file read/write (open, .write, .readlines)

## How to Run

    python3 memo_app.py

## Example Usage

    1. Add memo  2. Show memos  3. Exit
    Choose: 1
    Enter your memo: Buy milk
    Memo saved!
    1. Add memo  2. Show memos  3. Exit
    Choose: 2
    Buy milk
    1. Add memo  2. Show memos  3. Exit
    Choose: 3
    Goodbye!

## Test Cases
1. Normal case, e.g. Add a memo and confirm it appears in the list
2. Invalid input case, e.g. Entering 4 or a letter shows "Invalid choice."
3. Exit case, e.g. Entering 3 shows "Goodbye!" and the program ends

## What I Learned
The trickiest part was understanding why indentation matters so much — a while loop can look correct but still run forever if a variable isn't updated in the right place. I also learned the difference between return and print(), since print() only shows a value while return lets you actually use it later.