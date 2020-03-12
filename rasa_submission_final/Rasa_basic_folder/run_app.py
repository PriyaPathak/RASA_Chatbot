from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-519263176963-520205334277-522261234227-265904113cbd9bbf3e1c315e575bc00e', #app verification token
							'xoxb-519263176963-522365583506-IRKqnJLjNf0xl5rhB2PVO4Kx', # bot verification token
							'wHbev3FDPeZzCOfy3o8zo7Ew', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))