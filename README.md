# SaralGyaan PDF Parser
SaralGyaan PDF Parser is a command-line PDF parsing tool which allows you to:-
1. Delete Pages from a PDF
2. Merge PDFs
3. Sort Pages of a PDF
4. Split a PDF
## Installation
You can install SaralGyaan PDF Parser from PyPI:
```pip install sg-pdfparser```
The PDF Parser supports Python 3.6 and above.
## How to use?
The SaralGyaan PDF Parser is a command line application, named pdfparser. To start it you can simply open the terminal, go to the folder containing the PDF file(s) to be parsed and call the program:-
```
$ pdfparser
Welcome to PDF Parser

What do you want to do?

1. Delete Pages from a PDF
2. Merge PDFs
3. Sort Pages of a PDF
4. Split a PDF

Press ctrl + C to exit.
Enter your choice (1-4):
```
## Delete Pages from a PDF
If you select the option to delete pages, it will ask for the filename followed by '.pdf'
```
Enter your choice (1-4): 1
Delete Pages from a PDF
Enter the name of file with extension(.pdf)
```
Make sure the pdf file exist at the location and once you provide a valid pdf file, it will give you two options:-
```
What do you want to do?
 1. Delete specific pages
 2. Keep Specific pages
 ```
 Both the options accept comma separated values of pages or page ranges or both e.g. 1, 2, 3-5 or 1-2 or 2-3, 4-6.
 One, thing you need to know that if you use Keep specific pages and change the order like 1-2, 6-4, then it will re-arrange the pages too.

 ## Merge PDFs
 This options accepts comma separated file names and it will merge the files in the order, it is provided as an input.

 ## Sort pages of a PDF
 Sort pages, give you three options
 ```
 What do you want to do?
 1. Reverse order of all the pages
 2. Swap Pages
 3. Move certain pages to a specific index
```
1. The first one, will simply reverse the order of the pages.
2. The second one will swap two pages, you can input multiple or single swaps e.g. 1-3, 2-7, 8-9, etc.
3. The third one will move the page to a certain page number (not index). It also accepts comma separated values. So 21-2 will move page number 21 to 2 and hence shifting the rest of the page to right.

## Split a PDF
This gives you two options:-
```
What do you want to do?
 1. Split all the pages
 2. Split specific pages
```
1. The first option will make n splits for n-paged PDF file.
2. The second one will split the pdf into the ranges or pages as provided. e.g. 1, 3, 9-22, will give three split files first page, third page and pages from nine to twenty two.

## License

© 2020 Udit Vashisht

This repository is licensed under the MIT license. See LICENSE for details.
