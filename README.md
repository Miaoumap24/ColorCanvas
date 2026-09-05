# ColorCanvas

A lightweight desktop drawing application built with Python.

## Features

- **Drawing Tools:** Freehand Pencil, Eraser, Straight Line, Rectangle, and Ellipse.
- **Customization:** Color picker for custom stroke colors and an adjustable brush size slider.
- **Canvas Management:** One-click clear canvas option with a confirmation prompt.
- **Export:** Export vector drawings directly to PostScript (`.ps`) format.

## Requirements

- **Python 3.x**
- **Tkinter** (included in standard Python distributions for Windows and macOS).

> **Linux users:** If Tkinter is missing, install it via your package manager:
> ```bash
> sudo apt install python3-tk
> ```

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Miaoumap24/ColorCanvas.git
   cd ColorCanvas

```

2. Run the application:
```bash
python main.py

```



## Controls

| Tool | Action |
| --- | --- |
| **Pencil / Eraser** | Click and drag to draw freehand. |
| **Line / Shapes** | Click to set the origin, drag to adjust dimensions, release to place. |
| **Color / Size** | Select a custom palette color or tweak the slider to adjust thickness. |

## License

Distributed under the AGPL-3.0 License.
