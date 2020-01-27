#importing math module to use sin cos pi arcsin arctan arccos
from math import *
#Calculation of Epicentral distance,Azimuth and Backazimuth - Question
#taking inputs from the user and converting it in radian, rejecting invalid inputs
while True:
	try:
		lat_epc = input("Enter the latitude of earthquake epicentre : ")
	except NameError:
		print("Please enter a number!")
		#again start the loop
		continue
	else:
		break
while lat_epc < -90 or lat_epc > 90:
	print("Please enter a valid no between -90 to +90!")
	lat_epc = input("Enter the latitude of earthquake epicentre : ")
lat_epc = (pi/180)*lat_epc

while True:
	try:
		long_epc = input("Enter the longitude of earthquake epicentre : ")
	except NameError:
		print("Please enter a number!")
		#again start the loop
		continue
	else:
		break
while long_epc < -180 or long_epc > 180:
	print("Please enter a valid no between -180 to +180!")
	long_epc = input("Enter the longitude of earthquake epicentre : ")
long_epc = (pi/180)*long_epc

while True:
	try:
		lat_stn = input("Enter latitude of seismograph station : ")
	except NameError:
		print("Please enter a number!")
		#again start the loop
		continue
	else:
		break
while lat_stn < -90 or lat_stn > 90:
	print("Please enter a valid no between -90 to +90!")
	lat_stn = input("Enter latitude of seismograph station : ")
lat_stn = (pi/180)*lat_stn

while True:
	try:
		long_stn = input("Enter longitude of seismograph station : ")
	except NameError:
		print("Please enter a number!")
	else:
		break
while long_stn < -180 or long_stn > 180:
	print("Please enter a valid no between -180 to +180!")
	long_stn = input("Enter longitude of seismograph station : ")
long_stn = (pi/180)*long_stn

#Asking user whether to use geographic latitude or geocentric latitude
ask_lat = input("Do you want to use geographic latitude ? Type 1 if yes and type 0 if no ")
if ask_lat == 1:
	print("Using Geographic latitude, epicentral distance, azimuth and backaziumth will be calculated.")

	#Calculating epicentral distance
	epc_dist = acos(sin(lat_epc)*sin(lat_stn)+cos(lat_epc)*cos(lat_stn)*cos(long_stn-long_epc))
	epc_dist = (180/pi)*epc_dist
	print ("The epicentral distance is given by : %s degree." %epc_dist)
	epc_dist = epc_dist*111.12
	print ("The epicentral distance is given by : %s km." %epc_dist)
	#Calculating Azimuth
	az = asin((cos(lat_epc)*sin(long_stn-long_epc))/sin(epc_dist))
	az = (180/pi)*az
	print("The azimuth is given by : %s degree." %az)
	#Calculating Backazimuth
	baz = asin((cos(lat_stn)*sin(long_epc-long_stn))/sin(epc_dist))
	baz = (180/pi)*baz
	print("The back azimuth is given by : %s degree." %baz)
else:
	print("Using Geocentric latitude, epicentral distance, azimuth and back-aziumth will be calculated.")
	#calculating geocentric latitude
	b = 6356.7523
	a = 6378.1370
	gcen_lat_epc = atan((b/a)**2*tan(lat_epc))
	gcen_long_epc = long_epc
	gcen_lat_stn = atan((b/a)**2*tan(lat_stn))
	gcen_long_stn = long_stn
	#Calculating epicentral distance
	epc_dist = acos(sin(gcen_lat_epc)*sin(gcen_lat_stn)+cos(gcen_lat_epc)*cos
	(gcen_lat_stn)*cos(gcen_long_stn-gcen_long_epc))
	epc_dist = (180/pi)*epc_dist
	print ("The epicentral distance is given by : %s degree. " %epc_dist)
	epc_dist = epc_dist*111.12
	print ("The epicentral distance is given by : %s km." %epc_dist)
	#Calculating Azimuth
	az = asin((cos(gcen_lat_epc)*sin(gcen_long_stn-gcen_long_epc))/sin(epc_dist))
	az = (180/pi)*az
	print("The azimuth is given by : %s degree." %az)
	#Calculating Backazimuth
	baz = asin((cos(gcen_lat_stn)*sin(gcen_long_epc-gcen_long_stn))/sin(epc_dist))
	baz = (180/pi)*baz
	print("The back azimuth is given by : %s degree." %baz)
######################****************END OF THE
#PROGRAMME**************************#################################
