
# Initial Setup — Only Run Once
####

## Sign up for a Github account with your UD email

- Go to `https://github.com/signup`
- Make sure to create your own username to the same as your email username.
- You now can be added as a contributor to repos.

####

## Connect to the *ir-team-retreat* Repository

####

>#### STEP 1 — Open Git Bash
>
>####
>
>#### STEP 2 — Create local directories
>
>> - `mkdir -p C:/Users/<username>/ir/ir-pipelines`
>>   
>> - `cd C:/Users/<username>/ir/ir-pipelines`
>>
>> - `pwd`
>
>####
>
>#### STEP 3 — Clone the Repository
>
>> - `git clone https://github.com/sruddy1/ir-team-exercise.git`
>
>####
>
>#### STEP 4 — Create Your Personal Branch
>
>> - `cd ir-team-exercise`
>>
>> - `pwd`
>> 
>> - `git checkout -b team-exercise/<your-first-name>`
>>
>>   - Creates a ***branch*** in Github, which is essentially your own copy of the repo.
>>   - Disconnects your changes from the root repo, referred to as "main" or "master"
>>   - Allows changes to be made and pushed to Github without updating "main".
>>   - Prevents conflicts between users who are using separate branches. 

####

## Set up GitBash with Anaconda Commands and Python

####

>#### STEP 1 — Open Visual Studio Code
>
> - Click the 5th icon down on the left pane 
> - Click the install button for 3 python plugins: Pylance, Python, and Python debugger
>
>####
>
>#### STEP 2 — Turn on View Hidden Files
>
>> - Open `File Explorer` > `View` > `Show` > Select `Hidden Items`
>
>####
>
>#### STEP 3 — Create ~/.bashrc
>
>> - Open Git Bash
>> - (type) `cd ~`
>> - (type) `touch ~/.bashrc`
>
>####
>
>#### STEP 3 — Update ~/.bashrc
>
>> - Open VSC
>>
>> - Go to `File` > `Open File` > Open `C:\Users\<username>\.bashrc`
>>
>> - Confirm/Find path to conda.sh based on installation type:
>>
>>   - All Users Installation: `/c/ProgramData/anaconda3/etc/profile.d/conda.sh`
>>   - Single User Installation: `/c/Users/<username>/AppData/Local/anaconda3/etc/profile.d/conda.sh`
> 
>> - Confirm/Find path to anaconda3 folder based on installation type:
>>
>>   - All Users Installation: `/c/ProgramData/anaconda3`
>>   - Single User Installation: `/c/Users/<username>/anaconda3`
>
>> - Add the following command
>>
>>   ```
>>   if [ -f "/c/Users/<username>/AppData/Local/anaconda3/etc/profile.d/conda.sh" ]; then
>>    . "/c/Users/<username>/AppData/Local/anaconda3"
>>   fi
>>   ```
> 
>> - Add the following command
>>
>>   `export PATH="/c/Users/<username>/AppData/Local/anaconda3:$PATH"`
>>
>
>> - Save & Close File
>
>> - Open GitBash (if already open, close and reopen)
>>
>>   - `source ~/.bashrc`
>>
>>   - `conda init bash`
>>  
>>   - Close GitBash 


