# Mars Rovers challenge
**Introduction**
The aim of this problem is to navigate a squads of rovers landed on Mars. The instructions given to the rover should command it to change its direction to right or left, or to head/move forward without change in the direction. The programming language used to write the code is Python. 



**The approach**

The basic ideas are:

**1-** If you want to ask the rover to commit a rotation with an angle of 90 degrees, it means that the rover will move to the next cardinal compass direction. The nixt cardinal compass direction will depend on the type of rotation clockwise or anti-clockwise. For example: if the rover is pointing to the north, a one right rotation will make it point to east while a one left rotation will make it point to west. 
                 
**2-** Assuming the grid around the rover is the like  the four infinite regions of the two dimentional cartisian plane. Chck the next image. The psitive-Y axis points to North, the negative_Y axis points to south, the positive_X axis points to East and the negative_X axis points to West. 


**3-** Then, a right rotation will require -90 rotation, while a left rotation will require +90 degrees rotation. 

**4-** And, a move forward with no change in the direction will will add or subtract ONE from the currevt X or Y values. For example, if the current position is X= 3, Y=1, and the rover points to N and the instruction is only "M" to move forward. Then, as N is refering th the positive_X axis, a one should be added to the X value and the final position will be: X=4, Y=1, and direction same to the north.

**5-** As givin in the problem, the rover's lower left corner is (0,0), so the rover is "hypothatically" moving in its the cartisian first quarter of this 2_D plane. Look at the image. 

 


