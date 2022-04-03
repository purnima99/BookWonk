from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Book
import cv2
import time
import speech_recognition as sr
import pyaudio

from .BooksLib import ocr
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
import os
from PIL import Image
# Create your views here.


@login_required(login_url='/login/')
def collectionView(request):
    books = Book.objects.all()[:5]
    context = {
        'books': books
    }
    print(context['books'])
    print(f"The GET req : {request}")
    img_counter = 0
    # video capture source camera (Here webcam of laptop)
    cap = cv2.VideoCapture(1)
    if 'add_book_scan' in request.POST:
        print('Reading Starts')
        pageList = []
        while img_counter < 2:
            time.sleep(3)
            ret, frame = cap.read()  # return a single frame in variable `frame`
            if 'stop_read' in request.POST:
                print("Hello from while loop")
            img_name = "img{}.jpg".format(img_counter)
            cv2.imwrite('ReadingNow/'+img_name, frame)
            im = Image.open('ReadingNow/'+img_name)
            pageList.append(im)
            ocrObj = ocr.OCR()
            try:
                text = ocrObj.ocr(frame)
                print(text)
                with open("ReadingNow/text{}.txt".format(img_counter), 'w') as f:
                    f.write(text)
                language = 'en'
                myobj = gTTS(text=text, lang=language, slow=False)
                myobj.save("ReadingNow/tts.mp3")
                tts = AudioSegment.from_mp3("ReadingNow/tts.mp3")
                # play(tts)
            except:
                None
            img_counter += 1
        fileM = open('ReadingNow/tts.txt')
        textM = fileM.read()
        myobj = gTTS(text=textM, lang=language, slow=False)
        myobj.save("ReadingNow/tts.mp3")
        tts = AudioSegment.from_mp3("ReadingNow/tts.mp3")
        play(tts)
        im.save('ReadingNow/book.pdf', "PDF", resolution=100.0,
                save_all=True, append_images=pageList)
        pageList = []
        img_counter = 0
    return render(request, 'books/collection.html', context)


def readerView(request, bookName):
    print(bookName)
    book = Book.objects.get(bookName=bookName)
    context = {
        'bookPDF': book,
    }
    print(book)
    print(context['bookPDF'].location.url)
    if 'start_read' in request.POST:
        print("Reading Starts !")
        language = 'en'
        fileM = open('ReadingNow/tts.txt')
        text = fileM.read()
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save("ReadingNow/tts.mp3")
        tts = AudioSegment.from_mp3("ReadingNow/tts.mp3")
        play(tts)
        
    elif 'stop_read' in request.POST:
        print('Reading Ends')
    elif 'voice_commands' in request.POST:
        print('Voice Command')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Talk")
            audio_text = r.listen(source)
            print("Time over, thanks")
            try:
                mytext = r.recognize_google(audio_text)
                print("Text: "+mytext)
                if mytext == 'start reading':
                    print("Reading Starts !")
                    language = 'en'
                    fileM = open('ReadingNow/tts.txt')
                    text = fileM.read()
                    myobj = gTTS(text=text, lang=language, slow=False)
                    myobj.save("ReadingNow/tts.mp3")
                    tts = AudioSegment.from_mp3("ReadingNow/tts.mp3")
                    play(tts)
                elif mytext == 'stop reading':
                    print('Reading Ends')
                elif mytext == 'voice notes':
                    print('Take voice notes')
                    time.sleep(2)
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Talk")
                        audio_text = r.listen(source)
                        print("Time over, thanks")
                        try:
                            mytext = r.recognize_google(audio_text)
                            print("Text: "+mytext)
                            with open('Notes/readme.txt', 'a') as f:
                                f.write("\n")
                                f.write(mytext)
                        except:
                            print("Sorry, I did not get that")
            except:
                print("Sorry, I did not get that")
    elif 'voice_notes' in request.POST:
        print('Take voice notes')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Talk")
            audio_text = r.listen(source)
            print("Time over, thanks")
            try:
                mytext = r.recognize_google(audio_text)
                print("Text: "+mytext)
                with open('Notes/readme.txt', 'a') as f:
                    f.write("\n")
                    f.write(mytext)
            except:
                print("Sorry, I did not get that")
    return render(request, 'books/book.html', context)
