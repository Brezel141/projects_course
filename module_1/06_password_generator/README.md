# Password Generator

This Python script generates random passwords. The user can specify the length of the password, and whether it should include symbols and uppercase letters.

## How It Works

The script uses the `secrets` module to generate random passwords. The user can specify the length of the password, and whether it should include symbols and uppercase letters.

The script then generates a password that meets the specified criteria. It does this by creating a string of all possible characters (lowercase letters, digits, optional symbols, and optional uppercase letters), and then randomly selecting characters from this string until the password is of the desired length.

## Usage

Simply run the script, and it will generate 5 passwords each of length 10, with symbols and uppercase letters.

## Example

```bash
1 -> 9{Z5v6^0F U: True, S: True
2 -> 4Z7^2{1v0 U: True, S: True
3 -> 5^1Z4v7{0 U: True, S: True
4 -> 0{Z4^1v75 U: True, S: True
5 -> 1v0{Z^754 U: True, S: True