function check_real_number_02(number)
    return_msg = 'The Positive Number'
    if (number < 0) then
        return_msg = 'The Negative Number';
    end
    return return_msg;
end

print("The result is", check_real_number_02(10))
