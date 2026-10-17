# Proportional-derivative controller functions for the UUV mission 

import numpy as np 
import pandas as pd
import matplotlib as mpl 

class PDcontroller: 
    def __init__(self, kp, kd, previous_error=0):
        self.kp = kp
        self.kd = kd
        self.previous_error = previous_error 

