from Tkinter import *
from epic_error import *
import tkFileDialog, csv


class Grader(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        # Set defaults
        self.ERROR_SOUND = "audio/error.wav"
        self.student_data = {}
        self.fname = None

        # Pack original frame
        self.pack()

        # Structural
        header = Frame(master)
        header.pack(padx=10, pady=10)
        body1 = Frame(master)
        body1.pack(padx=10)
        body2 = Frame(master)
        body2.pack(padx=10)
        body3 = Frame(master)
        body3.pack(padx=10)
        footer = Frame(master)
        footer.pack(padx=10, pady=10)

        # File prompt information
        file_prompt = Label(header, text="Open grade file:") 
        open_file_button = Button(header, command=self.openFile, text="Open...")
        
        # Student number entry
        student_num_entry_prompt = Label(body1, text="Student Number") 
        self.student_num_entry  = Entry(body1)
        student_num_entry_prompt.pack(side="left")
        self.student_num_entry.pack(side="right")

        # Grade entry
        grade_entry_prompt = Label(body2, text="Grade")
        self.grade_entry   = Entry(body2, width=3)
        grade_entry_prompt.pack(side="left")
        self.grade_entry.pack(side="right")

        self.student_no = StringVar()
        self.grade      = StringVar()

        self.enter = Button(body3, text="Enter Grade", command=self.enterGrade)

        # Set defaults
        self.student_no.set("")
        self.grade.set("1")

        # Listen
        self.student_num_entry["textvariable"] = self.student_no
        self.grade_entry["textvariable"] = self.grade

        self.student_num_entry.bind('<Key-Return>',
                              self.enterGrade)

        # Data presenter

        self.records_processed_num = StringVar()
        self.records_processed_num.set("0")
        self.records_processed_label= Label(footer, text="Records Processed: ")
        self.records_processed_data = Label(footer, textvariable=self.records_processed_num)
        self.records_processed_label.pack(side="left")
        self.records_processed_data.pack(side="right")

        self.info_block_data = StringVar()
        self.info_block_label= Label(master, textvariable=self.info_block_data)
        self.info_block_label.foreground = "red"
        self.info_block_label.pack()


        file_prompt.pack(side="left")
        open_file_button.pack(side="right")


        self.enter.pack()


    def enterGrade(self, event=None):
    	student_number = self.student_no.get()
        if not student_number:
            NO_STUDENT_NO.alert()
            self.info_block_label.config(fg="#EE4000")
            self.info_block_data.set(NO_STUDENT_NO.description)

        elif not self.student_data:
            NO_DATA.alert()
            self.info_block_label.config(fg="#EE4000")
            self.info_block_data.set(NO_DATA.description)
    	
        else:
            try:
                old_value = self.student_data[str(student_number)]
                self.student_data[str(student_number)] = self.grade.get()
                if old_value not in [0, "", '', None]:
                    self.info_block_label.config(fg="#FFA824")
                    self.info_block_data.set("Warning: Overwriting grade for %s." % (student_number))

                else:
                    self.info_block_label.config(fg="#9ACD32")
                    self.info_block_data.set("Student %s updated." % (student_number))
                self.records_processed_num.set(str(int(self.records_processed_num.get()) + 1))

            except Exception as e:
                print e
                BAD_STUDENT_NO.alert()
                self.info_block_label.config(fg="#EE4000")
                self.info_block_data.set(BAD_STUDENT_NO.description)
            
            try:
                self.saveFile()
            except Exception as e:
                print e
        
        self.student_no.set("")
    def openFile(self):
        self.student_data = {}

        self.fname = tkFileDialog.askopenfilename(filetypes=[('.csv', '.csv')])

        with open(self.fname, 'rb') as csvfile:
             reader = csv.reader(csvfile, delimiter=',')
             for row in reader:
                try:
                    self.student_data[str(row[0].strip("#"))] = row[1]
                except Exception as e:
                    pass

    def saveFile(self):
        data_list = [["#"+str(key), self.student_data[key], "#"] for key in sorted(self.student_data.keys())]

        if self.fname:
            with open(self.fname, 'wb') as f:
                writer = csv.writer(f)
                writer.writerows(data_list)



grader = Grader()

grader.master.title("EPIC Grader")
grader.master.maxsize(260, 200)
grader.master.minsize(260, 200)

# start the program
grader.mainloop()