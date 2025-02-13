# CIDM6330
  For CIDM 6330 - Software Engineering

## A problem for which a designed software system could assist in improving or solving
  A small beach cleanup program relies on volunteers to collect, count, and dispose of discarded cigarette butts. The manual counting portion of this process proves to be time consuming. Other methods of measurement are either difficult or imprecise such as visual estimation or measuring by weight as the butts can be of varying sizes and can sometimes be waterlogged. Manually counting requires physically touching the butts is also undesirable and unsanitary for volunteers.

## The domain of practice or interest in which this problem is situated
This domain of practice for this problem is environmental advocacy and tracking. It will require knowledge in at least and not limited to:
  1. Mobile app development
  2. Image recognition
  3. Cloud storage and Processing
  4. Backend and APIs
  5. Dashboards and Analytics
  6. Location Services

Many of these areas can be vertically integrated using google cloud platform but there are other services available as well. If we want to have cross platform viability with a single codebase then I will likely need to learn React/Javascript.

## Your personal/professional interest in this problem domain
  I am a volunteer Treasurer for the Galveston chapter of the environmental advocacy group, Surfrider Foundation. One initiative unique to our chapter is the 'Hold On To Your Butts'. National headquarters has mentioned in roundtable meetings about using our local initiative as a pilot for a national beach cleaning app for Surfrider. The scope will eventually be larger as the foundation protects not just beaches but all waterways and resources in each given chapter's area. For example, our chapter's zone covers from bodies of water from Dallas west to central Texas down the Louisiana border and to Freeport.

## What sort of system you want to prototype that would allow you to better understand the problem, problem domain, or design considerations thereon.
  I want to prototype a mobile application that makes it easier and more efficient for volunteers to collect cigarette butts. The basic premise is that volunteers can take photos of the butts collected using a dedicated mobile application on their smartphone that will upload the images to a cloud based image recognition program to count the number of butts collected which will then feed data into a postgres database and then a live online dashboard. To increase user engagement (for the greater good) it may be wise to gamify the collection of trash to motivate users to seek out more cleanup opportunities.


## Introduction

  This project addresses the inefficiency and unsanitary conditions of manually counting cigarette butts during beach cleanups. We propose a mobile app to streamline this process using image recognition and cloud technology. Situated in environmental advocacy, the app will enhance volunteer efforts by automating data collection and providing real-time analytics.
  As a volunteer Treasurer for the Surfrider Foundation's Galveston chapter, I am invested in expanding our 'Hold On To Your Butts' initiative. This app will enable volunteers to photograph collected butts, automatically count them, and visualize data on a live dashboard, supporting broader conservation efforts.

## Requirements Statements

###  User Stories

###  Use Cases

###  Features

###  Gherkin Validation

Scenario: Volunteer (User) Photographs Cigarette Butts
<br> &nbsp;    Given   a volunteer has created a user profile
<br> &nbsp;      And   has a smartphone with working camera
<br> &nbsp;      And   collected cigarette butts
<br> &nbsp;     When   the user takes a photo of the collected butts
<br> &nbsp;     Then   the app uploads the image to the cloud
<br> &nbsp;      And   the image recognition software counts the butts
<br> &nbsp;      And   the count is stored in a PostGreSQL database
<br> &nbsp;      And   the data is displayed on a live dashboard

###  Scenario: Image recognition and cigarette butt count
Given a volunteer is using the mobile app while collecting cigarette butt canisters
When they take a photo

## Specifications

###  Concept

###  UX Notes

###  Interfaces (Controls)

### Behaviors
Feature/PackageA
![UML_Class_Diagram drawio (1)](https://github.com/user-attachments/assets/c7febc47-feff-4cc1-ba3d-3642ba321d6e)

  Feature/PackageN
