# Proportional-derivative controller functions for the UUV mission 

import numpy as np 
import pandas as pd
import matplotlib as mpl 

class PDcontroller: 
    # Defining attributes of the PD controller class (proportional and derivative gains, previous error) 
    def __init__(self, kp, kd, previous_error=0):
        self.kp = kp
        self.kd = kd
        self.previous_error = previous_error 


    def __call__(self, reference, depth):   
        error = reference - depth 
        action = (self.kp * error) + (self.kd * (error - self.previous_error))
        self.previous_error = error 
        return action 

    # When calling the instance it behaves like a function in itself, taking in parameters to compute controller action 

    def reset(self): # Reset the previous error to zero for the start of each cycle 
        self.previous_error = 0 

