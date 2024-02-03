# Project Documentation

## Introduction

This document provides essential information about the project and outlines the necessary steps to execute scripts using the Selenium container.

## Prerequisites

Ensure that you have the following prerequisites installed on your system:

- Docker
- Docker Compose

## Execution Instructions

### 1. Start Docker Containers

Open a terminal window and navigate to the project directory. Run the following command to start the Docker containers:

```sh
sudo docker-compose up -d
```

### 2. Restart Selenium Container
If you need to run the py script again, use the following command:

```shell
sudo docker-compose restart selenium
```

because you need reestablish the driver connection between containers

### 3. Run Script
Every time you bring up the Docker containers, the script will automatically run. If you want to execute the script manually, you can do so using the appropriate command for your specific script.