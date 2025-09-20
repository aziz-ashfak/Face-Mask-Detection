import os
import sys

def error_messege(error,error_details:sys):
    
    _,_,exc_tb = error_details.exc_info()
    filepath = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error = str(error)
    messege = "The error is happend in [{0}] file at line number [{1}] and the error is [{2}]".format(
        filepath,line_number,error
    )
    return messege

class CustomException(Exception):
    
    def __init__(self,error,error_details:sys):
        self.messege = error_messege(error,error_details)
        super().__init__(self.messege)
        
    def __str__(self):
        return self.messege
    