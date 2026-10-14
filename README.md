# B1 Scientific Coding practical task group 83

Coding practical task for the B1 Scientific Coding course at Oxford (MT26).

GH repo for group 83
Sania Mirza chri7089@ox.ac.uk
Yi Lu spet6182@ox.ac.uk

Quick IDE Setup Documentation (Windows)

0. VSCode & Python Installation

Python - https://www.python.org/downloads/

VSCode - https://code.visualstudio.com/

1. Virtual Environment

Open Vscode and clone the repo from github. After the project is opened, ```ctrl+shift+p``` and type ```>Python:Select Intepreter```.

Then select create virtual environment -> venv -> select a global python -> type ```.venv\replaceWithVEName``` -> install packages -> click ```requirement.txt``` -> confirm

VSCode will automatically activate the virtual environment. To do this manually, go to ```.venv\replaceWithVEName\Scripts```. ```activate.bat```, ```deactivate.bat``` are self-explanatory.

2. Install additional package ```ipykernel```

Open Vscode and clone the repo from github. After the project is opened, ```ctrl+shift+p``` and type ```>Python:Select Package Manager``` -> pip

Ctrl+`, or create new terminal (powershell), make sure the prompt says (replaceWithVEName), indicating the virtual environment is activated, run:

```Powershell
pip install ipykernel
```

3. Add ```uuv_mission``` package so the Jupyter note book can import it

Go to ```.venv\replaceWithVEName\Lib\site-packages```

Create a file with subfix .pth. e.g., zzz_custom.pth. Add a line of the absolute directory path of ```uuv_mission```. Save.

4. Add a line ```.venv/``` in file  ```.gitignore``` so the virtual environment does not get uploaded to GitHub

5. Verify Packages

Run this.

```Powershell
python -c "import numpy,pandas,matplotlib,ipykernel;print(f'numpy {numpy.__version__} | pandas {pandas.__version__} | matplotlib {matplotlib.__version__} | ipykernel {ipykernel.__version__}')"
```

Output should be something like this:

```Powershell
numpy 2.1.1 | pandas 2.2.3 | matplotlib 3.9.2 | ipykernel 7.4.0
```

6. Verify If Jupyter Notebook works

In ```demo.ipynb```, 

Run 

```Python
import sys  
print(sys.path)
```

Check for ```uuv_mission``` in the output
