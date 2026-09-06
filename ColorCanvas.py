# Copyright (C) 2026 Lixiod Technologies

import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox

class ColorCanvas:
    def __init__(self, root):
        self.root = root
        self.root.title("ColorCanvas")
        self.root.geometry("1000x700")

        # Configuration
        self.pen_color = "#2c3e50"
        self.bg_color = "#ffffff"
        self.brush_size = 5
        self.tool = "pen"  # "pen", "eraser", "line", "rectangle", "ellipse"
        self.start_x = None
        self.start_y = None
        self.current_shape = None

        self._init_ui()
        self._bind_events()

    def _init_ui(self):
        # Toolbar
        toolbar = tk.Frame(self.root, bg="#eceff1", bd=1, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Tools
        tk.Button(toolbar, text="✏️ Pencil", command=lambda: self.set_tool("pen")).pack(side=tk.LEFT, padx=2, pady=5)
        tk.Button(toolbar, text="🧹 Eraser", command=lambda: self.set_tool("eraser")).pack(side=tk.LEFT, padx=2, pady=5)
        tk.Button(toolbar, text="📏 Line", command=lambda: self.set_tool("line")).pack(side=tk.LEFT, padx=2, pady=5)
        tk.Button(toolbar, text="🔲 Rectangle", command=lambda: self.set_tool("rectangle")).pack(side=tk.LEFT, padx=2, pady=5)
        tk.Button(toolbar, text="⚪ Ellipse", command=lambda: self.set_tool("ellipse")).pack(side=tk.LEFT, padx=2, pady=5)

        # Color selection
        self.color_btn = tk.Button(toolbar, text="🎨 Color", command=self.choose_color, bg=self.pen_color, fg="white")
        self.color_btn.pack(side=tk.LEFT, padx=10, pady=5)

        # Size
        tk.Label(toolbar, text="Size:", bg="#eceff1").pack(side=tk.LEFT, padx=(10, 2))
        self.size_scale = tk.Scale(toolbar, from_=1, to=50, orient=tk.HORIZONTAL, command=self.change_size)
        self.size_scale.set(self.brush_size)
        self.size_scale.pack(side=tk.LEFT, padx=2)

        # Global
        tk.Button(toolbar, text="🗑️ Clear All", command=self.clear_canvas, bg="#e74c3c", fg="white").pack(side=tk.RIGHT, padx=5, pady=5)
        tk.Button(toolbar, text="💾 Save", command=self.save_image, bg="#2ecc71", fg="white").pack(side=tk.RIGHT, padx=5, pady=5)

        # Canvas
        self.canvas = tk.Canvas(self.root, bg=self.bg_color, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def _bind_events(self):
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def set_tool(self, tool):
        self.tool = tool

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose a color", color=self.pen_color)
        if color[1]:
            self.pen_color = color[1]
            self.color_btn.config(bg=self.pen_color)

    def change_size(self, val):
        self.brush_size = int(val)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

        if self.tool in ["line", "rectangle", "ellipse"]:
            if self.tool == "line":
                self.current_shape = self.canvas.create_line(
                    self.start_x, self.start_y, event.x, event.y,
                    fill=self.pen_color, width=self.brush_size, capstyle=tk.ROUND
                )
            elif self.tool == "rectangle":
                self.current_shape = self.canvas.create_rectangle(
                    self.start_x, self.start_y, event.x, event.y,
                    outline=self.pen_color, width=self.brush_size
                )
            elif self.tool == "ellipse":
                self.current_shape = self.canvas.create_oval(
                    self.start_x, self.start_y, event.x, event.y,
                    outline=self.pen_color, width=self.brush_size
                )

    def on_drag(self, event):
        if self.tool == "pen":
            self.canvas.create_line(
                self.start_x, self.start_y, event.x, event.y,
                fill=self.pen_color, width=self.brush_size,
                capstyle=tk.ROUND, smooth=True
            )
            self.start_x = event.x
            self.start_y = event.y
        elif self.tool == "eraser":
            self.canvas.create_line(
                self.start_x, self.start_y, event.x, event.y,
                fill=self.bg_color, width=self.brush_size * 2,
                capstyle=tk.ROUND, smooth=True
            )
            self.start_x = event.x
            self.start_y = event.y
        elif self.tool in ["line", "rectangle", "ellipse"] and self.current_shape:
            self.canvas.coords(self.current_shape, self.start_x, self.start_y, event.x, event.y)

    def on_release(self, event):
        self.current_shape = None

    def clear_canvas(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to clear the canvas?"):
            self.canvas.delete("all")

    def save_image(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".ps",
            filetypes=[("PostScript", "*.ps"), ("All files", "*.*")]
        )
        if filepath:
            self.canvas.postscript(file=filepath, colormode="color")
            messagebox.showinfo("Success", f"File saved successfully:\n{filepath}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorCanvas(root)
    root.mainloop()
