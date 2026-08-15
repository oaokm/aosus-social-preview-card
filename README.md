# Aosus Social Preview Card


## installation

## Step 1: Clone the Repository
```bash
git clone https://github.com/oaokm/aosus-social-preview-card.git
```

This command retrieves the entire source code of the **AOSUS Social Preview Card** project from its remote GitHub repository and creates a local copy on your machine. Cloning preserves the full commit history and makes it easy to pull future updates.



## Step 2: Navigate into the Project Directory
```bash
cd aosus-social-preview-card
```
This changes your current working directory to the freshly cloned project folder. All subsequent commands will be executed relative to this root path, ensuring that file references and environment paths are resolved correctly.



## Step 3: Create a Python Virtual Environment
```bash
python -m venv aosusSocialPreviewCardVenv
```
This generates an isolated Python virtual environment named `aosusSocialPreviewCardVenv` inside the project root. The virtual environment keeps all project‑specific dependencies separate from system‑wide packages, preventing version conflicts and improving reproducibility across different environments.


## Step 4: Activate the Virtual Environment
```bash
source aosusSocialPreviewCardVenv/bin/activate
```
This activates the virtual environment, modifying your shell session to use the Python interpreter and package manager from the isolated environment. *(On Windows, the equivalent command would be `aosusSocialPreviewCardVenv\Scripts\activate`.)* Once activated, any `pip` installations will be confined to this environment.



## Step 5: Install All Required Dependencies
```bash
pip install -r requirements.txt
```
This reads the `requirements.txt` file and installs every Python package listed there, along with their specified versions. This single step ensures that all necessary libraries (e.g., image processing, HTTP clients, or CLI frameworks) are available for the tool to function correctly.



## Step 6: Create a System‑Wide Symlink for the Virtual Environment's Python
```bash
sudo ln -s $(pwd)/aosusSocialPreviewCardVenv /usr/aosusSocialPreviewCardVenv/bin/python
```
This creates a symbolic link that makes the virtual environment's Python interpreter accessible at `/usr/aosusSocialPreviewCardVenv/bin/python`. Placing it under `/usr/` with `sudo` provides a fixed, canonical path that can be referenced by other system services, cron jobs, or scripts without worrying about the project's current location.



## Step 7: Create a Global Executable Symlink for the CLI Tool
```bash
sudo ln -s $(pwd)/aosusSocialCard/cli.py /usr/bin/aosusCard
```
This links the main CLI entry point (`cli.py`) to `/usr/bin/aosusCard`. Because `/usr/bin` is typically in the system `PATH`, you can now invoke the tool from any directory simply by typing `aosusCard`, without needing to specify the full path or the `.py` extension.



## Step 8: Make the CLI Script Executable
```bash
sudo chmod ugo+x ./aosusSocialCard/cli.py
```
This modifies the file permissions of `cli.py`, granting execute rights to the **u**ser (owner), **g**roup, and **o**thers. This is a necessary final step so that the operating system can run the script directly when you call `aosusCard` from the command line.



> **Final Note**  
> After completing these steps, ensure that the virtual environment is activated whenever you intend to use `aosusCard` (unless the script's shebang has been modified to point to the absolute path of the venv's Python). The tool is now ready for global use across your system.


## Genarate Social Preview Card by CLI
### 1. Command Syntax
```bash
aosusCard -gen <aosus article url>
```
This is the main command to generate a social preview card.

### 2. What It Does
It fetches the article from the provided URL, extracts basic article information a ready-to-use preview card image.

### 3. How to Run It
- Replace `<aosus article url>` with the actual article link (like this `https://discourse.aosus.org/t/topic/3916`).
- Run the command from any directory since `aosus` is installed globally.

### 4. Output
The generated card image is saved to `./aosusSocialCard/aosus_social_preview_card`.


## TCP/IP CLI Options

### 1. Check TCP/IP Status
```bash
aosusCard --tcp_status
```
This flag displays the current status of the TCP/IP server (e.g., running, stopped, or error state). It takes no additional arguments.

### 2. Start TCP/IP Server
```bash
aosusCard --tcp_start
```
This flag initializes and starts the TCP/IP server. Once executed, the server will begin listening for incoming connections.

### 3. Stop TCP/IP Server
```bash
aosusCard --tcp_stop
```
This flag gracefully shuts down the running TCP/IP server. It terminates all active connections and releases the bound port.

