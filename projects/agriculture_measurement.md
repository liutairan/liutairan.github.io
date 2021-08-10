---
layout: project-page
title: Aerial Robotics in Agricultural Measurements
excerpt: "Just about everything you'll need to style in the theme: headings, paragraphs, blockquotes, tables, code blocks, and more."
categories: [projects]
comments: false
---

### Project goal

The goal of this project was to create a robotic system that can capture information within or under the PLANT canopy such that the changes of the plants can be detected as early as possible.

### My role

Researcher

### My contribution

* Built an open-source drone platform for field monitoring
* Designed a telescopic structure for measurements under/within the plant canopy
* Developed an open-source graphical user interface (GUI) to define tasks, generate desired flight trajectory, and monitor drone's status and real-time trajectory

### Background

Drones have been used in precision agriculture for many years. In most of the applications, drones fly over the field and collect top surface data/images. Then, the data/images collected will be processed later to analyse the potential issues in the field. In this project, we use drones to do something different.

<br />    

The plant studied in this research is cotton. Cotton is a significant source of fabric and has been used in the textile industry for centuries. Nowadays, cotton is still a cash crop around the globe. The United States, produced over 20 million bales of cotton in 2017, is the largest raw cotton fiber exporter in the world. In the United States, most cotton is grown in 17 southern-tiered states, with Texas and Georgia ranking the top two.

<br />    

Two types of factors can cause serious economic devastation: cotton diseases and environmental conditions. Cotton diseases have existed and been noticed since a long time ago. These diseases are responsible for enormous losses in cotton production and quality. For example, Fusarium Hardlock of cotton, which is mainly caused by fungus Fusarium verticillioides, severely reduced the yield in Florida and other southeastern states. Cotton blue disease, a viral disease first identified in Alabama in 2017, has been subsequently found in most of the states close to it. There are more examples in the literature, such as cotton leaf curl disease (CLCuD), cotton root rot, pink bollworm infestation, Seedling Disease. The other factor affecting the growth of cotton plant is the adverse environmental conditions. The cotton plant has indeterminate growth habit, and is extremely sensitive to adverse environmental conditions, such as nutrition, moisture and temperature. Any deviation from the idealized growing conditions could cause the decrease of yield.

<br />    

For the serious economic devastation caused by these factors, successfully identifying the changes in plants and taking actions as early as possible is a crucial task. Cotton exhibits strong specific leaf nitrogen gradients in the canopy. The leaves closest to the sun are generally more photosynthetically active, but it also means that nutrition deficiency may not be captured very early if observed from an overhead platform. Since a lot of changes are revealed much earlier from in-canopy measurements, searching unexpected features in/under the canopy would be beneficial. Additionally, the in-canopy measurements can also provide an estimation of the detailed stage information of the growth cycle or even appropriate drainage and harvest date. This kind of data can help growers make decisions such as when to defoliate, terminate irrigation, or harvest.

<br />    

However, searching infected plants or collecting those in/under-canopy data over vast stretches of land is tedious, labor-intensive, and time-consuming. This kind of field operation is hardly a viable approach without the assistance of remote sensing and automated field robots. The remote sensing technologies, which have been applied to cotton disease detection for more than a century and widely used in cotton growth measurements, generally cannot penetrate the canopy and collect data in/under it.

<br />    

A feasible solution is to deploy a collaborative team composed of high-altitude-flying unmanned aerial vehicles (UAVs) and low-altitude-flying UAVs with different functionalities. Specifically, the high-altitude team is faster in flying speed, and has a better vision of the overall situation and wider view of the whole field; and the low-altitude team equipped with robot arms, which can penetrate the canopy, has better in-depth sensing capability.

<br />    

<img style="display:block; margin-left: auto; margin-right: auto;" src="../../Pics/agriculture_measurement/Drone-over-plants.png" width="480">
Figure 1: Drones fly over the fields to collect top surface data in the traditional approaches.

<br />    

<img style="display:block; margin-left: auto; margin-right: auto;" src="../../Pics/agriculture_measurement/Drone-with-arm-in-bush.png" width="480">
Figure 2: Drones use telescopic robot arms/structures to penetrate the canopy and collect the data in/under canopy.

### Scientific Progress

So far, we have built an open-source drone platform for field monitoring, in which the drone is equipped with manipulation capability through a custom-designed telescopic structure that can carry a camera/sensor. The telescopic structure, when deployed, can penetrate through the plant canopy and collect information under/within the canopy – something that is not possible to do with the available technologies in the field today. The telescopic structure in our design is collapsible and therefore does not affect the drone taking off or landing. The camera/sensor on this structure can be replaced to capture various conditions. Furthermore, our team has recently started to develop an open-source software platform for a swarm deployment and monitoring. A graphical user interface (GUI) has been developed with basic capabilities for defining tasks, e.g., by manually choosing desired flight trajectory and also by automatically generating the desired flight trajectory from the coverage area. With the drone in mission, status data (e.g., location, altitude, attitude, battery level) are transmitted and displayed on the GUI. The GPS location of the drone is also shown on the map so that the operator can monitor the real-time trajectory along with the desired one. The platform developed has been tested so far for a single drone and we plan to expand the system to a swarm of drones in the short future.

### Our Testbed

![On the bench](../../Pics/agriculture_measurement/OntheBench3.jpg)
Figure 3: The drone platform used in this research.

<img style="display:block; margin-left: auto; margin-right: auto;" src="../../Pics/agriculture_measurement/PoleFold.png" width="360">
Figure 4: Drone in the air, telescopic structure folded.

<img style="display:block; margin-left: auto; margin-right: auto;" src="../../Pics/agriculture_measurement/PoleUnfold.png" width="360">
Figure 5: Drone in the air, telescopic structure unfolded.


![On the bench](../../Pics/agriculture_measurement/Mission.png)
Figure 6: Mission planner.

![On the bench](../../Pics/agriculture_measurement/Monitor.png)
Figure 7: Real-time drone status monitoring from a computer.
