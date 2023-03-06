# Castro
Castro is an intepreted computer scripting language, with the sole purpose of automating scripting on windows. Setup and installation is below.

### Step 1. - Intepreter Installation
First, make sure you have the python intepreter installed and you have the pyautogui library also installed via pip or conda.<br>
Pip can be found at: https://packaging.python.org/en/latest/tutorials/installing-packages/ <br>
Conda can be found at: https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html<br>

### Step 2. - Run setup.py
Next, after installing please make sure that Castro folder is in your local disk, C:/. After youve made sure that Castro is on your local disk, run setup.py, this will execute a batch file, you can look at it, it has nothing malicious and is just there to link the .ico file and add some other information about .cst files.

### Step 3. - Execution
To execute your file, first make sure your working directory has main.py and your .cst file in it. Once this is all good, type in `py main.py yourfile.cst` and it will execute your file.

### Tutorial:
To see a writeup for Castro, check writeup.txt, that will help with this tutorial

#### Our first program:
For our first program, lets go for the standard hello world. Now, Castro is a computer automation language, so printing to the standard output is only really for logging but its a good first program<br>
`displayf("Hello, World!")`<br>
There it is, the first program, just run this and see if it is sucessful.<br>
In this program `display`, obviously means to display some data, and the `f` after `display` to make it `displayf` means formatted. Essentially, what we are doing here is just displaying a formatted string.<br>

#### Variables:
There are no variables in Castro, nor is there input, i was reluctant to add std output aswell. But, there are 3, predefined Const values, that can be used freely.<br>
`MOUSE_POS` Is one of these, stores the mouse pos and updates every frame.<br>
`PS_INF` Is another, this is a pseudo infinite number, used if you want something to do something forever but dont want to add 100 9's in your code, just ad 'PS_INF'
`BOUNDS` Is the last, this stores the bounds, or resolution of your screen.
again, as another little program, we can display these values so we can get an understanding of how they work, lets display them all.<br>
`displayf("Mouse position = ", MOUSE_POS)
displayf("Kinda infinite = ", PS_INF)
displayf("Screen Res = ", BOUNDS)`
this little program should display all these values 
