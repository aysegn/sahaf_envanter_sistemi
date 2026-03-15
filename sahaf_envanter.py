from tkinter import *
from tkinter import messagebox
def listele():
    liste_kutusu.delete(0,END)
    try:
        with open("envanter.txt","r",encoding="utf-8") as dosya:
            for satir in dosya:
                liste_kutusu.insert(END,satir.strip())
    except FileNotFoundError:
        pass
def sil():
    secili=liste_kutusu.curselection()

    if secili:
        cvp=messagebox.askyesno("Onay","Seçili kitabı silmek istediğinize emin misiniz?")
        if cvp:
            liste_kutusu.delete(secili)
            kalan_kitaplar= liste_kutusu.get(0,END)

            with open("envanter.txt","w",encoding="utf-8") as dosya:
                for kitap in kalan_kitaplar:
                    dosya.write(kitap + "\n")
            messagebox.showinfo("Başarılı","Kitap başarıyla silindi")
        else:
            messagebox.showwarning("Uyarı","Kütffen silmek için listeden bir kitap seçiniz")

def kaydet():
    ad=kitap_adi_kutusu.get()
    yazar=yazar_adi_kutusu.get()
    stok=stok_kutusu.get()

    if ad and yazar and stok:
        with open("envanter.txt","a",encoding="utf-8") as dosya:
            dosya.write(f"{ad} | {yazar} | {stok}\n")
            messagebox.showinfo("Bilgi", "Kitap Sisteme Eklendi")
        kitap_adi_kutusu.delete(0,END)
        yazar_adi_kutusu.delete(0,END)
        stok_kutusu.delete(0,END)
        listele()
    else:
        messagebox.showwarning("Hata","Lütfen tüm alanları doldurunuz")

root=Tk()
root.title("Sahaf Envanter Sistemi")
root.geometry("400x550")

Label(root,text="Kitap Adı: ").grid(row=0,column=0,sticky=W,pady=5)
kitap_adi_kutusu=Entry(root)
kitap_adi_kutusu.grid(row=0,column=1,sticky=W,pady=5)
Label(root,text="Yazar: ").grid(row=1,column=0,sticky=W,pady=5)
yazar_adi_kutusu=Entry(root)
yazar_adi_kutusu.grid(row=1,column=1,sticky=W,pady=5)
Label(root,text="Stok Adedi:").grid(row=2,column=0,sticky=W,pady=5)
stok_kutusu=Entry(root)
stok_kutusu.grid(row=2,column=1,sticky=W,pady=5)
Button(root,text="Kitabı Sisteme Ekle",command=kaydet,bg="green",fg="white",width=30).grid(row=3,column=0,columnspan=2,pady=5)
Button(root, text="Seçili Kitabı Sil", command=sil, bg="red", fg="white", width=20).grid(row=4, column=0, columnspan=2,pady=5)
liste_kutusu= Listbox(root,width=45,height=8)
Label(root,text="Kaydedilen Kitaplar",font=("Arial",10,"bold")).grid(row=5,column=0,columnspan=2,pady=(15,5))
liste_kutusu.grid(row=6,column=0,columnspan=2,padx=20,pady=10)
listele()
mainloop()
