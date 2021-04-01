# Bioimage

---

## Bioimaging course WiSe 2020/2021

### Dennis & Howard's Project  
We want to analyze a series of plant images acquired along a period of ~10 days. There are in total about  60 plants.  
Each image consist of 6 plants arranged in a 3 x 2 grid. However there is **no** identifier for the plant **in** the images, instead the identifier is on a separate text file.  
These identifiers are simply the plant number (1-60).

- Current approach: Do everything in one script if possible.
- ~~The script Loadscript.py load the images in one folder and slice them into six. The script loads the csv file in that folder as well.~~  
- ~~Another script could be written for binarizing the sliced images of individual plants and calculate the area.~~

Our current script, **gcCalc.py** aims to calculate the growth constant of plant(s). It contains 3 functions. One to load plant IDs which is written in a text file inside each folder, another function to load the images, and the last function to make the plot of the plant growth and fit it to an exponential growth function. This fit would yield the growth constant k. 

---

### Notes:
- Data is now included in this repo as well.
- ~~No header for csv file, but the order goes like this:~~  
~~filename, top left, top middle, top right, bottom left, bottom middle, bottom right.~~


