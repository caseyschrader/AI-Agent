# AI Agent

A Python-based AI agent built with Google's Gemini API that can interact with local files and execute tasks through function calling.

## Overview

This project demonstrates how to build an AI agent using Google's Gemini 2.5 Flash model. The agent can inspect directories, read files, and interact with a local calculator application while maintaining security boundaries.

**Note:** This project is a work in progress and is being actively developed.

## Features

- **File System Access**: Browse directories and read file contents within a permitted working directory
- **Security Controls**: Built-in path validation to prevent directory traversal attacks
- **File Truncation**: Automatically truncates large files at 10,000 characters to manage context
- **Calculator Integration**: Includes a fully functional calculator application with test suite
- **Verbose Mode**: Optional detailed output showing token usage and statistics

## Project Structure

```
ai_agent/
├── calculator/          # Calculator application
│   ├── pkg/
│   │   ├── calculator.py  # Core calculator logic
│   │   └── render.py      # JSON output formatting
│   ├── main.py           # Calculator CLI
│   └── tests.py          # Unit tests
├── functions/           # Agent function tools
│   ├── get_files_info.py   # Directory listing
│   └── get_file_content.py # File reading
├── main.py             # AI agent entry point
└── pyproject.toml      # Project dependencies
```

## Requirements

```
python >= 3.12
google-genai == 1.12.1
python-dotenv == 1.1.0
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

### Basic Usage

```bash
python main.py "Your prompt here"
```

### Verbose Mode

Get detailed information about token usage:

```bash
python main.py "Your prompt here --verbose"
```

### Calculator Application

The included calculator supports basic arithmetic operations:

```bash
python calculator/main.py "3 + 5 * 2"
```

Output:
```json
{
  "expression": "3 + 5 * 2",
  "result": 13
}
```

## Function Tools

### `get_files_info(working_directory, directory=".")`

Lists all files and directories within a specified path.

**Returns:**
- File name
- File size in bytes
- Whether it's a directory

**Security:** Prevents access outside the working directory.

### `get_file_content(working_directory, file_path)`

Reads and returns the contents of a file.

**Features:**
- UTF-8 encoding
- Automatic truncation at 10,000 characters
- Path validation to prevent directory traversal

**Security:** Only reads files within the permitted working directory.

## Calculator Features

- **Supported Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Operator Precedence**: Respects standard mathematical order of operations
- **Error Handling**: Validates expressions and provides clear error messages
- **JSON Output**: Formats results as structured JSON
- **Test Coverage**: Comprehensive unit tests included

### Calculator Examples

```bash
# Simple arithmetic
python calculator/main.py "10 + 5"

# Order of operations
python calculator/main.py "2 * 3 + 4"

# Complex expression
python calculator/main.py "2 * 3 - 8 / 2 + 5"
```

## Running Tests

### Calculator Tests

```bash
cd calculator
python tests.py
```

### Function Tests

```bash
python tests.py
```

## Security Features

- **Path Validation**: All file operations validate paths to prevent directory traversal
- **Working Directory Boundary**: Functions cannot access files outside the designated working directory
- **Error Handling**: Graceful handling of invalid paths, missing files, and permission errors

## Example Agent Interactions

```python
# List files in calculator directory
python main.py "What files are in the calculator directory?"

# Read a specific file
python main.py "Show me the contents of calculator/main.py"

# Analyze code
python main.py "Explain how the calculator handles operator precedence"
```

## Development

This project uses:
- **uv** for dependency management
- **Python 3.12** as the base version
- **Google Gemini 2.5 Flash** for AI capabilities

## Current Status

**Work in Progress**: This project is under active development. The following features are being implemented:

## Planned Features

- [ ] Implement actual function calling with Gemini API
- [ ] Add more file operation tools (write, delete, move)
- [ ] Expand calculator to support more operations (exponents, parentheses, etc.)
- [ ] Add conversation history and context management
- [ ] Implement streaming responses
- [ ] Add support for multiple working directories
- [ ] Create interactive REPL mode for agent conversations

## License

This is a learning/development project. Use and modify as needed.
