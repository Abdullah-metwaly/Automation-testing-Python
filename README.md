# Software Tesing 
## using: Python - selenium - behave


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This project is built to test some of  "http://automationpractice.com/" pages' functionality here are the features 

- Contact us
- Sign up
- ✨Purchaing an item
- Searching
## Project Structure

- The project has a main file that run the automation tests
- Each feature is written as a driven test according to the behave outline
- For each feature file there's a cooresponding step file contains the core code
   - Each of these files has some methods to test the the steps 
   - There's a locator file which locate html elements by xpath



In order to run the project you need to make sure of having the needed tools 
 - pip 
 - behave 
 - selenium 
 - webdriver-manage
 - click
 - PyHamcrest
 - parser
 


## Installation

Here are the installation commands to run them

Install the tools and start the project.

```sh
python install pip
pip install behave
pip install selenium
pip install PyHamcrest
pip install webdriver-manager
pip install click
```


Purpose of the project

> The project is only meant for educational practice
> There are more advance test to be written
> all the files are written based on the scenarios
> from the feature file in behave outline 
> which are end-user friendly 

#### Building for source

For production release:

```sh
python main.py requried-feature
```

in order to run the features file you need to call the main file followed by the command name

## example 

```sh
python main.py search
```
## Features options 
  all
  contact-us
  invalid-sign-up
  prdouct-with-options
  purchasing-item
  search
  valid-sign-up
