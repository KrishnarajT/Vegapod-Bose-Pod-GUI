the Vega_Venv folder is the python virtual environment. You can try a couple of things to get stuff working on the pi
The Main thing is to anyway download this entire drive folder. Then, 


First thing:

1. Copy paste the Vega Venv Folder into the desktop or anywhere, and go to it. 
2. In the terminal, cd into that folder, then cd into bin
3. Then type `source activate`, that should activate the environment
4. Then go back to where the rest of the files are, by the rest i mean like source.py and design folder and stuff
5. Then type `python Source.py`
6. If that runs the code, then great! if not, and probably not, then send me the error and try another method. 


Second Thing: 

1. As usual first copy all the files from the drive somewhere in the pi
2. Then you should see requirements.txt in them. 
3. In the terminal cd into where that is and then type `pip install -r requirements.txt`
4. That should then install everything thats necessary into the main python
5. Then again cd to where the Source.py file is then again type `python Source.py`
6. You prolly didnt even reach here, coz you wouldnt have install pyqt5 in step 3. but if did then this should be it. 

Third Thing. 

1. Try to install pyqt6. If it works without any errors, then let me know, ill modify my code for it. We will be able
to make our code compatible with pyqt6 by tomorrow or by sunday im not sure. 

Fourth Thing. 

2. We will have to recode everything on Tkinter. 

Fifth Thing. 

1. Go to the gui_env thing we made in uni today, go to lib folder inside that. 
2. Then just copy the PyQt5 folder from our Vega_Venv/lib/ folder and paste it into the `gui_env/lib/` folder. 
3. Again go to `gui_env/bin/` and then type `source activate`
4. Then cd into where the source.py file is, and type `python Source.py` again. 
5. If that works then also fine.


That is all we can do with respect to GUI in raspberry PI. One of these methods has to work, if not then I wont be able to help any more, someone else will have to 
fine some other way to implement GUIs. 
