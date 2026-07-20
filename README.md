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
  - senstivie API credentials stored separately using environment variables and excluded from version control
  - runtime settings managed through configuration files
- Used Git throughout development, including:
  - commits and version tracking
  - remote repository management
  - SSH authentication between the Linux environment and GitHub

## 📊 Example Output

**T-10 Day Summary: IBM**

| Date | Open | High | Low | Close | Volume | Daily Diff | Daily % Change |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2026-07-06 | 288.35 | 300.82 | 287.65 | 299.52 | 7,181,525 |   |    |
| 2026-07-07 | 305.66 | 311.80 | 300.49 | 306.13 | 8,618,569 | 6.61 | 2.21% |
| 2026-07-08 | 300.77 | 303.82 | 295.59 | 302.05 | 7,416,749 | -4.08 | -1.33% |
| 2026-07-09 | 285.83 | 297.28 | 284.44 | 295.30 | 10,841,979 | -6.75 | -2.23% |
| 2026-07-10 | 297.26 | 298.77 | 287.50 | 287.56 | 3,640,089 | -7.74 | -2.62% |
| 2026-07-13 | 290.50 | 297.50 | 289.10 | 290.23 | 5,024,243 | 2.67 | 0.93% |
| 2026-07-14 | 226.37 | 229.92 | 213.22 | 217.07 | 67,440,873 | -73.16 | -25.21% |
| 2026-07-15 | 220.97 | 223.81 | 211.03 | 211.20 | 29,590,356 | -5.87 | -2.70% |
| 2026-07-16 | 208.82 | 219.95 | 204.44 | 219.05 | 22,533,271 | 7.85 | 3.72% |
| 2026-07-17 | 215.62 | 217.17 | 210.22 | 212.67 | 13,150,177 | -6.38 | -2.91% |


|   | Value |
|---|---:|
| Average Close | 264.08 |
| Highest Close | 306.13 |
| Lowest Close | 211.20 |
| Average Daily Diff | -8.68 |
| Average Daily % Change | -3.02% |
| Maximum Gain | 3.72% |
| Maximum Loss | -25.21% |
| Average Volume | 17,543,783.10 |

## 🧠 Skills Demonstrated

- Linux command-line workflows and automation
- Bash scripting and process orchestration
- Python-based financial data processing
- API integration and data handling
- Environment-based configuration management
- Git workflows and SSH authentication
- Debugging Linux environments and managing dependencies
