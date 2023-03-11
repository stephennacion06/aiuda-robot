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
			
			if 2082 <= postal_code <= 2094:
				delivery_num = 1
				postal_x = 6.442
				postal_y = 1.198
			elif 2069 <= postal_code <=2081:
				delivery_num = 2
				postal_x = 11.782 
				postal_y = 1.654
			elif 2056 <= postal_code <=2068:
				delivery_num = 3
				postal_x = 16.782
				postal_y = 1.704
			elif 2043 <= postal_code <=2055:
				delivery_num = 4
				postal_x = 21.384
				postal_y = 2.004
			elif 2030 <= postal_code <=2042:
				delivery_num = 5
				postal_x = 26.273
				postal_y = 2.435
			elif 2017 <= postal_code <=2029:
				delivery_num = 6
				postal_x = 30.747
				postal_y = 2.707
			elif 2004 <= postal_code <=2016:
				delivery_num = 7
				postal_x = 35.459
				postal_y = 2.933
			elif 1991 <= postal_code <=2003:
				delivery_num = 8
				postal_x = 39.321
				postal_y = 3.112
			elif 1882 <= postal_code <=1990:
				delivery_num = 9
				postal_x = 43.196
				postal_y = 3.438
			else:
				print("INVALID Postal Code")
				pass
			#status_string = "Destination Address {0} is located at Delivery Point #{1}.".format(str(address_string),str(delivery_num))
			#print(status_string)
			return postal_x,postal_y
	except:
		print("INVALID ADDRESS")
