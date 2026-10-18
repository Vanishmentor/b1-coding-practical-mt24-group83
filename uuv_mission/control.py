# Proportional-derivative controller functions for the UUV mission 


# A class created for a generic PD controller 
class PDcontroller: 
    # Defining attributes of the controller class 
    def __init__(self, kp, kd, previous_error=0):
        self.kp = kp # Proportional gain 
        self.kd = kd # Derivative gain 
        self.previous_error = previous_error 

    # Defining the call method to compute the controller action based on reference and depth inputs
    def __call__(self, reference, depth):   
        error = reference - depth 
        action = (self.kp * error) + (self.kd * (error - self.previous_error))
        self.previous_error = error 
        return action 

    # When calling the instance it behaves like a function in itself, taking in parameters to compute controller action 

    def reset(self): # Reset function, to reset the previous error to zero for the start of each cycle 
        self.previous_error = 0 

