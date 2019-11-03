# Welcome to latte-universe!
Latte is a simple package manager written in Python that lets [Pythonista](https://omz-software.com/pythonista) and [StaSh](https://github.com/ywangd/stash) users share their Python scripts and packages of intrest quickly.
Go to the main Latte [repo](https://github.com/sn3ksoftware/latte) for more infomation.

## What is this repository for?

This repo is dedicated to hosting Latte 
packages for testing. You can add this 
repo to your Latte config by running the 
code below in StaSh:

```
latte add-repo https://raw.githubusercontent.com/sn3ksoftware/latte-universe/master
```

and you'll be all set!

## What are these _.latte_ files for?

`.latte` files contain metadata for Latte packages and repositories.
They are written in a way similar to [ConfigParser](https://docs.python.org/3/library/configparser.html)
(with keys/values delimited by `=` signs).

## P.S

At the time of this commit, it is not 
known what license Seanld's code is under, 
which is confusing due to Latte's source 
code being available online freely.
Hence, it is assumed their code is public 
domain. My modifications to their code 
would be under the MIT License.
