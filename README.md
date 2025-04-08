# Overtime Calculator

This is a simple Python script to calculate overtime based on sales performance and deadlines.

## 💡 What It Does

The script takes three inputs from the user:

- `quotafulfilled`: The amount of scrap sold (as a float).
- `profitquota`: The expected profit quota (as a float).
- `days until deadline`: The number of days left until the deadline (as an integer).

It then calculates the overtime value



## 🚀 How to Run the Script

### ▶️ Option 1: With Python installed

1. Make sure Python is installed on your computer.
2. Open a terminal (or command prompt).
3. Navigate to the folder where your script is located.
4. Run:

```bash
python overtime_calculator.py

🧠 Option 2: Run in PyCharm
Open PyCharm.

Create a new project or open an existing one.

Right-click in the project panel and choose New > Python File, name it overtime_calculator.

Paste in the code from the script.

Click the green ▶️ "Run" button at the top or right-click on the file and choose "Run".

🌐 Option 3: Run Online with OneCompiler
Go to OneCompiler Python

Paste the full script into the editor.

Click the "Run" button.

Enter your input in the terminal window below the editor.

👉 Try it instantly: Example on OneCompiler

📓 Option 4: Run in JupyterLab / Google Colab
If you're using a notebook interface like JupyterLab or Google Colab:

Paste the script in a code cell, like this:

scrap_sold = float(input("quotafulfilled: "))
profitquota = float(input("profitquota: "))
daysuntildeadline = int(input("days until deadline: "))

overtime = (scrap_sold - profitquota) / 5 + 15 * daysuntildeadline
print("\novertime:", overtime)
Run the cell.

Enter input when prompted in the notebook interface.
