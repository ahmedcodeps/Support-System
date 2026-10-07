# Customer Support Request System

## Features

The system includes:

* Dictionaries for storing customer and request information
* A set to prevent duplicate request IDs
* A queue to process requests in the order they were received
* A stack to undo the most recent update
* High-priority handling for urgent requests
* Searching by request ID or customer name
* Sorting by date, priority, or status
* Recursion for displaying replies
* Comparisons of searching and sorting approaches
* Time and space complexity analysis

## Requirements

Before running the program, make sure you have:

* Python 3 installed
* VS Code or another Python editor
* A terminal

## Setup

### 1. Open the project

Open the `support_system` folder in VS Code.

### 2. Open the terminal

### 3. Activate the virtual environment

If the project uses a virtual environment named `.venv`, run:

```bash
source .venv/bin/activate
```

After activation, the terminal should show `(.venv)` at the beginning of the line.

### 4. Check Python

Run:

```bash
python --version
```

You should see a Python 3 version.

If `python` is not recognized, try:

```bash
python3 --version
```

## Running the Program

Make sure you are in the folder containing `support_system.py`.

Run:

```bash
python support_system.py or python3 support_system.py
```

## Debugging Note

During development, one possible problem is receiving a `python: command not found` error when trying to run the program. This happens when the terminal does not recognize the `python` command. The issue can be fixed by activating the project's virtual environment with:

```bash
source .venv/bin/activate
```

After activation, the program can be run with:

```bash
python support_system.py
```

Another possible problem is using `python` when the system only recognizes `python3`. In that case, the program can be started with:

```bash
python3 support_system.py
```

When debugging the program, I checked the error message, identified whether the problem was related to Python or the project code, and then tested the program again after making the correction. Testing one part of the program at a time also made it easier to identify problems with the queue, stack, searching, and sorting features.
