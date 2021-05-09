# Mira Ensley-Field 
# Project Proposal

## The purpose of your project.

I love the incredible access to outdoor recreation  I enjoy here in Logan, Utah. Many of my friends and I keep rough track of what we're up to and some of out favorite spots using the free version of 'strava' a popular app that creates visual maps of where you've been and compares you to your friends and other users who have very relaxed privacy settings. This is nice for visualization, but for ecologically-minded people like me, it would even cooler if we could see what sorts of ecosystem gradients and landcover types our activities take us through. 

For this project, I will create a tool that takes  a .gpx file that users can download from the free version of Strava and reports summary information and a visualization to the user with the ecological side of their outdoor activity.

## A description of the data that needs to be supplied in order for your code to work. 

The user must supply a .gpx file. I will see if I can generalize the file type after I've started. I will supply data for the spatial extent of Utah of landcover data (from NLCD), and (ideally) the level II and level III ecoregion data from CEC (Commission for Environmental Cooperation).

## A description of what the output is and how to use it (if the use isn't immediately obvious to somebody new to the project).

The output will be a map with layers showing the ecological variables I'm using in my analysis. It will additionally create a new .shp file with fields that show how much distance of the original .gpx file intersected with the different ecological variables I am using. Lastly, it will include a printed summary of information in terms of percent and total miles spent in different ecoregions and landcover classifications.

## Anything else that is relevant.

It would be also neat if I could find a way to apply this tool to many .gpx files at once. It would also be an interesting project to analyize on a larger scale the sorts of ecosystems and landcover classifications that are favored by different users and different activity types.
