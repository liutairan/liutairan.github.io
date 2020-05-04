---
layout: project-page
title: Multi-Agent System Formation Control
excerpt: "Just about everything you'll need to style in the theme: headings, paragraphs, blockquotes, tables, code blocks, and more."
categories: [projects]
comments: false
---

### Background   
Formation control is the behavior that a group of agents acquire and maintain a prescribed geometric shape in space.   

The agents could be ground vehicles, spaceships, satellites, aerial vehicles, etc.   

Formation control can be classified as formation shape problem and formation maneuvering problem.   

Three methods are typically used in formation shape control: a) regulate the global position of each agent; b) regulate the relative position of agent pairs; or c) regulate a set of inter-agent distances (magnitude of the relative position vector).   

The first method, also called position-based control, requires absolute position information which either comes from an external sensor such as an overhead camera or optical motion capture system (e.g. Vicon), or onboard sensors such as a camera or GPS. This method is centralized and thus has a single point of failure. The second method, sometimes called displacement-based control, requires the agents to have a common global coordinate frame or that their local coordinate frames be aligned which may not be feasible in practice. Unlike the previous two methods, the feedback variables in the third method, also known as distance-based control, can be calculated in each agent's local coordinate frame, which does not have to be aligned with a global coordinate frame or with each other. As a result, the desired formation is, at best, only acquired up to translation and rotation; i.e., the agents can converge to any formation that is isomorphic to the desired one.   

In our research, we mainly use the third method, i.e., distance-based control.   

### Problem Statement

### Solutions   

![I'm a relative reference to a repository file](../../Pics/formation_control/FormationShapeMethodsCompare.png)

### Experimental Validations   

##### Switching formation shape control with distance + area/angle feedback   

I would like to express my special thanks to my colleague Victor Fernandez-Kim, for creating this testbed to run the experiments.


<iframe class="youtube-player" type="text/html" width="360" height="300" src="https://www.youtube.com/embed/eE_6TtT_Rao" frameborder="0" allowfullscreen></iframe>

<iframe class="youtube-player" type="text/html" width="360" height="300" src="https://www.youtube.com/embed/MM_Ag7OJfnM" frameborder="0" allowfullscreen></iframe>

##### Distance and area control of planar formations: Maneuvering   

I would like to express my special thanks to Robotarium @ Georgia Tech for their help in running the experiments.

<iframe class="youtube-player" type="text/html" width="360" height="300" src="https://www.youtube.com/embed/yJQnG5hxHcc" frameborder="0" allowfullscreen></iframe>
