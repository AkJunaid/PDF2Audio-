#!/usr/bin/env python3
"""
Simple GUI for PDF to Audiobook Converter
Run this if you prefer a graphical interface
"""

try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk
    from pdf_to_audiobook import PDFToAudiobook
    import threading
except ImportError:
    print("GUI requires tkinter. Install it or use the command-line version.")
    exit(1)


class AudiobookConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to Audiobook Converter")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Variables
        self.pdf_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.engine_var = tk.StringVar(value="gtts")
        self.language_var = tk.StringVar(value="en")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="🎧 PDF to Audiobook Converter",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=20)
        
        # PDF File Selection
        pdf_frame = tk.Frame(self.root)
        pdf_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(pdf_frame, text="PDF File:", width=12, anchor='w').pack(side=tk.LEFT)
        tk.Entry(pdf_frame, textvariable=self.pdf_path, width=40).pack(side=tk.LEFT, padx=5)
        tk.Button(pdf_frame, text="Browse", command=self.browse_pdf).pack(side=tk.LEFT)
        
        # Output File Selection
        output_frame = tk.Frame(self.root)
        output_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(output_frame, text="Output File:", width=12, anchor='w').pack(side=tk.LEFT)
        tk.Entry(output_frame, textvariable=self.output_path, width=40).pack(side=tk.LEFT, padx=5)
        tk.Button(output_frame, text="Browse", command=self.browse_output).pack(side=tk.LEFT)
        
        # Engine Selection
        engine_frame = tk.Frame(self.root)
        engine_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(engine_frame, text="TTS Engine:", width=12, anchor='w').pack(side=tk.LEFT)
        tk.Radiobutton(engine_frame, text="gTTS (Online)", variable=self.engine_var, 
                      value="gtts").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(engine_frame, text="pyttsx3 (Offline)", variable=self.engine_var, 
                      value="pyttsx3").pack(side=tk.LEFT)
        
        # Language Selection
        lang_frame = tk.Frame(self.root)
        lang_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(lang_frame, text="Language:", width=12, anchor='w').pack(side=tk.LEFT)
        languages = [("English (US)", "en"), ("English (UK)", "en-gb"), 
                    ("English (AU)", "en-au"), ("English (IN)", "en-in")]
        for text, value in languages:
            tk.Radiobutton(lang_frame, text=text, variable=self.language_var, 
                          value=value).pack(side=tk.LEFT, padx=5)
        
        # Progress Bar
        self.progress = ttk.Progressbar(self.root, mode='indeterminate')
        self.progress.pack(pady=20, padx=20, fill=tk.X)
        
        # Status Label
        self.status_label = tk.Label(self.root, text="Ready to convert", fg="blue")
        self.status_label.pack(pady=5)
        
        # Convert Button
        self.convert_button = tk.Button(
            self.root, 
            text="Convert to Audiobook",
            command=self.convert,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10
        )
        self.convert_button.pack(pady=20)
    
    def browse_pdf(self):
        filename = filedialog.askopenfilename(
            title="Select PDF file",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.pdf_path.set(filename)
    
    def browse_output(self):
        filename = filedialog.asksaveasfilename(
            title="Save audiobook as",
            defaultextension=".mp3",
            filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")]
        )
        if filename:
            self.output_path.set(filename)
    
    def convert(self):
        pdf_file = self.pdf_path.get()
        
        if not pdf_file:
            messagebox.showerror("Error", "Please select a PDF file")
            return
        
        # Run conversion in a separate thread
        thread = threading.Thread(target=self.run_conversion)
        thread.daemon = True
        thread.start()
    
    def run_conversion(self):
        try:
            self.convert_button.config(state=tk.DISABLED)
            self.progress.start()
            self.status_label.config(text="Converting... Please wait", fg="orange")
            
            converter = PDFToAudiobook(
                pdf_path=self.pdf_path.get(),
                output_path=self.output_path.get() if self.output_path.get() else None,
                engine=self.engine_var.get(),
                language=self.language_var.get()
            )
            
            success = converter.convert()
            
            self.progress.stop()
            
            if success:
                self.status_label.config(text="Conversion completed successfully!", fg="green")
                messagebox.showinfo("Success", f"Audiobook saved to:\n{converter.output_path}")
            else:
                self.status_label.config(text="Conversion failed", fg="red")
                messagebox.showerror("Error", "Conversion failed. Check console for details.")
        
        except Exception as e:
            self.progress.stop()
            self.status_label.config(text="Error occurred", fg="red")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
        
        finally:
            self.convert_button.config(state=tk.NORMAL)


def main():
    root = tk.Tk()
    app = AudiobookConverterGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
