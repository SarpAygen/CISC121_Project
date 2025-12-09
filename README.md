# CISC121_Project

Algorithm Choice — Binary Search
I selected Binary Search because:
It has a clear decision-making pattern (left, right, or found).
It reduces the search space in half each turn, which is easy to visualize.
It aligns well with interactive learning since users can act as the algorithm.
It demonstrates key algorithmic concepts such as divide-and-conquer and efficiency.
This makes binary search ideal for a gamified teaching tool.


Decomposition:

Generate a sorted list based on difficulty.
Randomly select a target value.
Highlight the active search range.
Compute and verify midpoint guesses.
Update search boundaries after each comparison.
Track steps and mistakes.
Display feedback and visualization to the user.


Pattern Recognition
Binary search repeatedly:
Calculates mid using (low + high) // 2
Compares mid value to target
Eliminates half the search range
The game mirrors this repetitive decision-making cycle.


Abstraction:

Hides code complexity (sorting, indexing, evaluation).
Shows only:
list,
range,
midpoint,
success/failure feedback.
Simplifies binary search logic into interactive choices.

Algorithm Design

Input: Difficulty selection and user mid/direction choices
Processing: Compute correct mid, validate choices, update search range
Output: Visualized list, dynamic feedback, success/failure result

To validate that my Binary Search game works correctly, I performed a series of manual tests across different scenarios and difficulty levels. My testing focused on correctness, edge cases, user interaction, and feedback clarity.

Tests Performed

Started multiple new games at Easy, Medium, and Hard difficulties:
Verified list sizes matched expected ranges.

<img width="1881" height="866" alt="image" src="https://github.com/user-attachments/assets/de11ca4b-8091-4934-887c-b8c322f81c0a" />
<img width="1903" height="868" alt="image" src="https://github.com/user-attachments/assets/8304f28e-9204-4225-aff5-4dbac8e5e538" />
<img width="1909" height="888" alt="image" src="https://github.com/user-attachments/assets/b0631ae3-cf55-4d2f-b598-e30417d06120" />


Played full rounds using correct choices:
Confirmed the game properly declared success.

<img width="1901" height="700" alt="image" src="https://github.com/user-attachments/assets/927a61ed-feea-4a2a-9ae2-fcd31771ed3d" />
<img width="1905" height="636" alt="image" src="https://github.com/user-attachments/assets/ca75820c-1729-4549-81ff-3eb9d27cd70f" />
<img width="1902" height="680" alt="image" src="https://github.com/user-attachments/assets/a86ea273-6585-4a27-923a-a2c9dd4fd14a" />



Intentionally selected wrong mid values:
Verified that mistake tracking and error messages displayed correctly.

<img width="1902" height="688" alt="image" src="https://github.com/user-attachments/assets/d39569a8-b503-4647-be4b-8dc27471470b" />
<img width="1913" height="683" alt="image" src="https://github.com/user-attachments/assets/6d5dbf32-77fd-4bbc-9c9b-066ad0d4523f" />


Chose incorrect directions (Left/Right):
Game correctly flagged errors and updated mistake count.

<img width="1919" height="700" alt="image" src="https://github.com/user-attachments/assets/406f2dbf-0240-447e-ab6b-9ddd838f9204" />


Tested restarting using New Game:
Confirmed state resets and generates a new list/target every time.

<img width="1909" height="871" alt="image" src="https://github.com/user-attachments/assets/48b01a91-9a37-43c8-a39a-166b3f5eb601" />
<img width="1905" height="857" alt="image" src="https://github.com/user-attachments/assets/7587be9d-4889-44ba-a992-f6935c5b4c2f" />
<img width="1915" height="881" alt="image" src="https://github.com/user-attachments/assets/8c606d10-a4b1-4549-8b42-874cab383e25" />
<img width="1910" height="864" alt="image" src="https://github.com/user-attachments/assets/98ff1ad8-b52d-4404-a81d-b893ceb90f2d" />


Tried invalid inputs (blank mid, out-of-range mid, non-integer input):
Application handled errors safely and displayed guidance.

<img width="1903" height="733" alt="image" src="https://github.com/user-attachments/assets/6c735d59-336e-4ef0-8fdd-8491a02cd93e" />
<img width="1913" height="728" alt="image" src="https://github.com/user-attachments/assets/6eedb599-0726-456d-bc26-1176a768e066" />
<img width="1919" height="748" alt="image" src="https://github.com/user-attachments/assets/c074a96c-0f1a-46a9-abdd-ad337f4d54e5" />
<img width="1919" height="694" alt="image" src="https://github.com/user-attachments/assets/36b2a401-e4c1-4d6f-8227-9f0e55e4e328" />


Huggin Face Link: https://huggingface.co/SarpAygen/App.py/blob/main/app.py

Steps To Run: To run my project you need to first have the Gradio module installed. Then you need any IDE that can run python and you can run the program from there where it will then give you a local link to run it on any browser. You then select a diffaculty then press new game to reset it to that diffuculty and then enjoy learning and having fun. You have to enter the mid index and which side the target is at acting like a binary search algorithm.

Author & Acknowledgment: For this project I used ChatGPT to help me with writing comments on the code wherever necessery. I also used it to brainstrom ideas for the project. I did not need ChatGPT for the logic part of the code as I was able to code most of it on my own from the stuff I have learned but I did use it to learn how to use Gradio and sometimes to help me with stuff I was stuck on using Gradio while working on my project since it was my first time using it. Other than that All of the code is my own and I did not need AI help.
