import sys
import os
import dominate
from dominate.tags import *
from dominate.util import text
import pandas as pd
from datetime import datetime

class img(html_tag):
    pass

def confirmedSpeakers(speakers):

    with div(_class="grid-container", style="grid-auto-flow: dense;"):

        for _, speaker in speakers.iterrows():
            try:
                with figure(_class="circle-image-box-with-caption"):
                    img(src=os.path.join( '..', 'img', speaker['imgfile']), _class="wow rotateIn")
                    with figcaption():
                        with h5():
                            with a(href=speaker['url']):
                                name = speaker['speaker']
                                text( name.split()[0]) ; br()
                                text( ' '.join( name.split()[1:]) )
            except:
                pass
                                # for s in speaker['speaker'].split():
                            #     text(s) ; br()
                        
def scheduledTalks(schedule):
    # schedule.
    with ul(_class="timeline list"):
        i = 0
        for _, day in schedule.iterrows():
            with li():
                with span(_class="itemlabel"):
                    span(f'Day {i+1}', _class="hbox llap")
                with p():
                    with span(_class="bf"):
                        with span():
                            text(\
                                pd.to_datetime(day['date']).strftime('%A %d %B, %Y')\
                                +' '+\
                                day['time'].strftime('%H:%M'))
                            # text(.strftime('%A %d %B, %Y'))
                with ul( style="list-style-type:disc;"):
                    with li():
                        text(f"Talk ({day['location']}):")
                        a(day['speaker'], href=day['url'])
                        button(_class="collapsible collapsible-abstract")
                        with div(_class="content"):
                            with p(day['abstract']):
                                try:
                                    if not pd.isnull( day['connected-papers']) :
                                        br()
                                        br()
                                        text('Papers connected with this talk:')
                                        with ol():
                                            for paper in day['connected-papers'].split(';'):
                                                li(paper)
                                    else:
                                        pass
                                except:
                                    pass
                        button(_class="collapsible collapsible-bio")
                        with div(_class="content"):
                            p(day['bio'])
            i += 1
    script(src="collapsible.js")

def scheduledTalksMulti(schedule):
    with ul(_class="timeline list"):

        days = schedule['date'].unique()
        i = 0
        for _, day in enumerate(days):
            with li():
                with span(_class="itemlabel"):
                    span(f'Day {i+1}', _class="hbox llap")
                with p():
                    with span(_class="bf"):
                        with span():
                            text( pd.to_datetime(day).strftime('%A %d %B, %Y'))
                j = 0
                for _, session in schedule.loc[ schedule['date']==day].iterrows():
                    with ul( style="list-style-type:disc;"):
                        with li():
                            text(f"Session {j+1} ({session['location']}):")
                            a(session['speaker'], href=session['url'])
                            button(_class="collapsible collapsible-abstract")
                            with div(_class="content"):
                                with p(session['abstract']):
                                    try:
                                        if not pd.isnull( session['connected-papers']) :
                                            br()
                                            br()
                                            text('Papers connected with this talk:')
                                            with ol():
                                                for paper in session['connected-papers'].split(';'):
                                                    li(paper)
                                        else:
                                            pass
                                    except:
                                        pass
                            button(_class="collapsible collapsible-bio")
                            with div(_class="content"):
                                p(session['bio'])
                    j += 1
            i += 1
    script(src="collapsible.js")

def parseAndSortCsv(filename):
    df = pd.read_csv(filename)
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    df['time'] = pd.to_datetime(df['time'], ).dt.time 
    df.sort_values(by=['date', 'time'], inplace=True)

    return df

def getSpeakers(schedule):
    speakers = schedule[['speaker', 'url', 'imgfile'] ]
    return speakers

def buildSpeakersAndSchedules(inp):
    filename = f'./csv/{inp}.csv'
    schedule = parseAndSortCsv(filename)
    speakers = getSpeakers(schedule)

    sys.stdout = open(f"./schedules/{inp}-schedule.html", "w")

    #build html
    doc = dominate.document(title='')
    with doc.head:
        link(rel='stylesheet', href='schedule.css')
        script(type='text/javascript', src='script.js')
        base(target='_top')
    with doc:
        script(type='text/javascript', src='script.js')
        if inp == 'seminar':
            scheduledTalks(schedule)
        else:
            scheduledTalksMulti(schedule)
    print(doc)
    # sys.stdout.close()


    sys.stdout = open(f"./schedules/{inp}-speakers.html", "w")

    #build html
    doc = dominate.document(title='')
    with doc.head:
        link(rel='stylesheet', href='../css/extras.css')
        meta(charset="UTF-8")
        base(target='_top')
        meta(name="viewport", content="width=device-width, initial-scale=1.0")
        meta(name="viewport", content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=0")
        link(rel="stylesheet", href="../css/prism.css")
        script(type='text/javascript', src='script.js')
        link(href="././fonts.googleapis.com/css92b2.css?family=Source+Sans+Pro:400,600", rel="stylesheet")
        link(rel="stylesheet", href="../css/font-awesome.min.css")
        link(rel="stylesheet", href="../css/katex.css")
        link(rel="stylesheet", href="../css/main.css")
        link(rel="stylesheet", href="../css/latex.css")
        link(rel="stylesheet", href="../css/latex-highlighting.css")
        script(type="text/javascript", src="./js/jquery-3.2.1.min.js", charset="utf-8")
        script(type="text/javascript", src="./js/main.js", charset="utf-8")
    with doc:
        confirmedSpeakers(schedule)

    print(doc)
    # sys.stdout.close()

files = ['seminar', 'reading-group-1', 'reading-group-2']
for file in files:
    buildSpeakersAndSchedules(file)
