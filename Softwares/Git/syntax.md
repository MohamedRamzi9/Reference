

### initialization 
```git
git init <dir>     // initializes a new git in the specified directory, or in the current directory if no directory is specified
```

### Status 
```git
git status    // shows the current status of the working directory and staging area, including untracked, modified, and staged files
```

### Staging
```git
git add <files>    // adds specific files to staging
git add .    // adds all items in the working directory to staging 

git reset <files>    // removes specific files from staging
git reset    // removes all items from staging
git reset --hard    // removes all items from staging and discards all current changes in working directory
```

### Restoring
```git
git restore <files>    // discards current changes in the specified files and reverts them to the last committed state
git restore .   // same as above but for all files in working directory
git restore --source=<commit> <files>    // reverts the specified files to the state they were in at the given commit of the form `HEAD~n` or commit hash
git restore --source=<commit> .    // same as above but for all files in working

git restore --staged <files>    // reverts the specified files in staging  to their last committed state
git restore --staged .    // same as above but for all files in staging

git restore --source=<commit> --staged --worktree <files>    // both removes the specified files from staging and reverts them to a previous commit state
git restore --source=<commit> --staged --worktree .    // same as above but for all files in working directory and staging
```

### Commit 
```git
git commit -m "added new function to script.js" // creates a commit with all previously staged changes

git log --oneline    // shows a summary of all commits with their hashes and messages in one line each
```

### Amending 
```git
git add forgotten_file    // adds forgotten files from last commit to staging
git commit --amend -m "New message for last commit"    // replaces the message of the last commit, additionally, if there are new staged changes, it adds them to the last commit too
git commit --amend --no-edit    // same as above but keeps the last commit message unchanged 
```

### Resetting
```git
// HEAD~n means going back n commits from the last commit

git reset --soft HEAD~1    // undo last commit and keep all changes staged
git reset --mixed HEAD~1    // undo last commit and unstage all changes
git reset --hard HEAD~1    // undo last commit and discard all current changes 

// to undo the initial commit or undo all commits all the way back to the root, we use the following command
git update-ref -d HEAD    // undo initial commit and keep all changes staged
git reset    // unstage all changes after executing the first command
git checkout .    // discard all current changes after executing the first command
```

### Reverting 
```git
git revert HEAD    // creates a new commit that undoes the changes of the last commit
git revert HEAD~n    // creates a new commit that undoes the changes of the nth commit from the last commit
git revert HEAD~n..HEAD    // creates multiple new commits, each undoing one of the last n commits (reverted from newest to oldest)
git revert --no-commit HEAD~n..HEAD    // same as above but stages all changes without creating the new commits, allowing to modify them before committing
git commit -m "Revert last n commits"    // creates one new commit that applies all the staged revert changes together

git revert --continue    // continues the revert process after resolving any conflicts
git revert --abort    // aborts the revert process and reverts back to the state before starting the revert

```

### Stashing
```git
git stash    // saves all tracked changes to a new stash and reverts working directory to last commit state
git stash push -m "work in progress"    // saves changes with a custom message
git stash -u    // same as above but also includes untracked files
git stash -a    // same as above but also includes ignored files

git stash list    // lists all saved stashes
git stash show    // shows a summary of changes in the latest stash
git stash show -p stash@{n}    // shows the changes saved in the nth stash

git stash apply    // reapplies the most recent stash to the working directory
git stash pop    // reapplies the most recent stash and removes it from the stash list
git stash apply stash@{n}    // reapplies the nth stash to the working directory
git stash drop stash@{n}    // deletes the nth stash from the stash list
git stash clear    // deletes all stashes from the stash list
```

### Branches
```git
git branch    // lists local branches
git branch --show-current    // shows the current branch name

git branch <name>    // create a new branch with the given name
git switch <name>    // switch to another branch by name
git switch -c <name>    // creates a new branch and switches to it 

git branch -d <name>    // deletes a given branch safely 
git branch -D <name>    // deletes a given branch even if not merged yet

git branch -m <old_name> <new_name>    // renames the given branch from old_name to new_name

```
  
### Remote repository 
```git
git remote add origin https://github.com/user/repo.git    // add a remote repository and call it origin
git remote -v    // lists all remote repositories with their URLs
git remote remove <name>    // removes a remote repository by name

git branch -r    // lists all remote branches
git branch -a    // lists all local and remote branches
git branch -vv    // shows local branches with their linked upstream tracking remote branches 
git branch --set-upstream-to=<remote>/<branch>   // sets the upstream tracking for the current local branch to the given remote branch
git push origin --delete <branch>    // deletes the given branch from the remote repository, but keeps its local tracking branch stale
git fetch --prune    // removes all stale remote tracking branches of all remotes that no longer exist in the remote repository
git remote prune <remote>    // removes all stale remote tracking branches of the specified remote that no longer exist in the remote repository
```

### Cloning
```git
git clone <remote> <directory>    // clones the remote repository into the given local directory, if no directory is specified, it uses the repository name as the new directory name
```

### Fetching
```git
git fetch <remote>    // fetches all new changes from all the remote repository branches into the local repository
git fetch <remote> <branch>    // fetches all new changes from the remote repository for the given branch into the local repository
```

### Pushing 
```git
git push <remote> <branch>    // pushes commits from the local branch to the remote repository branch of the same name
git push <remote> <local_branch>:<remote_branch>    // same as above except the remote branch name can be different from the local branch
git push -u <remote> <branch>    // sets the upstream tracking which links the local branch to the remote branch (if specified different names else same names) for future pushes and pulls
git push    // uses the local branch and remote branch names by default set by upstream tracking using -u flag
```

### Pulling 
```git
git pull    // pulls all new changes from the remote repository into the current branch
git pull --rebase    // pulls all new changes from the remote repository and rebases current branch on top of them
git pull <remote> <branch>    // pulls all new changes from the remote repository for the given branch into the current branch
```

### Merging 
```git
git switch main    // sets the current branch as main
git merge <branch> -m "Merging <branch> into main"    // merges the given branch with the current branch and creates a new commit with a custom message 
git merge <branch> --allow-unrelated-histories    // merges two branches with unrelated histories, happens when merging two different repositories or when they were created before initial commit

git merge --continue    // continues the merge process after resolving conflicts
git merge --abort    // aborts the merge process and reverts back to the state before starting the merge
```

### Rebasing
```git
git rebase <branch>    // rebases the current branch on top of the given branch, effectively moving all commits of the current branch to start from the latest commit of the given branch
```