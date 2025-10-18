# Split_DF

You can list the page numbers and the required file name to split the pdf into many parts automatically

create a text file(.txt) in the following format:
____________________
filename1: start(inclusive)-end(inclusive)
filename2: start-end
filename3: start-end
.
.
.
____________________

Run 'splitter.py' in Python to start the application


NOTE: 
  Make sure the PDF file you're splitting doesn't have a password.
  The filenames you split the PDF into must not contain whitespaces.
  Make sure there is a space after the colon(:)
  Make sure there is no space before or after the hyphen(-) when defining the range


created by: HASEEB AHMED;
Date Created: 26 Oct, 2024
