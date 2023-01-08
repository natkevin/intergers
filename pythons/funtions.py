# Online Python - IDE, Editor, Compiler, Interpreter
def calculate_round_square(length_x, length_y=90):
    """Function to calculate a round
    - Input 
      -- length_x as Numeric
      -- length_y as Numeric with default value = 90
    - Ouput:
      -- around = 2*(length_x + length_y)
    """
    around = 2*(length_x + length_y)
    return around 


def calculate_square_area(length_x,length_y=90):
    """Function to calculate a square area
    - Input 
      -- length_x as Numeric
      -- length_y as Numeric with default value = 90
    - Ouput:
      -- area = length_x * length_y
    """
    area = length_x * length_y
    return area


if __name__ == "__main__":
    # length array used tupple
    ls = (10,20,30,40,50,60)
    
    # calculate around base ls 
    arounds = []
    for l in ls:
        print("Length : %s" % (l,))
        # calculate_round_square with length_x=l and length_y=90
        a = calculate_round_square(l)
        print("Around : %s" % (a,))
        
        # add around a to arounds array 
        arounds.append(a)
        
        
    print("Length row :") 
    print(ls)
    print("Arounds row :")
    print(arounds)
    # ========================================================================
    # length array used tupple
    ls = (10,20,30,40,50,60)
    
    # calculate around base ls 
    areas = []
    for l in ls:
        print("Length : %s" % (l,))
        # calculate_round_square with length_x=l and length_y=90
        a = calculate_square_area(l)
        print("Area : %s" % (a,))
        
        # add around a to arounds array 
        areas.append(a)
        
        
    print("Length row :") 
    print(ls)
    print("Areas row :")
    print(areas)
    
    
    
    
