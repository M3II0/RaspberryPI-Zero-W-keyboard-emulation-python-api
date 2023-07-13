## What API does?
This python API can send keystrokes into device where is Raspberry PI Zero W connected.
You don't need to find keystrokes by yourself!

## Supported systems (Systems that can receive keycodes)
- Win10
- Win11

## Supported keyboard-layouts
- EN ('en')
- SK ('sk')

## Supported characters
- a-z
- A-Z
- 0-9 (Configure keyboard-layout to correct use)
- .*-=/+

## Requirements
- Set-up your Raspberry PI Zero W as USB HID device
NOTE: Make sure that /dev/hidg0 file exists

## Usage
- Copy & Paste api.py into your project folder

## Examples

Setting keyboard-layout
```python
import api

api.lang = "sk"
api.lang = "en"
```

Shutting down system
```python
import api

api.shutDown()
```

Writing text
```python
import api

api.writeText("Your text will be sent into device!")
```

Running shortcut
![image](https://github.com/M3II0/RaspberryPI-Zero-W-keyboard-emulation-python-api/assets/73041364/77a1a6f3-5b2f-4bdd-8087-0da7dd9c8da5)

```python
import api

api.shortcut("ctrl", "a")
```

## Recommendation
For more methods, look into api.py!
