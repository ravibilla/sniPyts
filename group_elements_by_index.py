# Group elements by index
def group_elements_by_index(inputLists):
    outputLists = []
    for j in range(len(inputLists[0])):
        outputLists.append([])
        for i in range (len(inputLists)):
            outputLists[j].append(inputLists[i][j])
    
    return(outputLists)

Lists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(f"Grouped elements by index: {group_elements_by_index(Lists)}")
