# Updating Docs for Existing Submodules

## Step 1 — Update submodules inside ir-docs-portal Repo

Run in GitBash:
> ```bash
> cd ~/ir/ir-pipelines/ir-docs-portal
> git submodule update --remote --merge
> cd ~/ir/ir-pipelines/ir-docs-portal
> git add ir-pipelines
> git commit -m "update submodules"
> git push
> cd ~/ir/ir-pipelines/ir-docs-portal
> mkdocs gh-deploy --force
> ```

- View documentation here: `https://sruddy1.github.io/ir-docs-portal/`
> <mark>Note: May take several minutes for update to take effect</mark>