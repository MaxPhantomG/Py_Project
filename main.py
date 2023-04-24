import src.TextEditor as txt

root = txt.Tk()
root.title("Блокнот")
root.geometry("700x500")
root.minsize(width=400, height=400)
txt.TextEditor(root)
root.mainloop()


