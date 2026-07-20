# Linux Market Monitoring Tool 🐧

## 🔍 Overview

Personal project exploring Linux workflows by building a market monitoring tool within an Ubuntu virtual machine environment. Automated the retrieval of financial market data, processed daily price movements, and generated summary reports through a Bash and Python workflow.

## 🛠️ Technologies

- Ubuntu Linux virtual machine
- Bash scripting
- Python
- Pandas
- Alpha Vantage API
- Git and GitHub
- SSH key authentication
- Environment variables and configuration files
- CSV data processing

## 🚀 Project Journey

- Provisioned a Linux development environment through virtualisation:
  - Created an Ubuntu virtual machine
  - Configured the operating system and development tooling
  - Installed required packages and Python dependencies
- Built a Bash orchestration script to manage the workflow, including:
  - API data retrieval
  - file validation
  - logging
- Developed a Python analysis script to process market data, returning stats such as:
  - daily price changes
  - percentage movements
  - volume statistics
- Implemented separation of configuration and application logic:
  - Senstivie API credentials stored separately using environment variables and excluded from version control
  - runtime settings managed through configuration files
- Used Git throughout development, including:
  - commits and version tracking
  - remote repository management
  - SSH authentication between the Linux environment and GitHub

## 🧠 Skills Demonstrated

- Linux command-line workflows and automation
- Bash scripting and process orchestration
- Python-based financial data processing
- API integration and data handling
- Environment-based configuration management
- Git workflows and SSH authentication
- Debugging Linux environments and managing dependencies
