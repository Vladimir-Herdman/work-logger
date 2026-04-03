# Installing the Application
This project was built using `uv` to handle python library and versionion
management. You can manually use `uv` to build and run every time, or use the
automation scripts in `scripts/` to configure everything for you.

This project assumes `uv` as a tool present on your system, but if needed,
here's a link to the `uv` website [download page](https://docs.astral.sh/uv/getting-started/installation/), or get it on your system
how you're used to acquiring third-party software.

## Manually
To install dependencies for your system, run `uv sync`. This will create
a `.venv` and download a python3.13 version (if not available on your
system), as well as any depended on python libraries.
- From here, `uv run src/main.py` will start the `pywebview` GUI.

If you're interested in creating an executable rather than running the `main.py`
file each time, run the below command after syncing to use `pyinstaller`.
- `___`

## Windows
The automation script `___` in `scripts/` will install `uv`, dowload necessary
libraries, use `pyinstaller` to generate an executable, and then remove all
downloaded files to leave just the executable.

Otherwise, if you follow the steps as above in the manual installation section,
it should still work the same for you. I recommend using `winget` for installing
tools on Windows (I like it), specifically `uv`, which will handle getting the
proper python and library dependencies for you, simplifying the process greatly.

