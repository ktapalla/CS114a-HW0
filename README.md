# README - COSI 114a HW0

The code provided in this repository contains the solutions to HW0 for COSI 114a - Fundamentals of Natural Language Processing I. As this assignment was done for a class, some helper files and testing files were provided. All student-written solutions to the assignment were written in the ``` hw0.py ``` file. 

## Installation and Execution 

Get the files from GitHub and in your terminal/console move into the project folder. To run the test file included with the files given to students, run the following: 

``` bash 
python test_hw0.py 
```

Doing this will run the set of tests in the test file that was provided to students to test their code. Running the test file will print a score to the user's console indicating the success of the program for each given test case.  

## Assignment Description 

### Generating Sentences from a File 

A common text format in NLP for tokenized text is to store the text with one sentence per line and each token separated by a space. The ``` gen_sentences(path) ``` method implements a generator function that opens the specified path using UTF-8 encoding and yielding each sentence as a list of strings. 

The parameter being passed in is the path to the file being opened. The path is not manipulated in any way and is simply opened as-is. It is assumed that the string provided references a valid path, and that no error handling related to the path is necessary. 

The code provided assumes that every line in the input consists of: 

1. A sentence with zero or more tokens, with a single space between each token. A token consists of one or more characters that are not a space or a newline. 
2. At most there will be one newline at the end of the line. 

Note: As instructed in by the professor, any lines that contain only a new line are skipped over and do not yield anything for that line. 

To get each token in a line, the lines are split using the space character. It is assumed that the space character does not occur at the beginning or end of the line, and that there will never be two adjacent space characters. Any character other than a space or newline can be a token (or part of a token). 

This portion of the assignment can be debugged alone using the following line: 

``` bash 
python debug_gen_sentences.py <path>
```

If the user wishes to debug this portion of the code, then they should replace ``` <path> ``` with the path file that they wish to use for debugging. For example, if they wanted to test it using the provided ``` hw0_tokenized_text_1.txt ``` file within the ``` test_data ``` folder, they would run the following in their console (assuming that the user is in the directory of the project): 

``` bash 
python debug_gen_sentences.py test_data/hw0_tokenized_text_1.txt
```

After running the test, the console should print a list containing every token for each line in the file. 

### Sarcastic Casing 

The function ``` case_sarcastically(text) ``` takes a single string argument and returns a single string. The returned string is the same length as the original string, but the casing of some characters are changed in a somewhat rude and mocking fashion. Casing is changed based on the following rules: 

1. Characters are classified by whether they are targets for the case-changing process or are transparent. Any character that is not affected by casing- ones for which char.upper() == char.lower()- is considered transparent. All other characters are considered targets. 
2. All transparent characters are copied to the output unchanged. 
3. The first target character is lowercase in the output. The casing of target characters alternate between uppercase and lowercase thereafter, regardless of how many transparent characters occur between targets. The ``` .upper() ``` and ``` .lower() ``` methods are used for the changing of case. 

### Prefix and Suffix 

Two functions, ``` prefix(s, n) ``` and ``` suffix(s, n) ```, are also defined. Both take a string ``` s ``` and an integer ``` n ``` as arguments, and returns a string. The string returned is a length ``` n ``` prefix (first ``` n ``` characters) or suffix (final ``` n ``` characters) of ``` s ```. The implementation of the code was required to do the following: 

1. If ``` n ``` is greater than the length of ``` s ```, then it raises a ``` ValueError ``` 
2. If ``` n ``` is not a positive number, then it raises a ``` ValueError ```. It is assumed that the functions are only being passed  correct-type inputs, so there is no need to check variable types. 

### Sorted Unique Characters 

The function ``` sorted_chars(s) ``` takes a single string as an argument and returns a list of strings. The list of strings contains each of the unique characters of ``` s ``` in sorted order. ``` s ``` is guaranteed to be a string of length zero or more. The sorting is done through a pre-existing ``` sorted(iterable) ``` function already built into python. 