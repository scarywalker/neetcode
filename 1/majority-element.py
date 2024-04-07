def majority_element(elements:list):
    output:list = [0,0]
    for element in set(elements):
        count = elements.count(element)
        if count > output[0]:
            output = [count,element]
    return output[1]