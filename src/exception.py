import sys
import logging

def errorMessageDetail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    errorMessage = "Error occured in python script name [{0}] \n" \
    "Line number [{1}] , Error message : [{2}]".format(
    file_name, exc_tb.tb_lineno, str(error) 
    )

    return errorMessage

class CustomException(Exception):
    def __init__(self, errorMessage, error_detail:sys):
        super().__init__(errorMessage)
        self.errorMessage = errorMessageDetail(errorMessage, error_detail=error_detail)

    def __str__(self):
        return self.errorMessage

if __name__ == "__main__":
    try:
        x = 10/0

    except Exception as e:
        logging.info("Exception occured - Divide by 0...")
        raise CustomException(e, sys)