# Tool Assigner
A Python application to assign materials to tools using a stable matching algorithm based on compatability and customer preferences.

## Features
- Parses a text file of tools, materials, and their respective attributes.
- Calculates compatibility between each tool and material using dot product.
- Runs Gale–Shapley (aka Stable Matching) algorithm with customer preference-based proposals.
- Outputs a .txt file with stable-matched, human-readable results. 
- Stores inputs and outputs into /data/ folder for organization and convenience
- Sample inputs and outputs for quick testing
- Unit tests for more in-depth/higher coverage testing

## Requirements
- Python 3.12+
### Dependencies
- None as of the latest update.
- If dependencies are needed in a future update, run:
```markdown
pip install -r requirements.txt
```

## Installation
```markdown
git clone https://github.com/Hamoda434/ToolAssigner/
```

## How to Use 
In \ToolAssigner\data\input\ create a .txt file containing a sample of tools and materials, where **num_of_materials % num_of_tools == 0**

**T** is a tool line. **T#** is a tool. **M** is a material line. **M#** is a tool.
**S:#** represents Speed value, **A:#** represents Accuracy value, and **C:#** represents Cost value.
Materials have preferences, wherein **"T#>T%"** means **T# is preferred over T%**

(A sample .txt file with proper format, input.txt is stored in \ToolAssigner\data\input\ for your convenience)

The file should be formatted like this
```markdown
T T0 S:7 A:7 C:10 
T T1 S:2 A:1 C:1 
T T2 S:7 A:6 C:4 
M M0 S:3 A:9 C:2 T2>T0>T1 
M M1 S:4 A:3 C:7 T0>T2>T1 
M M2 S:4 A:0 C:10 T0>T2>T1 
M M3 S:10 A:3 C:8 T2>T0>T1 
M M4 S:6 A:10 C:1 T0>T2>T1 
M M5 S:6 A:7 C:7 T0>T2>T1 
M M6 S:8 A:6 C:9 T2>T1>T0 
M M7 S:7 A:1 C:5 T2>T1>T0 
M M8 S:8 A:2 C:3 T1>T0>T2 
M M9 S:10 A:2 C:1 T1>T2>T0 
M M10 S:6 A:4 C:5 T0>T2>T1 
M M11 S:8 A:4 C:7 T0>T1>T2
```
At the root of the project run the program, with:
```markdown
python -m ToolAssigner.main <name_of_your_txt_file>.txt
```

The result is stored in \ToolAssigner\data\output\ as "<name_of_your_txt_file>_output.txt" 

An example of how the result is formatted:
```markdown
T0: M5(161) M11(154) M2(128) M4(122) 
T1: M9(23) M8(21) M7(20) M1(18) 
T2: M6(128) M3(120) M10(86) M0(83) 
```

Please note that if you reuse a input filename with new content, the old output file will be overwritten with new results.

## Edge Cases Currently Covered

- Edge Case -> How it's Handled
- All materials and tools have same preference and compatibility -> Materials get first come, first serve assignment to tools.
- At least one tool, no materials -> Tools are listed with nothing assigned to them.
- One tool, multiple materials -> All materials are assigned to the one tool.
- M0 prefers T0, M1 prefers T1, T0 has better compatability with M1, T1 has better compatability with M0 (Deadlock) -> Material is the "proposer", so preference breaks deadlock: M0 is paired with T0 and M1 with T1
- Tools and/or materials don't have their attributes (S,A,C,Pref) in the same order -> The parser is order agnostic.
- The tools and materials have required attributes (S,A,C,Pref) but also have extraneous attributes -> extraneous attributes are recorded, but are not used in the matching algorithm.

## Edge Cases Currently NOT Covered and/or Raises Error
- Num_of_material % Num_of_tools != 0 (including Num_of_tools = 0).
- Malformed input/Missing required attributes (ex. A material has no preferences, a tool is missing a "S" attribute).
- Input not saved in a .txt file. 

## Resources 
Both GeeksForGeeks and the Wikipedia article for the Stable Matching problem were crucial to understanding the basics of the algorithm used in the project. The resources are linked below:
- https://www.geeksforgeeks.org/stable-marriage-problem/
- https://en.wikipedia.org/wiki/Stable_matching_problem

 ## AI Disclosure
AI was not used to generate any code crucial to the program's operations *(except one case noted below), but AI was used to assist the programmer in the following ways:

- Explaining how the stable matching problem algorithm to the programmer in a visual manner.
- Setting up the logger and logger.info(). 
- Listening to the programmer's current thought process and whether her ideas would work as she expected (ex. The programmer asking if a stack-based approach for the proposals had any unforeseen drawbacks).
- Compacting particularly wordy lines of code into neater one-liners. For example, turning:
```markdown 
    if "S" not in sub_dict or if "A" not in sub_dict" or if "C" not in sub_dict
```
to 
```markdown
    required_attrs = ("S", "A", "C")   
    if not all(attr in sub_dict for attr in required_attrs)
```
- Suggesting potential edge cases to test.
- Providing a guideline for important information to include in the README.md
- *The one case where ChatGPT was used to generate code crucial to the program's operations is writing the output file to the \ToolAssigner\data\output\ path. While writing to that path is important to the project's overall functionality it was ultimately deemed far enough removed from the central goals of the project (parsing input, stable matching, formatting output) that the programmer decided to use ChatGPT to help write that particular portion of the code. The ChatGPT generated lines are denoted as such in write_output.py.