
# Initial Setup — Only Run Once
####

## Sign up for a Github account with your UD email

- Go to `https://github.com/signup`
- <mark>Warning</mark>: Change the username assigned to you to your UD username. 
- You now can be added as a contributor to repos.

####

## Connect to the *ir-team-retreat* Repository

####

## STEP 1 — Open Git Bash
>
####
>
## STEP 2 — Create local directories

Run in GitBash:

> ```bash
> cd ~
> mkdir -p ir/ir-pipelines
> cd ~/ir/ir-pipelines
> ```

####

>
## STEP 3 — Update Git credentials

Run in GitBash:

> ```bash
> git config --global user.name "first last"
> git config --global user.email "<name>1@udayton.edu"
> ```
>
####
>
## STEP 4 — Clone the Repository

Run in GitBash:

> ```bash
> git clone https://github.com/sruddy1/ir-team-exercise.git
> ```
> 
####
>
## STEP 5 — Create Your Personal Branch

Run in GitBash:

> ```bash
> cd ir-team-exercise
> git checkout -b team-exercise/<your-first-name>
> ```

- Creates a ***branch*** in Github, which is essentially your own copy of the repo.
- Disconnects your changes from the root repo, referred to as "main" or "master"
- Allows changes to be made and pushed to Github without updating "main".
- Prevents conflicts between users who are using separate branches.

####
>
## STEP 6 — Authenticate Git Account

Run in GitBash:

> ```
> git credential-manager github login
> ```

- An authentication window will pop up. Go through the steps to authenticate.
- Now your local machine is authenticated and linked to your github account.

####


####

## Set up GitBash with Anaconda Commands and Python

####

## STEP 1 — Open Visual Studio Code

- Click the 5th icon down on the left pane 
- Click the install button for 3 python plugins: `Pylance`, `Python`, and `Python debugger`

####
>
## STEP 2 — Turn on View Hidden Files

- Open `File Explorer`
- Go to `View` > `Show` > Select `Hidden Items`

####

## STEP 3 — Create ~/.bashrc

Run in GitBash:

> ```bash
> cd ~
> touch ~/.bashrc
> ```

####

## STEP 4 — Update ~/.bashrc

- Open Visual Studio Code (VSC)

- Go to `File` > `Open File` > Open `C:\Users\<username>\.bashrc`

- Using File Explorer: Confirm/Find path to conda.sh based on installation type:

> - All Users Installation: `/c/ProgramData/anaconda3/etc/profile.d/conda.sh`

> - Single User Installation: `/c/Users/<username>/AppData/Local/anaconda3/etc/profile.d/conda.sh`

- Using File Explorer: Confirm/Find path to anaconda3 folder based on installation type:

> - All Users Installation: `/c/ProgramData/anaconda3`

> - Single User Installation: `/c/Users/<username>/anaconda3`

- Copy-paste the following command to the `.bashrc` file that is open in VSC:

> ```bash
> export PATH="/c/Users/<username>/AppData/Local/anaconda3:$PATH"
> if [ -f "/c/Users/<username>/AppData/Local/anaconda3/etc/profile.d/conda.sh" ]; then
> . "/c/Users/<username>/AppData/Local/anaconda3/etc/profile.d/conda.sh"
> fi
> ```

- Save & Close File

- Close & Reopen GitBash

> ```bash
> conda init bash
> ```
  
- Close GitBash 
 

