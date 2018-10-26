# Toolset for an easy management of 3GPP specifications

Handling many 3GPP standards could be complex and a timelasting procedure. The ongoing standardization and different release versions are leading to frequent updates of the standard documents. The following tools might be helpful and are free to use.

### Prerequisites and Installing

The scripts are written in python. Version 3.6 or more up to date is needed. We implemented the scripts under Microsoft Windows 10 and if you want using the toolset in a comprised way, you also need Microsoft Word and Excel.
Several python packages are needed as well. You can use the python package index (pip) for installing the needed packages as follows:

```
pip install pywin32
pip install openpyxl
pip install lxml
pip install requests
pip install pypdf2
pip install bibtexparser
```

Infos regarding to python and the pip you'll find here: https://www.python.org/ or https://pypi.org/

## Usage of *standardsHelper.py*

* First of all, visit the 3GPP Portal via https://portal.3gpp.org/ and choose the tab *Specifications*.
* Fill out the corresponding fields for searching the standards you are interested in. For example, we search for all standards of the series 38.
* More than one hundred standards will be found. You can download each standard by clicking on the glasses-button first. A popup window will appear. Under the tab *Versions* you are able to download the standard by clicking the individual version-number. A download-window will appear which allows you to save the standard as zip-file.
* The previous point has shown, that this could be very costly, especially if you want to download many standarddocuments.
* The common approach using this script is to download the excelfile by clicking on the exceliconbutton in the upper right corner.
* Save the excelfile in the folder besides this script.
* Make a copy of the excelfile. You should reuse the excelfile for any further runs of this script. Name one copy of the excelfile *REFERENCE-EXCELFILE*.
* Then run this script as follows:

```
python standardsHandler.py LATEST-EXCELFILE REFERENCE-EXCELFILE
```

* The script checks whether there is a standard in the *LATEST-EXCELFILE* which is not in the *REFERENCE-EXCELFILE*. If this is the case, the complete row will saved into the *REFERENCE-EXCELFILE*. The script also generates new columns for the version-number and the corresponding date. These columns refer to the online data.
* Then, the standards in the *REFERENCE-EXCELFILE* are distributed over several threads. Every thread connect the individual download-site of each standard and looks up which version and date is available.
* After all threads are finished every standard version-number and date are compared with the looked up online verion-number and date. If there is a different version and date online than in the *REFERENCE-EXCELFILE*, the newest version will be downloaded.
* All changed standards will be downloaded. The zip-files are opened and if there is only one doc- or docx-file, this file will be converted to pdf and the doc- and zipfile will be deleted. Otherwise the zip-file has to be handled manually.
* If the download of the zip-file was successful, the corresponding row of the standard in the *REFERENCE-EXCELFILE* will be updated.
* In the last step there are a *check-txt*-file and a *log-file* generated with additonally information.
* Use the *REFERENCE-EXCELFILE* for following updates. The only thing you have to do is to download the *LATEST-EXCELFILE* as described in the first step.

**Attention!**
The converting into pdf might take a while, especially when you use the script the first time and many zip-files are downloaded. 

**Important remark:**
Within the REFERENCE-EXCELFILE there will be columns generated with name *Version* and *Date* and *VersionTwo* and *DateTwo*. The data referring to these columns is retrieved online from the individual specification site. For example, consider the specification of standard 36.300 --> https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=2430.
Choose the tab *Versions*. The versions are sorted by the release. In this case the columns *Version* and *Date* correspond to the release at the top and the latest published version, *VersionTwo* and *DateTwo* always correspond to the release which comes next to the first release. 
Regarding to 36.300 the latest version of release 15 and release 14 would be checked. If there are newer versions available, it would be downloaded and the referring field in the column would be updated.

## Usage of *pdfExtracter.py*
* Be sure, there is a folder with name *Standards* in the same directory as this script. 
* All PDF-Files in the *Standards*-Folder will be searched through and the individual scope-section will be read.
* This script uses several threads to shorten the procedure.
* After all threads are finished a textfile with name *scopeOfStandards.txt* is generated.
* In this txt-document are all scope-sections of all captured standarddocuments saved.
* Now it is possible to do a keywordsearch within this txt-file. 

```
python pdfExtracter.py
```

## Usage of *standardsToBib.py*
* This script extracts the standards within the *REFERENCE-ECXELFILE* into a bib-file.
* With the optional parameter *-i* there just will be the standards extracted which are marked as important within the *REFERENCE-EXCELFILE*.
* Because a specific standards can have several release versions, the version-number and the corresponding date is saved into the *note*-field.

```
python standardsToBib.py REFERENCE-EXCELFILE OUTPUT-BIBFILE [-i]
```

## Authors

* **Thomas Deinlein** - https://github.com/deinleinT

## License

See the [LICENSE.md](LICENSE.md) file for details.

