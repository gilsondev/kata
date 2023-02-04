# Phone Validator

Given a file with valid area codes and a second file with phone numbers, print the number of valid phone numbers per area code.

From the second file, a phone number is valid if it respects the following rules:

1. have exactly 3 digits, in addition to having between 7 and 12 digits
2. Can have an optional "+" character at the beginning of any digit
3. Can start with 00, unless it starts with a "+" sign
4. If it starts with 00, those two digits do not count in the maximum number of digits
5. There can be no letters
6. There can be no symbols other than "+".
7. There can be no space between "+" and the first digit, but you can have any amount of space

## Example

```
$ ./program codes.txt phones.txt
```

**File content**

- codes.txt

```
245
244
681
091
```

- phones.txt

```
245780009185
00245672543222
544980000000
22377
244761029384
```

**Output**

```
245:2 244:1
```
