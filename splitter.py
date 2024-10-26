#splits pdfs automatically


#SETUP MODULES
import os

os.system("pip install numpy, PyPDF2")

if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")

#Application
from numpy import array
from PyPDF2 import PdfReader, PdfWriter
import tkinter as tk
import ctypes
from tkinter import filedialog

def SplitPDF(fileName, pdfPath, outPath):
    with open(fileName, "r") as file:
        text = file.read()

    splits = (array(text.split()).reshape((-1, 2)))

    PDF = PdfReader(pdfPath)

    for file, splitRange in splits:
        file = outPath + '\\' + file[:-1] + '.pdf'
        splitRange = [int(page) for page in splitRange.split('-')]
        lower, upper = splitRange[0]-1, splitRange[1]

        writer = PdfWriter()
        for i in range(lower, upper):
            writer.add_page(PDF.pages[i])

        with open(file, "wb") as outputPdf:
            writer.write(outputPdf)
        print(file, "created\n")

def Menu():

    def SplitPDFPressed():

        fileName = splitFileEntry.get()
        pdfPath = PDFFileEntry.get()
        outPath = OutFolderEntry.get()

        if (fileName.strip() == '') or (pdfPath.strip() == '') or (outPath.strip() == ''):
            pass
        else:
            SplitPDF(fileName, pdfPath, outPath)

    def BrowseButton(fileType):

        
        if fileType == "split":
            filePath = filedialog.askopenfilename(filetypes = [("Text Files", ".txt")])
            splitFileEntry.insert(index = 0, string = filePath)
        elif fileType == "pdf":
            filePath = filedialog.askopenfilename(filetypes = [("PDF", ".pdf")])
            PDFFileEntry.insert(index = 0, string = filePath)
        elif fileType == "out":
            filePath = filedialog.askdirectory()
            OutFolderEntry.insert(index = 0, string = filePath)

    window = tk.Tk()
    window.geometry("500x300+100+100")
    window.title("SPLIT DF")
    window.resizable(False, False)

    myappid = 'CBC.Windu.SplitDF.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    window.iconbitmap("logo.ico")

    MainFrame = tk.Frame(window, width = 500, height = 300)

    FrameLeft = tk.Frame(MainFrame, width = 250, height = 300, bg = "#7BDCD0")
    FrameRight = tk.Frame(MainFrame, width = 250, height = 300, bg = "#555E6B")
    FrameLeft.pack(side = 'left')
    FrameLeft.pack_propagate(False)
    FrameRight.pack(side = 'left')
    FrameRight.pack_propagate(False)
    MainFrame.pack()

    SplitButton = tk.Button(MainFrame, text = "SPLIT", font = ('Courier', 30), command = SplitPDFPressed, bg = "#689D9E", activebackground = "#689D9E")
    SplitButton.place(anchor = tk.S, x = 250, y = 290)

    splitFileText = tk.Label(MainFrame, bg = "#7BDCD0", text = "Split File", font = ('Courier', 12))
    splitFileText.place(anchor = tk.N, x = 55, y = 50)
    splitFileEntry = tk.Entry(MainFrame, width = 20, font = ('Courier', 15))
    splitFileEntry.place(anchor = tk.N, x = 230, y = 50)

    PDFFileText = tk.Label(MainFrame, bg = "#7BDCD0", text = "PDF File", font = ('Courier', 12))
    PDFFileText.place(anchor = tk.N, x = 55, y = 100)
    PDFFileEntry = tk.Entry(MainFrame, width = 20, font = ('Courier', 15))
    PDFFileEntry.place(anchor = tk.N, x = 230, y = 100)

    browseSplitButton = tk.Button(MainFrame, text = "BROWSE", font = ('Courier', 10), command = lambda: BrowseButton("split"), bg = "#689D9E", activebackground = "#689D9E")
    browseSplitButton.place(anchor = tk.N, x = 400, y = 50)

    browsePDFButton = tk.Button(MainFrame, text = "BROWSE", font = ('Courier', 10), command = lambda: BrowseButton("pdf"), bg = "#689D9E", activebackground = "#689D9E")
    browsePDFButton.place(anchor = tk.N, x = 400, y = 100)

    OutFileText = tk.Label(MainFrame, bg = "#7BDCD0", text = "Out Dir", font = ('Courier', 12))
    OutFileText.place(anchor = tk.N, x = 55, y = 150)
    OutFolderEntry = tk.Entry(MainFrame, width = 20, font = ('Courier', 15))
    OutFolderEntry.place(anchor = tk.N, x = 230, y = 150)

    browseOutButton = tk.Button(MainFrame, text = "BROWSE", font = ('Courier', 10), command = lambda: BrowseButton("out"), bg = "#689D9E", activebackground = "#689D9E")
    browseOutButton.place(anchor = tk.N, x = 400, y = 150)
  

    window.mainloop()


Menu()

    
