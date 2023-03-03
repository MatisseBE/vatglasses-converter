
## File preparations

  

#### 'Your GNG ESE file'

In your text editor, perform a find and replace using REGEX (in VSC enable this icon:)![show regex symbol](https://cdn.discordapp.com/attachments/1071509192680153239/1071831914526298203/image.png)
This action will convert all your ES coordinates to the coordinate system used by vatglasses.

**Attention**

A) Convert for all hemispheres NESW (North, East, South, West). Currently, only coordinates that are in the NE hemisphere are converted. Perform as many find and replaces as neccessary.

B) Check if the delimiter between two hemispheres is correct in the REGEX. Here ':' is used (character before "E"). Adapt if neccesarry and/or perform as many find and replaces as neccessary.
```
Find: N0?([0-9]{2}).([0-9]{2}).([0-9]{1,2})(.[0-9]{3,})?:E([0-9]{3}).([0-9]{2}).([0-9]{1,2})(.[0-9]{3,})?
Replace: $1$2$3:$5$6$7
```

  Example:
```
ESE coordinate line
COORD:N51.01.22:E005.13.15
COORD:N51.02.16:E005.05.08

New coordinate line with vatglasses coordinate system
COORD:510122:0051315
COORD:510216:0050508
```
 
### 'File with sectors for airspace.txt'
This file will contain the sector data from ESE. Take a look at the example.
This are all the sectors with their corresponding owners and sectorlines (borders).
From the GNG ESE, copy all **sector data** to this file as shown in the example. It may include comments. 

**Important** Make sure to only include sectors from your vACC! You can do this by either excluding them from this txt file (CTR+F) OR filter them out later in the script with your own code. You should also leave out GND and DEL sectors.

### 'File with sectorslines for airspace.txt'
This file will contain the **border coordinates** from ESE. Take a look at the example. 
These are all the borders that surround a sector (at a certain FL-block).
From the GNG ESE, copy all **sectorlines** to this file as shown in the example. It may include comments. 
No need to filter here.

### 'File with positions for positions.txt'
This file will contain **positions** from the ESE. Take a look at the example. 
From the GNG ESE, copy all **positions** to this file as shown in the example. It may include comments. 

 
### Open 'create airspace from ESE .py' file
This file creates the "airspace" key in the vatglass json.
Here will will need to make some adjustments so the file can run without any problems. 

On line 178 you will find the function *Findname(sector)*. This function is used to assign a sector to a group based on the name of the sector. The function strips the sector name and checks to which group it must belong and assigns it. You will need to change this function to your needs and groups. Don't forget to also change the first line.

**Attention**
"groups" Is another key in the vatglasse's json. You will need to create this part of the json manually. Make sure the groupkeys are identical between the function and json. Corresponding example for Belux in the vatglasse's json: 
```
"groups":{
	"EBBU":{
	"name":"Brussels"
	},
	"ELLX":{
	"name":"Luxembourg"
	},
	"EDYY":{
	"name":"Maastricht"
	},
...
}
```

Under this the *Findname(sector)* function, line 203 for me, you will find a for loop. Change the *name* variable such that it works with your setup. Just like before the example takes the sectorname from ESE and makes some amendments.

Awesome! You can now run the file!

### Open 'create POSITIONS from ESE .py' file
This file creates the "positions" key in the vatglass json.
The *similarhex(position)* function is an attempt at giving every position group (TWR/APP/ACC) a color group with every position of that group having a different shade.  This function is pretty bad and that's okay. You can change the colors of sectors afterwards or play with the function yourself. You might want to change the initial default color groups though, but if not, it will all still work just fine.

If you want to (include or) exclude a certain position like, amend line 88. 

### Open 'create a PART OF AIRPORTS .py' file
This file does most of the work for the "airports" key. Use [vatspy-data-project](https://github.com/vatsimnetwork/vatspy-data-project/blob/master/VATSpy.dat) to get name, callsign and coordinates of all the controlled airports. Paste it in the Python file and run it. 
**Important** 
Add a topdown structure!  (It's actually **bottum up** in this case - starting with the lowest radar position and **not TWR**. I.e.: BA is the controller ID for Brussels Arrival)
 ```
 "EBBR":{
"callsign":"Brussels",
"coord":[50.9013,4.4901],
"topdown":["BA","BD","BW","BE"]
}
```
Optional: If there is no topdown structure, or the airport in uncontrolled, you can add run the file again and add the value of the output straight to the vatglass json without a new key.
![show regex symbol](https://cdn.discordapp.com/attachments/727230055301906483/1080591518273900565/image.png)

### What's next?
1. Create a json entry with keys:
* airspace - You made this with the script.
* groups - As explained earlier (check example). 
	* Make sure that NO sector has been assigned group "OTHER". You will need to check your *findname(sector)* function and make sure that all sectors have a condition made for them.
	* OTHER may not be a key in your groups json. 
* positions - You made this with the script.
* callsigns - You can probably copy paste a large portion of this one from other vACCs (Check example).
* airports - You partly made this with a script
* (the optional uncontrolled airports as explained under Open 'create a PART OF AIRPORTS .py' file.)

2. Next, format the file using the Prettier - Code formatter extention in VSC.
3. Upload under the assigned file in the beta repo as assigned by vatglasse's dev. 

