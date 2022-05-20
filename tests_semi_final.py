
from semi_final import MarsRover     #import the main file 
import unittest                      #the python library used for testing 

rover_upper_right_corner = '5 5'.split()    #the input testing value of the upper right corner 
rover_current_position = '1 2 N'.split()    #the input testing X_value, y_value and the direction of the rover when giving the instructions 
rover_instructions = 'LMLMLMLMM'            #the input instructions to the rover 


class Testing(unittest.TestCase):
    
    
    """A function to define the objects and their connection with the class"""
    def setUp(self): 
        
        self.rover = MarsRover(current_position= rover_current_position, instructions = rover_instructions, upper_right_corner = rover_upper_right_corner)
    





    
    """"A function to test the general movement fucntion used in the main code file, 
    ###to apply right and left rotation and moving forward without changing the direction """
    def test_general_movement(self):
        
        self.assertListEqual(self.rover.general_movement(), [1, 3, 'N'], "Your output does NOT mach the expected output!")
    
    
    
    
    

    """A function to check that the output is in the right format, as the first two values are numbers,
    ###and the third is a direction in a form of N or S or W or E"""
    def test_the_outpu_format(self):
  
        
        #To test that the output X value is an integer 
        self.assertIsInstance(self.rover.general_movement()[0], int, "The X-value of the output is NOT an integer!") 
        #To test that the output Y value is an integer 
        self.assertIsInstance(self.rover.general_movement()[1], int, "The Y-value of the output is NOT an integer!")
        #To test that the output direction is N or S or W or E
        self.assertIn(self.rover.general_movement()[2], MarsRover.direction_letters, "The final direction is not N or E or S or W!")
        

                      

if __name__ == "__main__":
    unittest.main()
