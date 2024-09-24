# 0x1A. Application Server

## Background Context

Your web infrastructure is already serving web pages via Nginx installed in your first web stack project. This project will enhance your setup by adding an application server to handle dynamic content for your Airbnb clone project.

## Concepts

For this project, you will explore the following concepts:
- Web Server
- Server
- Web Stack Debugging

## Requirements

### General
- A `README.md` file is mandatory at the root of the project folder.
- All Python code must use `python3`.
- All config files must include comments.

### Bash Scripts
- All files should be executable and end with a new line.
- Scripts must pass Shellcheck without errors.
- The first line of all scripts must be `#!/usr/bin/env bash`.
- The second line must describe what the script does.

## Servers

| Name            | Username | IP               | State  |
|-----------------|----------|------------------|--------|
| 381966-web-01   | ubuntu   | 100.26.229.180   | running |
| 381966-web-02   |          |                  |        |
| 381966-lb-01    |          |                  |        |

## Project Tasks

### 0. Set Up Development with Python
- Install `net-tools` on your server:  
  ```bash
  sudo apt install -y net-tools
  ```
- Clone your AirBnB project to the server.
- Configure the Flask application to serve content from `/airbnb-onepage/` on port 5000.

### 1. Set Up Production with Gunicorn
- Install Gunicorn and any necessary libraries.
- Ensure your Flask application object is named `app`.
- Bind Gunicorn to localhost on port 5000.

### 2. Serve a Page with Nginx
- Configure Nginx to serve the page from `/airbnb-onepage/` on port 80.
- Proxy requests to the application server running on port 5000.
- Include your Nginx config file as `2-app_server-nginx_config`.

### 3. Add a Route with Query Parameters
- Add a service to handle requests at `/airbnb-dynamic/number_odd_or_even/<int:n>` using Gunicorn on port 5001.

### 4. API Setup
- Clone your AirBnB clone v3 repository.
- Set up Nginx to route `/api/` to a Gunicorn instance on port 5002.

## Resources

- [Application Server vs Web Server](#)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu](#)
- [Upstart Documentation](#)
