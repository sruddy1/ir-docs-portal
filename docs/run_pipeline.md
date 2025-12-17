# Run the `ir-team-exercise` Pipeline Stored on GitHub

####

## STEP 0 — Clone the Repository <mark>(Only if you haven't yet)</mark>

- Open GitBash

- Run in GitBash:

> ```bash
> cd ~/ir/ir-pipelines
> git clone https://github.com/sruddy1/ir-team-exercise.git
> cd ir-team-exercise
> git checkout -b team-exercise/<your-first-name>
> ```

- Creates a ***branch*** in Github, which is essentially your own copy of the repo.
- Disconnects your changes from the root repo, referred to as "main" or "master"
- Allows changes to be made and pushed to Github without updating "main".
- Prevents conflicts between users who are using separate branches. 

####

## STEP 1 — Update the Pipeline Configuration File

- Open Visual Studio Code (VSC)
  
- Click `File` > `Open File`   

- Navigate to and open

  `C:\Users\<username>\ir\ir-pipelines\ir-team-exercise\configs\config.yaml`

- In file, update:
> **name**: '<First name\>'
> 
> **box_root**: C:/Users/`<username>`/Box

- Save & Close

####

## Step 3 — Build & Activate the Python Virtual Environment

- Open Git Bash

- Run in GitBash

> ```bash
> cd C:/Users/<username>/ir/ir-pipelines/ir-team-exercise
> python -m venv .venv
> source .venv/Scripts/activate
> ```

- `python ...` installs the base version of python locally in the directory, called a `virtual environment`
- `source ...` activates the virtual environment.

> While activated, all installations of python packages that follow will be installed into the virtual environment. Therefore, every pipeline can have its own python installation.

####

## Step 4 — Install Packages into the Virtual Environment

- Install External python packages.

Run in GitBash:
> ```bash
> python -m pip install -r requirements.txt
> ```

- `requirements.txt` contains a list of python packages and their versions that were used to build the pipeline.
- If other packages are installed or different versions of the packages than what is listed in `requirements.txt`, the pipeline is not guaranteed to run successfully.

- Install the Pipeline functions `ir-team-exercise/src/ir_team_exercise` as a Python Package.

Run in GitBash:
> ```bash
> python -m pip install -e .
> ```

- This installs all the `*.py` files contained in `./src/ir_team_exercise` as a python package inside the virtual environment
- Allows you to access the functions inside python scripts, e.g. if you want to use the function `validate_columns` contained inside `./src/ir_team_exercise/checks.py` then you would add this to your python script:
> ```python
> from ir_team_exercise.checks import validate_columns
> ```

####

## STEP 5 — Make the virtual environment selectable by Jupyter Notebook

Run in GitBash:
> ```bash
> python -m ipykernel install --user --name=ir-team-exercise
> ```

- Note: This is not required to run the pipeline.
- This makes the virtual environment accessible by jupyter notebook so that one can run the pipeline interactively using jupyter notebooks.

####

## STEP 5 — Run the Pipeline

Run in GitBash:
> ```bash
> python run.py
> deactivate
> ```

####

## STEP 6 — Check the Output Directory (specific to `ir-team-exercise` repo)

- Open File Explorer
- Navigate to `C:\Users\<username>\Box\Inst Res Collab\Team Retreat Pipeline Results\<First Name>`
- Confirm the pipeline successfully output the results file.

####

## STEP 7 — Push Branch to Github

Run in GitBash:
> ```bash
> git status
> git add .
> git commit -m "Successfully ran pipeline"
> git push -u origin team-exercise/<name>
> ```

- `git status` lets you see what files have been updated, added or deleted.
- `git add .` stages all tracked and untracked files for a commit, i.e. you are telling git I want to push all changes in my local repo to the remote repo. (note: Ignore `LF will be replaced by CRLF...` warning.)
- `git commit -m "message"` packages all the added changes and prepares it for a push to the remote repo. If the commit is important, the message should describe the high level view of what has changed so that you can identify it in case you ever want to revert the repo back to a previous state.
- `git push -u origin team-exercise/<your name>` pushes the commit to the same branch of the remote repo. This does not push to the main repo. The main repo stays the same.

####

## Run Branch a second, third,... time in the Future

Run in GitBash:
> ```bash
> cd ~/ir/ir-pipelines/ir-team-exercise
> git checkout team-exercise/<name>
> ```

Then,
- Update Config File if needed.
- Build environment (only if you haven't previously)
- Activate environment
- Install External Packages (only if requirements have changed since last build)
- Install Pipeline Package (only if changes have been made to the src/ .py files
- Run Pipeline
- Deactivate Environment
- `git add .` > `git commit -m ""` > `git push -u origin <branch>` (if you want to keep a record of any changes to tracked files)

####

## All Commands

####

GitBash:
> ```bash
> git clone https://github.com/<github-account-name>/<name-of-repo>.git
> cd <path-to-repo>/<name-of-repo>
> git checkout main
> git checkout -b <branch-folder>/<branch-name>
> ```

- Update config file using VSC located here: `<name-of-repo>/configs/config.yaml`
- Make sure all the directories that are referenced in the config file exist.

>```bash
> python -m venv .venv
> source .venv/Scripts/activate
> python -m pip install -r requirements.txt
> python -m pip install -e .
> python -m ipykernel install --user --name=ir-team-exercise
> python run.py
> deactivate
> git add .
> git commit -m "Type informative message"
> git push -u origin <branch-folder>/<branch-name>
> ```

####
