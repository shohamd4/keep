#!/bin/bash

# Keep Taskmaster Initialization Script
# This script helps you get started with Keep using Taskmaster

set -e

echo "🚀 Initializing Keep with Taskmaster..."
echo "======================================"

# Check if taskmaster is installed
if ! command -v taskmaster &> /dev/null; then
    echo "❌ Taskmaster is not installed."
    echo "Please install Taskmaster first:"
    echo "  npm install -g @taskmaster-ai/cli"
    echo "  or visit: https://github.com/taskmaster-ai/taskmaster"
    exit 1
fi

echo "✅ Taskmaster is installed"

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo "❌ Docker is not running."
    echo "Please start Docker and try again."
    exit 1
fi

echo "✅ Docker is running"

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry is not installed."
    echo "Please install Poetry first:"
    echo "  curl -sSL https://install.python-poetry.org | python3 -"
    exit 1
fi

echo "✅ Poetry is installed"

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed."
    echo "Please install Node.js first:"
    echo "  https://nodejs.org/"
    exit 1
fi

echo "✅ Node.js is installed"

echo ""
echo "🎯 Starting Keep setup with Taskmaster..."
echo ""

# Run the quick-start script
taskmaster run quick-start

echo ""
echo "🎉 Keep has been initialized successfully!"
echo ""
echo "📋 Next steps:"
echo "  1. Open http://localhost:3000 to access the Keep UI"
echo "  2. Open http://localhost:8080 to access the Keep API"
echo "  3. Check logs with: taskmaster run logs"
echo "  4. Run tests with: taskmaster run test"
echo ""
echo "📚 Useful commands:"
echo "  taskmaster run dev     - Start development environment"
echo "  taskmaster run test    - Run all tests"
echo "  taskmaster run lint    - Format and lint code"
echo "  taskmaster run clean   - Clean up development artifacts"
echo "  taskmaster run logs    - View application logs"
echo ""
echo "📖 For more information, see TASKMASTER.md" 