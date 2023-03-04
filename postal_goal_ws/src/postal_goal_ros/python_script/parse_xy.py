def get_postal_xy(address_string):
	# address_string = input('Please Enter Destination Address:' )
	try:
		if address_string == 'STARTING POINT':
			postal_x = 0.053
			postal_y = 0.692
			print("Going to Starting Point")
		
		elif address_string == 'END POINT':
			postal_x = 48.984
			postal_y = 4.040
			print("Going to End Point")
		
		else:
			postal_code = int([int(i) for i in address_string.split() if i.isdigit()][0]) 
			delivery_num = 0
			postal_x = 0
			postal_y =0
			
			if 2074 <= postal_code <= 2094:
				delivery_num = 1
				postal_x = 1.974
				postal_y = 0.124
			elif 2059 <= postal_code <=2073:
				delivery_num = 2
				postal_x = 3.833 
				postal_y = -0.246
			elif 2040 <= postal_code <=2058:
				delivery_num = 3
				postal_x = 6.314
				postal_y = -0.508
			elif 2028 <= postal_code <=2039:
				delivery_num = 4
				postal_x = 7.540
				postal_y = -0.728
			elif 2009 <= postal_code <=2027:
				delivery_num = 5
				postal_x = 8.816
				postal_y = -0.773
			elif 1995 <= postal_code <=2008:
				delivery_num = 6
				postal_x = 10.0263834
				postal_y = -0.926
			elif 1972 <= postal_code <= 1994:
				delivery_num = 7
				postal_x = 11.741
				postal_y = -1.418
			else:
				print("INVALID Postal Code")
				pass
			#status_string = "Destination Address {0} is located at Delivery Point #{1}.".format(str(address_string),str(delivery_num))
			#print(status_string)
			return postal_x,postal_y
	except:
		print("INVALID ADDRESS")

