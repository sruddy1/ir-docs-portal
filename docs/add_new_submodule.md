# Adding New Submodule w/ Documentation to `ir-docs-portal` Repo

## Step 1 — Add submodule <reponame\> to documentation repo (`ir-docs-portal`)

Run in GitBash:
> ```bash
> cd ~/ir/ir-pipelines/ir-docs-portal
> git submodule add https://github.com/sruddy1/<reponame\>.git ir-pipelines/<reponame\>
> git submodule update --init
> git add .gitmodules ir-pipelines/<reponame>
> git commit -m "added <reponame\>"
> git push
> ```

## Step 2 — Add new repo documentation to mkdocs flow

- Open VSC
- `File` -> `Open File`
- Navigate to and open `ir-docs-portal/scripts/gen_portal_ref_pages.py`
- Find python variable `PIPELINE_LABELS`
- Add another row to this variable in the same format as the other rows: "<reponame\>": "<pretty label\>"

Example
> 
> `"ir-enrollment-projection": "Enrollment Projection"`
> 
> <mark>Warning: You need to add a ',' to the line above the new line you have added.</mark>
>

- Save and close file
- `File` -> `Open File`
- Navigate to and open `ir-docs-portal/mkdocs.yml`
- Locate `plugins` -> `mkdocstrings` -> `handlers` -> `python` -> `paths`
- Add a new row in the same format as the other rows: - ir-pipelines/<reponame\>/src
- Save & close file

## Step 3 — Add, Commit, Push changes to `ir-docs-portal` Repo

Run in GitBash:
> ```bash
> cd ~/ir/ir-pipelines/ir-docs-portal
> git add .
> git commit -m "added <reponame>"
> git push
> ```

## Step 4 — Update Github

Run in GitBash:
> ```bash
> cd ~/ir/ir-pipelines/ir-docs-portal
> mkdocs gh-deploy --force
> ```

- View documentation here: `https://sruddy1.github.io/ir-docs-portal/`
> <mark>Note: May take several minutes for update to take effect</mark>