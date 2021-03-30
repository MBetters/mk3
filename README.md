# MK3 Robot Python Code

## First Time Setup, for N00bs

- [Install Git Bash](https://git-scm.com/downloadshttps://git-scm.com/downloads).
  - Make sure you check any checkboxes asking if you want to add `Git` to your `System PATH`.
- Open PowerShell and run `Get-Command git`. The `Source` column should say something like `C:\Program Files\Git\cmd\git.exe`. If it doesn't then redo the first step, since you didn't install `Git` and add it to your `System PATH` properly.
- `cd` wherever you want to clone this repo, then run `git clone https://github.com/MBetters/mk3.git`, then `cd` into this repo (`cd mk3`).
- Run `python -m venv venv`
  - `-m venv` means run the [VirtualEnv](https://docs.python.org/3.8/library/venv.html) module
  - The `venv` at the end is the name of the VirtualEnv to create. Calling it `venv` isn't very creative since that's the name of the `venv` module, but it's clean.
- Run PowerShell as an Administrator (by right-clicking it and clicking `Run as Administrator`), then run `Set-ExecutionPolicy -ExecutionPolicy Unrestricted`. At the prompt, say `A` and hit Enter. This will allow `.\venv\Scripts\Activate.ps1` to run in PowerShell later.
- [Install VS Code](https://code.visualstudio.com/download).
- Open VS Code, do `File` --> `Open Folder...`, and navigate to the `mk3` folder and select it. VS Code should open this folder.
- In VS Code, hit `Ctrl + Shift + Backtick` (the backtick key can be found to the left of the `1` key on your keyboard). That should open a new "Integrated Terminal" at the bottom of your VS Code window.
- The Integrated Terminal should have automatically "activated" the `venv` VirtualEnv, meaning you should see `(venv)` at the beginning of the terminal's prompt.
  - **SIDENOTE 1**: This means commands like `python` will use `venv\Scripts\python.exe` instead of something like `C:\Python38\python.exe`. You can verify this by doing `where python` in the Integrated Terminal. The `venv`'s `python.exe` should be the first one on the list.
  - **SIDENOTE 2**: The same thing should happen when you run `where pip`. Note that `pip` is just a Python package installer.
  - **SIDENOTE 3**: From now on, run all commands for this project in the Integrated Terminal with `venv` activated. If you want to use PowerShell instead, then just remember to first `cd` into this repo's directory, then run `.\venv\Scripts\Activate.ps1`.
- Upgrade `pip`: `python -m pip install --upgrade pip`
- Install all requirements: `pip install -r requirements.txt`
