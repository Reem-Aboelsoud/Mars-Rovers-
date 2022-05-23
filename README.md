# Mars Rovers challenge
**Introduction**

The aim of this problem is to navigate a squads of rovers landed on Mars. The instructions given to any rover should command it to change its direction to right or left, or to head/move forward without any change in its direction. The programming language used to write the code is Python. 



**The strategy**

The strategy ideas are:

**1-** If you want to ask the rover to commit a rotation with an angle of 90 degrees, it means that the rover will move to another cardinal compass direction. The next cardinal compass direction will depend on the type of rotation: clockwise or anti-clockwise. For example, if the rover is pointing to the North, a one right rotation will make it point to the East while a one left rotation will make it point to the West. 
                 
**2-** Assuming the grid around the rover is like the four infinite regions of the two dimentional cartisian plane. Check the image in the same zipped file. The psitive-Y axis points to the North, the negative_Y axis points to the South, the positive_X axis points to the East and the negative_X axis points to the West. 


**3-** Then, a one right rotation will require -90 rotation, while a one left rotation will require +90 degrees rotation. 

**4-** A one move forward with no change in the direction will add or subtract ONE from the current X or Y values. For example, if the current position is X= 3, Y=1, and the rover points to N and the instruction is only, M, a one move forward. Then, as N is refering the positive_Y axis, one should be added to the Y value and the final position will be: X=3, Y=2, and the same direction to the North.

**5-** As givin in the problem, the rover's lower left corner is (0,0), so the rover is "hypothatically" moving in the cartisian first quarter of this 2 dimentional plane. All in all, all the values of the input and output of both X and Y values should be positive values. Look at the image. 

 
 
 
 
 **Files**
 The zipped file includes lib folder which contains the main code "calculate.py" to solve the required task, and app.py which runs the application required using flask, and tamplets folder which contains index.html that contains all the instruction to creat the application, and static folder which contains app.js and style.css which are used mainly for, obviously, decorating the app and restricting some input values and formate, and requirment.txt file which contains all the required packages and libraries to run the code, and finaly this README file which have some infromation about the contents of the whole zipped file.


