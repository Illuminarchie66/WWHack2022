# WWHack2022
This project takes in an audio clip of a movie quote, and then gathers the top 5 movies that have that quote, and the times that the quote is said in the movies. 
It does this by transcribing the audio file into plain text, and then webscraping to find the movies where the quotes are from. 
This is useful for that moment you are thinking of where that one quote from a movie comes from; now by entering it, you can find out!

The final product is on a website, where you upload the audio clip. Unfortunately you cannot enter the audio in real time (as of now). 
To run the product though, you must run the bat file attached with the product, as to install the necessary libraries. 

The libraries and APIs used are:
- Selenium
- BeautifulSoup4
- Flask
- AssemblyAI

Currently the delegation of work has been broken down like so:
- Front end, interface andd aquiring the audio file: Pavel Skerbakovs (Materol#6825)
- Audio file to plain text transcription: Ivan Kudryavtsev (Rexonance#6691)
- Webscraping for the quotes and associated movies: Archie Harrodine (Illuminarchie#8292)
- Installation and upload: Icen Zeyada (Icen#4060)

Instructions to run:
    To install the required modules you need to run Mazam.bat as an adminstrator.
    To run the program you need to type this command in terminal (Powershell/command prompt) "python website.py" without the quotes.
    You then have to open the website 127.0.0.1:5000.

