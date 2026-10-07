### Overview

I am making a sandbox in the style of the course simmodeltwin.net. There should be more information in the agents.md about what this specifically means, but in short it is a web-based simulation that contains some data, some rule for how to apply that data, a clock for running the rule forward in time, and some sliders that will let us change the variables and assumptions in the dataset. If an agents.md with more context is missing from this session, please do not complete this prompt, and direct the person running this to tutorial 4. 

### data
Any new processed datasets should go in data/Processed. 

### objectives
**Idea**: 
	A simulation built off of [[Urbanist "Stated" Principles]]
		Simulation trained off of a specific stated principle
			Ex: People stay by the edges of a building, people slow down around trees
	Compared with observations of the actual movement
		Representational play of people moving in a space over multiple instances
	The simulation will be "pitted" against each other in order to uncover
			Who is the most "right"
				#Curiosity Is there a way to make "right" mean "right in this context"
			What combination of simulations make the "most right" assumption

**Point of This**
	Similar to [[Affective Vision]] the output is enriching "stated principles"
		Providing context of when they happen, to what effect, and enriching the actual principle
		The principles are a way of enriching existing behavioral movement models to be
			More attuned to urban movement 
	Discovering if there are a series of principles (thus environmental conditions) that lead to desired actions like socialization
		Is almost the reverse end of [[Affective Vision]]- Looking at the people and the principles that guide their movement not their behavioral types 

**Computational Tools**: 
	- Algorithm is built off of an initial "Stated Principle"
		Two ways to go about it
			1) Identifying when a principle is happening and not. A way to flag when people think a principle should be happening but is not- Is there a way to embed context from a person here
			2) See if there is a principle that is having more of an effect than *default setting* of sed behavior- Ex: walking from place to place, going to recreate
				This is a simulation more to see where people are being *cracked* and by what that might be
	- Pedestrian simulations to model movement (Movement Engine)
		"Social force model for pedestrian dynamics"
		Pedestrian 
	- Multi Agent Debate- Agents then debate with each other to understand why the "real" example is or isnt executing on that action
		Simulations combine to create a number of scenarios to identify which principle is *most at play* 
			#Curiosity Is there a way to signify a missing principle?
				Maybe when simulation does not have a specific principle to attach to an action occurring
	- Informing behavioral patterns from larger simulations/understandings of behavioral movement
		- Looking at [MIT movement simulation](https://www.nature.com/articles/s44284-025-00383-y) 

Output
	This is to be a preposition of simulation type that I will build and how to do it. The data will be scarce and more of an idea of how to build something like this
### data prep - the rule

This is to be a preposition of simulation type that I will build and how to do it. The data will be scarce and more of an idea of how to build something like this

The "rule"- Identify pedestrian movements from a real life example from computational vision analysis. Simulations will then run in the same environment based off of their rule set.
- **Closeness**- Quantifying how close to the path taken the individual simulation is
- **Highlight Nuance**- The shortest path simulation will be the "default" mode. Identify when the individual person goes away from the shortest path. This will "highlight" when a potential Urban stated principle might be at play 

Likely data to use
- Real life footage of a specific urban scene- This is where through object detection softwares pedestrian movements will be identified
- A recreation of the basic geometric signifiers at play- The sandbox the simulations play in
- Contextual movement data- Take from other city wide simulations of urban movement like [MIT movement simulation](https://www.nature.com/articles/s44284-025-00383-y) a contextual understanding of where people are moving in an urban environment can be made. These will likely produce lines that people go along. The point is for the simulations here to identify when they are straying from the path as a way to understand discrepancy

Output
	- The path taken will be overlaid onto a grid. Each grid will have a rating of how much the person stuck to the "default" path and how much they branced off.
	- It will then identify how much the simulation following one principle was "right" in simulating the movement in that specific grid instance

The data should come out as a scoring of how "right" each simulation was and how many times the person strayed from the default path
### the run

In the class parlance, the "run" is applying the rule over time. The interactive variables should work like this:
- Highlighting when the default mode of travel (shortest path) was not being followed in percentages
- Highlighting how correct certain simulations were correct and where
- Simulate an instance of one pedestrian movement per run
	- There are likely multiple pedestrians at a time so this could help identify where they are going
	- Identify after understanding of where they are and where they end up where their default route might be based off of [MIT movement simulation](https://www.nature.com/articles/s44284-025-00383-y) 


### the interactive
Here is an unordered list of what the interactive should have: 
- in the center a map of the observed paths, the times they strayed from the default path and when a stated principle might have been at play
- On the left: a score sheet of the urbanist principles simulated "score sheet"- It is highlighting how right the simulation was in how it was used
- On the right: Highlighting instances when the simulation was off of its default route
- Clicking on items on the left will highlight where sed stated principle was right along the path
- Clicking items on the right will highlight when the path got off of the default route and show the where the other simulations were within each instance
- Bottom: A time bar to scroll through when in the simulation a thing is happening
- Highlighting the pedestrian along its route depending on where it is placed along the timeline 
- limitations- There are a lot of even more micro movements of people negotiating with the crowd that might divert someone from a default path. I do not know yet how to have the simulation incorporate that understanding.

Okay, that is all, please let me know if you have any questions or if anything is not clear.
```
