## Objective: Fix the existing code and make it function properly.

* Expected behavior: When the user runs the program, it will show the prompt `Enter ISBN and length: `. The user can enter the ISBN code they want to validate in `ISBN,length` format. The ISBN code should not contain hyphens, followed by its length (`10` or `13`), separated by a comma.
* Example inputs: `1530051126,10` for ISBN-10 codes. `9781530051120,13` for ISBN-13 codes.

# User Stories:

1. You should fix the `IndentationError` in the current code.
2. Even if the user does not enter a comma separated value, the program should handle the `IndexError` without crashing.
3. When the user does not enter a comma separated value, they should see the message `Enter comma-separated values.` in the console, and the program should terminate.
4. Even if the user enters a non-numeric value for the length, the program should handle the `ValueError` without crashing.
5. When the user enters a non-numeric value for the length, they should see the message `Length must be a number.` in the console, and the program should terminate.
6. You should fix the off-by-one error in the `validate_isbn` function.
7. You should fix the `TypeError` in the current code that occurs when the user enters a valid ISBN code.
8. You should fix the `IndexError` in the current code when the user enters a valid ISBN code.
9. Even if the user enters an incorrect ISBN code with characters other than numbers, the program should handle the `ValueError` that occurs without crashing.
10. When the user enters an incorrect ISBN code with characters other than numbers, they should see the message `Invalid character was found.` in the console.
11. When the user enters `1530051126,10`, they should see the message `Valid ISBN Code.`
12. When the user enters `9781530051120,13`, they should see the message `Valid ISBN Code.`
