# Taskmaster for Keep

This project uses [Taskmaster](https://github.com/taskmaster-ai/taskmaster) to manage development tasks and workflows for the Keep AIOps platform.

## Quick Start

To get started with Keep using Taskmaster:

```bash
# Install dependencies and start development environment
taskmaster run quick-start

# Or run individual tasks
taskmaster run setup
taskmaster run dev
```

## Available Tasks

### Setup Tasks

- **`setup`** - Initial project setup and dependencies installation
  - Installs Python dependencies with Poetry
  - Installs UI dependencies with npm
  - Creates and configures state directory

### Development Tasks

- **`dev`** - Start development environment
  - Starts Keep backend, frontend, and websocket server with Docker Compose
  - Starts UI development server for hot reloading

- **`logs`** - View application logs
  - View all service logs
  - View specific service logs (backend, frontend)

### Testing Tasks

- **`test`** - Run tests
  - Run Python tests with pytest
  - Run UI tests with npm
  - Run tests with coverage

- **`lint`** - Run linting and code formatting
  - Format Python code with black and isort
  - Lint Python code with ruff
  - Lint and format UI code with ESLint and Prettier

### Build and Deploy Tasks

- **`build`** - Build the project
  - Build UI with Next.js
  - Build Docker images

- **`deploy`** - Deploy the application
  - Deploy with Docker Compose
  - Deploy with Grafana monitoring

### Utility Tasks

- **`clean`** - Clean up development artifacts
  - Stop and remove Docker containers
  - Clean Python cache files
  - Clean node modules and build cache

- **`docs`** - Generate and serve documentation
  - Start documentation server

- **`monitoring`** - Start monitoring stack
  - Start Grafana and Prometheus

## Scripts

Taskmaster provides convenient scripts that combine multiple tasks:

- **`quick-start`** - Complete setup and start development environment
- **`full-test`** - Run linting and all tests
- **`production-deploy`** - Build and deploy for production

## Environments

The configuration includes environment-specific settings:

- **Development** - Uses NO_AUTH for easy local development
- **Production** - Uses KEYCLOAK for authentication

## Usage Examples

```bash
# Start development environment
taskmaster run dev

# Run all tests
taskmaster run test

# Format and lint code
taskmaster run lint

# View logs
taskmaster run logs

# Clean up everything
taskmaster run clean

# Quick start for new developers
taskmaster run quick-start
```

## Keep Project Overview

Keep is an open-source AIOps and alert management platform that provides:

- 🔍 **Single pane of glass** - Best-in-class customizable UI for all your alerts and incidents
- 🛠️ **Swiss Army Knife for alerts** - Deduplication, correlation, filtering and enrichment
- 🔄 **Deep integrations** - Bi-directional syncs with monitoring tools, customizable workflows
- ⚡ **Automation** - GitHub Actions for your monitoring tools
- 🤖 **AIOps 2.0** - AI-powered correlation and summarization

## Project Structure

```
keep/
├── keep-ui/          # React/TypeScript frontend
├── keep/             # Python backend
├── docker-compose.yml # Docker services
├── pyproject.toml    # Python dependencies
├── taskmaster.json   # Taskmaster configuration
└── README.md         # Project documentation
```

## Getting Help

- [Keep Documentation](https://docs.keephq.dev)
- [Keep GitHub Repository](https://github.com/keephq/keep)
- [Taskmaster Documentation](https://github.com/taskmaster-ai/taskmaster) 