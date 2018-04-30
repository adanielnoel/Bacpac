# BacPac
This repository contains the code for the project: "BacPac", which we developed in HackDelft 2018. The purpose of the app is to cut costs for backpackers.
The aim of the app is to recommend a path. The app is able to find PoI(points of interest) given a travel time and budget from the user. At the same time, the app connects together people on the same itinerary.

## Description

What really brings this team together is that we all love travelling, and we’ve done a lot of it. In fact, we’ve just recently returned from a minor abroad in Singapore, which gave us the chance to backpack all around SouthEast Asia together.
The only way we were able to make our dream trips through Thailand, Malaysia and Indonesia a reality was by spending countless hours in front of websites expecting us to spend more money than we’d ever seen in our lives for two nights in some torn down bungalow eating expired instant noodles.
The app consists of two services. The first finds optimised itineraries given a geographical area, a budget and a range of dates. This automatically finds landmarks, budget hotels with good reviews in each, allocates time in each landmark based on popularity, considers travelling distance and cost to find the optimal order, and finally generates a comprehensive summary. The second service connects the user to backpackers that are looking for a similar experience. By joining others the user can considerably lower his/her expenses (the amount saved is also calculated).



![Alt text](extra/c1a1dd36-b174-43fb-a886-d2ebaab1e232.jpg?raw=true "Bacpac interface")

![Alt text](extra/945182d2-a1cf-46de-a627-2d3a359885ac-1.jpg?raw=true "Bacpac pathfinder")

![Alt text](extra/aa654dcb-8a4b-4c36-950d-a3b5d657a1c4-1.jpg?raw=true "Bacpac messaging")
## Dataset
Dataset used has been created from the Web and in particular from the Booking Api, which includes review scores, popularity of the location, price of the hotels, extras etc...

## Simulation
To start simulation run: main.py

### Requirements

Python 3.6.2 

Booking APi 2.0

Plotly
