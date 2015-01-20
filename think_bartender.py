##PROJECT -PIRATE BARTENDER
##DATED: 15/01/2015
#-------------------------
import random
#Ask questions to the customer

questions = {"strong": " Do ye like yer drinks strong? ",
	"salty": "Do ye like it with a salty tang?",
	"bitter": "Are ye a lubber who likes it bitter?",
	"sweet": "Would ye like a bit of sweetness with yer poison?",
	"fruity": "Are ye one for a fruity finish?"}
ingredients = {
   "strong": ["glug of rum", "slug of whisky", "splash of gin"],
   "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
   "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
   "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
   "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

# Function to capture the style of drink
# ----------------------------------------
def stye_of_drink():
  finished = False
  while not finished :
    #While the finished is True this loop executes
    #Create an empty list to capture the response from the customer
	  response = []
	  #Create an empty list to capture the corresponding key from the response
	  response_bool = []
	  #create an empty dictionary, which will be populated by response[] and response_bool[]
	  final_res_dict = {}
	  for keys,values in questions.items():
	  	print values
	  	#Take the input from the user on questions from the dictionary questions
	  	response_1 = raw_input(' Y/N ')
	  	if response_1 == 'Y':
	  		response.append(keys)
	  		response_bool.append(True)
	  	elif response_1 == 'N':
	  		response.append(keys)
	  		response_bool.append(False)
	  	elif len(response_1) == 0:
	  		print "That's it bye"
	  		# Loop to construct the dictionary from the lists response[] and response_bool[]
	  		for col_res in range(len(response)):
	  			final_res_dict[response[col_res]] = response_bool[col_res]
	  		# Flip the value of finished to True to break the while loop
	  		finished = True
	  		break
  #print response
  #print response_bool
  #print final_res_dict
  #return final_res_dict
      
#Function to construct the drink
#---------------------------------

def Construct_drink(final_res_dict):
  # Empty list to capture the drink value
  drink_list = []
  # Empty dictionary to capture the parameter> dictionary from
  # the Function stye_of_drink()
  Choice_res_dict = {}
  Choice_res_dict = final_res_dict 
  #print Choice_res_dict
  
  for choice,selection in Choice_res_dict.items():
    if selection == False:
      continue
    elif selection == True:
      drink_list.append(random.choice(ingredients[choice]))
    else:
      break
  print "value of drink list is {}".format(drink_list)
  return drink_list

#def drink_creation():
def main():
  stye_of_drink_x = stye_of_drink()
  drink_list_x = Construct_drink(stye_of_drink_x)
  print " The drinks ordered is/are {} ".format(drink_list_x)

# main Function
# taken from the solution provided
# tried to change the main function name and then tried to call it
# didn't work
if __name__ == "__main__":
  main()
  
