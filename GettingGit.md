# Vocabulary 
* init
* add
* commit
* merge
* branch
* push
* pull
* clone

# Getting Started Local Machine 
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
  
# From Remote 

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


