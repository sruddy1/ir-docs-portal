# Run an Existing Pipeline Stored on GitHub


####

## Update Configuration File

####

>#### STEP 0 — Clone the Repository
>
>> - Open GitBash
>>
>> - `cd .../ir/ir-pipelines`
>> 
>> - if you haven't cloned the repo yet: `git clone https://github.com/sruddy1/ir-team-exercise.git`
>>
>> - `cd ir-team-exercise`
>>
>> - `git checkout -b team-exercise/<your-first-name>`
>>
>>   - Creates a ***branch*** in Github, which is essentially your own copy of the repo.
>>   - Disconnects your changes from the root repo, referred to as "main" or "master"
>>   - Allows changes to be made and pushed to Github without updating "main".
>>   - Prevents conflicts between users who are using separate branches. 

>#### STEP 1 — Open Visual Studio Code
>
>####
>
>#### STEP 2 — Open the Pipeline Configuation File in VSC
>
>> - Click `File` > `Open File`
>>   
>> - Navigate to `C:\Users\<username>\ir\ir-pipelines\ir-team-exercise\configs\config.yaml`
>
>####
>
>#### STEP 3 — Change file paths to match your local machine
>
>> - **name**: 'First name'
>> - **box_root**: C:/Users/`<username>`/Box
>
>####
>
>#### STEP 4 — Save & Close

####

## Build & Activate the Python Virtual Environment

####

>#### STEP 1 — Open Git Bash
>
>####
>
>#### STEP 2 — Deactivate Existing Environment
>
>> - `deactivate`
>>   - a `deactivate: command not found` is good!
>>   - if the error does not appear that's also good, and it means you had an environment active that is now deactivated.
>
>####
>
>#### STEP 3 — Build the Virtual Environment
>
>> - `cd C:/Users/<username>/ir/ir-pipelines/ir-team-exercise`
>>   
>> - `python -m venv .venv`
>
>#### 
>
>#### STEP 4 — Activate the Virtual Environment
>
>> - `source .venv/Scripts/activate`
>>
>>   - This loads the python version used to build the pipeline.
>

####

## Install Packages into the Virtual Environment

####

>#### STEP 1 — Install External Python Packages into the Virtual Environment
>
>> - `pip install -r requirements.txt`
>>
>>   - `requirements.txt` contains a list of packages along with their version numbers used to build the pipeline.
>
>####
>
>#### STEP 2 — Install the Pipeline Python Package into the Virtual Environment
>
>> - `pip install -e .`
>>
>> - This installs all the `*.py` files contained in `./src/ir_team_exercise` as a python package inside the virtual environment
>>
>> - Allows you to access the functions inside python scripts, e.g. if you want to use the function 'validate_columns' contained inside `./src/ir_team_exercise/checks.py` then you would add this to your python script:
>>
>>   `from ir_team_exercise.checks import validate_columns`
>
>####
>
>#### STEP 3 — Make the virtual environment selectable by Jupyter Notebook
>
>> - `python -m ipykernel install --user --name=myenv --display-name "ir-team-exercise"`
>
>####


####

## Run the Pipeline

####

>
> - `python run.py`
>
> - `deactivate`
>


####

## Check Results Folder

####

> - Use File Explorer to navigate to `C:\Users\<username>\Box\Inst Res Collab\Team Retreat Pipeline Results\<First Name>` and confirm the pipeline successfully output the results file.

####

## Push Branch to Github

####

> - `git status` : see what files have been changed locally
>   
> - `git add .` : add all changed files to the commit
>> - Ignore `LF will be replaced by CRLF...` warning.
>
> - `git commit -m "Successfully ran pipeline"` : collect changes into a commit
>   
> - `git push -u origin team-exercise/<name>` : push commit to the github branch of the repo (this does not change the main repo)

####

## Run Branch in the Future

####

> - Open Git Bash
> - `cd C:/Users/<username>/ir/ir-pipelines/ir-team-exercise` : Navigate to the repo on your local machine.
> - `git checkout team-exercise/<name>` : if the analysis hasn't been updated, otherwise git checkout a new branch from main as done previously
> - Then,
>> - Update Config File if needed.
>> - Build environment (only if you haven't previously)
>> - Activate environment
>> - Install External Packages (only if requirements have changed since last build)
>> - Install Pipeline Package (only if changes have been made to the src/ .py files
>> - Run Pipeline
>> - Deactivate Environment
>> - git add > commit > push changes (if you want to keep a record of any changes to tracked files)

####

## All Commands

####

> - Open Git Bash
>   
> - if repo not currently on local machine
>>   - `git clone https://github.com/<github-account-name>/<name-of-repo>.git`
>     
> - `cd <path-to-repo>/<name-of-repo>`
>
> - `git checkout main` : necessary in case your local repo is linked to an existing branch.
>
> - `git checkout -b <branch-folder>/<branch-name>`
>
> - Update config file using VSC located here: `<name-of-repo>/configs/config.yaml`
>
>> - Make sure all the directories that are referenced in the config file exist.
>
> - `python -m venv .venv` : only run if you haven't already created the .venv folder
>
> - `source .venv/Scripts/activate` 
>
> - `pip install -r requirements.txt` : run only if new requirements were added since the last time you built the virtual env
>
> - `pip install -e .` : run everytime you make changes to the `*.py` files in src
>
> - `python run.py`
>
> - `deactivate`
>
> - `git add .`
>
> - `git commit -m "Type informative message"`
>
> - `git push -u origin <branch-folder>/<branch-name>`
>
####
