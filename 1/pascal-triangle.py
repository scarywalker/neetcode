def pascal_triangle(rows:int)->list:
    output:list = []
    for index in range(rows):
        output.append( [1] * (index + 1))
        if index > 1:
            for sub_index in range(1,len(output[index])-1):
                output[index][sub_index] = output[index-1][sub_index-1] + output[index-1][sub_index]
    return output

print(pascal_triangle(1))