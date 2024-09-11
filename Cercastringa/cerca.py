
import os
import PyPDF2

lTextExtension = [".py", ".txt", ".js", ".cvs", ".json", ".html", ".css"]

def CercaStringaInNomeFile(sFile, sStinga):
    # mettiamo tutto minuscolo
    sFileLC = sFile.lower()
    sStringaLC = sStinga.lower()

    # usiamo sFileLower.find() che torna -1 se la parola non c'è o la pos se c'è
    if(sFileLC.find(sStringaLC)>=0):
        return True
    else:
        return False

    # torniamo true oppure false


def CercaStringaInTextFile(sFile, sStringa):
    iRet = -1
    with open(sFile, "r") as file1:
        sRiga = ""
        sRiga = file1.readline()
        while len(sRiga) > 0:
            iRet = sRiga.lower().find(sStringa.lower())
            if iRet >= 0:
                return True
            iRet = file1.readline()
    return False


def CercaInFilePdf(sFile,sString):
	object = PyPDF2.PdfReader(sFile)
	numPages = len(object.pages)
	for i in range(0, numPages):
		pageObj = object.pages[i]
		text = pageObj.extract_text()
		text = text.lower()
		if(text.find(sString)!=-1):
			return True
	return False


def CercaStringaInContenutoFile(sPathFile, sStringa):
    sOutFileName,sOutFileExt = os.path.splitext(sPathFile)
    if sOutFileExt.lower() in lTextExtension:
        bret = CercaStringaInTextFile(sPathFile, sStringa)
    elif sOutFileExt.lower() == ".pdf":
        bret = CercaInFilePdf(sPathFile, sStringa)


    return bret


sRoot = input("Inserisci directory in cui cercare:")
sParola = input("Inserisci la stringa da cercare:")
sOutDir = input("Inserisci la dir di output:")

iNumFileTrovati = 0

for root, dirs, files in os.walk(sRoot):
    print(f"Sto guardando {root} che contiene {len(dirs)} subdir e {len(files)} files")
    for file in files:
        print(f"Devo vedere se {file} contiene {sParola}")
        bret = CercaStringaInNomeFile(file, sParola)
        if bret == True:
            iNumFileTrovati += 1
        else:
            sFilePathCompleto = os.path.join(root, file) # root + "/" + file
            bret = CercaStringaInContenutoFile(sFilePathCompleto, sParola)
            if bret == True:
                iNumFileTrovati += 1
        if bret == True:
            print("Trovata parola in file" + file)


print(f"Ho trovato {iNumFileTrovati} files")

