def check_real_number_01(number):
    """
    The method for checking the real number is POSITVE/NEGATIVE
    INPUT:
      - number <variable as paramater> : numeric <type as numeric>
    OUPUT:
      - information <variable as goal/result/output> : string <type as string>
    """
    
    if (number >= 0):
        return 'The Positive Number'
    else:
        return 'The Negative Number'
      
      
def check_real_number_02(number):
    """
    The method for checking the real number is POSITVE/NEGATIVE
    INPUT:
      - number : numeric
    OUPUT:
      - information : string
    """
    
    return_msg = 'The Positive Number'
    if (number < 0):
        return_msg = 'The Negative Number'
    
    return return_msg
