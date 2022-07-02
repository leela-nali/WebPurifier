import tkinter as tk
import tkinter.ttk as ttk
import tksheet as tks

class App(tk.Frame):
    def __init__(self):
        super().__init__()
    
    # Tab - init
    tabController = ttk.Notebook()
    tabController.pack(expand = 1, fill = "both")

    # Tab - Home
    tabHome = ttk.Frame(tabController)
    tabController.add(tabHome, text = "Home")
    # Tab - Filters
    tabFilters = ttk.Frame(tabController)
    tabController.add(tabFilters, text = "Filters")
    # Tab - Logs
    tabLogs = ttk.Frame(tabController)
    tabController.add(tabLogs, text = "Logs")
    
    




    def widgetHome(self):
        labelFrame = LabelFrame(self.tabHome, text = "Home")
        labelFrame.grid(column = 0, row = 0, padx = 8, pady = 4)
        label = Label(labelFrame, text = "Enter Your Name:")
        label.grid(column = 0, row = 0, sticky = 'W')
        textEdit = Entry(labelFrame, width = 20)
        textEdit.grid(column = 1, row = 0)
        label2 = Label(labelFrame, text = "Enter Your Password:")
        label2.grid(column = 0, row = 1)
        textEdit = Entry(labelFrame, width = 20)
        textEdit.grid(column= 1, row = 1)

    def widgetFilters(self):
        labelFrame = LabelFrame(self.tabFilters, text = "Filters")
        labelFrame.grid(column = 0, row = 0, padx = 8, pady = 4)

    def widgetLogs(self):
        labelFrame2 = LabelFrame(self.tabLogs, text = "Logs")
        labelFrame2.grid(column = 0, row = 0, padx = 8, pady = 4)
        label = Label(labelFrame2, text="Enter Your Name:")
        label.grid(column=0, row=0, sticky='W')
        textEdit = Entry(labelFrame2, width=20)
        textEdit.grid(column=1, row=0)
        label2 = Label(labelFrame2, text="Enter Your Password:")
        label2.grid(column=0, row=1)
        textEdit = Entry(labelFrame2, width=20)
        textEdit.grid(column=1, row=1)
    self.widgetLogs()
    self.widgetFilters()
    self.widgetHome()

if __name__ == "__main__":
    app = App()
    app.mainloop()