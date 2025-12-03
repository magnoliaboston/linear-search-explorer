# linear-search-explorer

Step 1:
Why Linear Search?
_____________________
  For this project, I decided to use linear search in my Python app because it fits both the scale of the work and my learning goals as a computing student. Linear search is straightforward and easy to understand, which makes it great for clearly showing how a search algorithm works without adding unnecessary complexity. Since it doesn’t require the data to be sorted beforehand, it works well with the small, unsorted datasets I’m using in this project. It also makes it easier for me to test, debug, and think about how the algorithm performs, which helps me build a stronger understanding of efficiency and problem-solving. Even though linear search isn’t the fastest option for very large datasets, it’s a practical and meaningful choice for learning the core ideas behind searching algorithms in a simple, manageable way.
_____________________
Demo Video/Screenshot

_____________________
Test Plan: Edge Cases & Normal Cases

**Test 1**

Input List :   1,2,3,4,5  

Target :  3  

Expected Result : Found at position 2  

Actual Result : Screenshot 1  

Notes :  Normal case, target in middle

**Test 2**

Input List :  1,2,3,4,5  

Target : 1

Expected Result : Found at position 0

Actual Result : Screenshot 2

Notes : Target at start

**Test 3**

Input List :  1,2,3,4,5  

Target : 

Expected Result : Found at position 4 

Actual Result : Screenshot 3 

Notes : Target at end

**Test 4**

Input List : 1,2,3,4,5  

Target : 6

Expected Result :  Item not found 

Actual Result :  Screenshot 4 

Notes : Target not in list

**Test 5**

Input List :  `` (empty) 

Target : 1

Expected Result : Item not found  

Actual Result :  Screenshot 5

Notes : Empty list

**Test 6**

Input List : 10 

Target : 10 

Expected Result : Found at position 0 

Actual Result : Screenshot 6

Notes : Single-item list

**Test 7**

Input List : 10,10,20 

Target : 10 

Expected Result : Found at position 0

Actual Result : Screenshot 7 

Notes : Duplicate values, first occurrence returned

**Test 8**

Input List : a,2,3

Target : 2

Expected Result :  Error: invalid input 

Actual Result :  Screenshot 8 

Notes : Non-numeric input

**Test 9**

Input List : 1 , 2 , 3

Target : 2

Expected Result :  Found at position 1 

Actual Result : Screenshot 9 

Notes : Extra spaces in input

**Test 10**

Input List : -5,0,5 

Target : -5

Expected Result : Found at position 0  

Actual Result :  Screenshot 10 

Notes : Negative numbers handled

_________________________________
Step 2:
Pillars of Computational Thinking
_________________________________
Decomposition:

- Take the list and the target value.
- Start at the first item.
- Compare the current item to the target.
- If it matches, return its position.
- If not, move to the next item and repeat.
- If the end of the list is reached with no match, return that the item wasn’t found.

These smaller steps make the algorithm easier to understand and implement.

**Pattern Recognition:**

In linear search, the main pattern is a repeated cycle of checking each element in order. The algorithm moves through the list one item at a time, comparing each value to the target. This repeating pattern of “reach the next item and compare it to the target” continues until the item is found or the list ends. Unlike some other algorithms, linear search doesn’t swap values or rearrange anything, it simply follows the same comparison pattern for every element in the list.

**Abstraction:**

For abstraction in my linear search program, I only show the user the important information, like whether the item was found and where it is in the list. I hide unnecessary details such as every comparison the algorithm makes or how the loop works. These behind-the-scenes steps aren’t useful to the user, so keeping them hidden makes the program cleaner and easier to understand.

**Algorithm Design:**

In my linear search program, the algorithm follows a simple flow using the graphical user interface (GUI). First, the user inputs the list of values and the target item through text boxes or dropdown fields in the GUI. Once they press the search button, the program begins the processing stage, where the linear search algorithm goes through the list one item at a time and checks for a match. After the search is complete, the output is shown back to the user on the screen, either telling them the position of the item or that it wasn’t found. This input → processing → output flow keeps the interaction smooth and makes the algorithm easy for the user to understand and use.
_________________________________
Flowchart:
<img width="1640" height="2038" alt="image" src="https://github.com/user-attachments/assets/e2987002-204f-4b91-96cb-a86a82265e38" />
       
_________________________________
Steps to Run:

1. Start at the beginning of the list, the algorithm begins by checking the first element in the list.

2. Compare the current element with the target value. At each index, it checks if the value in the list matches the number the user is searching for.

3. If the value matches the target, the algorithm stops immediately.

4. If the value does not match the target, the algorithm moves to the next element and repeats the comparison.

5. Continue until the end of the list. The algorithm keeps checking each item one by one in order.

6. If the whole list is searched and no match is found then it will be displayed to the user. 

_________________________________

Hugging Face Link:
https://huggingface.co/spaces/magboston/linear_search_explorer
_________________________________
Author and Awknowledgment:

This Linear Search Explorer application was developed by Magnolia Boston as part of a learning project focused on understanding basic search algorithms and improving programming skills in Python. The goal of the project was to design an interactive and easy-to-understand tool that demonstrates how linear search works step by step. The project included building the core search logic, handling user input, designing test cases, and producing a console-based version suitable for demonstration and assessment.

I would like to say a thank you to Professor Kain for aiding in the development of this project by providing sufficient knowledge and support this term. As well as, external academic aids that helped me navigate uncertain concepts and tools/platforms for this project such as informative youtube tutorials and step by step instructions on how to work with Huggy Space. 

_________________________________
