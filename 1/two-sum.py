def two_sum(number_list:list,result:int)->list:
    for i,a in enumerate(number_list):
        for j,b in enumerate(number_list):
            if a + b == result:
                return [i,j]