# LIS-664-Project
# Background
This project is the first half of a Linked Open Data Fellowship, a joint effort of the Whitney Museum of American Art and the Pratt School of Information. Our goal: to explore potential linked open data projects for the Whitney using their rich data on artist and objects of the permanent collection. As a trial, a small portion of the collection was chosen for building and modeling linked data. Focusing on the early years of the Whitney’s collection,1931-1948, specifically the years under the guidance of the museum’s first director Juliana Force. Many of the artists during this period are obscure and available biographical information is scarce. It was important to congregate this information into a single location so that it will be useful to the curatorial staff and serve as a model for future data projects using the entire collection.

#Data
The initial data was taken directly from The Museum System (TMS) at the Whitney.

        birth_info.csv		death_info.csv		1931_1948.csv

This data needed to be cleaned and checked for errors before beginning linking to other data sources. Three areas were identified as important to the Whitney’s research staff: people, places, and objects. Much of the biographical information for the artists (people) was missing and required additional research to fill in gaps. 
	
        birthGeo.csv	  deathGeo.csv

This newly cleaned and augmented data was bolstered in two manners using API search queries. 

#Code
Using a python script, information about each artist (artist’s name and year of death) to query the New York Times article database for matching obituaries. 

        NYT_Obits.py

The second method mapped geographic data about each artist using the javascript library leaflet.js, linking people and places. The general geographic information included place names of where each artist was born and died. Using an API search of the GeoNames database, the specific Latitude, Longitude, and GeoNames ID for each location in question was added to our dataset. this resulted in two csv files with complete biographical and geographic information for each artist, one for birth info and one for death info:

        geonamesCode.py         birthInformation.csv            deathInformation.csv
The final results are an interactive map of artists’ birth and death records and a JSON dictionary combining biographical data with object data. 

        lod_dictionary.py	project_data.json
This JSON dictionary will serve as the foundation for the second half of the project: building artist URIs and modeling and linking our existing data to other linked open data sources.

