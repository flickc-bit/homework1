# Library Management System

## AI Policy Reminder

You can use the internet, including AI engines, but you must use them similar to if you had a smart friend to work with:

1. You CAN ask high-level questions:
   For example, "Does Python have a built-in ability to read JSON files, or do I need to import something?"

2. You CANNOT ask for the solution code by entering this assignment as a prompt.
   For example, "Generate a Python program to read the given files and generate the following output: .." is NOT PERMITTED

3. You MAY ask for SAMPLE code to demonstrate various examples of Python usage
   For example, "Can you show me a short example of how to read lines from a file on disk?"
   This is acceptable because you're asking for help on a general principle, from which you must
   still apply to the specifics of this assignment.

4. Whenever you learn something new from AI that you then apply to your work, you MUST CITE the exact prompt(s) and LLM engine that you used.

### Assignment Objectives

This assignment is written to help you identify your current strengths/weaknesses in the following areas:

- File I/O and parsing strategies
- Data structure choices for inventory management
- String processing and command parsing
- Error handling approaches
- Data aggregation and analysis techniques
- Output formatting and presentation


### Assignment Instructions

You've been hired to build a library management system that processes daily operations. 
The system reads the current inventory and a log of commands, then outputs results to 
help librarians manage their collection and analyze usage patterns.

Your program should handle:
  - Malformed lines in input files
  - Empty files
  - Missing files (graceful error handling)

You can handle these situations by making sure that your output matches the "expected output files"
provided.  We may also run your program against other input files to ensure that you're handling
these edge cases appropriately and not hardcoding your prior knowledge of the input files.

**Problem 1: Library Operations Processor**

  See instructions in file `library_processor.py`

**Problem 2: Usage Analytics Generator**

  See instructions in file: `analytics_generator.py`

### Grading Rubric

Each problem can earn up to 5 points, for a total of 10 points.

For each problem:

* Up to 4 points for overall output correctness
* 1 point for graceful handling of missing/empty files

