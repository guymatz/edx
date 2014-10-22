# 6.00.1x Problem Set 7
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *
import pdb


#-----------------------------------------------------------------------
#
# Problem Set 7

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

class NewsStory():
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.ttl = title
        self.subj = subject
        self.summ = summary
        self.link = link
    def getGuid(self):
        return self.guid
    def getTitle(self):
        return self.ttl
    def getSubject(self):
        return self.subj
    def getSummary(self):
        return self.summ
    def getLink(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

#class NewNewsStory(NewsStory):
#    def __init__(self, guid, title, subject, summary, link, date):
#        NewsStory.__init__(self, guid, title, subject, summary, link)
#        self.date= date
 
class Trigger(object):
    def __init__(self):
        """
        return an object initialiazed with word to search for
        """
        pass
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError
    def __str__(self):
        return self.__class__

class WordTrigger(Trigger):
    def __init__(self, search_word):
        Trigger.__init__(self)
        self.search_word = search_word.lower()
    def cleanse(self, story):
        """
        return story suitable for string matching,
        i.e. cleansed of punctuation, and in all
        lower case
        """
        return ''.join([x if x not in string.punctuation else ' ' for x in story ]).lower().split()
    def isWordIn(self, text):
        #print(self.search_word, text)
        return self.search_word in text
    def __str__(self):
        return self.__class__ + ": " + self.search_word
        
class TitleTrigger(WordTrigger):
    def __init__(self, search_word):
        WordTrigger.__init__(self,search_word)
    def evaluate(self, story):
        """
        Returns true if word is in title
        """
        scrubbed_title = self.cleanse(story.getTitle())
        return self.isWordIn(scrubbed_title)
        
class SubjectTrigger(WordTrigger):
    def __init__(self, search_word):
        WordTrigger.__init__(self, search_word)
    def evaluate(self, story):
        scrubbed_subject = self.cleanse(story.getSubject())
        return self.isWordIn(scrubbed_subject)
        
class SummaryTrigger(WordTrigger):
    def __init__(self, search_word):
        WordTrigger.__init__(self, search_word)
    def evaluate(self, story):
        scrubbed_summary= self.cleanse(story.getSummary())
        return self.isWordIn(scrubbed_summary)

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
    def evaluate(self, story):
        return not self.trigger.evaluate(story)
    
class AndTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)
        
class OrTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
    def evaluate(self, story):
        return self.t1.evaluate(story) or self.t2.evaluate(story)

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        Trigger.__init__(self)
        self.phrase = phrase
    def evaluate(self, story):
        return self.phrase in story.getTitle() or self.phrase in story.getSubject() or self.phrase in story.getSummary()
    def __str__(self):
        return self.type + ": " + self.phrase
        
# Question 9

# TODO: PhraseTrigger


#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    #pdb.set_trace()
    filtered_stories = []
    for s in stories:
        print s.getTitle()
        print("\t%s" % s.getSubject())
        print("\t%s" % s.getSummary())
        if s in filtered_stories:
            continue
        for t in triggerlist:
            if t.evaluate(s):
                filtered_stories.append(s)
                break
    return filtered_stories

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    #print("==================")
    #print("triggerType: %s" % triggerType)
    #print("params: %s" % params)
    #print("name: %s" % name)
    ttype = ''
    if triggerType in ['AND','OR','NOT']:
        if triggerType == 'AND':
            ttype = AndTrigger
        elif triggerType == 'OR':
            ttype = OrTrigger
        elif triggerType == 'NOT':
            ttype = NotTrigger
        list_of_triggers= []
        for t in params:
            list_of_triggers.append(triggerMap[t])
        t = ttype(*list_of_triggers)
    else:
        if triggerType == 'SUBJECT':
            ttype = SubjectTrigger
        elif triggerType == 'SUMMARY':
            ttype = SummaryTrigger
        elif triggerType == 'TITLE':
            ttype = TitleTrigger
        elif triggerType == 'PHRASE':
            ttype = PhraseTrigger
        params = ' '.join(params)
        t = ttype(params)
    triggerMap[name] = t
    return t


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:
        linesplit = line.split(" ")
        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])
        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])
    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll

def main():
    triggerlist = readTriggerConfig("triggers.txt")

def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        #t1 = TitleTrigger("Obama")
        #t2 = SubjectTrigger("Romney")
        #t3 = PhraseTrigger("Election")
        #t4 = OrTrigger(t2, t3)
        #triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        triggerlist = readTriggerConfig("triggers.txt")
        print triggerlist

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            pdb.set_trace()
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()
#     main()
