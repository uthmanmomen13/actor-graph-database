# tmdb functions spec

## Getting the skeleton code:

### **Do NOT run `git clone`**

1. First create a repository in Github (**not** git) via this link: https://github.com/new

2. Create a new repository using git by running the following commands in a directory of your choosing:
```
git init
git branch -M master
git remote add origin <YOUR GITHUB REPO LINK HERE>
git push -u origin master
```
A variation of these commands are present in the "...or create a new repository on the command line" section after you create a repository on Github.

3. Add this project's repository as remote and alias it to `source`:
```
git remote add source https://github.com/BearCloud/fa20-project-starter.git
```

4. Run the following command to pull starter code:
```
git pull source master
```
## Installing packages/virtual env
#### if you already have a python virtual environment you can use that. otherwise follow these instructions
1. `python3 -m venv devopsEnv`
2. activate the virtual env `source devopsEnv/bin/activate`
3. to deactive just type `deactivate` in your terminal
4. when you are in the virtual env run `pip install tmdbsimple`
5. run `python -m unittest TestFunctions` to check if there are any module errors

## High level overview

![Alt text](/images/im1.png)
![Alt text](/images/im2.png)

---
### **get_actor_id**
#### In order to get the movies an actor is in we first need the actor's tmdb id. You should make use of <code> tmdb.Search()</code>. 
---
### **get_list_of_movies**
#### Now that we have the actor Id we can make a search request for <code> combined-credits</code> of the actor. This will return only movie data. One problem is that a lot of other data is still returned so you will need to traverse through the large response and pick out the movie titles only. 

---
### **some tips**
#### the response types are usually lists or dictionaries so it may take some fiddling around to get a hang of how to easily parse out the data. Python dictionaries have the `keys()` method which returns a list of dictionary keys so this may be useful. As usual if you need any help message me.