''' 
    By Edwin Roman, with love from Rep. Dominicana. Lunes a Miércoles
'''
data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maximum_subarray(data_set: list):
    max_storage = []
    for idx, val in enumerate(data_set):
        
        if idx == len(data_set) - 1:
            break
        
        tem_max_storage = []
        for x in range(idx + 1, len(data_set)):
            tem_max_storage.append( ([idx, x], sum(data_set[idx:x + 1])) )

        tem_max_storage = sorted(tem_max_storage, key= lambda x: x[1], reverse= True)
        max_storage.append( tem_max_storage[0] )
    
    return sorted( max_storage, key= lambda x: x[1], reverse= True )
        
        
max_values = maximum_subarray(data) 

print("The possibles maximums values are: ", max_values)
print(f"The maximum sum serie is from {max_values[0][0]} and it value is  {max_values[0][1]}.")
print("By Edwin Roman, with love from Rep. Dominicana. Lunes a Miércoles")