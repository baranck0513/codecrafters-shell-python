# A Shell Made in Python

A fully functional, Unix-like shell built from scratch. It includes a complete REPL, command parsing, built-ins, quoting rules, redirection, pipelines, autocompletion, command history, and persistent history storage.

This project was built to deeply understand how real shells such as Bash and Zsh work internally — from parsing and execution to process management, pipes, and file descriptors.

The final result is a feature-rich interactive shell that behaves closely to traditional POSIX shells.

## 📦 Technologies & Concepts

- `Python`
- `Process management (fork/exec/spawn)`
- `PATH resolution`
- `File descriptors`
- `Pipes`
- `Command parsing / tokenizing`
- `Advanced quoting and escaping`
- `Autocompletion engine`
- `Command history (in-memory + persistent)`
- `Redirection (>, >>, <, 2>, 2>>)`
- `Pipelines (cmd1 | cmd2 | cmd3)`
- `Built-ins with custom logic`

## 🥀 Features
### ▶ Core Shell Behavior
- Fully interactive REPL with prompt
- Graceful handling of invalid or missing commands
- Structured parsing before command execution

### ▶ Built-in Commands
- `echo` — prints the given arguments
- `exit` — terminates the shell with a status code
- `pwd` — prints the current directory
- `cd` — supports:
  - absolute paths
  - relative paths
  - home directory (`cd ~` or just `cd`)

### ▶ External Program Support
- Searches executables using `$PATH`
- Executes programs with arguments
- Replaces the current process only for external commands
- Clear error messages for missing or non-executable files

### ▶ Quoting Support
All major quoting rules are implemented:
- Single quotes — literal text, no escaping
- Double quotes — allows escaping and special characters
- Backslash escaping
   - inside single quotes
   - inside double quotes
   - outside quotes
- Executing commands that are themselves inside quotes

### ▶ Redirection
Supports both stdout and stderr:
- `command > file`
- `command >> file`
- `command 2> file`
- `command 2>> file`
- `command < file`

Includes correct open modes, truncation, and file descriptor manipulation

### ▶ Autocompletion (Tab Completion)
A fully functional autocompletion engine:
- Completion for built-ins
- Completion for external executables
- Completion for arguments
- Partial and multiple match suggestions
- Graceful fallback when no completion exists

### ▶ Pipelines
Complete support for Unix-style pipelines:
- `cmd1 | cmd2`
- Pipelines containing built-ins
- Multi-stage pipelines (`cmd1 | cmd2 | cmd3 | ...`)

Each pipe is implemented via connected file descriptors and spawned processes

### ▶ Command History
- `history` builtin
- Lists previous commands
- Supports limiting number of stored entries
- Arrow-key navigation:
   - Up arrow → previous command
   - Down arrow → next command
- Re-executing commands from history by number

### ▶ History Persistence
My shell keeps history even after exit:
- Reads history from file at startup
- Writes history back on exit
- Appends new entries efficiently
- Optional write-on-exit or append-on-exit behavior

This mimics Bash-style persistent history

## 🤨 How It Was Built
1- Prompt, input handling, and REPL

2- Invalid command handling

3- Built-ins (exit, echo, pwd, cd, type)

4- Executable lookup through $PATH

5- Process execution for external programs

6- Advanced quoting & tokenising

7- Stdout, stderr, and stdin redirection

8- Pipelines using OS pipe()

9- Command history and navigation

10- Persistent history using a file

11- Autocompletion engine

## 🤓☝️ What I Learned
### Parsing & Tokenisation
- Handling multiple token types
- Correct implementation of quoting and escaping
- Understanding how real shells interpret text

### Process Management
- Working with subprocesses
- Connecting processes with pipes
- Redirecting file descriptors properly

### File Descriptors & Redirection
- Overriding stdout (`1`) and stderr (`2`)
- Appending vs truncating
- Managing input files via `<`

### Interactive Terminal Handling
- Capturing arrow keys
- Managing input buffers
- Implementing autocompletion logic

### Shell Architecture
- Parser → Executor pipeline
- Built-ins vs external commands
- History system design
- Persistent storage strategy
