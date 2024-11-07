"""

These keywords are used to control the flow of loops.

1. Break:
The break statement is used to exit a loop prematurely, regardless of the loop's condition.
Example:
for i in range(1, 6):
    if i == 3:
        break
    print(i)
Explanation: This will print 1 and 2, and when i becomes 3, the loop will break and stop executing.

2. Continue:
The continue statement is used to skip the current iteration of the loop and proceed with the next iteration.
Example:
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
Explanation: This will print 1, 2, 4, and 5. When i is 3, the continue statement skips the print(i) statement and proceeds with the next iteration.

3. Pass:
The pass statement is a placeholder. It does nothing and allows the program to continue execution. It's often used as a placeholder when you have a block of code that you intend to implement later.
Example:
for i in range(1, 6):
    if i == 3:
        pass  # Do nothing for i == 3
    print(i)
Explanation: This will print 1, 2, 3, 4, and 5. The pass statement does nothing when i is 3, but the loop continues.

NOTE: pass is really useful, since you can't leave an empty block in python code instead of empty block we can use pass.

"""