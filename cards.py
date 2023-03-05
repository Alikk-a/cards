from tkinter import *
from tkinter import ttk
import sqlite3, datetime
from PIL import Image, ImageTk
from tkinter import filedialog
import os

class Card_en:
    def __init__(self):

        self.frame_all = ttk.Frame(borderwidth=5,  relief=RIDGE)
        self.frame_all.grid(row=5, column=0, columnspan=9, pady=20, padx=20)
        self.notebook = ttk.Notebook(self.frame_all, height=230, width=700)
        self.notebook.pack()

        # s = ttk.Style()
        # s.configure('My.TFrame', background='red') # in frame style='My.TFrame',
        self.frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_ru = ttk.Frame(borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame.grid(row=0, column=0, columnspan=1, pady=20)
        self.frame_ru.grid(row=0, column=0, columnspan=1, pady=20)

        self.notebook.add(self.frame, text="ENGLISH",  compound=LEFT)
        self.notebook.add(self.frame_ru, text="Translate",  compound=LEFT)

        # Label(self.frame, anchor="w", text='Слово: ').grid(row=1, column=1)
        self.first_word = self.init_label(0, 21, 16, 2, 1)
        self.second_word = self.init_label(0, 21, 16, 3, 1)
        self.third_word = self.init_label(0, 21, 16, 4, 1)

        # Label(self.frame_ru, text='перевод: ').grid(row=1, column=1)
        self.meaning1 = self.init_label(1, 37, 16, 2, 1)
        self.meaning2 = self.init_label(1, 37, 16, 3, 1)
        self.meaning3 = self.init_label(1, 37, 16, 4, 1)

        # Label(self.frame, text='транскрипт: ').grid(row=1, column=2)
        self.trans1 = self.init_label(0, 15, 12, 2, 2)
        self.trans2 = self.init_label(0, 15, 12, 3, 2)
        self.trans3 = self.init_label(0, 15, 12, 4, 2)

        # Label(self.frame, text='доп: ').grid(row=1, column=3)
        self.dop1 = self.init_label(0, 15, 12, 2, 3)
        self.dop2 = self.init_label(0, 15, 12, 3, 3)
        self.dop3 = self.init_label(0, 15, 12, 4, 3)

        self.meandop1 = self.init_label(1, 15, 12, 2, 2)
        self.meandop2 = self.init_label(1, 15, 12, 3, 2)
        self.meandop3 = self.init_label(1, 15, 12, 4, 2)

        # блок подсказок
        self.frame_help = ttk.Frame(self.frame, width=230)
        self.frame_help.grid(row=11, column=2, columnspan=3, pady=10, padx=5)
        self.frame_help_ru = ttk.Frame(self.frame_ru, width=230)
        self.frame_help_ru.grid(row=11, column=2, columnspan=2, pady=10, padx=5)

        self.imgen = ttk.Label(self.frame_help, relief="groove")
        self.imgru = ttk.Label(self.frame_help_ru, relief="groove")

        self.texten = Label(self.frame_help, width=15, font=("Arial", 12))
        self.textru = Label(self.frame_help_ru, width=15, font=("Arial", 12))


    def init_label(self, n_frame, width, font_size, grid_row, grid_col):
        frame = [self.frame, self.frame_ru]
        in_label = Label(frame[n_frame], anchor="w", width=width, font=("Arial", font_size))
        in_label.grid(row=grid_row, column=grid_col)
        return in_label


class Card_edit:
    def __init__(self, id_cur):

        self.edit_wind = Toplevel()
        self.edit_wind.title('Change Card')
        self.edit_wind.geometry("1000x350+300+350")

        query = 'SELECT * FROM dictionary_full WHERE ID=?'
        parameters = (id_cur, )
        c = self.run_query_ed(query, parameters)
        row = c.fetchone()

        self.frame_all_edit = ttk.Frame(self.edit_wind, borderwidth=5, height=230, width=550, relief=RIDGE)
        self.frame_all_edit.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

        self.frame_edit = ttk.Frame(self.frame_all_edit, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_ru_edit = ttk.Frame(self.frame_all_edit, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_edit.grid(row=0, column=0, columnspan=1, pady=20)
        self.frame_ru_edit.grid(row=0, column=1, columnspan=1, pady=20)

        Label(self.frame_edit, text='WORDS').grid(row=0, column=1)
        self.first_word_edit = self.init_item(row[1], 0, 15, 1, 1)
        self.second_word_edit = self.init_item(row[8], 0, 15, 2, 1)
        self.third_word_edit = self.init_item(row[15], 0, 15, 3, 1)

        Label(self.frame_edit, text='транскрипт').grid(row=0, column=2)
        self.trans1_edit = self.init_item(row[3], 0, 11, 1, 2)
        self.trans2_edit = self.init_item(row[10], 0, 11, 2, 2)
        self.trans3_edit = self.init_item(row[17], 0, 11, 3, 2)

        Label(self.frame_edit, text='доп').grid(row=0, column=3)
        self.dop1_edit = self.init_item(row[4], 0, 7, 1, 3)
        self.dop2_edit = self.init_item(row[11], 0, 7, 2, 3)
        self.dop3_edit = self.init_item(row[18], 0, 7, 3, 3)

        Label(self.frame_edit, text='type').grid(row=0, column=4)
        self.type1_edit = self.init_item(row[5], 0, 7, 1, 4)
        self.type2_edit = self.init_item(row[12], 0, 7, 2, 4)
        self.type3_edit = self.init_item(row[19], 0, 7, 3, 4)

        Label(self.frame_ru_edit, text='перевод').grid(row=0, column=1)
        self.meaning1_edit = self.init_item(row[2], 1, 30, 1, 1)
        self.meaning2_edit = self.init_item(row[9], 1, 30, 2, 1)
        self.meaning3_edit = self.init_item(row[16], 1, 30, 3, 1)

        Label(self.frame_ru_edit, text='доп-ru').grid(row=0, column=2)
        self.meandop1_edit = self.init_item(row[6], 1, 7, 1, 2)
        self.meandop2_edit = self.init_item(row[13], 1, 7, 2, 2)
        self.meandop3_edit = self.init_item(row[20], 1, 7, 3, 2)

        Label(self.frame_ru_edit, text='type-ru').grid(row=0, column=3)
        self.meantype1_edit = self.init_item(row[7], 1, 7, 1, 3)
        self.meantype2_edit = self.init_item(row[14], 1, 7, 2, 3)
        self.meantype3_edit = self.init_item(row[21], 1, 7, 3, 3)

        Label(self.frame_edit, text='help-img').grid(row=4, column=1)
        self.imgen_edit = self.init_item(row[24], 0, 11, 5, 1)
        self.imgen_edit.grid(row=5, column=1)
        Label(self.frame_edit, text='help-text').grid(row=4, column=2)
        self.texten_edit = self.init_item(row[25], 0, 11, 5, 2)

        Label(self.frame_ru_edit, text='help-img').grid(row=4, column=1)
        self.imgru_edit = self.init_item(row[28], 1, 11, 5, 1)
        Label(self.frame_ru_edit, text='help-text').grid(row=4, column=2)
        self.textru_edit = self.init_item(row[29], 1, 11, 5, 2)

        Button(self.frame_edit, text='ADD img', command=lambda: self.open_file(0)).grid(row=7, column=1)
        Button(self.frame_edit, text='DEL img', command=lambda: self.del_file(row[24], 0)).grid(row=7, column=2)
        Button(self.frame_ru_edit, text='ADD img', command=lambda: self.open_file(1)).grid(row=7, column=1)
        Button(self.frame_ru_edit, text='DEL img', command=lambda: self.del_file(row[28], 1)).grid(row=7, column=2)

        Button(self.edit_wind, text='Change CARD', command=lambda: self.edit_records(id_cur)).grid(row=3, column=0)


        self.word_imp = IntVar()
        important = [1, 2, 3, 4, 5]
        self.combobox = ttk.Combobox(self.edit_wind, width=3, justify=CENTER, values=important, state="readonly")
        self.combobox.grid(row=4, column=1)
        if row[31] != None:
            self.combobox.set(row[31])

        self.word_onoff = IntVar()
        self.onoff = ttk.Checkbutton(self.edit_wind, text="OFF CARD", variable=self.word_onoff)
        self.onoff.grid(row=3, column=1, padx=6, pady=6)
        if row[30] == 1:
            self.word_onoff.set(1)
        else:
            self.word_onoff.set(0)

        # similar card
        self.tree = ttk.Treeview(self.edit_wind, height=7, columns=1)
        self.tree.grid(row=0, column=2, columnspan=1)
        self.tree.column("#0", width=130)
        self.tree.column("#1", width=210)
        self.tree.heading('#0', text='WORD', anchor=CENTER)
        self.tree.heading('#1', text='Translate', anchor=CENTER)
        Button(self.edit_wind, text='Check Similar', command=lambda: self.get_similar()).grid(row=3, column=2)

        self.edit_wind.mainloop()

    def init_item(self, row_n, n_frame, width, grid_row, grid_col):
        frame = [self.frame_edit, self.frame_ru_edit]
        in_item = Entry(frame[n_frame], width=width, textvariable=StringVar(frame[n_frame], value=row_n))
        in_item.grid(row=grid_row, column=grid_col)
        return in_item

    def get_similar(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = "SELECT * FROM dictionary_full WHERE (word1 LIKE ? Or (meaning1 LIKE ? AND meaning1 NOT NULL)) AND id != ?"
        parameters = ('%'+str(self.first_word_edit.get())+'%', '%'+str(self.meaning1_edit.get())+'%', id_current, )
        db_rows = self.run_query_ed(query, parameters)
        for row_tree in db_rows:
            print(row_tree)
            self.tree.insert('', 0, text=row_tree[1], values=(row_tree[2], ))


    def del_file(self, name_img, num):
        field = [self.imgen_edit, self.imgru_edit]
        field[num].delete(0, END)
        path = 'img/'+name_img
        # os.remove(path)   удаление файла, но он может использоваться и в другой карте - пока заглушено


    def open_file(self, num):
        field = [self.imgen_edit, self.imgru_edit]
        filepath = filedialog.askopenfilename()
        name_file = filepath.split('/')[-1]
        ext = name_file.split('.')[-1]
        if ext == 'jpg' or ext == 'png' or ext == 'gif':
            field[num].delete(0, END)
            field[num].insert(0, name_file)
            self.save_img(filepath, name_file)
        else:
            self.message['text'] = 'Only - jpg / png / gif'

        print(filepath, ' - file: ', name_file, 'extension - ', ext)

    def save_img(self, filepath, name_file):
        image_new = Image.open(filepath)
        image_new.thumbnail((50, 50))
        image_new.save('img/' + name_file)

    def edit_records(self, id_cur):
        print('edit_records - ', id_cur)
        query = """
                UPDATE dictionary_full SET word1 = ?, word2 = ?, word3 = ?, 
                                        meaning1 = ?, meaning2 = ?, meaning3 = ?,
                                        trans1 = ?, trans2 = ?, trans3 = ?,
                                        dop1 = ?, dop2 = ?, dop3 = ?,
                                        type1 = ?, type2 = ?, type3 = ?,
                                        meandop1 = ?, meandop2 = ?, meandop3 = ?,
                                        meantype1 = ?, meantype2 = ?, meantype3 = ?,
                                        imgen = ?, texten = ?,
                                        imgru = ?, textru = ?,
                                        onoff = ?, important = ?
                                    WHERE ID = ?
                """
        parameters = (self.first_word_edit.get(), self.second_word_edit.get(), self.third_word_edit.get(),
                      self.meaning1_edit.get(), self.meaning2_edit.get(), self.meaning3_edit.get(),
                      self.trans1_edit.get(), self.trans2_edit.get(), self.trans3_edit.get(),
                      self.dop1_edit.get(), self.dop2_edit.get(), self.dop3_edit.get(),
                      self.type1_edit.get(), self.type2_edit.get(), self.type3_edit.get(),
                      self.meandop1_edit.get(), self.meandop2_edit.get(), self.meandop3_edit.get(),
                      self.meantype1_edit.get(), self.meantype2_edit.get(), self.meantype3_edit.get(),
                      self.imgen_edit.get(), self.texten_edit.get(),
                      self.imgru_edit.get(), self.textru_edit.get(),
                      self.word_onoff.get(), self.combobox.get(),
                      id_cur)    # datetime.datetime.now() - current datetime
        self.run_query_ed(query, parameters)
        # self.wind.message['text'] = 'word {} changed'.format(self.first_word_edit)
        self.edit_wind.destroy()

    def run_query_ed(self, query, parameters=()):
        print(parameters)
        with sqlite3.connect(db_name, isolation_level=None, timeout=0.1) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

class Main_window:
    # clicks = -1
    def __init__(self, window):

        self.wind = window
        self.card_en = Card_en()

        self.img_next_open = Image.open('pict/next.png')
        self.img_next = ImageTk.PhotoImage(self.img_next_open)
        self.img_prev_open = Image.open('pict/prev.png')
        self.img_prev = ImageTk.PhotoImage(self.img_prev_open)

        self.btn_next_en = ttk.Button(command=self.next, image=self.img_next, compound=RIGHT, text="EN  ").grid(row=1, column=0)
        self.winen = IntVar()
        self.winen_cb = ttk.Checkbutton(text="EN - YES!", variable=self.winen).grid(row=2, column=0, padx=3, pady=3)


        self.btn_next_ru = ttk.Button(command=self.next_ru, image=self.img_next, compound=RIGHT, text="RU  ").grid(row=1, column=1)
        self.winru = IntVar()
        self.winru_cb = ttk.Checkbutton(text="RU - YES!", variable=self.winru).grid(row=2, column=1, padx=3, pady=3)

        self.btn_prev = ttk.Button(command=self.prev, image=self.img_prev, compound=LEFT, text="").grid(row=1, column=3)

        self.but_change = ttk.Button(command=self.change_word, text="Change").grid(row=1, column=7)
        self.but_add = ttk.Button(command=self.add_word, text="ADD").grid(row=1, column=8)

        # self.on_off = Label(text='')
        # self.on_off.grid(row=6, column=7)

        # buttons start
        self.btn_start_en = ttk.Button(command=self.start_en, text="Start-EN").grid(row=6, column=0, pady=10, padx=15)
        self.btn_start_ru = ttk.Button(command=self.start_ru, text="Start-RU").grid(row=6, column=1, pady=10, padx=10)
        self.btn_start_en_ni = ttk.Button(command=self.start_en_ni, text="NI-En").grid(row=6, column=2, pady=10, padx=10)
        self.btn_start_ru_ni = ttk.Button(command=self.start_ru_ni, text="NI-Ru").grid(row=6, column=3, pady=10, padx=10)
        self.btn_important = ttk.Button(command=self.sel_important, text="IMP_4-5").grid(row=6, column=4, pady=10, padx=10)
        self.but_help = ttk.Button(command=self.hide_show, text="HELP off - on").grid(row=6, column=8, pady=10, padx=10)
        self.but_del = ttk.Button(command=self.alarm_del_word, text="DEL").grid(row=7, column=8, pady=10, padx=10)

        self.frame_progress = ttk.Frame(borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_progress.grid(row=7, column=0, columnspan=7, pady=10)
        self.message = Label(self.frame_progress, fg='green')
        self.message.grid(row=7, column=4, columnspan=4)

    def move_cards(self, clicks):   # если вызов через .bind и событие то в аргументы добавть event
        global row
        if row != [] and clicks <= len(row)-1:
            self.card_en.first_word["text"] = self.no_none(row[clicks][1])
            self.word_type(row[clicks][5], 0)
            self.card_en.second_word["text"] = self.no_none(row[clicks][8])
            self.word_type(row[clicks][12], 1)
            self.card_en.third_word["text"] = self.no_none(row[clicks][15])
            self.word_type(row[clicks][19], 2)
            self.card_en.trans1["text"] = self.no_none(row[clicks][3])
            self.trans_attention(row[clicks][3])
            self.card_en.trans2["text"] = self.no_none(row[clicks][10])
            self.card_en.trans3["text"] = self.no_none(row[clicks][17])
            self.card_en.dop1["text"] = self.no_none(row[clicks][4])
            self.card_en.dop2["text"] = self.no_none(row[clicks][11])
            self.card_en.dop3["text"] = self.no_none(row[clicks][18])

            self.card_en.texten["text"] = self.no_none(row[clicks][25])
            self.card_en.texten.grid(row=1, column=2)
            self.card_en.textru["text"] = self.no_none(row[clicks][29])
            self.card_en.textru.grid(row=1, column=2)

            # if row[clicks][30] == 1:
            #     self.on_off["text"] = 'Слово ВЫКЛ'
            # else:
            #     self.on_off["text"] = 'Слово вкл'


            self.message['text'] = 'Word - '+str(clicks+1) + ' of ' + str(len(row)) + '  last EN - ' + str(row[clicks][32]) + '  !!!->' + str(row[clicks][31])  + ' WEn->' + str(row[clicks][23])  + ' WRu->' + str(row[clicks][27])

            if row[clicks][24] != None and row[clicks][24] != '' and os.path.exists('img/'+row[clicks][24]):
                img = Image.open('img/'+str(row[clicks][24]))
                self.imgen = ImageTk.PhotoImage(image=img)
                self.card_en.imgen.config(image=self.imgen)
                self.card_en.imgen.grid(row=1, column=1)
            else:
                self.card_en.imgen.grid_forget()

            if row[clicks][28] != None and row[clicks][28] != '' and os.path.exists('img/'+row[clicks][28]):
                imgru = Image.open('img/'+str(row[clicks][28]))
                self.imgru = ImageTk.PhotoImage(image=imgru)
                self.card_en.imgru.config(image=self.imgru)
                self.card_en.imgru.grid(row=1, column=1)
            else:
                self.card_en.imgru.grid_forget()

            self.card_en.meaning1["text"] = self.no_none(row[clicks][2])
            self.word_type(row[clicks][7], 3)
            self.card_en.meaning2["text"] = self.no_none(row[clicks][9])
            self.word_type(row[clicks][14], 4)
            self.card_en.meaning3["text"] = self.no_none(row[clicks][16])
            self.word_type(row[clicks][21], 5)
            self.card_en.meandop1["text"] = self.no_none(row[clicks][6])
            self.card_en.meandop2["text"] = self.no_none(row[clicks][13])
            self.card_en.meandop3["text"] = self.no_none(row[clicks][20])

            # Progressbar
            percent = 100/len(row)*clicks
            ttk.Progressbar(self.frame_progress, orient="horizontal", length=210, value=percent).grid(row=7, column=0, columnspan=3)

            global id_current
            id_current = row[self.clicks][0]
            print('current id  ', id_current, ' Word - ', row[clicks][1])
        else:
            self.message['text'] = 'Больше НЕТ ничего в работу'

    def word_type(self, type, num_word):
        word_color = [self.card_en.first_word, self.card_en.second_word, self.card_en.third_word,
                      self.card_en.meaning1, self.card_en.meaning2, self.card_en.meaning3]
        if type == 'v':
            word_color[num_word]["foreground"] = 'brown'
        elif type == 'n':
            word_color[num_word]["foreground"] = 'blue'
        elif type == 'a':
            word_color[num_word]["foreground"] = 'green'
        else:
            word_color[num_word]["foreground"] = 'black'

    def trans_attention(self, trans):
        if trans is not None:
            if '.' in trans:
                self.card_en.trans1["foreground"] = 'red'
            else:
                self.card_en.trans1["foreground"] = 'black'

    def no_none(self, expr):
        expr_nn = f"{'' if expr is None else expr}"
        return expr_nn

    # on/off block help
    def hide_show(self):
        if self.card_en.frame_help.winfo_viewable():
            self.card_en.frame_help.grid_remove()
        else:
            self.card_en.frame_help.grid()

        if self.card_en.frame_help_ru.winfo_viewable():
            self.card_en.frame_help_ru.grid_remove()
        else:
            self.card_en.frame_help_ru.grid()

    def prev(self):
        self.clicks -= 1
        self.move_cards(self.clicks)

    today = datetime.datetime.now().date()
    imp3day = datetime.datetime.now().date() - datetime.timedelta(days=1)
    imp3Wday = datetime.datetime.now().date() - datetime.timedelta(days=3)
    imp4day = datetime.datetime.now().date() - datetime.timedelta(days=4)
    imp5day = datetime.datetime.now().date() - datetime.timedelta(days=7)
    def start_en(self):
        query = """
                SELECT *, date(dataen) AS dat FROM dictionary_full 
                WHERE (onoff == 0 Or onoff Is Null) 
                    And (((dat < ? Or dataru Is NULL) And (important = 5 Or important = 4 Or important Is NULL))
                    Or ((dat < ? Or dataru Is NULL) And important = 3 And winen = 0)
                    Or ((dat < ? Or dataru Is NULL) And important = 3 And winen = 1)
                    Or ((dat < ? Or dataru Is NULL) And important = 2)
                    Or ((dat < ? Or dataru Is NULL) And important = 1))
                ORDER BY important DESC, dat ASC
                LIMIT 700
                """
        parameters = (self.today, self.imp3day, self.imp3Wday, self.imp4day, self.imp5day, )
        c = self.run_query(query, parameters)
        global row
        row = c.fetchall()
        self.clicks = -1
        self.next()

    def start_ru(self):
        query = """
                SELECT *, date(dataru) AS dat FROM dictionary_full 
                WHERE (onoff == 0 Or onoff Is Null) 
                    And (
                        ( (dat < ? Or dataru Is NULL) And (important = 5 Or important = 4 Or important Is NULL) )
                    Or ( (dat < ? Or dataru Is NULL) And important = 3  And winen = 0 )
                    Or ( (dat < ? Or dataru Is NULL) And important = 3  And winen = 1 )
                    Or ( (dat < ? Or dataru Is NULL) And important = 2 )
                    Or ( (dat < ? Or dataru Is NULL) And important = 1 )
                    )
                ORDER BY important DESC, dat ASC
                LIMIT 700
                """
        parameters = (self.today, self.imp3day, self.imp3Wday, self.imp4day, self.imp5day, )
        c = self.run_query(query, parameters)
        global row
        row = c.fetchall()
        self.clicks = -1
        self.next_ru()

    def start_en_ni(self):
        query = """
                SELECT *, date(dataen) AS dat FROM dictionary_full 
                WHERE (onoff == 0 Or onoff Is Null) 
                    And ((dat < ? Or dataru Is NULL) And important = 2
                    Or (dat < ? Or dataru Is NULL) And important = 1)
                ORDER BY important ASC, winen ASC, dat ASC
                LIMIT 700
                """
        parameters = (self.imp4day, self.imp5day, )
        c = self.run_query(query, parameters)
        global row
        row = c.fetchall()
        self.clicks = -1
        self.next()

    def start_ru_ni(self):
        query = """
                SELECT *, date(dataru) AS dat FROM dictionary_full 
                WHERE (onoff == 0 Or onoff Is Null) 
                    And ((dat < ? Or dataru Is NULL) And important = 2
                    Or (dat < ? Or dataru Is NULL) And important = 1)
                ORDER BY important DESC, winru ASC, dat ASC
                LIMIT 700
                """
        parameters = (self.imp4day, self.imp5day, )
        c = self.run_query(query, parameters)
        global row
        row = c.fetchall()
        self.clicks = -1
        self.next_ru()

    def sel_important(self):
        query = """
                SELECT *, date(dataru) AS dat FROM dictionary_full 
                WHERE (onoff == 0 Or onoff Is Null) And (important = 5 Or important = 4)
                ORDER BY important DESC, dat ASC
                """
        c = self.run_query(query)
        global row
        row = c.fetchall()
        self.clicks = -1
        self.next()

    def next(self):
        self.en_win()
        self.winen.set(0)
        self.card_en.notebook.select(self.card_en.frame)
        self.clicks += 1
        self.move_cards(self.clicks)

    def next_ru(self):
        self.ru_win()
        self.winru.set(0)
        self.card_en.notebook.select(self.card_en.frame_ru)
        self.clicks += 1
        self.move_cards(self.clicks)


    def en_win(self):
        print('Record changed - EN ', id_current)
        query = """
                UPDATE dictionary_full SET winen = ?, dataen = ? WHERE ID = ?
                """
        parameters = (self.winen.get(), datetime.datetime.now(), id_current)
        self.run_query(query, parameters)

    def ru_win(self):
        print('Record changed - RU - ', id_current)
        query = """
                UPDATE dictionary_full SET winru = ?, dataru = ? WHERE ID = ?
                """
        parameters = (self.winru.get(), datetime.datetime.now(), id_current)
        self.run_query(query, parameters)

    def change_word(self):
        self.card_ed = Card_edit(id_current)

    def add_word(self):
        query = """
                INSERT INTO dictionary_full VALUES
                (NULL, ?, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
                 NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
                 NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
                 NULL, NULL)
                """
        parameters = ('new', )
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            lid = cursor.lastrowid
            print('insert  ', lid)
            conn.commit()
        global id_current
        id_current = lid
        # id_current = 386 #last[0]
        print(id_current)
        self.card_add = Card_edit(id_current)

    def alarm_del_word(self):
        self.alarm_del = Toplevel()
        self.alarm_del.title("Delete")
        self.alarm_del.geometry("311x191+500+200")
        query = """
                SELECT * FROM dictionary_full WHERE id = ?
                """
        parameters = (id_current, )
        c = self.run_query(query, parameters)
        row_id = c.fetchone()
        print('current id  ', id_current, ' Word - ', row_id[1])

        self.lab_del_qst = Label(self.alarm_del, font=("Times", 14), foreground='brown', text='Are you sure?\nDELETE card').grid(padx=15, pady=10, row=1, column=0, columnspan=2)
        self.lab_card = Label(self.alarm_del, font=("Arial", 16), foreground='green', text=str(row_id[1]).upper()).grid(padx=15, pady=10, row=2, column=0, columnspan=2)
        self.img1 = Image.open('pict/del.png')
        self.img_del = ImageTk.PhotoImage(self.img1)
        self.img2 = Image.open('pict/cancel.png')
        self.img_cancel = ImageTk.PhotoImage(self.img2)
        self.but_delete = ttk.Button(self.alarm_del, command=self.del_word, image=self.img_del, compound=LEFT,  text="DELETE").grid(padx=15, pady=10, row=3, column=0, columnspan=1)
        self.but_cancel = ttk.Button(self.alarm_del, command=self.del_cancel, image=self.img_cancel, compound=LEFT, text="Cancel").grid(padx=15, pady=10, row=3, column=1, columnspan=1)


    def del_cancel(self):
        self.alarm_del.destroy()

    def del_word(self):
        query = """
                DELETE FROM dictionary_full WHERE id = ?
                """
        parameters = (id_current, )
        self.run_query(query, parameters)
        print('WORD with id  ', id_current, ' DELETED')
        self.alarm_del.destroy()

    # connect DB
    def run_query(self, query, parameters=()):
        print(parameters)
        with sqlite3.connect(db_name, isolation_level=None, timeout=1) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

# START ALL
global db_name
db_name = 'dictionary_my.db'
global row
row = []
global id_current
id_current = 0

if __name__ == '__main__':
    window = Tk()
    application = Main_window(window)
    window.title("CARDS on Tkinter")
    window.geometry("750x500+400+100")
    ttk.Style().configure("TButton", font="helvetica 8 bold", foreground="#1c679d", background="#B2DFDB")
    # window.configure(bg='')
    window.option_add("*tearOff", FALSE)  # del ------ in menu
    window.iconphoto(True, PhotoImage(file='pict/favicon.png')) #True - for child_windows too
    window.update_idletasks()
    window.attributes("-alpha", 0.95)

    window.mainloop()
