<!-- METADATA -->

<!-- based on template v0.0 -->

<!-- Objectives
- Provide beginners with a solid foundation in software version control and Git
  basics.
- Recognize Git as the standard version control system (VCS) for modern
  development.
- Explore Git's internal model and core concepts, the three states, commits,
  branches, and remotes.
- Explain how to use the Git CLI, configure it, access help,
  and perform the basic day-to-day commands.
-->

[pro]: https://git-scm.com/book/en/v2

# Introduction to Software Version Control and Git

`2/Oct/2025`

---

## Why is Version Control Important?

Software version control is the practice of systematically managing multiple
versions of a software project (such as releases, bug patches, and feature
updates) in an organized way. It ensures that the history of changes remains
accessible to developers and users, enabling traceability, collaboration, and
reliable access to past versions.

Every software project benefits from version control, whether it's a simple
script or a large scale software effort. By using version control, developers
and maintainers gain essential capabilities like tracing the entire history of
every file in the project, reverting the project to any previous state, managing
concurrent versions, and collaborating effectively across teams and codebases.
In simple terms, any piece of software that is intended to last should be placed
under version control.

Learning how to effectively use version control is one of the most valuable
skills to learn as a developer (and many other roles as well). It's guaranteed
that eventually you will use version control while working on real projects.
Mastering version control practices will significantly enhance your
productivity, collaboration, and overall technical ability.

## What is Git?

The stupid content tracker, also known as Git, is a Version Control System (VCS)
originally created to meet the needs of the Linux project. Its creator, Linus
Torvalds, designed it to be distributed, blazingly fast, scalable to Linux-sized
projects, and flexible enough to support a wide variety of workflows.

Although Git is not the only VCS (some companies, most notably Meta, use other
VCS or proprietary systems), it has become the industry standard, according to
this 2023
[Stack Overflow blog](https://stackoverflow.blog/2023/01/09/beyond-git-the-other-version-control-systems-developers-use/).
93% of developers worldwide use Git. In practice, this means you will almost
certainly use it at some point in your career.

## Git's Version Control Model

Git's unique approach to modeling version control makes it stand out from
earlier VCSs. Traditional VCSs stored changes as a stack of diffs between file
versions, but Git introduced the concept of snapshots. Each commit captures the
entire state of the project at a given moment. This model makes Git more
reliable, efficient, and flexible, forming the foundation for features like
branching, merging, and powerful history tracking.

### Repositories

At the heart of Git is the repository, often shortened to repo. A repo is the
complete database of your project's history, storing every commit, branch, and
tag. Unlike older centralized systems, Git repos are lightweight and portable.
You can create one in any folder with a single command, or clone an existing
project from another source. Because the repo includes the entire history, it
allows you to travel back in time, branch off experiments, and collaborate with
others without losing track of the project's state.

### Commits as Snapshots

A commit in Git is a snapshot of the entire project tree at the moment you
commit, including every file that is tracked, and some metadata like the author
and timestamp. Even though it records the full state of the project, Git is
smart. If a file hasn't changed, Git doesn't duplicate it but simply reuses the
data from previous commits. This makes storing snapshots efficient while still
giving you the ability to restore your project to any point in time.

Each commit is identified by a unique cryptographic checksum (a SHA-1 hash).
This checksum acts like a fingerprint. If even a single character in a file
changes, the resulting commit hash will be completely different. This guarantees
integrity and makes it impossible to alter history without detection.

Commits are also linked together in a chain through parent relationships. Every
commit (except the very first one) has at least one parent commit, forming a
history that Git can walk through. When branches diverge and merge, commits can
have multiple parents, which is how Git represents merges. Thanks to this
structure, Git can always tell what came before and can reliably track the
evolution of a project over time.

#### Diff Commits Diagram

![img](https://git-scm.com/book/en/v2/images/deltas.png)

> Image source: _Pro Git (2nd Edition)_, Chapter 1: What is Git?

#### Snapshot Commits Diagram

![img](https://git-scm.com/book/en/v2/images/snapshots.png)

> Image source: _Pro Git (2nd Edition)_, Chapter 1: What is Git?

### Integrity, Locality and Recovery

Three of Git's strongest features are integrity, locality, and recovery.

- Integrity means that everything Git stores is protected by cryptographic
  checksums. Your data cannot be corrupted without Git detecting it.

- Locality means every clone of a repo contains the full project history,
  enabling offline work and independent backups.

- Recovery is possible because Git never truly deletes data immediately. Even if
  you make mistakes, you can often recover lost commits using features like the
  reflog. These guarantees give developers confidence that their work is safe
  and traceable.

### The Three States

To understand Git, it's essential to know its three states:

- The working directory, where you actively edit files.

- The staging area (index), where you prepare changes you intend to commit.

- The repo, where committed snapshots are stored permanently.

This model allows precise control, as you can decide which edits to commit, keep
some changes unstaged, or revert back at any point.

![img](https://git-scm.com/book/en/v2/images/areas.png)

> Image source: _Pro Git (2nd Edition)_, Chapter 1: What is Git?

#### File Lifecycle Diagram

![img](https://git-scm.com/book/en/v2/images/lifecycle.png)

> Image source: _Pro Git (2nd Edition)_, Chapter 2: Recording Changes to the
> Repository.

### Branches and Remotes

A branch in Git is simply a movable pointer to a commit. The default branch is
usually called `main` or `master`. When you create a new branch, Git makes a
pointer that starts at the current commit, and as you add new commits, that
branch pointer advances automatically.

Because branches are lightweight, Git encourages developers to create many of
them, one branch for each feature, bug fix, or experiment. This makes it safe to
try new ideas without affecting the stability of the main codebase. Later,
branches can be merged or discarded as needed.

Branches become even more powerful when combined with remotes. A remote is a
reference to another copy of the repo, typically hosted on a primary server such
as GitHub, GitLab, or a self-managed server. Remote branches represent the
history of collaborators and allow you to share your own work. For example,
`origin/main` refers to the `main` branch on the default remote named `origin`.
By pushing and pulling, local branches can stay synchronized with their remote
counterparts, enabling effective teamwork across different machines and
locations.

#### Diverging Branches Diagram

![img](https://git-scm.com/book/en/v2/images/advance-master.png)

> Image source: _Pro Git (2nd Edition)_, Chapter 3: Branches in a Nutshell.

#### Remote Branch Diagram

![img](https://git-scm.com/book/en/v2/images/remote-branches-1.png)

> Image source: _Pro Git (2nd Edition)_, Chapter 3: Remote Branches.

### Tags

A tag is a human-readable label that points to a specific commit. Unlike
branches, which move forward as new commits are added, tags are fixed, they
always refer to the same snapshot. Developers often use tags to mark important
milestones in a project, such as releases (v1.0, v2.1.3) or stable points in
history.

### Commit History

The commit history in Git is not just a simple list of changes, it's organized
as a Directed Acyclic Graph (DAG). Each commit records the entire state of the
project at that point in time and points back to one or more parent commits,
forming a graph of relationships. The directed part means commits always point
backward in time (to their parents), and the acyclic part means history never
loops back on itself.

This structure allows Git to represent branching and merging naturally, a branch
is simply a pointer to one path through the graph, and a merge commit has
multiple parents, linking previously diverged histories back together. By
walking this graph, Git can answer powerful questions, like:

- When was this line of code introduced?

- What changes were made between two points in history?

- How did two branches diverge, and where do they join again?

#### This Repo's History

```bash
$ git log --graph --oneline --all
 7b22226 (HEAD -> workshop_intro_git) workshop: add intro to git and version control
|  6944570 (workshop_adv_git) workshops: add modern version control
|/
 f79a410 (origin/main, origin/HEAD, main) Leetcode: 200.number_of_islands (#15)
 21c411a Leetcode: 226.invert_binary_tree: (#11)
 19ef6d7 workshops: add intro to competitive programming (#16)
 bb0c6d3 leetcode: 53 added maximum subarray dp and kadane
 ff440ae leetcode: 206 reverse linked list add iterative and recursive
...
 dfd9ac9 ci: add github workflows for pr checks and markdown integrity
 1eaef47 feat: add formatters, ruff and prettier in dprint and clang-format
 6c19f45 fix: formatting and links in markdown sources using new tools
 345be65 feat: add dprint and lychee tools with configs
|  8093a49 (origin/resource-git, resource-git) resource: add git resources
|/
 784a829 fix: rename lectures to workshops
 c8a1523 doc: add difficulty ranges on resources
 af8b474 doc: add resource contribution guidelines
...
 49d1afa doc: add contributing guide
 b720945 doc: add root readme
 f93545d Initial commit
```

### Distributed VCS

Unlike older centralized systems, Git is a distributed VCS. Every clone of a Git
repo contains the entire history of the project (all commits, branches, and
tags). This means you don't need a network connection to inspect history, create
new branches, or even commit changes.

The distributed model also makes collaboration flexible, developers can work
independently, sync with each other when needed, and experiment freely without
blocking teammates. Because every clone is a full backup, Git is also highly
resilient, no single server crash can destroy the project history.

#### Centralized Model Diagram

![img](https://git-scm.com/book/en/v2/images/centralized.png)

> Image source: _Pro Git (2nd Edition)_, Chapter 1: About Version Control.

#### Distributed Model Diagram

![Distributed model](https://git-scm.com/book/en/v2/images/distributed.png)

> Image source: _Pro Git (2nd Edition)_, Chapter 1: About Version Control.

## Basic Git CLI Usage

### Don't Be Afraid of the CLI

For many beginners, the command line can feel intimidating and confusing
compared to a graphical interface. However, when it comes to Git, the CLI
(Command Line Interface) is the most direct and reliable way to interact with
the system. Almost all advanced workflows, tutorials, and troubleshooting guides
assume familiarity with Git commands on the CLI and by learning Git through the
command line, you not only gain confidence in understanding what Git is really
doing under the hood, but you also avoid the limitations or abstractions that
GUIs sometimes impose. Once you're comfortable with the CLI, using graphical
tools becomes a choice, not a crutch.

### Installing the Git CLI

Before we can use the Git CLI, it needs to be installed on your system.

- Linux: Most distributions already include Git in their package managers:

```bash
sudo apt install git # Debian/Ubuntu
sudo dnf install git # Fedora
sudo pacman -S git # Arch
```

- macOS: Git comes preinstalled with Xcode's Command Line Tools. Alternatively
  you can it install with Homebrew by running:

```bash
brew install git
```

- Windows: The recommended option is
  [Git for Windows](https://gitforwindows.org/), which installs Git along with
  Git Bash, a lightweight terminal that provides a Unix-like environment.

After installation, confirm that Git is ready by running:

```bash
git --version
```

This will display the version of Git installed, ensuring your setup was
successful.

### Getting Help

Git has extensive built-in documentation, and knowing how to access it is
essential. Whenever you encounter a new command or get stuck, you don't need to
leave the terminal.

To get help on a specific command use:

```bash
man git [<command>]
git help [<command>]
# or the more lightweight
git [<command>] --help
```

This opens a manual page describing the command's options, usage, and examples.
Git's help pages can feel dense, but they are the authoritative source of truth.
Combined with community resources like the [Pro Git book][pro], they ensure you
always have reliable guidance at hand.

### Configuring Git

Before diving into day-to-day Git commands, it's important to understand how Git
is configured. Git reads its settings from configuration files that define your
identity, preferences, and project-specific rules. Two of the most commonly used
are `.gitconfig` and `.gitignore`.

#### .gitconfig and git config

The `.gitconfig` file stores Git configuration options, you can use `.gitconfig`
to set your identity, preferred editor, or even define shortcuts (aliases) for
commands you use often. There are typically three levels of configuration,
configurations at a higher level override the ones in lower levels.

- System: Applies to every user on the machine.
- Global: Applies to your user account (`~/.gitconfig`).
- Repo: Applies only to the current repo (`.git/config`).

You can use the `git config` command to set these configurations at the
different levels.

```bash
# repo level
git config [<conf>]
# user level
git config --global [<conf>]
# system level
git config --system [<conf>]

# list your configurations at the given level
git config [--global | --system] --list

# set vscode as git's editor
git config --global core.editor code --wait

# user identity
git config --global user.name "John Doe"
git config --global user.email "johndoe@example.com"

# aliases
git config --global alias.lg 'log --oneline --graph'
```

When working with remote repos on GitHub, authentication is required.
Traditionally this was done with HTTPS and passwords, but GitHub now requires
SSH keys or personal access tokens for secure authentication. Setting up SSH
keys is the recommended method for most developers. Follow the
[official GitHub guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
to generate an SSH key, add it to your GitHub account, and configure your local
environment.

- kata:
  [configure-git](https://github.com/eficode-academy/git-katas/blob/master/configure-git/README.md)

#### .gitignore

Not every file in your project should be tracked. Build outputs, temporary
files, log files, or secrets like `.env` should be excluded from version
control. The `.gitignore` file tells Git which files or directories to ignore.
Read the official docs on the `.gitignore`
[pattern format](https://git-scm.com/docs/gitignore#_pattern_format).

Each repo can have its own `.gitignore` file, and you can also define a global
one for files you never want to track (like OS-specific files):

```bash
git config --global core.excludesfile ~/.gitignore_global
```

GitHub maintains a large collection of ready-to-use
[.gitignore templates](https://github.com/github/gitignore) for different
programming languages, frameworks, and development environments. These templates
are a great starting point when setting up a new project.

- kata:
  [ignore](https://github.com/eficode-academy/git-katas/blob/master/ignore/README.md)

### Creating a Repository

Once Git is configured, the first step in any project is to create or obtain a
repo. Git offers two common ways to start, `git init` and `git clone`.

#### git init

The `git init` command creates a new, empty Git repo in the current directory.
It sets up the `.git` folder, which contains all the internal structures Git
uses to track history.

```bash
mkdir repo
cd repo
git init
```

#### git clone

The `git clone` command creates a copy of an existing repo. This is the most
common way to start collaborating on projects, since it downloads both the files
and the full history of the repo. The basic usage is:

```bash
git clone https://github.com/user/repo.git
```

By default, Git names the remote origin and sets up a tracking branch so your
local main stays connected to the remote main. This makes it easy to fetch
updates and push your own work back.

### Working with the File Lifecycle

The Git file lifecycle describes how changes move from your working directory,
through the index, and into the repo. Understanding this process is essential to
controlling what gets saved in your project's history.

Together, `git status`, `git add`, and `git commit` form the basic workflow loop
of Git: check changes -> stage selected changes -> commit them into history.

#### git status

The `git status` command shows the current state of your working directory and
index, which are staged for commit, and which are untracked. It's often the
first command you'll run before deciding what to do next.

```bash
git status
# compact output
git status --short
```

#### git add

The `git add` command stages changes, moving them from the working directory
into the index. This gives you control over which modifications will be included
in the next commit. You can add individual files, directories, or all changes at
once.

```bash
git add [<path>]
# stage all in this directory
git add .
# stage all in the repo
git add --all
```

- kata:
  [basic-staging](https://github.com/eficode-academy/git-katas/blob/master/basic-staging/README.md)

#### git commit

The `git commit` command takes the changes currently staged and saves them as a
snapshot in the repo. Each commit has a unique identifier (SHA-1 hash) and
records your name, email, date, and the commit message you provide.

```bash
git commit
```

- kata:
  [basic-commits](https://github.com/eficode-academy/git-katas/blob/master/basic-commits/README.md)

### Viewing the Commit History

One of Git's biggest strengths is the ability to explore the history of a
project. You can see who made changes, when they were made, and exactly what was
modified. Two essential commands for this are `git log` and `git diff`.

#### git log

The `git log` command displays the commit history. By default, it shows each
commit's hash, author, date, and commit message.

```bash
# log from HEAD
git log
# log from commit
git log [<commit>]
```

#### git diff

The git diff command shows the actual changes between two states of the repo. By
default, it compares your working directory to the index. This means it shows
what you've modified but not yet staged.

```bash
# compare working dir and index
git diff
# check what will be committed
git diff --staged
# compare commit A and B
git diff [<A>] [<B>]
```

### Undoing Actions

Mistakes happen, wrong commit messages, unwanted changes, or files that
shouldn't have been tracked. Git provides safe ways to undo actions without
losing control of your project's history. Three useful commands for this are
`git commit --amend`, `git restore`, and `git rm`.

#### git commit --amend

The `git commit --amend` command lets you modify the most recent commit. This is
useful if you forgot to include a file or need to fix a typo in the commit
message. Amending replaces the last commit with a new one, so it should only be
used for commits that have not yet been pushed to a shared remote to avoid
conflicts.

```bash
# add a missing file to the last commit
git add forgotten-file
git commit --amend
```

- kata:
  [amend](https://github.com/eficode-academy/git-katas/blob/master/amend/README.md)

#### git restore

The `git restore` command reverts changes in your working directory or staging
area. This is helpful when you've modified a file by mistake or staged it
accidentally and want to return to a clean state.

```bash
# discard changes in working directory
git restore file.txt
# unstage a file but keep changes in working dir
git restore --staged file.txt
```

- kata:
  [restore](https://github.com/eficode-academy/git-katas/blob/master/restore/README.md)

#### git rm

The `git rm` command removes files from both the working directory and from
Git's tracking files. Use it when you want Git to stop tracking a file
completely.

```bash
# remove tracked file
git rm .env
# remove tracked file but keep it in the working dir
git rm --cached .env
# remove folder and its contents
git rm -r secrets/
```

### Tagging

#### Lightweight Tags

Lightweight tags are just pointers to a commit with no additional information.
Think of them as quick bookmarks in history. While faster to create, they are
less useful for long-term project history.

```bash
git tag v1.0.0-light
```

#### Annotated Tags

Annotated tags are the recommended type for most cases. They are stored as full
objects in the Git database and can contain metadata such as the tagger's name,
email, date, and an optional message. They can also be signed with GPG for
verification.

```bash
# create new annotated tag
git tag -a v1.0.0
# view tag metadata content
git show v1.0.0
# push tag to remote
git push --tags [<remote>]
```

- kata:
  [git-tag](https://github.com/eficode-academy/git-katas/blob/master/git-tag/README.md)

### Managing Branches

Branches are one of Git's most powerful features, allowing you to work on
separate lines of development without affecting the stability of the main code.
They are lightweight, easy to create, and encourage experimentation.

#### git branch

The `git branch` command is used to list, create, or delete branches.

```bash
# list all local branches
git branch
# create a new branch called feature/login
git branch feature/login
# delete a branch safely (only if merged with the default)
git branch -d old-branch
```

- kata:
  [basic-branching](https://github.com/eficode-academy/git-katas/blob/master/basic-branching/README.md)

#### git checkout

The `git checkout` command switches your working directory to another branch or
commit. When you switch, Git updates your files to match the state of that
branch.

```bash
# switch to an existing branch
git checkout feature/login
# create and switch to a new branch
git checkout -b hotfix/api
```

### Merging Branches

At some point, work from one branch needs to be integrated back into another.
This is where merging comes in.

#### git merge

The `git merge` command combines the history of one branch into another. If the
changes are in a straight line (no divergent commits), Git performs a
fast-forward merge by simply moving the branch pointer forward.

If branches have diverged, Git performs a 3-way merge, creating a new commit
that combines both histories.

```bash
# Merge the feature/login branch into main
git checkout main
git merge feature/login
```

If Git encounters conflicting changes, it will pause the merge and ask you to
resolve conflicts manually before completing the process.

- kata:
  [ff-merge](https://github.com/eficode-academy/git-katas/blob/master/ff-merge/README.md)
- kata:
  [3-way-merge](https://github.com/eficode-academy/git-katas/blob/master/3-way-merge/README.md)

### Remotes

A remote is a reference to another copy of the repo, usually hosted on a server
such as GitHub, GitLab, Bitbucket, or your own infrastructure. Remotes make
collaboration possible by allowing developers to share commits, branches, and
tags. The default remote created when cloning a repo is named `origin`.

#### git remote

The `git remote` command manages the list of remotes associated with your repo.

```bash
# list remotes and their URLs
git remote -v
# add remote
git remote add origin https://github.com/user/repo.git
# remove remote
git remote remove origin
```

#### git push --set-upstream

When you create a new branch locally, Git does not automatically know which
remote branch it should be connected to. To link your local branch with a remote
branch, you use the `--set-upstream` (or shorthand `-u`) option when pushing for
the first time.

```bash
# set origin/feature/login as the upstream for feature/login
git checkout -b feature/login
git push --set-upstream origin feature/login
```

## Best Practices

Following best practices in Git helps to keep your repo organized, maintainable,
and easier to collaborate on. Clear conventions reduce confusion and make the
history of the project more valuable for everyone.

### Naming Conventions

Branch names should clearly describe the purpose of the work being done. This
makes it easy to understand what each branch is for when collaborating in a team
or when revisiting the project later.

- Be descriptive. Use names that describe the change, e.g. `feature/login-form`,
  `fix/typo-readme`, or `docs/update-contribution-guide`.
- Use slashes to group branches. Prefixes like `feature/`, `fix/`, `docs/`, or
  `chore/` help categorize work.
- Keep them short but meaningful. Avoid overly long names, but ensure the branch
  is identifiable.
- Avoid personal names. Instead of `sebastian-work`, use a functional
  description like `feature/payment-integration`.

Good branch naming makes it easier to manage pull requests, code reviews, and
collaboration.

### Commit Messages

Commit messages are the primary way of documenting why changes were made. A good
message explains the intent behind a change, not just what files were modified.
For larger projects, many teams follow the
[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) standard,
which defines a structured format (`feat:`, `fix:`, `docs:`) to make commit
history more consistent and machine-parseable.

- Write clear, concise messages. A commit message should summarize the intent of
  the change in one sentence. Avoid vague messages like `fix` or `update`.
- Use the imperative mood. Phrase messages like commands, e.g.
  `add user profile page` instead of `added user profile page`. Think: _If
  applied, this commit will..._
- Optionally follow the 50/72 rule. Keep the subject line under 50 characters
  and wrap the body text at 72 characters. This improves readability in logs and
  tools.
- Explain the "why," not just the "what". The diff already shows what changed.
  The message should explain the reasoning or context.

```gitcommit
commit 345be656fd49e480a24f9d646e66b52a1a8f9829
Author: Sebastian Certuche <sebascertuche@gmail.com>
Date:   Thu Aug 7 15:52:07 2025 -0600

    feat: add dprint and lychee tools with configs

    Dprint configurations only includes the plugin for markdown, more
    plugins have to be added on any new languages which need formatting.

    Lychee's default config file was added, the only non default
    configuration is the list of accepted status codes for URLs,
    Informational codes were added as to assert the existence of the
    resource, and the 403 code was added as some pages such as leetcode,
    return such code to bots.

 .gitignore          |   1 +
 CONTRIBUTING.md     |  15 ++++++
 devtools/check.sh   |   9 ++++
 devtools/format.sh  |   7 +++
 devtools/install.sh |  25 ++++++++++
 dprint.json         |   9 ++++
 lychee.toml         | 131 ++++++++++++++++++++++++++++++++++++++++++++++++++++
 7 files changed, 197 insertions(+)
```

---

## Bibliography

- [Pro Git (2nd Edition)][pro]
- [Git Katas](https://github.com/eficode-academy/git-katas)

## Additional Resources

- [Git Exercises](https://gitexercises.fracz.com/exercise/master)
- [Learn Git Branching](https://learngitbranching.js.org/)

## Authors

- Sebastian Certuche @sebascert
