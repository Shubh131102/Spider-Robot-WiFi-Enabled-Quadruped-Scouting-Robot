import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Spider Quadruped Control")
        self.geometry("420x240")
        tk.Label(self, text="Pose / Gait Control", font=("Segoe UI", 14, "bold")).pack(pady=10)

        btn = tk.Button(self, text="Send Neutral Pose", command=self.send_neutral)
        btn.pack(pady=5)

        self.status = tk.Label(self, text="Ready", fg="green")
        self.status.pack(pady=10)

    def send_neutral(self):
        # TODO: send I2C/serial packet to Arduino -> PCA9685
        self.status.config(text="Neutral pose sent")

if __name__ == "__main__":
    App().mainloop()
