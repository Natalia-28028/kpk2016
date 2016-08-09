import tkinter

def button1_command():
    print('Dafault')

def print_hello(event):
    #print('Hello!')
    print(dir(event))
    print(event.delta)
    print(event.time)
    print(event.num)
    print(event.x)
    print(event.y)
    print(event.x_root)
    print(event.y_root)
    print(event.widget)
    me = event.widget
    if me == button1:
        print('Hello!')
    elif me == button2:
        print('You print key2!')
    else:
        raise ValueError()

root = tkinter.Tk()

button1=tkinter.Button(root, text = "Button 1", command=button1_command)
button1.bind("<Button>", print_hello)
button1.pack()

button2=tkinter.Button(root, text = "Button 2")
button2.bind("<Button>", print_hello)
button2.pack()

root.mainloop()

