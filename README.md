# Welcome to Latte!

Latte is a package distribution system for 
[StaSh](https://github.com/ywangd/stash), 
a command-line interface for the 
[Pythonista](http://omz-software.com/pythonista/) 
Python IDE.

Latte was originally conceived and coded 
by [Seanld](https://github.com/Seanld) as 
a way to easily share scripts made by the 
Pythonista community to other users of 
StaSh and Pythonista in general. My fork 
is an attempt to:

- [ ] Add more advanced features to Latte, 
i.e package search, support for 
internal/external dependencies
- [ ] Revive the Latte documentation 
(Seanld's website is down...)
- [ ] Keep it less convulated than StaSh's 
current pip implementation. 

## What is this repository for?

This repo is dedicated to hosting Latte 
packages for testing. You can add this 
repo to your Latte config by running the 
code below in StaSh:

```
latte add-repo 
https://raw.githubusercontent.com/sn3ksoftware/lattepkgs
```

and you'll be all set!

## P.S

At the time of this commit, it is not 
known what license Seanld's code is under, 
which is confusing due to Latte's source 
code being available online freely.
Hence, it is assumed their code is public 
domain. My modifications to their code 
would be under the MIT License.
