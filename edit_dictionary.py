from tkinter import ttk
from tkinter import *
import sqlite3


class Dictionary:
    db_name = 'dictionary_my.db'

    def __init__(self, window):

        self.wind = window
        self.wind.title('Редактирование словаря')

        # создание элементов для ввода слов и значений
        frame = LabelFrame(self.wind, text='Введите новое слово')
        frame.grid(row=0, column=0, columnspan=7, pady=20)
        Label(frame, text='Слово: ').grid(row=1, column=1)
        self.word1 = Entry(frame)
        self.word1.focus()
        self.word1.grid(row=2, column=1)
        self.word2 = Entry(frame)
        self.word2.grid(row=3, column=1)
        self.word3 = Entry(frame)
        self.word3.grid(row=4, column=1)

        Label(frame, text='Значение: ').grid(row=1, column=2)
        self.meaning1 = Entry(frame)
        self.meaning1.grid(row=2, column=2)
        self.meaning2 = Entry(frame)
        self.meaning2.grid(row=3, column=2)
        self.meaning3 = Entry(frame)
        self.meaning3.grid(row=4, column=2)

        Label(frame, text='Транскрипция: ').grid(row=1, column=3)
        self.trans1 = Entry(frame)
        self.trans1.grid(row=2, column=3)
        self.trans2 = Entry(frame)
        self.trans2.grid(row=3, column=3)
        self.trans3 = Entry(frame)
        self.trans3.grid(row=4, column=3)

        Label(frame, text='доп: ').grid(row=1, column=4)
        self.dop1 = Entry(frame)
        self.dop1.grid(row=2, column=4)
        self.dop2= Entry(frame)
        self.dop2.grid(row=3, column=4)
        self.dop3 = Entry(frame)
        self.dop3.grid(row=4, column=4)

        Label(frame, text='тип: ').grid(row=1, column=5)
        self.type1 = Entry(frame)
        self.type1.grid(row=2, column=5)
        self.type2 = Entry(frame)
        self.type2.grid(row=3, column=5)
        self.type3 = Entry(frame)
        self.type3.grid(row=4, column=5)

        Label(frame, text='перевод-доп: ').grid(row=1, column=6)
        self.meandop1 = Entry(frame)
        self.meandop1.grid(row=2, column=6)
        self.meandop2 = Entry(frame)
        self.meandop2.grid(row=3, column=6)
        self.meandop3 = Entry(frame)
        self.meandop3.grid(row=4, column=6)

        Label(frame, text='перевод-тип: ').grid(row=1, column=7)
        self.meantype1 = Entry(frame)
        self.meantype1.grid(row=2, column=7)
        self.meantype2 = Entry(frame)
        self.meantype2.grid(row=3, column=7)
        self.meantype3 = Entry(frame)
        self.meantype3.grid(row=4, column=7)


        ttk.Button(frame, text='Сохранить', command=self.add_word).grid(row=7, columnspan=2, sticky=W + E)
        self.message = Label(text='', fg='green')
        self.message.grid(row=7, column=0, columnspan=2, sticky=W + E)

        # таблица слов и значений
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Слово', anchor=CENTER)
        self.tree.heading('#1', text='Значение', anchor=CENTER)

        # кнопки редактирования записей
        ttk.Button(text='Удалить', command=self.delete_word).grid(row=5, column=0, sticky=W + E)
        ttk.Button(text='Изменить', command=self.edit_word).grid(row=5, column=1, sticky=W + E)

        # заполнение таблицы
        self.get_words()

    # подключение и запрос к базе
    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # заполнение таблицы словами и их значениями
    def get_words(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT * FROM dictionary_full ORDER BY word1 DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            print(row)
            self.tree.insert('', 0, text=row[1], values=(row[2], ))

    # валидация ввода
    def validation(self):
        return len(self.word1.get()) != 0 and len(self.meaning1.get()) != 0

    # добавление нового слова
    def add_word(self):
        if self.validation():
            query = 'INSERT INTO dictionary_full VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)'
            parameters = (self.word1.get(), self.meaning1.get(), self.trans1.get(), self.dop1.get(), self.type1.get(), self.meandop1.get(), self.meantype1.get(),
                          self.word2.get(), self.meaning2.get(), self.trans2.get(), self.dop2.get(), self.type2.get(), self.meandop2.get(), self.meantype2.get(),
                          self.word3.get(), self.meaning3.get(), self.trans3.get(), self.dop3.get(), self.type3.get(), self.meandop3.get(), self.meantype3.get()
                          # self.dataen.get(), self.winen.get(), self.imgen.get(), self.texten.get(),
                          # self.dataru.get(), self.winru.get(), self.imgru.get(), self.textru.get()
                          )
            self.run_query(query, parameters)
            self.message['text'] = 'слово {} добавлено в словарь'.format(self.word1.get())
            self.word1.delete(0, END)
            self.meaning1.delete(0, END)
            self.word2.delete(0, END)
            self.meaning2.delete(0, END)
        else:
            self.message['text'] = 'введите слово и значение'
        self.get_words()

    # удаление слова
    def delete_word(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Выберите слово, которое нужно удалить'
            return
        self.message['text'] = ''
        word = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM dictionary_full WHERE word1 = ?'
        self.run_query(query, (word,))
        self.message['text'] = 'Слово {} успешно удалено'.format(word)
        self.get_words()

    # рeдактирование слова и/или значения
    def edit_word(self):
        self.message['text'] = 'да-да-да'
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Выберите слово для изменения'
            return
        word = self.tree.item(self.tree.selection())['text']
        old_meaning = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Изменить слово'

        Label(self.edit_wind, text='Прежнее слово:').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=word), state='readonly').grid(row=0,
                                                                                                         column=2)

        Label(self.edit_wind, text='Новое слово:').grid(row=1, column=1)
        # предзаполнение поля
        new_word = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=word))
        new_word.grid(row=1, column=2)

        Label(self.edit_wind, text='Прежнее значение:').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_meaning), state='readonly').grid(row=2,
                                                                                                                column=2)

        Label(self.edit_wind, text='Новое значение:').grid(row=3, column=1)
        # предзаполнение поля
        new_meaning = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_meaning))
        new_meaning.grid(row=3, column=2)

        Button(self.edit_wind, text='Изменить',
               command=lambda: self.edit_records(new_word.get(), word, new_meaning.get(), old_meaning)).grid(row=4,
                                                                                                             column=2,
                                                                                                             sticky=W)
        self.edit_wind.mainloop()

    # внесение изменений в базу
    def edit_records(self, new_word, word, new_meaning, old_meaning):
        query = 'UPDATE dictionary_full SET word1 = ?, meaning1 = ? WHERE word1 = ? AND meaning1 = ?'
        parameters = (new_word, new_meaning, word, old_meaning)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'слово {} успешно изменено'.format(word)
        self.get_words()


if __name__ == '__main__':
    window = Tk()
    application = Dictionary(window)
    window.mainloop()