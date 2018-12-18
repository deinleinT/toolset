# Toolset for an easy management of 3GPP specifications

Handling many 3GPP specifications could be complex and a timelasting procedure. The ongoing standardization and different release versions are leading to frequent updates of the specification documents. The following tools might be helpful and are free to use.

### Prerequisites and Installing

The scripts are written in python. Version 3.6 or more up to date is needed. The scripts were implemented under Microsoft Windows 10 and if you want using the toolset in a comprised way, you also need Microsoft Word and Excel.
Several python packages are needed as well. You can use the python package index (pip) for installing the needed packages as follows:

```
pip install pywin32 openpyxl lxml requests pypdf2 bibtexparser
```

Infos regarding to python and the pip you'll find here: https://www.python.org/ or https://pypi.org/

## Usage of *specificationsHelper.py*

* First of all, visit the 3GPP Portal via https://portal.3gpp.org/ and choose the tab *Specifications*.
* Fill out the corresponding fields for searching the specifications you are interested in. For example, we search for all specifications of the series 38.
* More than one hundred specifications will be found. You can download each specification by clicking on the glasses-button first. A popup window will appear. Under the tab *Versions* you are able to download the specification by clicking the individual version-number. A download-window will appear which allows you to save the specification as zip-file.
* The previous point has shown, that this could be very costly, especially if you want to download many specifications.
* The common approach using this script is to download the excelfile by clicking on the excel-icon-button in the upper right corner.
* Save the excelfile in the folder besides this script.
* Make a copy of the downloaded excelfile. Name one copy of the excelfile *REFERENCE-EXCELFILE.xlsx*. You should reuse the *REFERENCE-EXCELFILE.xlsx* for any further runs of this script. The *REFERENCE-EXCELFILE.xlsx* is maintained automatically by the script. If you want to know whether there are new versions of specifications available you just have do download the *LATEST-EXCELFILE.xlsx* as mentioned above. 
* Then run this script as follows:

```
python specificationsHandler.py LATEST-EXCELFILE.xlsx REFERENCE-EXCELFILE.xlsx [-3] [-w | -wx]
```

* The script checks whether there is a specification in the *LATEST-EXCELFILE.xlsx* which is not in the *REFERENCE-EXCELFILE.xlsx*. If this is the case, the complete row will saved into the *REFERENCE-EXCELFILE.xlsx*. The script also generates new columns for the version-number and the corresponding date. These columns refer to the online data.
* Then, the specifications in the *REFERENCE-EXCELFILE.xlsx* are distributed over several threads. Every thread connect the individual download-site of each specification and looks up which version and date is available.
* After all threads are finished every specification version-number and date are compared with the looked up online verion-number and date. If there is a different version and date online than in the *REFERENCE-EXCELFILE.xlsx*, the newest version will be downloaded.
* All changed specifications will be downloaded. The zip-files are opened and if there is only one doc- or docx-file, this file will be converted to pdf and the doc- and zipfile will be deleted. Otherwise the zip-file has to be handled manually.
* If the download of the zip-file was successful, the corresponding row of the specification in the *REFERENCE-EXCELFILE.xlsx* will be updated.
* In the last step there are a *check-txt*-file and a *log-file* generated with additionally information.
* Use the *REFERENCE-EXCELFILE.xlsx* for following updates. The only thing you have to do is to download the *LATEST-EXCELFILE.xlsx* as described in the first step.
* **NEW**: Since version 1.3 it is possible to extract only Word-documents from the corresponding Zip-file (without conversion to pdf), if the optional parameter *-w* is passed. You can pass both optional parameters (*-3* *-w*, the order does not matter) or just one of it.
* **NEW**: Since version 1.4 it is possible to pass the parameter *-wx* (instead of *-w*). By passing this parameter only Word-documents will be extracted AND all *.doc*-files will be converted into *.docx*-format.

**Attention!**
The converting into *pdf* (and *docx* as well) might take a while, especially when you use the script the first time and many zip-files are downloaded. 

**Important remark:**
Within the REFERENCE-EXCELFILE.xlsx there will be columns generated with name *Version* and *Date* and *VersionTwo* and *DateTwo*. The data referring to these columns is retrieved online from the individual specification site. For example, consider the specification with id 36.300 --> https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=2430.
Choose the tab *Versions*. The versions are sorted by the release. In this case the columns *Version* and *Date* correspond to the release at the top and the latest published version, *VersionTwo* and *DateTwo* always correspond to the release which comes next to the first release. 
Regarding to 36.300 the latest version (and date) of release 15 and release 14 would be checked and compared to the values which are saved in the REFERENCE-EXCELFILE.xlsx. If there are newer versions available, it would be downloaded and the referring field in the column would be updated. It is also possible to check whether there is a third published release of a specification by passing the optional parameter *-3*.

## Usage of *pdfExtracter.py*
* Be sure, there is a folder with name *Specifications* in the same directory as this script. 
* All PDF-Files in the *Specifications*-Folder will be searched through and the individual scope-section will be read.
* This script uses several threads to shorten the procedure.
* After all threads are finished a textfile with name *scopeOfSpecifications.txt* is generated.
* In this txt-document are all scope-sections of all captured specificationdocuments saved.
* Now it is possible to do a keywordsearch within this txt-file. 

```
python pdfExtracter.py
```

**Important remark:**
Despite the usage of several threads for extracting the scope of each pdf the finishing of this script could take a while. It depends on the number of pdfs in the *Specifications*-Folder.


## Usage of *specificationsToBib.py*
* This script extracts the specifications within the *REFERENCE-ECXELFILE* into a bib-file.
* With the optional parameter *-i* only the specifications will be extracted which are marked as important within the *REFERENCE-EXCELFILE.xlsx*. Important specifications can be marked within the column *important* in the *REFERENCE-EXCELFILE.xlsx*.
* Because a specific specification can have several release versions, the version-number and the corresponding date is saved into the *note*-field.

```
python specificationsToBib.py REFERENCE-EXCELFILE.xlsx OUTPUT-BIBFILE [-i]
```

## Authors

* **Thomas Deinlein** - https://github.com/deinleinT

## License

See the [LICENSE.md](LICENSE.md) file for details.

