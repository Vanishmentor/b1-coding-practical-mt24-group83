# B1 Scientific Coding practical task group 83

Coding practical task for the B1 Scientific Coding course at Oxford (MT26).

GH repo for group 83

Sania Mirza chri7089@ox.ac.uk

Yi Lu spet6182@ox.ac.uk

# Quick IDE Setup Documentation (Windows&MacOS)

0. VSCode & Python Installation

Python - https://www.python.org/downloads/

VSCode - https://code.visualstudio.com/


1. Virtual Environment

Open Vscode and clone the repo from github. After the project is opened, ```ctrl+shift+p``` and type ```>Python:Select Intepreter```.

Then select create virtual environment -> venv -> select a global python -> type ```.venv\replaceWithVEName``` -> install packages -> click ```requirement.txt``` -> confirm

VSCode will automatically activate the virtual environment. 

To do this manually on **Windows**, go to ```.venv\replaceWithVEName\Scripts```. Double click ```activate.bat```, ```deactivate.bat``` to activate or deactivate.

To do this manually on **MacOS**, to activate, execute this in the terminal. **It cannot run it directly by double clicking.** Replace the directory with the correct one pointing to the ```bin/activate``` file. 

```bash
source .venv/replaceWithVEName/bin/activate
```

```bin/activate``` creates a function to deactivate. Just run this in the terminal to deactivate:

```bash
deactivate
```

* ```replaceWithVEName``` is a placeholder used to represents the custom name choosed to identify the virtual environment.


2. Install additional package ```ipykernel```

```ctrl+shift+p``` and type ```>Python:Select Package Manager``` -> pip

Ctrl+`, or create new terminal, make sure the prompt says (replaceWithVEName), indicating the virtual environment is activated, run:

```
pip install ipykernel
```


3. Configure python path

Go to ```.venv\replaceWithVEName\Lib\site-packages```

Create a file with subfix .pth. e.g., zzz_custom.pth. Add a line of the absolute directory path of root directory of the local repository. Save.


4. Add a line ```.venv/``` in file  ```.gitignore``` so the virtual environment does not pollute GitHub repo.


5. Verify Packages

Run this.

```powershell
python -c "import numpy,pandas,matplotlib,ipykernel;print(f'numpy {numpy.__version__} | pandas {pandas.__version__} | matplotlib {matplotlib.__version__} | ipykernel {ipykernel.__version__}')"
```

Output should be something like this:

```powershell
numpy 2.1.1 | pandas 2.2.3 | matplotlib 3.9.2 | ipykernel 7.4.0
```


6. Verify If Jupyter Notebook works

In ```demo.ipynb```, 

Run:

```python
import sys  
print(sys.path)
```

Check for ```uuv_mission``` in the output

# Project Summary

## System Engineering

This role should only edit ```uuv_mission/dynamic.py```.

1. **Cave profile** and **target path** in ```data/mission.csv```. Complete the constructor ```from_csv``` of the Mission class which returns a mission object containing the **cave profile** and **target path** from the .csv. 

2. Complete class ```ClosedLoop```. Create interface for controller to receive ```observation_t``` and output ```actions```.

Use the ```pandas``` package, which helps reading and processing the .csv

## Control Engineering

This role should create a new module for controller and ideally edit that under ```uuv_mission```.

Create a separate module ```controller.py``` under package ```uuv_mission```. The controller should take in ```observation_t``` and return ```actions``` and behave as a PD controller. 

## Integration

The way the controller connects with ```ClosedLoop``` should be communicated before hand. e.g., if a function is used to apply the controller, the system engineer needs to know the name of the function and the name of the module that contains the function.
