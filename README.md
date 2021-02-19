# MK3 Robot Python Code

## First Time Setup, for N00bs

- [Install Git Bash](https://git-scm.com/downloadshttps://git-scm.com/downloads).
  - Make sure you check any checkboxes asking if you want to add `Git` to your `System PATH`.
- Open PowerShell and run `Get-Command git`. The `Source` column should say something like `C:\Program Files\Git\cmd\git.exe`. If it doesn't then redo the first step, since you didn't install `Git` and add it to your `System PATH` properly.
- Run `git clone `
- `cd` into this directory (directory is another word for folder).
- Run `py -3 -m venv venv`
  - `py -3` means run Python 3
  - `-m venv` means run the [VirtualEnv](https://docs.python.org/3.8/library/venv.html) module
  - The `venv` at the end is the name of the VirtualEnv to create. Calling it `venv` isn't very creative since that's the name of the `venv` module, but it's clean.
- [Install VS Code](https://code.visualstudio.com/download).
- Close and reopen PowerShell.
- `cd` into this directory, then run `code .`. This folder should open in VS Code.
- Close PowerShell.
- In VS Code, hit `Ctrl + Shift + Backtick` (the backtick key can be found to the left of the `1` key on your keyboard). That should open a new "Integrated Terminal" at the bottom of your VS Code window. The Integrated Terminal should automatically "activate" the `venv` VirtualEnv, which will prepend `(venv)` to the shell's prompt. This means commands like `python` will use `venv\Scripts\python.exe`. You can verify this by doing `where python`. The `venv`'s `python.exe` should be the first one on the list. The same thing should happen when you run `where pip`. Note that `pip` is just a Python package installer.
- Upgrade your `venv`'s `pip` by running `python -m pip install --upgrade pip` in the Integrated Terminal.
