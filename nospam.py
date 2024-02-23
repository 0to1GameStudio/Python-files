menu = [
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","spam"],
    ["egg","bacon","spam"],
    ["egg","bacon","sausage","spam"],
    ["spam","bacon","suasage","spam"],
    ["spam","sausage","spam","bacon","spam","tomato","spam"],
    ["spam","egg","spam","spam","bacon","spam"],
    ]

print("\n",menu)


#for meal in menu:
   # if "spam" not in meal:
    #    print(meal)
   #     for item in meal:
  #          print(item)
 #   else:
#        print("{0} has a spam score of {1}".format(meal,meal.count("spam")))


for meal in menu:
    print("\n")
    print(meal, "contains sausage" if "sausage" in meal else "contains bacon" if "bacon" in meal else "contains egg")



#for meal in menu:
 #   for item in meal:
  #      if item != "spam":
   #         print(item)
    #print()

#for meal in menu:
 #   if "spam" not in meal:
  #      print(meal)

#meals = [meal for meal in menu if "spam" not in meal]
#print(meals)
#for meal in menu:
 #   for index in range(len(meal) -1, -1, -1):
#        if meal[index] == "spam":
 #           del meal[index]
  #  print(meal)
   # for item in meal:
    #    print(item)





