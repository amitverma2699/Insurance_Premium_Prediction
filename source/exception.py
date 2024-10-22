import sys

class myexception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()

        self.lineno=exc_tb.tb_lineno
        self.filename=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in [{0}] Line number [{1}] Error message [{2}]".format(self.filename, self.lineno, str(self.error_message))
    

