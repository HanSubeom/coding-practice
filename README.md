# Memo App

## Introduction
A simple CLI program that lets you add and view memos from the terminal.

## Concepts Used
- input/print
- if/elif/else
- while loop
- functions (def, return)
- file read/write (open, .write, .readlines)
- enumerate() and list indexing

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
    1. Add memo  2. Show memos  3. Exit  4. Delete memo
    Choose: 4
    --- Your Memos ---
    1: Buy milk!
    2: Buy juice!
    Enter the number to delete: 1
    Memo deleted!

## Test Cases
1. Normal case, e.g. Add a memo and confirm it appears in the list
2. Invalid input case, e.g. Entering 4 or a letter shows "Invalid choice."
3. Exit case, e.g. Entering 3 shows "Goodbye!" and the program ends
4. Delete case, e.g. Choosing 4 and entering a valid number removes that memo from the list

## What I Learned
The trickiest part was understanding why indentation matters so much — a while loop can look correct but still run forever if a variable isn't updated in the right place. I also learned the difference between return and print(), since print() only shows a value while return lets you actually use it later.
I also learned the difference between 0-based list indexing and 1-based numbers shown to the user, and why "w" mode is needed instead of "a" when rewriting a file after deletion.