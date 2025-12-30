## Objective: Build a credit card validator using the Luhn algorithm.
The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a simple checksum formula used to validate a variety of identification numbers, like credit card numbers. These are the steps to validate a number using the Luhn algorithm:
   - Starting from the right, and excluding the rightmost digit (the check digit), double the value of every other digit.
   - If the result of doubling a digit is greater than `9`, sum the digits to get a single digit. Alternatively, you can subtract `9` from the result.
   - If the sum of all the digits is a multiple of `10`, then the number is valid; else it is not valid.

# User Stories:

1. You should define a function named `verify_card_number` that takes a string of digits (representing a card number) and verifies whether it is valid according to the Luhn algorithm.
2. Within the `verify_card_number` function:
   - You should handle any dashes or spaces that may be present in the card number passed to it.
   - Return `VALID!` if the card number is valid; otherwise, return `INVALID!`.

When you complete the project, you should see the following messages depending on the input:
```
453914889           =>	VALID!
4111-1111-1111-1111 => 	VALID!
1234 5678 9012 3456 =>	INVALID!
```
