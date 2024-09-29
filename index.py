from tkinter import *
import speedtest
root = Tk()
root.title("Speed Test")
root.geometry("500x400")
root.configure(background="gray")

label = Label(root, text="Internet Speed Check", font=("Lucida Sans Unicode", 20, "bold", "italic"), fg="#ffffff", bg="gray")
label.place(relx=0.5, rely=0.1, anchor=CENTER)

label_download = Label(root, text="Download Speed ⬇️", font=("Segoe Print", 18, "bold"), fg="green", bg="gray")
label_download.place(relx=0.25, rely=0.5, anchor=CENTER)

label_upload = Label(root, text="Upload Speed ⬆️", font=("Segoe Print", 18, "bold"), fg="blue", bg="gray")
label_upload.place(relx=0.75, rely=0.5, anchor=CENTER)

label_download_speed = Label(root, font=("Yu Gothic Light", 14, "bold"), fg="green", bg="gray")
label_download_speed.place(relx=0.25, rely=0.6, anchor=CENTER)

label_upload_speed = Label(root, font=("Yu Gothic Light", 14, "bold"), fg="green", bg="gray")
label_upload_speed.place(relx=0.75, rely=0.6, anchor=CENTER)

def speedCheck():
    
    st = speedtest.Speedtest()
    download_speed = round(st.download()/1000000, 2)
    print(download_speed)
    label_download_speed['text'] = str(download_speed) + "mbps"
    upload_speed = round(st.upload()/1000000, 2)
    print(upload_speed)
    label_upload_speed['text'] = str(upload_speed) + "mbps"


btn_speed_check = Button(root, text="Check Speed", command=speedCheck, bg="blue", fg="white", relief=FLAT)
btn_speed_check.place(relx=0.5, rely=0.3, anchor=CENTER)

root.mainloop()    