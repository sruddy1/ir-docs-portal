# Adding New Markdown File to ir-docs-portal Sidebar

## Step 1: Create blank .md file
>
> - Open up Gitbash
> - `cd ~/ir/ir-pipelines/ir-docs-portal/docs`
> - `touch <filename>.md`
>

## Step 2: Edit .md file
>
> - Open up VSC
> - File -> Open File
> - Naviate to and open `~/ir/ir-pipelines/ir-docs-portal/docs/<filename>.md`
> - Write or copy-paste your markdown text
> - Save & Close file
>

## Step 3: Update mkdocs.yml
>
> - Stay in VSC
> - File -> Open File
> - Naviate to and open `~/ir/ir-pipelines/ir-docs-portal/mkdocs.yml`
> - Locate `nav:`
> - Add a new row in the same format as the other lines:
>   
>   `- <pretty label>: <filename>.md`
>
> - Save & Close file
>

## Step 4: Add, Commit, Push changes to ir-docs-portal Repo
>
> - Open Gitbash
> - `cd ~/ir/ir-pipelines/ir-docs-portal`
> - `git add .`
> - `git commit -m "add <filename>.md to docs"
> - `git push`
>   

## Step 5: Update Github
>
> - Stay in Gitbash
> - `cd ~/ir/ir-pipelines/ir-docs-portal`
> - `mkdocs gh-deploy --force`
> - View documentation here: `https://sruddy1.github.io/ir-docs-portal/`
>><mark>Note: May take several minutes for update to take effect</mark>
