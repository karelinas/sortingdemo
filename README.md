This directory contains an interactive sorting demo.

Requirements:
* Linux/Unix machine
    * Tested on Ubuntu 18.04
    * MacOS and Windows Subsystem for Linux might work but are untested
* `Bash`
* `Python 3.6` or newer (tested with 3.6.9)
* `pip3`
* `virtualenv`

The demo uses images from `static/images` and performs interactive sorting on
them. Place your own images there to sort anything you like.

To run the demo, type `./run.sh` in the `demo/` folder. This installs the
dependencies in a virtual environment (using `virtualenv`) and starts the demo
server on http://localhost:5000


Credits:
    Merge-insertion sort implementation by The Algorithms https://github.com/TheAlgorithms/Python