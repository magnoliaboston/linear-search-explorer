# linear-search-explorer

Step 1:
Why Linear Search?
_____________________
  For this project, I decided to use linear search in my Python app because it fits both the scale of the work and my learning goals as a computing student. Linear search is straightforward and easy to understand, which makes it great for clearly showing how a search algorithm works without adding unnecessary complexity. Since it doesn’t require the data to be sorted beforehand, it works well with the small, unsorted datasets I’m using in this project. It also makes it easier for me to test, debug, and think about how the algorithm performs, which helps me build a stronger understanding of efficiency and problem-solving. Even though linear search isn’t the fastest option for very large datasets, it’s a practical and meaningful choice for learning the core ideas behind searching algorithms in a simple, manageable way.
_____________________
Demo Video/Screenshot
_____________________


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

Pattern Recognition:

In linear search, the main pattern is a repeated cycle of checking each element in order. The algorithm moves through the list one item at a time, comparing each value to the target. This repeating pattern of “reach the next item and compare it to the target” continues until the item is found or the list ends. Unlike some other algorithms, linear search doesn’t swap values or rearrange anything, it simply follows the same comparison pattern for every element in the list.

Abstraction:

For abstraction in my linear search program, I only show the user the important information, like whether the item was found and where it is in the list. I hide unnecessary details such as every comparison the algorithm makes or how the loop works. These behind-the-scenes steps aren’t useful to the user, so keeping them hidden makes the program cleaner and easier to understand.

Algorithm Design:

In my linear search program, the algorithm follows a simple flow using the graphical user interface (GUI). First, the user inputs the list of values and the target item through text boxes or dropdown fields in the GUI. Once they press the search button, the program begins the processing stage, where the linear search algorithm goes through the list one item at a time and checks for a match. After the search is complete, the output is shown back to the user on the screen, either telling them the position of the item or that it wasn’t found. This input → processing → output flow keeps the interaction smooth and makes the algorithm easy for the user to understand and use.
_________________________________
Flowchart:
_________________________________
Steps to Run:
_________________________________

Hugging Face Link:
_________________________________
Author and Awknowledgment:
_________________________________
