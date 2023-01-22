
def variable_y(x):
    """Function to calculate reverse comparison
    from the case if x = -2, then y = 9
    base a formula y = a/x, then a = x*y
                    a = -2 * 9 = -18
      -- length_x as Numeric
      -- length_y as Numeric with default value = 90
    - Ouput:
      -- area = length_x * length_y
    """
    
    y = -18/x 
    return y

def variable_y_s(x):
    """Function to calculate reverse comparison
    from the case if x = 1.5, then y = 7.5
    base a formula y = a/x, then a = x*y
                    a = 1.5 * 7.5 = 11.25
      -- length_x as Numeric
      -- length_y as Numeric with default value = 90
    - Ouput:
      -- area = length_x * length_y
    """
    
    y = 11.25/float(x) 
    return y
    
if __name__ == "__main__":
    print('hallo')
    number_x = [-2, 0, 3, 6,]
    for x in number_x:
        try:    
            y = int(variable_y(x))
        except:
            y = 'undefinite'
        print('x = %s' %(x,))
        print('y = %s' % (y,))
        
        
    number_x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 1.5, 2.0]
    for x in number_x:
        try:    
            y = variable_y_s(x)
        except:
            y = 'undefinite'
        print('x = %s' %(x,))
        print('y = %s' % (y,))
