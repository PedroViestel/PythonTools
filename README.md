# Python Unreal Clean Architecture Example

## Table of contents
* [General info](#general-info)
* [Features](#features)
* [Setup](#setup)

## General info
This project is a refactor of another repository, containing a collection of scripts that help find problems and possible optimizations, but adapted to use Clean Architecture, making the code more flexible and reusable The project uses dependency injection and dependency inversion principles, also, uses an implementation of mediator pattern with pipeline behaviors.
Also, a batch import was added, where o pick a folder and selected if you want to import meshes, audio or textures. A preview will show the files and you can decide the files to import.

## Features
To prevent having to manually update the code or close and open the unreal editor, a behavior was created to refresh the code prior to execution to facilitate the development Also, before the project initiation, it checks if the necessary packages are installed, if not, the pip commands will run in the background.

## Setup
To run this project:

```
$ Enable the plugins: Editor Scripting Utilities and Python Editor Script Plugin
$ Place the folder named Tools inside the project you want to use
$ In project Settings, python section, add a additional path pointing to the script folder
$ Open the editor blueprint widget inside the tools folders and run
```

The original repository: https://github.com/CB-Game-Developer/UnrealEngine-LogOptimisationsHelperScripts
 
