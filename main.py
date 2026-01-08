import tkinter as tk
from tkinter import filedialog
from ocr import extract_text

def main():
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="Select image(s)",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.bmp *.tiff")
        ]
    )

    if not file_paths:
        print("No files selected.")
        return

    for path in file_paths:
        print("\n" + "=" * 20)
        print(f"Extracted text from: {path}")
        print("=" * 20)

        try:
            text = extract_text(path)
            print(text if text else "[No text detected]")
        except Exception as e:
            print(f"Error processing file: {e}")

if __name__ == "__main__":
    main()