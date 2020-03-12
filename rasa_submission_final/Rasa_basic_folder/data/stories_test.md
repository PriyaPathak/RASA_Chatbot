## Generated Story -6916733993147115547
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - utter_goodbye
    - export
	

## Generated Story 7919520327720085456
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mirzapur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mirzapur"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - export
		

## Generated Story -3963420557996539435
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - utter_goodbye
    - export


## Generated Story
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Ramgarh"}
    - slot{"location": "Ramgarh"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - export


## Generated Story 2241680345240405528
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "chennai"}
    - utter_goodbye
    - export


## Generated Story 3476949032558683348
* greet
    - utter_greet
* restaurant_search{"location": "lakhanpur"}
    - slot{"location": "lakhanpur"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - export


