from tkinter import*
import calendar

def calendar_see():
    window=Tk()
    window.config(bg='light pink')
    window.title('Complete year Calendar')
    window.geometry('570x620')
    get_year=int(year_entry.get())
    window_content=calendar.calendar(get_year)
    year_cal=Label(window,text=window_content,font=('ariel',12,'bold'))
    year_cal.grid(row=5,column=1,padx=20)
    window.mainloop()


if __name__== '__main__':
    app=Tk()
    app.config(background='yellow')
    app.title('GUI CALENDAR')
    app.geometry('280x170')

    name=Label(app,text='CALENDAR',background='light pink',font=('Ariel',20,'bold'))
    name.grid(row=1, column=1)
    year=Label(app,text='Enter the year',bg='light blue',font=('arial',15,'bold'))
    year.grid(row=2,column=1)

    year_entry=Entry(app,font=('Arial',15,'bold'))
    year_entry.grid(row=3,column=1)
    
    button=Button(app,text='SUBMIT',fg='red',bg='black',command=calendar_see)
    button.grid(row=4,column=1)

    app.mainloop()
