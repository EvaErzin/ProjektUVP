from tkinter import *

IZ_DAT = 0
IZ_VNOSA = 1


class Argo():

    def __init__(self, master):
        self.stanje = IZ_VNOSA
        self.niz = ''
        Label(master, text = 'Pretvornik besedila').grid(row = 0, column = 0, columnspan = 4)        
        Label(master, text = 'Vnesi besedilo:').grid(row = 1, column = 0)
        Label(master, text = 'Prevedi v:').grid(row = 3, column = 0)
        self.vnos = StringVar(master)
        vneseni = Entry(master, textvariable=self.vnos)
        vneseni['width'] = 35
        vneseni.grid(row = 1, column = 1, columnspan = 3)

        self.izhod = StringVar(master)
        izhodni = Entry(master, textvariable=self.izhod)
        izhodni['width'] = 35
        izhodni.grid(row = 4, column = 1, columnspan = 3)

        papagaj = Button(master, text = 'papagajščino', command = self.pap)
        papagaj.grid(row=3, column=1)
        
        lat = Button(master, text = 'latovščino', command = self.lat)
        lat.grid(row=3, column=2)
        
        nazaj = Button(master, text = 'nazajščino', command = self.nazaj)
        nazaj.grid(row=3, column=3)

        dat = Button(master, text='ali izberi datoteko' , command=self.odpri)
        dat.grid(row = 2, column = 0, columnspan = 4)


    def odpri(self):
        self.ime = filedialog.askopenfilename()
        if self.ime == '':
            return
        else:
            niz1 = ''
            with open(self.ime) as f:
                for vrstica in f:
                    niz1 += vrstica.strip() + ' '
        self.niz = niz1
        self.stanje = IZ_DAT

    def pap(self):
        if self.stanje == IZ_VNOSA:
            self.niz = self.vnos.get()
        self.papagajscina(self.niz)
        self.niz = ''
        self.stanje = IZ_VNOSA

    def lat(self):
        if self.stanje == IZ_VNOSA:
            self.niz = self.vnos.get()
        self.latovscina(self.niz)
        self.niz = ''
        self.stanje = IZ_VNOSA
        
    def nazaj(self):
        if self.stanje == IZ_VNOSA:
            self.niz = self.vnos.get()
        self.nazajscina(self.niz)
        self.niz = ''
        self.stanje = IZ_VNOSA

    def papagajscina(self, niz):
        retval = ''
        for i in range(len(niz)):
            if niz[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                retval += '{0}{1}{2}'.format(niz[i], 'p', niz[i].lower())
            else:
                retval += niz[i]
        if self.stanje == IZ_DAT:
            with open('{0}_papagajscina.txt'.format(self.ime.split('.')[0]), 'wt') as f:
                print(retval, '\n', file = f)
            self.izhod.set('Shranjeno!')
        else:
            with open('papagajscina.txt', 'at') as g:
                print(niz, '->', retval, file = g)
            self.izhod.set(retval)
                
    def latovscina(self, niz):
        retval = ''
        for i in range(len(niz)):
            if niz[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                retval += '{0}la'.format(niz[i])
            else:
                retval += niz[i]
        if self.stanje == IZ_DAT:
            with open('{0}_latovscina.txt'.format(self.ime.split('.')[0]), 'wt') as f:
                print(retval, '\n', file = f)
            self.izhod.set('Shranjeno!')
        else:
            with open('latovscina.txt', 'at') as g:
                print(niz, '->', retval, file = g)
            self.izhod.set(retval)
                
    def nazajscina(self, niz):
        retval = ''
        for i in range(len(niz)-1, -1, -1):
            retval += niz[i]
        if self.stanje == IZ_DAT:
            with open('{0}_nazajscina.txt'.format(self.ime.split('.')[0]), 'wt') as f:
                print(retval, '\n', file = f)
            self.izhod.set('Shranjeno!')
        else:
            with open('nazajscina.txt', 'at') as g:
                print(niz, '->', retval, file = g)
            self.izhod.set(retval)
        

root = Tk() 
aplikacija = Argo(root) 
root.mainloop()
