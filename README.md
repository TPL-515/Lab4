# Lab 4

For this lab we will be creating scheduled runs for our jobs and manipulating their run intervals.

## Getting Started

First clone the lab locally and install the dependencies like so:

```bash
git clone git@github.com:TPL-515/Lab1.git
cd Lab1/
pip install -e ".[dev]"
```

This should install all of the required dependencies for the lab.

## Running the Lab

In order to run the lab just run the following command:

```bash
dagster dev
```

From here you should be able to navigate to the UI hosted at: http://localhost:3000

## Lab Tasks

For this lab you will be asked to perform the following tasks

1) Verify that the assets run first within the U.I.

2) Start running the job on a regular schedule from within the U.I.

3) Create a new job with the order being run, walk, crawl

4) Schedule the new job to run every 5 minutes

5) Validate that the job is running every 5 minutes within the U.I.
