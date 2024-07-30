import json
import sys


#transform the transition dict to a new one easier to use
# transitions[from_state][read] = {to_state, write, action}
def init_transitions(params: dict) -> dict:
	transitions: dict	= {}

	for from_state in params:
		for transition in params[from_state]:
			transitions[from_state][transition["read"]] = {
				"to_state": transition["to_state"],
				"write": transition["write"],
				"action": transition["action"]
			}


# check only  component required are present and none are missing
def	validate_components(config: dict) -> bool:
	return set(config.keys()) == {"name", "alphabet", "blank", "states", "initial", "finals", "transitions"}


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
	pass


# run every checking function
def validate_machine(config: dict) -> bool:
	return (
		validate_components(config) and
		validate_alphabet(config["alphabet"]) and
		config["blank"] in config["alphabet"] and
		validate_states(config["states"]) and
		config["initial"] in config["states"] and
		validate_finals(config["states"], config["finals"])
	)


# print the machine configuration
def	print_machine(config: dict) -> None:
	print(f"""
Name:		{config['name']}
Alphabet: 	{config['alphabet']}
States:		{config['states']}
Initial:	{config['initial']}
Finals:		{config['finals']}
{ for init_state in config['transitions']:
	for read in config['transition'][init_state]
		""
}
""")


# print tape with head position and latest transition
def	print_current(tape: list, rd_index: int, state: str, transition: dict, blank: str) -> None:
	print_len: int	= 30
	tape_str: str	= ''.join(tape)
	tape_print = ''.join(tape)[:print_len] if len(tape) >= print_len else ''.join(tape) + blank * (print_len - len(tape))
	transition_print = f"({state}, {tape[rd_index]}) -> ({transition['to_state']}, {transition['write']}, {transition['action']})"

	print(f"[{tape_print[:rd_index] + '<' + tape_print[rd_index] + '>' + tape_print[rd_index + 1:]}] {transition_print}")


# check if the machine is stuck in an infinite loop
def	check_loop(history: list) -> bool:
	pass


# run the main routine of the machine
def run(machine: dict, tape: list, loopcheck_interval: int) -> None:
	state: str			= machine["initial"]
	rd_index: int		= 0
	running: bool		= True
	transitions: dict	= machine["transitions"]
	cycle: int			= 0
	history: list		= []
	
	while running:
		cycle += 1
		history.append(f"{rd_index}-{tape[rd_index]}-{state}")
		if cycle % loopcheck_interval == 0 and check_loop(history) == True:
			print("!! error: infinite loop detected")
			exit(1)

		if not state in transitions or not tape[rd_index] in transitions:
			print(f"!! error: transition not found for state {state} and character {tape[rd_index]} !!")
			exit(1)
		
		transition = transitions[state][tape[rd_index]]
		print_current(tape, rd_index, transition, machine["blank"])

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
	
	machine["transitions"] = init_transitions()
	
	