############################################################################################ Generated Story 7882715103327446561
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search
    - validate_price
    - action_restaurant
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "rohancn23@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -3898277359004523010
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "rohancn23@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story 7048052416262072766
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai", "price": "more than 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - slot{"price": "more than 700"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "rohancn23@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story 7895360618332411983
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "rohancn23@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
	
############################# STORIES WITH ALL VALID PARAMS AND SEND MAIL NOT CHOESN ############################ 

## Generated Story -6062178547877207050
* greet
    - utter_greet
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Lucknow"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -3898277359004523010
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story 7048052416262072766
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai", "price": "more than 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - slot{"price": "more than 700"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story 7895360618332411983
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
	
########################## STORIES WITH INVALID LOCATION ##########################################	
	
## Generated Story -4032620909897627882
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mirzapur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mirzapur"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story 596563140856362927
* greet
    - utter_greet
* restaurant_search{"location": "wasseypur"}
    - slot{"location": "wasseypur"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -4666364952305038038
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "wasseypur"}
    - slot{"location": "wasseypur"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

############################ STORIES WITH INVALID CUISINE ENTERED #############################

## Generated Story 4851377152726938344
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search
    - validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Delhi"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "rohancn23@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -625261534328078868
* greet
    - utter_greet
* restaurant_search{"cuisine": "moroccan", "location": "Mumbai"}
    - slot{"cuisine": "moroccan"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* email{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story 7895360618332411983
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search
    - validate_cuisine
    - slot{"csn_avl": "0"}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "rohancn23@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
	
################################## STORIES WITH INVALID PRICE #############################
	
## Generated Story 2894257700257618989
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Kochi", "price": "200 to 600"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kochi"}
    - slot{"price": "200 to 600"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Kochi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "rohancn23@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -1273872810590943832
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "less than 500"}
    - slot{"price": "less than 500"}
    - validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "chennai"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "less than 300"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story -3898277359004523010
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "less than 500"}
    - slot{"price": "less than 500"}
    - validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "rohancn23@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

	
#######################

## Generated Story -6662270146725728901
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "rohancn23@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
	
## Generated Story -6662270146725728901
* greet
    - utter_greet
* restaurant_search{"cuisine": "egyptian"}
    - slot{"cuisine": "egyptian"}
    - validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Generated Story 4702155743682014719
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "bsripada@asu.edu"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart


## Generated Story -7138325739664143672
* greet
    - utter_greet
* restaurant_search
    - validate_location
    - utter_ask_location
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search
    - validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - slot{"cuisine": "italian"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_goodbye
    - export
   

## Generated Story 8985425235444342110
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "north indian"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export
 ## Generated Story 2146677127089587799
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search
    - validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export   