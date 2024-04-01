def replace_elemnts_with_greatest_element_on_right_side(elements):
    output = []
    for element in elements:
        sorted_remains = sorted(elements[len(output)+1:])
        if len(sorted_remains) > 0:
            output.append(sorted_remains[-1])
    output.append(-1)
    return output

print(replace_elemnts_with_greatest_element_on_right_side([17,18,5,4,6,1]))
