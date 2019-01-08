'''
Created on Apr 18, 2018

@author: deinlein thomas
'''
    
import PyPDF2 
import os
import sys
import threading
import multiprocessing


class MyThread(threading.Thread):

    def __init__(self, pdfList):
        threading.Thread.__init__(self)
        self.__pdfList = pdfList
    
    def run(self):
        print("")
        print("Starting Thread " + str(threading.current_thread().getName()) + " Number of Pdfs: " + str(len(self.__pdfList)))
        counterProgress = 0
        
        for s in self.__pdfList: 
            progress = (int) (counterProgress / len(self.__pdfList) * 100)
            print("Processing Specification " + str(s) + " in Thread " + str(threading.current_thread().getName()) + ", Thread progress: " + str(progress) + "% ...\n")
            try:
                pdfFile = PyPDF2.PdfFileReader(s)
                pageCount = pdfFile.getNumPages()
            except Exception as e:
                print (str(e))
                allScopes[s] = "Error with Specification " + str(s) + " " + str(e)
                continue
            pagesFound = []
            startFound = False
            try:
                title = str(pdfFile.getDocumentInfo().getText("/Title")) + " --> " + str(pdfFile.getDocumentInfo().getText("/Subject"))
            except Exception as e:
                title = "Was unreadable from PDF!"
            allTitles[s] = title

            for pageNum in range(1, pageCount):  # ignore page 1
                try:
                    page = pdfFile.getPage(pageNum)
                    pageText = page.extractText().lower().replace("\n", "")
                except:
                    continue
                if start in pageText and points not in pageText:
                    pagesFound.append(pageNum)
                    startFound = True
                    
                if stop in pageText and startFound and points not in pageText:
                    if(pageNum + 1 < pageCount):
                        pagesFound.append(pageNum + 1)
                    else:
                        break
                    if (pageNum + 2 < pageCount):
                        pagesFound.append(pageNum + 2)
                    else:
                        break
                    if (pageNum + 3 < pageCount):
                        pagesFound.append(pageNum + 3)
                    else:
                        break
                    if (pageNum + 4 < pageCount):
                        pagesFound.append(pageNum + 4)
                    else:
                        break
                    if (pageNum + 5 < pageCount):
                        pagesFound.append(pageNum + 5)
                    else:
                        break
                    if (pageNum + 6 < pageCount):
                        pagesFound.append(pageNum + 6)
                    else:
                        break
                    break
                else:
                    continue
            text = ""
            for nr in pagesFound:   
                page = pdfFile.getPage(nr)
                text += page.extractText().lower().replace("\n", "")
             
            scope = text.find(start.lower())
            references = text.find(stop.lower())
            whatIWant = text[scope:references]
            whatIWant = whatIWant.replace("\n", "")
            temp = ""
            counter = 0
            for t in whatIWant:
                if counter == 130:
                    temp += "\n"
                    counter = 0
                temp += t
                counter += 1
            allScopes[s] = temp
            counterProgress += 1

        print("\n\n*** Finished Thread " + str(threading.current_thread().getName()) + "\n\n")
    

def get_arg(index):
    return sys.argv[index]


#########################################################################
try:
    start = get_arg(1)
    stop = get_arg(2)
    textFileName = get_arg(3)
    direct = get_arg(4)
except IndexError as e:
    start = "scope"
    stop = "references"
    textFileName = "scopesOfSpecifications"
    direct = "./Specifications"

dirList = os.listdir(direct)
dirList.sort()
pdfs = []

for g in dirList:
    if ".pdf" in g:
        pdfs.append(direct + "/" + g)

numProcessors = (int)(multiprocessing.cpu_count()) * 2

points = "............"
allScopes = dict()
allTitles = dict()
###############################
# 
threads = []
print("Starting with reading PDFs...\n")
print("Number of all PDFS: " + str(len(pdfs)))

startTwo = 0
intervalTwo = round(len(pdfs) / numProcessors) - 1
if intervalTwo <= 0:
    intervalTwo = 1;

# the first thread of each excel must pass True in constructor
threadOne = MyThread(pdfs[startTwo:intervalTwo])
startTwo += intervalTwo

# append all to array
threads.append(threadOne)

while startTwo < len(pdfs):
    endTwo = startTwo + intervalTwo + 1
    if endTwo > len(pdfs):
        endTwo = len(pdfs)
    threads.append(MyThread(pdfs[startTwo:endTwo]))  
    startTwo = endTwo 

# join
for t in threads:
    t.start()

for t in threads:
    t.join()
print("\n*******Threads finished!*********\n")

##############################
######

# write into textfile
print("Write the file...\n")
if textFileName != "":
    out = open(textFileName + ".txt", "w")
else:
    out = open("allScopes.txt", "w")
out.write("\n\n")
out.write("-------------------------------------------------------------------------------------------------------------------------------------\n\n")
for s in sorted(allScopes):
    out.write("PDF: " + s + "\n\n")
    out.write("Title: " + str(allTitles.get(s," *** ERROR OCCURED ***")) + "\n\n")
    out.write("All Text from " + start + ":\n")
    try:
        out.write(str(allScopes[s]))
    except (UnicodeEncodeError, UnicodeDecodeError, UnicodeError):
        out.write("ERROR IN THIS Specification")
    out.write("\n\n")
    out.write("-------------------------------------------------------------------------------------------------------------------------------------\n\n")
out.close()
        
print("\n\n\n FINISHED!")
