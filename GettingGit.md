# Vocabulary 

| Getting Started     |             |
| Local Machine       | From Remote | 
| ------------------- | ----------- | 
| git init            | git clone   |
| create a local repo | retrieves code from remote machine |


* add - add files to repo
* commit - bundle up the files and approve
* branch - creates a branch of the codebase to enable modifications
* merge - merges one or more branche back together in named branch
* pull - retrieves code from remote machine to local machine 
* push - sends code from local machine to remote machine

# Local Machine Only
```shell
mkdir CodeBase
cd CodeBase
git init
```
* add a few files
```shell
git add .
git commit -m "First add of files"
```
  
# Connecting to Remote Repository

## Setup a directory to download files (pull)

```shell
cd Desktop
mkdir RemoteCode
cd RemoteCode
pwd
```

## Download a copy of the files from the remote server  (clone)
```shell
git clone https://github.com/jctmcclain/Python-Intro
```

## check to see that the Python-Intro directory was downloaded

### Apple
```shell
ls 
```

### Windows
```shell
dir
```

## Enter into the Python-Intro (change directory or cd)
```shell
cd Python-Intro
```

## View the files

### Apple
```shell
ls 
```

### Windows
```shell
dir
```

## Update the local files 
```shell
git pull
```


