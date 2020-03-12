from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.events import AllSlotsReset
import zomatopy
import send_mail
import json
import pandas as pd
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"35a1d24cad5c2653361da4c1e0daf8da"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		prc = tracker.get_slot('price')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),20)
		d = json.loads(results)
		rest_name_list = []
		rest_location_list = []
		rest_rating_list = []
		rest_price_list = []
		if d['results_found'] == 0:
			dispatcher.utter_message("No Results")
		else:
			rest_name_list = [restaurant['restaurant']['name'] for restaurant in d['restaurants']]
			rest_location_list = [restaurant['restaurant']['location']['address'] for restaurant in d['restaurants']]
			rest_rating_list = [restaurant['restaurant']['user_rating']['aggregate_rating'] for restaurant in d['restaurants']]
			rest_budg_list = [restaurant['restaurant']['average_cost_for_two'] for restaurant in d['restaurants']]
			pd.set_option('display.max_colwidth', -1)
			rest_df = pd.DataFrame({'name':rest_name_list, 'location':rest_location_list, 'rating':rest_rating_list, 'avg_cost_for2':rest_budg_list})
			if prc == "less than 300":
				rest_df_filter = rest_df[rest_df['avg_cost_for2']<300]
			elif prc == "300 to 700":
				rest_df_filter = rest_df[(rest_df['avg_cost_for2']>=300) & (rest_df['avg_cost_for2']<=700)]
			else:
				rest_df_filter = rest_df[(rest_df['avg_cost_for2']>700)]
			rest_df_sorted = rest_df_filter.sort_values(by=['rating'], ascending=False)
			dispatcher.utter_message("-----Here are the top " + cuisine + " restaurants in " + loc + " with avg. budget of " + prc + " Rs. for 2 people-----")
			for row in rest_df_sorted.head(5).iterrows():
				dispatcher.utter_message(row[1]['name']+" in "+row[1]['location']+" has been rated "+row[1]['rating']+"\n")
		return [SlotSet('location',loc),SlotSet('cuisine',cuisine),SlotSet('price',prc)]

class ValidateLocation(Action):
	def name(self):
		return 'validate_location'

	def location_list(self):
		return["ahmedabad","bangalore","chennai","delhi","hyderabad","kolkata","mumbai","pune","agra","ajmer","aligarh","amravati","amritsar","asansol","aurangabad","bareilly","belgaum","bhavnagar","bhiwandi","bhopal","bhubaneswar","bikaner","bokarosteelcity","chandigarh","coimbatore","cuttack","dehradun","dhanbad","durgbhilainagar","durgapur","erode","faridabad","firozabad","ghaziabad","gorakhpur","gulbarga","guntur","gurgaon","guwahatiâ€šgwalior","hublidharwad","indore","jabalpur","jaipur","jalandhar","jammu","jamnagar","jamshedpur","jhansi","jodhpur","kannur","kanpur","kakinada","kochi","kottayam","kolhapur","kollam","kota","kozhikode","kurnool","lucknow","ludhiana","madurai","malappuram","mathura","goa","mangalore","meerut","moradabad","mysore","nagpur","nanded","nashik","nellore","noida","palakkad","patna","pondicherry","prayagraj","raipur","rajkot","rajahmundry","ranchi","rourkela","salem","sangli","siliguri","solapur","srinagar","sultanpur","surat","thiruvananthapuram","thrissur","tiruchirappalli","tirunelveli","tiruppur","ujjain","bijapur","vadodara","varanasi","vasaivirarcity","vijayawada","visakhapatnam","warangal"]
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		if loc.lower() not in self.location_list():
			dispatcher.utter_message("Location not found")
			return [SlotSet('loc_avl',"0")]
		else:
			dispatcher.utter_message("Location found")
			return [SlotSet('loc_avl',"1")]

class ValidateCuisine(Action):
	def name(self):
		return 'validate_cuisine'
	def cuisine_list(self):
		return["chinese","mexican","italian","american","south indian","north indian"]
	def run(self, dispatcher, tracker, domain):
		csn = tracker.get_slot('cuisine')
		if csn == None or csn.lower() not in self.cuisine_list():
			dispatcher.utter_message("Please enter valid cuisine from the given list.")
			return [SlotSet('csn_avl',"0")]
		else:
			dispatcher.utter_message("Cuisine found")
			return [SlotSet('csn_avl',"1")]

class ValidatePrice(Action):
	def name(self):
		return 'validate_price'
	def price_list(self):
		return["less than 300","300 to 700","more than 700"]
	def run(self, dispatcher, tracker, domain):
		prc = tracker.get_slot('price')
		if prc == None or prc.lower() not in self.price_list():
			dispatcher.utter_message("Please enter valid price range from the given list.")
			return [SlotSet('prc_avl',"0")]
		else:
			dispatcher.utter_message("Price range valid")
			return [SlotSet('prc_avl',"1")]
			
class SendMail(Action):
	def name(self):
		return 'mail_results'

	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"35a1d24cad5c2653361da4c1e0daf8da"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		prc = tracker.get_slot('price')
		emailid = tracker.get_slot('emailid')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),20)
		d = json.loads(results)
		rest_name_list = []
		rest_location_list = []
		rest_rating_list = []
		rest_price_list = []
		if d['results_found'] == 0:
			dispatcher.utter_message("No Results")
		else:
			rest_name_list = [restaurant['restaurant']['name'] for restaurant in d['restaurants']]
			rest_location_list = [restaurant['restaurant']['location']['address'] for restaurant in d['restaurants']]
			rest_rating_list = [restaurant['restaurant']['user_rating']['aggregate_rating'] for restaurant in d['restaurants']]
			rest_budg_list = [restaurant['restaurant']['average_cost_for_two'] for restaurant in d['restaurants']]
			pd.set_option('display.max_colwidth', -1)
			rest_df = pd.DataFrame({'name':rest_name_list, 'location':rest_location_list, 'rating':rest_rating_list, 'avg_cost_for2':rest_budg_list})
			if prc == "less than 300":
				rest_df_filter = rest_df[rest_df['avg_cost_for2']<300]
			elif prc == "300 to 700":
				rest_df_filter = rest_df[(rest_df['avg_cost_for2']>=300) & (rest_df['avg_cost_for2']<=700)]
			else:
				rest_df_filter = rest_df[(rest_df['avg_cost_for2']>700)]
			rest_df_sorted = rest_df_filter.sort_values(by=['rating'], ascending=False)
			
		rest_df_html = rest_df_sorted.head(10).to_html(index=False)
		html_msg = "<p>Hi!<br>Here are the top %s restaurants in %s for budget of %s<br><br>"%(cuisine,loc,prc)+rest_df_html+"</p>"
		send_mail.mail_results(emailid, html_msg)
		
class GetMail(Action):
	def name(self):
		return 'get_mail'
	
	def run(self, dispatcher, tracker, domain):
		return [SlotSet('emailid',tracker.latest_message.text)]
		
class ActionSlotReset(Action):  
    	def name(self):         
        	return 'action_slot_reset'  
    	def run(self, dispatcher, tracker, domain):         
        	return[AllSlotsReset()]		
