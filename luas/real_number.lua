function check_real_number_02(number)
    --[[
        The method for checking the real number is POSITVE/NEGATIVE
        INPUT:
          - number : numeric
        OUPUT:
          - information : string
    ]]
    
    return_msg = 'The Positive Number'
    if (number < 0) then
        return_msg = 'The Negative Number';
    end
    return return_msg;
end

print("The result is", check_real_number_02(10))
