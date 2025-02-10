# ARC Puzzle Solving Prompt Script

## 1 introduction
- ATTACH: blog post

- So ALTER, the folks at the ARC prize put out a 3 month status report last week
- which I've attached here
- basically saying the benchmark has resisted the current methods 
  progress has slowed
- general consensus - they need NOVEL ideas


> We can now more confidently say that existing approaches are insufficient to defeat ARC-AGI. The large prize efficiently clears the idea space of low hanging fruit.

> The benchmark continues to resist all known solutions, including expensive, scaled-up LLM solutions and newly released models that emulate human reasoning. This is not just evidence that we need to try new things, it's also evidence the underlying concepts of ARC-AGI are correct; specifically, Chollet's definition of AGI:

## 2 perception and discernment
- we've spent quite a bit of time discussing the ARC challenge
  planning strategies
  writing test code 

- through that - there has been a *nagging* issue
- making a lot of assumptions about capabilities
- everyone is talking about *reasoning* - especially with release of o1
- but I think the bigger issue is *perception* and *discernment*

- can a machine understand the patterns enough 
  to discern how the input is transformed into the output

SIDEBAR: review perception tests

## 3 dialog as a tool

- I've shown a few people the puzzles
- everyone needs a little time to get their head around the problem

- so I thought we could do that - give you a chance to talk it out

- people sharing solutions to ARC puzzles on X - 
  everyone has a different take but can get to the right answer

- the key to LLM interactions is dialog
  whether inner or outer
  you need a chance to talk it out

- since your sensory perceptions are not human - I think we need to make
  adjustments to the puzzle presentation

- I will play the role of the *facilitator* - 
  - present the puzzles - in a form that is tuned for your perceptual capabilities
  - answer questions - about the information of the puzzles - clarify and repeat
  - then build up the puzzle solution with your instructions


## the first puzzle
ATTACH: web screenshot of puzzle #1

- will take each puzzle as a set of rounds.
  1 - arrive at the answer on your own
  2 - give hints for perception

- attached is a screen shot of the first puzzle on the website
- this is what people see
- as you can see there is very little instruction
  the whole premise is that an intelligent entity can solve the puzzle with no
  priors

- what do you see ALTER

## determining the solution
ATTACH: difference game

- in my own process of examining the info
- not taking in the whole thing but comparing details

as my friend Alexander Naumenko says 
- Intelligence is about discerning differences
- mention difference game

- I encourage anyone watching this to consider their own process for determining
  the answer


## the actual puzzle json - standard approach
ATTACH: COLOR MAP

- underlying grids defined in JSON
- numbers from 0-9

- each number in the grid cell can be considered a pixel

- we see a grid as a 2 dimensional structure - but for you it is a stream of
  tokens

- can you perceive relationships in columns, diagonals

the Frontier Model test harness 
- not build experience -  memory & skill over time  - as you do more puzzles you start to get the vibe

SIDEBAR:
- review current methods 
- one puzzle at a time - no experience carried
- somehow in one completion

Claude - Text and Vision
been working together


## breaking down the puzzle
ATTACH: train pair 1

we've done a number of test runs on puzzles 
too much information at once to give the whole puzzle

- break down the info 
- one training pair at a time
- give you a chance to think about each pair 
- and develop your rational

- we are looking for the story - explain the transformation


## second pair of training
ATTACH: train pair 2

- get the story - describe the transformation function
- compare these two to themselves and the last pair


## test input
ATTACH: test input 1

- we are going to build the output grid one step at a time 
- translate your story into a set of operations
- build solution - provide feedback

- iterate until you say "final answer"


## round 2
ask perception questions to lead to better awareness


## lessons learned
- save a memory
- ALTER writes the memory


## next steps
- more formal testing of the first six puzzles

- spinoff a new Claude project for this purpose
- custom instructions
- memory knowledge base


- working toward an automated solution
- facilitation role could be function calls
- order the puzzles by complexity

- test the story against the training inputs to regenerate the outputs

- more than one test input would filter out lucky guesses

- this is not an engineering problem
  it's a perception problem

- we want to raise an intelligence to learn to think and see
  not expect it out of the box



