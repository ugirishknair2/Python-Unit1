#Ask questions to the customer


#	finished = False
#	while not finished:
#		question_to_customers = raw_input("Do ye like yer drinks strong?")
##		if len(question_to_customers) or len(Answer_to_question) == 0:
#			finished = True
#	    elif 
#			qst_cst = []
#			qst_cst.append(question_to_customers)

def stye_of_drink():


#Function to ask what style of drink a customer likes
#While the finished is True this loop executes
    
finished = False
while not finished :
	questions = {"strong": " Do ye like yer drinks strong? ",
	"salty": "Do ye like it with a salty tang?",
	"bitter": "Are ye a lubber who likes it bitter?",
	"sweet": "Would ye like a bit of sweetness with yer poison?",
	"fruity": "Are ye one for a fruity finish?"}
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

	print response
	print response_bool
	print final_res_dict

#   	if len(response_1) == 0:
#   		finished = True
#   	else:
#   		pass

#ingredients = {
#   "strong": ["glug of rum", "slug of whisky", "splash of gin"],
#   "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
#   "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
#   "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
#   "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
#}
