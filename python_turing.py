import json
import sys


#transform the transition dict to a new one easier to use
# transitions[from_state][read] = {to_state, write, action}
def init_transitions(params: dict) -> dict:
	transitions: dict	= {}

	for from_state in params:
		transitions[from_state] = {}
		for transition in params[from_state]:
			if from_state in transitions and transition["read"] in transitions[from_state]:
				print(f"!!! error: double definition for transition transition [{from_state}][{transition['read']}]!!!")
				exit(1)
			transitions[from_state][transition["read"]] = {
				"to_state": transition["to_state"],
				"write": transition["write"],
				"action": transition["action"]
			}
	return transitions


# check only  component required are present and none are missing
def	validate_components(config: dict) -> bool:
	return set(config.keys()) == ["name", "alphabet", "blank", "states", "initial", "finals", "transitions"]


# ensure every member is a single character and there are no duplicates
def validate_alphabet(alphabet: list) -> bool:
	return (
		all(
			isinstance(letter, str)
			and len(letter) == 1
			for letter in alphabet
		) and
		len(alphabet) == len(set(alphabet))
	)


# ensure there are no duplicates
def validate_states(states: list) -> bool:
	return len(states) == len(set(states))


# ensure final states are in the states list and there are no duplicates
def validate_finals(states: list, finals: list) -> bool:
	return (
		all(
			final in states
			for final in finals
		) and
		len(finals) == len(set(finals))
	)


# ensure every transition is well defined  with :
# initial state from states list, read char from alphabet, to_state from states, action is in list {LEFT, RIGHT, STAY}
# ensure there aren't two transitions with the same initial state and read char
def	validate_transitions(config: dict) -> bool:
	transitions:dict	= config["transitions"]

	for from_state in transitions:
		if from_state in config["finals"]:
			return False
		for transition in transitions[from_state]:
			if (
				from_state not in config["states"] or
				set(transition.keys()) != {"read", "to_state", "write", "action"} or
				transition["read"] not in config["alphabet"] or
				transition["to_state"] not in config["states"] or
				transition["write"] not in config["alphabet"] or
				transition["action"] not in {"LEFT", "RIGHT", "STAY"}
			):
				return False
	return True




# run every checking function
def validate_machine(config: dict) -> bool:
	return (
		validate_components(config) and
		validate_alphabet(config["alphabet"]) and
		config["blank"] in config["alphabet"] and
		validate_states(config["states"]) and
		config["initial"] in config["states"] and
		validate_finals(config["states"], config["finals"]) and
		validate_transitions(config)
	)


# print the machine configuration
def print_machine(config: dict) -> None:
	transitions_str:str	= ""

	for init_state in config['transitions']:
		for transition in config['transitions'][init_state]:
			to_state = transition['to_state']
			write = transition['write']
			action = transition['action']
			read = transition['read']
			transitions_str += f"({init_state}, {read}){' ' * (10 - len(init_state))} -> ({to_state}, {write}, {action})\n"

	print(f"""Alphabet:       {config['alphabet']}
States:         {config['states']}
Initial:        {config['initial']}
Finals:         {config['finals']}

{transitions_str}""")


# print tape with head position and latest transition
def	print_current(tape: list, rd_index: int, state: str, transition: dict, blank: str) -> None:
	print_len: int		= 30
	tape_str: str		= ''.join(tape)
	tape_print			= ''.join(tape)[:print_len] if len(tape) >= print_len else ''.join(tape) + blank * (print_len - len(tape))
	transition_print	= f"({state}, {tape[rd_index]}){' ' * (10 - len(state))} -> ({transition['to_state']}, {transition['write']}, {transition['action']})"

	print(f"[{tape_print[:rd_index] + '<' + tape_print[rd_index] + '>' + tape_print[rd_index + 1:]}] {transition_print}")


# run the main routine of the machine
def run(machine: dict, tape: list) -> None:
	state: str			= machine["initial"]
	rd_index: int		= 0
	running: bool		= True
	transitions: dict	= machine["transitions"]
	tape				= list(tape)
	
	while running:
		if state in machine["finals"]:
			return
		if not state in transitions or not tape[rd_index] in transitions[state]:
			print(f"\n!! error: transition not found for state {state} and character {tape[rd_index]} !!\n")
			exit(1)
		
		transition = transitions[state][tape[rd_index]]
		print_current(tape, rd_index, state, transition, machine["blank"])

		tape[rd_index] = transition["write"]
		state = transition["to_state"]
		if transition["action"] == "LEFT":
			rd_index -= 1
		elif transition["action"] == "RIGHT":
			rd_index += 1
		


# get args from launching command, parse the json config file, validate the machine and the tape, then run the main routine
if __name__ == '__main__':
	args: list		= sys.argv[1:]
	machine: dict	= {}

	if len(args) != 2:
		print("wrong number of arguments")
		exit(1)
	
	with open(args[0], 'r') as file:
		machine = json.load(file)
	
	if not validate_machine(machine):
		print("invalid configuration")
	
	
	print(f"""
*************************************************************************
*                                                                       *
*                       {machine["name"] + ' ' * (48 - len(machine["name"]))}*
*                                                                       *   
*************************************************************************
"""
	)
	print_machine(machine)
	print("*************************************************************************\n")

	machine["transitions"] = init_transitions(machine["transitions"])
	run(machine, args[1])
	
	