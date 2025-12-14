# Software Introduction

####

### 1. Anaconda
- An all-inclusive resort for running software: jupyter notebook, python, and others.
- Software runs inside their own local environment, preventing conflicts with the environment of your physical machine.
- Default local environment is "base", but one can create new environments per project/pipeline.
    
> *An environment is a virtual computer with (in our case) its own Python installation, python libraries/packages, and specific library/package versions, which can be completely different from what is installed on the physical machine or other environments.*
>
>> **When linked to a python pipeline**
>> - Guarantees successful runs across time.
>>   - Runs under the same conditions in which it was ***successfully*** built.
>>   - Prevents breaks caused by updates to python packages in the future. 
>> - Guarantees successful runs across separate physical machines.
>>   - Gives the user the software recipe to build the correct environment, instead of using their machine's native environment.

####

### 2. Jupyter Notebook
- Included in the Anaconda distribution.
- Useful when you want to run python interactively: explore the data, generate plots, run and test python scripts as one builds them. 
- To run a python script non-interactively, one exports the notebook as an **Executable Script**. This creates a python/**.py** file used to either:
> - store python functions that collectively build a package — packages allow you to easily call functions inside other python scripts.
> - executes the pipeline: reads data, processes data into results, outputs results.
>> ***Note:*** *jupyter notebooks are ***not*** used to run the pipeline or build the pipeline's associated python package.*
- Has ability to run under any python environment (or "kernel") created within Anaconda — i.e. can emulate the true pipeline environment.
    
####

### 3. Visual Studio Code
- A text editor with python syntax highlighting.
- It can run python code but I use it to easily edit python scripts (.py), rather than run code. 

####

### 4. Github
- **Github** is a cloud service that stores repositories of code, allowing for simultaneous collaboration. 
> ***It's Box but for code, not data!***
- Cloud repositories are downloaded, or ***cloned***, onto your physical machine. 
> - make changes locally
> - **push** those changes to the cloud repository

####

### 5. Git

- **Git** is version control softare through which your local repository and the cloud repository communicate.
- It comes with a suite of commands that give users control over that relationship.
- The emphasis is on **CONTROL**. 
> - User control can become very complex when there are several collaborators making changes daily and simultaneously.     
>> **For or our purposes, we will be avoiding that complexity and only need to learn a small number of commands, simple version-control concepts, and basic best practices.**

**Main Git commands run locally in Git Bash**
> - `git init` — initialize local folder for github
> - `git clone <repository url>` — copy a repo in the cloud to your local computer
> - `git checkout -b <name>` — create a "branch" on which to make changes to the repo.
> - `git status` — what is different between your local repo and the cloud repo
> - `git commit -m "<description>"` — package all the local changes under a single purpose, preparing them to be pushed to the cloud  
> - `git add <file>` or `git add .` — add an untracked file or all untracked files (".") to be added to the commit.
> - `git rm <file>` — remove a file from being tracked by the repo 
> - `git push -u origin main` or `git push -u origin <branch>` — push the local changes to the repo or to a branch off the repo.
> - `git config --global user.name <your name>` — connect your github account to your local machine
> - `git config --global user.email <your email>` — connect your github account to your local machine 

####

### 6. Git Bash

- **Git Bash** is a command-line terminal for Windows that lets you run Git commands and, as a bonus, many Linux-style system commands inside a Bash shell.
- Python was built for Unix/Linux systems.
- Most servers run Linux with Bash, so nearly all software and data engineers are fluent in Bash—much more than Windows command line.

**Common Linux-Bash system commands**

> - `cd <path/to/folder>` — navigate to a folder
> - `pwd` — print the directory you are in
> - `mkdir <name>` — create a folder  
> - `ls` — list files in the current directory  
> - `cp <file> <path>` — copy a file to a new location  
> - `rm <file>` — delete a file  
> - `touch <file.ext>` — create an empty file with the given extension
