def tea_order(customer_name, tea_type, *args): #**kwargs    #if using *args and ##kwargs, *args comes first
    print(customer_name, "ordered a", tea_type, "tea")
    #for key, value in kwargs.items():
    #   print("  - Add", key, ":", value)
    print("args contains:", args)
    for arg in args:
        print("   - Add:", arg)
# for arg in extras:
#print("   - Add:", arg)
tea_order("Alice", "chamomile")
tea_order("Bob", "black", "oat", "honey") #milk="oak"
tea_order("Tony", "black", "oat", "honey") #milk="oat", sweetener="honey" #positional arguments before keyword arguments (args, kwargs)

#eves_extras = "almond", "sugar", "lemon"
#tea_order("Eve", "green", milk="almond", sweetemer="sugar", flavor="lemon")
#tea_order("Eve", "green", **eves_extras)



# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"