from flask import Flask, render_template
from app import app
from flask import jsonify
from flask import request

import pprint, datetime

#To get the current time and split it into hours, minutes and seconds
current_time = datetime.datetime.now().time()
time_now = str(current_time).split(':')
time_hours = time_now[0]
time_mins = time_now[1]
time_sec = time_now[2]
#Departure Event
class departure(object) :
	def __init__(self, station_name, direction, train_id, departure_time, type) :
		self.station_name = station_name
		self.direction = direction
		self.train_id = train_id
		self.departure_time = departure_time
		self.type = type
		
	def __repr__(self):
	 	return self.station_name + " " +  self.departure_time

#Test Data	 	
departure_event = []	 	
departure_event.append(departure("Gilroy", "NB", 222, "21:10", "Bullet") )
departure_event.append(departure("Gilroy", "SB", 212, "10:25", "local") )
departure_event.append(departure("Gilroy", "NB", 242, "11:10", "LS") )
departure_event.append(departure("SanJose", "SB", 222, "09:10", "local") )
departure_event.append(departure("SanJose", "NB", 122, "08:10", "Bullet" ))
departure_event.append(departure("MountainView", 'NB', 222, "10:10", "LS") )
departure_event.append(departure("MountainView", 'NB', 262, "14:10", "LS") )
departure_event.append(departure("SanFrancisco", 'SB', 622, "18:10", "Bullet") )
departure_event.append(departure("SanFrancisco", 'NB', 422, "22:50", "local") )
departure_event.append(departure("SanFrancisco", 'SB', 226, "07:10", "LS") )
departure_event.append(departure("Sunnyvale", 'NB', 292, "09:10", "Bullet") )
departure_event.append(departure("Sunnyvale", 'NB', 922, "22:50", "LS") )
departure_event.append(departure("Hayward", 'SB', 827, "10:10", "Bullet") )	
departure_event.append(departure("Hayward", 'SB', 132, "10:50", "LS") )
departure_event.append(departure("Hayward", 'NB', 422, "11:10", "local") )
departure_event.append(departure("SanBruno", 'SB', 269, "17:10", "local") )
departure_event.append(departure("SanBruno", 'NB', 252, "08:10", "Bullet") )
departure_event.append(departure("SanBruno", 'SB', 262, "22:54", "local") )
departure_event.append(departure("Tamien", 'NB', 223, "19:09", "LS") )
departure_event.append(departure("Tamien", 'NB', 282, "18:56", "local") )

@app.route('/')
@app.route('/index')
def index() :
	return render_template("index_new.html")
	
@app.route('/preferences')
def preferences() :
	if request.cookies.has_key('source') :
	
		if request.cookies['source'] != None :
			a = str(request.cookies['source'])
	else :
		a = 'SanFrancisco'
	
	station = a
	lst = []
	lst.append(a + ":---->")
	for i in departure_event :
		if i.station_name == station and i.departure_time.split(":")[0] >= time_hours and i.departure_time.split(":")[1] >= time_mins:
			lst.append(i.direction + " --- " + str(i.train_id) +" --- " + i.departure_time + " --- " + i.type)  
			
	return jsonify(result = lst)
	
@app.route('/traintable')
def list_of_trains() :
	a = request.args.get('a', 0, type=str)
	station = a
	
	lst = []
	lst.append(a + ":---->")
	for i in departure_event :
		if i.station_name == station and i.departure_time.split(":")[0] >= time_hours and i.departure_time.split(":")[1] >= time_mins:
			lst.append(i.direction + " --- " + str(i.train_id) +" --- " + i.departure_time + " --- " + i.type) 
			  
	return jsonify(result = lst)
    
    