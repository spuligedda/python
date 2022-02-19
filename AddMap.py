from operator import add # import the add operator from the operator module  
# initialize the lt1 and lt2 as the Python list' element  
lt1 = [4, 8, 12, 16, 20, 24]  
lt2 = [2, 4, 6, 8, 10, 12]  
  
# display the original items of the lists lt1 and lt2  
print ("Display the elements of List 1 " + str(lt1))  
print ("Display the elements of List 2 " + str(lt2))  
  
# use map() function with add operator to add the elements of the lists lt1 and lt2  
res_lt = list( map (add, lt1, lt2)) # pass the lt1, lt2 and add as the parameters  
  
# Display the sum of the two list  
print (" Sum of the list 1 and list 2 is : " + str(res_lt))  