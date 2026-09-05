from function_identification import*

mylist=[]
print("Filling list....")
fill_inventory(mylist)
print("Showing")
display_inventory(mylist)

print("Searching....")
find_by_name(mylist)
print("Changing....")
depreciate_by_name(mylist, 20)

print("Removing....")
print(delete_by_serial(mylist))
display_inventory(mylist)

print("Resuming...")
summarize_values(mylist)