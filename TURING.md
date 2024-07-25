# Turing Machine: Execution Logic

## Introduction

A Turing machine is a theoretical computing model that operates on an infinite tape divided into discrete cells. Each cell can hold a symbol from a predefined alphabet. The machine uses a set of rules to manipulate these symbols and perform computations. This document provides an overview of the execution logic of a Turing machine based on a general configuration schema.

## Components of the Turing Machine

### 1. Alphabet
The alphabet is a set of symbols that the Turing machine can recognize and manipulate. These symbols include both the input symbols and any symbols that the machine might write during its operation.

### 2. Blank Symbol
The blank symbol represents an empty cell on the tape. It is a special symbol in the alphabet used to indicate that a cell does not contain any meaningful data.

### 3. States
A Turing machine has a finite set of states. These states represent the different conditions or situations the machine can be in during its operation. The machine starts in an initial state and can transition between states according to the defined rules.

### 4. Initial State
The initial state is the state in which the machine begins its operation. This state must be one of the states defined in the machine's configuration.

### 5. Final States
Final states, also known as accepting states, are the states in which the machine can halt. When the machine reaches a final state, it stops its computation.

### 6. Transitions
Transitions define the rules for moving from one state to another. Each transition specifies:
- The current state and the symbol currently read from the tape.
- The state to transition to next.
- The symbol to write on the tape.
- The action to take, which can be moving the tape head left (LEFT), right (RIGHT), or staying in place (STAY).

## Execution Cycle

The Turing machine operates in a series of steps, collectively known as the execution cycle. The cycle includes the following stages:

### 1. Initialization
- The machine is set to the initial state.
- The tape head is positioned over the first cell of the input tape.

### 2. Reading
- The machine reads the symbol from the cell currently under the tape head.

### 3. Transition Lookup
- The machine uses the current state and the read symbol to look up the corresponding transition rule from the transition table.

### 4. Writing
- The machine writes the specified symbol from the transition rule into the current cell on the tape.

### 5. Moving
- The machine moves the tape head in the direction specified by the transition rule (LEFT, RIGHT, or STAY).

### 6. State Change
- The machine transitions to the next state as specified by the transition rule.

### 7. Halting
- If the machine transitions into a final state, it halts and stops executing further steps.
- If not, it repeats the cycle from the reading step.
