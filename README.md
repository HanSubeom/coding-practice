# Memo App

## Introduction
A simple CLI program that lets you add and view memos from the terminal

## Concepts Used
- input/print
- if/elif/else
- while loop
- functions (def, return)
- file read/write (open, .write, .readlines)

## How to Run

\`\`\`bash
python3 memo_app.py
\`\`\`

## Example Usage

\`\`\`text
![alt text](<스크린샷 2026-09-10 오전 12.04.18.png>)
\`\`\`

## Test Cases
1. Normal case, e.g. Add a memo and confirm it appears in the list
2. Invalid input case, e.g. Entering 4 or a letter shows "Invalid choice."
3. Exit case, e.g. Entering 3 shows "Goodbye!" and the program ends

## What I Learned
The trickiest part was understanding why indentation matters so much — a while loop can look correct but still run forever if a variable isn't updated in the right place. I also learned the difference between return and print(), since print() only shows a value while return lets you actually use it later