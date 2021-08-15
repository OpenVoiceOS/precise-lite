# Mycroft Precise-Lite

*A lightweight, simple-to-use, RNN wake word listener.*

Precise is a wake word listener.  The software monitors an audio stream ( usually a microphone ) and when it recognizes a specific phrase it triggers an event.  For example, at Mycroft AI the team has trained Precise to recognize the phrase "Hey, Mycroft".  When the software recognizes this phrase it puts the rest of Mycroft's software into command mode and waits for a command from the person using the device.  Mycroft Precise is fully open source and can be trined to recognize anything from a name to a cough.

## Usage

```bash
precise-lite-listen my_model_file.net
```

To convert it into tflite run

```bash
precise-lite-convert my_model_file.net
```

And you can run then tflite

```bash
precise-lite-listen my_model_file.tflite
```
