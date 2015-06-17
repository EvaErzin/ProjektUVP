from tkinter import *

IZ_DAT = 0
IZ_VNOSA = 1
SAMOGLASNIKI = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
locila = '.,:;-?!"' + "'"
LOCILA = ['.', ',', ':', ';', '-', '?', '!', '"', "'"]

class Argo():

    def __init__(self, master):
        self.stanje = IZ_VNOSA
        self.niz = ''
        Label(master, text = 'Vnesi besedilo:').grid(row = 0, column = 0)
        Label(master, text = 'Prevedi v:').grid(row = 2, column = 0)
        
        self.vnos = StringVar(master)
        vneseni = Entry(master, textvariable=self.vnos)
        vneseni['width'] = 35
        vneseni.grid(row = 0, column = 1, columnspan = 3)

        self.izhod = StringVar(master)
        izhodni = Entry(master, textvariable=self.izhod)
        izhodni['width'] = 35
        izhodni.grid(row = 3, column = 1, columnspan = 3)

        papagaj = Button(master, text = 'papagajščino', command = self.pap)
        papagaj.grid(row=2, column=1)
        
        lat = Button(master, text = 'latovščino', command = self.lat)
        lat.grid(row=2, column=2)
        
        nazaj = Button(master, text = 'nazajščino', command = self.nazaj)
        nazaj.grid(row=2, column=3)

        dat = Button(master, text='ali izberi datoteko' , command=self.odpri)
        dat.grid(row = 1, column = 0, columnspan = 4)


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
        self.vnos.set(self.ime)

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
            if niz[i] in SAMOGLASNIKI:
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
        seznam = niz.split(' ')
        retval = ''
        for niz1 in seznam:
            niz2 = ''
            if not niz1.isalpha():
                niz2 = niz1.lstrip(locila)
                niz1 = niz1.rstrip(locila)
            if len(niz1) > 1 and niz1[-2] in SAMOGLASNIKI:
                for i in range(len(niz1) - 2):
                    if niz1[i] in SAMOGLASNIKI:
                        retval += '{0}la'.format(niz1[i])
                    else:
                        retval += niz1[i]
                retval += '{0}{1}la'.format(niz1[-2], niz1[-1])
            else:
                for i in range(len(niz1)):
                    if niz1[i] in SAMOGLASNIKI:
                        retval += '{0}la'.format(niz1[i])
                    else:
                        retval += niz1[i]
            for i in range(len(niz2)):
                if niz2[i] in LOCILA and (i == len(niz2) - 1 or not niz2[i+1].isalpha()):
                    retval += niz2[i]
            retval += ' '
                    
        if self.stanje == IZ_DAT:
            with open('{0}_latovscina.txt'.format(self.ime.split('.')[0]), 'wt') as f:
                print(retval, '\n', file = f)
            self.izhod.set('Shranjeno!')
        else:
            with open('latovscina.txt', 'at') as g:
                print(niz, '->', retval, file = g)
            self.izhod.set(retval)
                
    def nazajscina(self, niz):
        seznam = niz.split(' ')
        retval = ''
        zadnjiznak = ''
        for niz1 in seznam:
            jeprvi = False
            niz2 = ''
            zacloc = ''
            if len(niz1) > 0:
                zadnjiznak = niz1[-1]
                if niz1 == seznam[0] or zadnjiznak in ['.', '!', '?'] or niz1[0] in ['"', "'"]:
                    jeprvi = True
            if not niz1.isalpha():
                niz2 = niz1.lstrip(locila)
                niz1 = niz1.rstrip(locila)
            if len(niz1) > 0 and niz1[0] in LOCILA:
                retval += niz1[0]  #  Na začetku besede naj bi bili samo narekovaji.
                niz1 = niz1.lstrip(locila)
            if len(niz1) > 0:
                if niz1[0].isupper():
                    if len(niz1) > 1 and (niz1[0] != 'I' and niz1[1] != "'"):  #  Upošteva tudi angleške okrajšave kot npr I'm in I'll (ohrani se velika začetnica I-ja).
                        retval += niz1[-1].upper() 
                        for i in range(2, len(niz1)):
                            retval += niz1[-i]
                        retval += niz1[0].lower()
                    elif jeprvi:  #  Če je ena od prej omenjenih kratic in na začetku besede bo imela prva črka veliko začetnico.
                        retval += niz1[-1].upper()
                        for i in range(2, len(niz1) + 1):
                            retval += niz1[-i]
                    else:  #  Drugače ne.
                        for i in range(1, len(niz1) + 1):
                            retval += niz1[-i]
                else:
                    for i in range(1, len(niz1) + 1):
                        retval += niz1[-i]
                for i in range(len(niz1), len(niz2)):
                    if niz2[i] in LOCILA:
                        retval += niz2[i]
            else: retval += ' ' #  Dvojni oz. večkratni presledki se ohranijo.
            for i in range(1, len(zacloc)+1):
                retval += zacloc[-i]
            retval += ' '
        if self.stanje == IZ_DAT:
            with open('{0}_nazajscina.txt'.format(self.ime.split('.')[0]), 'wt') as f:
                print(retval, '\n', file = f)
            self.izhod.set('Shranjeno!')
        else:
            with open('nazajscina.txt', 'at') as g:
                print(niz, '->', retval, file = g)
            self.izhod.set(retval)
        

root = Tk()
root.wm_title('Pretvornik besedila')
aplikacija = Argo(root) 
root.mainloop()
