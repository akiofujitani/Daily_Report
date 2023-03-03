import tkinter, logging, pystray, gui_builder
from tkinter.scrolledtext import ScrolledText
from os.path import abspath
from PIL import Image, ImageTk
from tkcalendar import Calendar
from datetime import datetime

logger = logging.getLogger('gui')


class Main_App(tkinter.Tk):
    def __init__(self, *args, **kwargs) -> None:
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title('Relatório diário')
        self.minsize(width=800, height=600)
        self.columnconfigure(0, weight=1)

        # Menu bar
        menu_bar = tkinter.Menu(self)
        file_menu = tkinter.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Salvar', command=self.save_command)
        file_menu.add_separator()
        file_menu.add_command(label='Sair', command=self.quit_command)

        edit_menu = tkinter.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label='Configuração', command=self.configuration_command)

        help_menu = tkinter.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label='Ajuda Índice', command=self.help_index_command)
        help_menu.add_command(label='Sobre', command=self.about_command)
        
        menu_bar.add_cascade(label='Arquivo', menu=file_menu)
        menu_bar.add_cascade(label='Editar', menu=edit_menu)
        menu_bar.add_cascade(label='Ajuda', menu=help_menu)
        self.config(menu=menu_bar)

        # Main app fields
        last_report = tkinter.LabelFrame(self, text='Último relatório', font=('Arial', 15))
        last_report.grid(column=0, row=0, columnspan=6, sticky='nesw', padx=(5), pady=(5,0))

        last_report_scroll = ScrolledText(last_report, width=40, height=10)
        last_report_scroll.grid(column=0, row=0, columnspan=5, rowspan=3, sticky='nesw', padx=(5, 0), pady=(5))
        last_report_scroll.configure(font=('Arial', 10), state='disabled')
        last_report.columnconfigure(0, weight=1)

        # Test calendar
        today = datetime.now().date()
        calendar_widget = Calendar(self, selectmode='day', year=today.year, month=today.month, day=today.day)
        calendar_widget.grid(column=0, row=1, columnspan=3, stick='nesw', padx=(5), pady=(5,0))



    # Commands
    def save_command(self):
        logger.debug('Save command')


    def quit_command(self):
        logger.debug('Quit command')
        self.quit()
    

    def configuration_command(self):
        logger.debug('Configuration command')
    

    def help_index_command(self):
        logger.debug('Help index command')


    def about_command(self):
        logger.debug('About command')
        gui_builder.About('Sobre', 
                    'Aplicativo:    Daily Report\nDesenvolvido por:  Akio Fujitani\nVersão:   0.10.00\ne-mail:  akiofujitani@gmail.com',
                    './Images/Bedo.jpg')


if __name__ == '__main__':
    logger = logging.getLogger()

    main = Main_App()
    main.mainloop()