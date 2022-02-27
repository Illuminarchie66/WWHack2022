# WWHack2022
This project takes in an audio clip of a movie quote, and then gathers the top 5 movies that have that quote, and the times that the quote is said in the movies. 
It does this by transcribing the audio file into plain text, and then webscraping to find the movies where the quotes are from. 
To run the programa nd install the required modules you need to run Mazam.bat as an adminstrator.
This is useful for that moment you are thinking of where that one quote from a movie comes from; now by entering it, you can find out!

The final product is on a website, where you upload the audio clip. Unfortunately you cannot enter the audio in real time (as of now). 
To run the product though, you must run the bat file attached with the product, as to install the necessary libraries. 

The libraries and APIs used are:
- Selenium
- BeautifulSoup4
- Flask
- AssemblyAI

Currently the delegation of work has been broken down like so:
- Front end, interface andd aquiring the audio file: Pavel Skerbakovs
- Audio file to plain text transcription: Ivan Kudryavtsev
- Webscraping for the quotes and associated movies: Archie Harrodine
- Installation and upload: Icen Zeyada
