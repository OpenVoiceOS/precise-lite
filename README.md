# Mycroft Precise

*A lightweight, simple-to-use, RNN wake word listener.*

Precise is a wake word listener.  The software monitors an audio stream ( usually a microphone ) and when it recognizes a specific phrase it triggers an event.  For example, at Mycroft AI the team has trained Precise to recognize the phrase "Hey, Mycroft".  When the software recognizes this phrase it puts the rest of Mycroft's software into command mode and waits for a command from the person using the device.  Mycroft Precise is fully open source and can be trined to recognize anything from a name to a cough.

## Supported Operating Systems

Precise is designed to run on Linux.  It is known to work on a variety of Linux distributions including Debian, Ubuntu and Raspbian.  It probably operates on other \*nx distributions.

## Training Models

### Train your own model

You can find info on training your own models [train-guide](https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word#how-to-train-your-own-wake-word). It requires
running through the **source install instructions** first.

**Note: Please use the training-guide mentioned in the link. It's really helpful and the repo is tested using the commands mentioned in the link.**
Custom training Method [link](https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word#how-to-train-your-own-wake-word)

### Data Collection

To collect data your own data, use the [data collection repo](https://github.com/AmateurAcademic/wakeword-recorder-py.git) by Bartmoss and Dan. 


## Installation

First create a virtual environment to install python packages.

```bash
python3 -m venv venv-name
source /path/to/venv/venv-name/bin/activate
pip install --upgrade pip
```

### Source Install

Start out by cloning `dev` branch of the repository:

```bash
git clone https://github.com/bkhti4/mycroft-precise.git
cd mycroft-precise
```

After this, run the setup script:

```bash
./setup.sh
```
## Usage

Finally, you can write your program and run it as follows:
```bash
source ./path/to/venv/venv-name/bin/activate  # Change the python environment to include precise library
```

Sample Python program:
```python
#!/usr/bin/env python3

from precise_runner import PreciseEngine, PreciseRunner

engine = PreciseEngine('.venv/bin/precise-engine', 'my_model_file.pb')
runner = PreciseRunner(engine, on_activation=lambda: print('hello'))
runner.start()

# Sleep forever
from time import sleep
while True:
    sleep(10)
```

In addition to the `precise-engine` executable, doing a **Source Install** gives you
access to some other scripts. You can read more about them [here][executables].
One of these executables, `precise-listen`, can be used to test a model using
your microphone after the model has been trained:

[executables]:https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word#how-to-train-your-own-wake-word

```bash
source .venv/bin/activate  # Gain access to precise-* executables
precise-listen my_model_file.net
```

To convert it into tflite run

```bash
precise-convert my_model_file.net
```

And you can run then tflite

```bash
precise-listen my_model_file.tflite
```
