# Create a New Git Repository

## Step 1: Create and Configure on Github
>
> - Go to `https://github.com/Decision-Support`
> - Click `Repositories` in the header
> - Click `ir-pipeline-template`
> - On the far right click `Use this template` -> `Create new repository`
> - Give the repository a unique name in the form: `ir-<project>-<name>`
> - Select `Private`
> - Click `Create Repository`
>
####
## Step 2: Configure on Machine
>
> - Open GitBash
> ```bash
> cd ~/ir/ir-pipelines
> git clone https://github.com/Decision-Support/ir-<project>-<name>.git
> cd ir-<project>-<name>
> python -m venv .venv
> source .venv/Scripts/activate
> pip install -r requirements.txt
> python init_repo.py
> pip install -e .
> python -m ipykernel install --user --name=myenv --display-name "ir-<project>-<name>"
> deactivate
> git add -A
> git commit -m "repo initialization"
> git push
> ```
####
