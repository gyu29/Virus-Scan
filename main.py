import tkinter as tk
import subprocess
import clamav

class SecurityScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Scanner v1.0")
        self.root.geometry("800x400")
        
        # Create and place the background image
        background_image = tk.PhotoImage(file="background.png")
        background_label = tk.Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Create the 'scan' button
        scan_button = tk.Button(root, text="Scan", command=self.start_scan)
        scan_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
    def start_scan(self):
        scan_results = self.perform_scan()
        
        # Print results in terminal
        for result in scan_results:
            print(result)
        
    def perform_scan(self):
        clamscan = clamav.ClamScan()
        print("Running virus scan...")
        clamscan.scan("/")
        for virus in clamscan.infected:
            print(f"Virus found: {virus}") 

if __name__ == "__main__":
    root = tk.Tk()
    app = SecurityScannerApp(root)
    root.mainloop()
