from tkinter import Tk, Canvas

from datetime import datetime
events = [
    'Halloween,10/31/2023',
    'Christmas,12/25/2023',
    'City Skylines II Released,8/18/2023',
    'My Birthday,1/5/2024',
]
    

root = Tk()
c = Canvas(root, width=800, height=800, bg='black')
c.pack()
c.create_text(250, 50,
        anchor='w',
        fill='orange',
        font='Arial 28 bold underline',
        text='My Countdown Calendar')
offset = 0
for event in events:
    split_event = event.split(',')
    title = split_event[0]
    date_string = split_event[1]
    real_date = datetime.strptime(
                    date_string, '%m/%d/%Y')
    time_diff = str(real_date - datetime.now())
    offset = offset + 120
    title_text = title + ' | ' + date_string
    print(title)
    c.create_text(50, offset,
        anchor='w',
        fill='fuchsia',
        font='Arial 25 bold',
        text=title_text)
    c.create_text(50, offset + 50,
        anchor='w',
        fill='white',
        font='Arial 25 bold',
        text=time_diff)

