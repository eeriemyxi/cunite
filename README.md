# Cunite

![](https://files.catbox.moe/rriwz7.png)

Web interface to select a random video from a random Pornhub subscription.

# Installation
### First Method
```bash
git clone --depth 1 --branch main <REPO URL> cunite
pip install ./cunite
```
### Second Method
```bash
pip install git+<REPO URL>@main
```
# How To Run
Set environment variables `RELOAD` and `STORAGE_SECRET` then run the module.
```bash
RELOAD=false STORAGE_SECRET=somethingsecret python -m cunite
```
