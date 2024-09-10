# Iterating Over Data Challenge: Solution
This repository is the class activity for Iterating Over Data in Unit 1.

## Instructions
Start by cloning this repository. After setting up your virtual environment and installing required packages (see instructions below) as a group you should: 
- Look at the provided function stub
- Look at the provided tests
- Implement the functions to make the tests pass
- The first 3 functions build on each other.
    - Consider using each previous function to help build the next!
- The 4th function is there for whimsy, but it can still be tricky!

The first is done in class together.

## Getting Started
1. In Github click on the green "Code" button in Github and then copy the URL. This will allow you to download a copy of this project into your projects folder. This command makes a new folder called `Iterating-Over-Data-Challenge`, and then puts the project into this new folder. 

After copying the URL, run the following command in your terminal:

```
$ git clone <paste your copied URL here>
```

Use `ls` to confirm there's a new project folder

1. Move your location into this project folder

```bash
$ cd Iterating-Over-Data-Challenge
```

2. Create a virtual environment named `venv` for this project:

```bash
$ python3 -m venv venv
```

3. Activate this environment:

```bash
$ source venv/bin/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

4. Install dependencies once at the beginning of this project while your virtual environment is activated. Note that `(venv)` is not part of the command below that you need to run.

```bash
$ (venv) pip install -r requirements.txt
```
5. After installing dependencies, use the following command to run your tests:
   
```bash
$ (venv) pytest
```

You should see 2 failed test and 8 skipped tests. Comment out the skip decorators (`@pytest.mark.skip`) located above the skipped to tests to have them run. 