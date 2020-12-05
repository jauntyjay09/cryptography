import PySimpleGUI as sg

sg.theme('Dark Blue 17')
layout = [
    [sg.Text('I am Soteria',font=("Helvetica", 25),background_color='#327ba2',relief=sg.RELIEF_RIDGE)],
    [sg.Text('Welcome', font=("Arial", 20))],
    [sg.Text('Select a host', size=(15, 1))],
    [sg.Radio('Image!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('text', "RADIO1")],
    [sg.Text('Choose a operation', size=(15, 1))],
    [sg.Radio('Encrypt     ', "RADIO2", default=True, size=(10,1)), sg.Radio('Decrypt', "RADIO2")],
    [sg.Text('File 1', size=(8, 1)), sg.Input(), sg.FileBrowse()],
    [sg.Text('Your secret message(Text/image file', size=(15, 1))],
    [sg.Checkbox('text-to-text?', size=(10,1))],
    [sg.Text('File 2', size=(8, 1)), sg.Input(), sg.FileBrowse()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Project Soteria', layout)
event, values = window.read()
window.close()
print(values[0], values[1], values[2],values[3],values[4],values[5])

    
if (values[0]==True and values[2]==True):
    import encimg as tp
    import textreader as t
    tp.img=values[4]
    text=t.call(values[6])
    tp.data=text
    tp.encode()
    sg.Popup('Success!')
    

elif(values[0]==True and values[3]==True):
    import decimg as dp
    dp.img=values[4]
    s=dp.call()
    sg.Popup('Your secret message was',s)






    


