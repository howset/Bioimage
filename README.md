# Bioimage

---

## Bioimaging course WiSe 2020/2021

Dennis & Howard's Project  
We want to analyze a series of plant images acquired along a period of  ~10 days. There are in total about  60 plants.  
Each image consist of 6 plants arranged in a 3 x 2 grid. However there is **no** identifier for the plant **in** the images, instead the identifier is on a separate text file.  
These identifiers, simply the plant number (1-50), have been combined in a csv file **inside** each folder.

- The script Loadscript.py load the images in one folder and slice them into six. The script loads the csv file in that folder as well.  
- Another script could be written for binarizing the sliced images of individual plants and calculate the area.

---

### Notes:
No header for csv file, but the order goes like this:  
filename, top left, top middle, top right, bottom left, bottom middle, bottom right.


