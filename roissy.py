from ebooklib import epub

# minimal metadata

book = epub.EpubBook()
book.set_identifier('258')
book.set_title('Core Game')
book.set_language('en')
book.add_author('Chateau Heartise')

book.set_cover("image.jpg", open('images.jpeg', 'rb').read())

# Chapters
intro = epub.EpubHtml(title='Introduction', file_name='intro.xhtml',
                      lang='en')
intro.content='<span><strong>The Roissy Reader: \
    Chateau Heartiste on Game </strong></span> \
    <br /> \
            <div id="pid_877175" style="padding: 5px 0 5px 0;">  \
                            “Heartiste is the intellectual linchpin of the \
    Manosphere.” — <a href="http://www.rooshvforum.com/thread-36585-post-7437 \
87.html#pid743787" target="_blank">Frost</a><br /> \
                            <br /> \
                            “heartiste is the Aristotle of the manosphere.\
                            His site is the bedrock of what people consider\
                            common knowledge…” — <a href="http://www.rooshvf\
                            orum.com/thread-36585-post-743125.html#pid743125"\
                            target="_blank">MikeCF</a><br />\
                            <br />\
                            "There is no greater entry point for the curious\
                            man,  no better archive,  no blog more skilled and\
                            entertaining at truth telling,  nobody overlaps\
                            the various worlds of truth better,  nobody\
                            reduces the opposition to point and sputter\
                            better than Heartiste.” — LaidNYC (now defunct)\
                            <br />\
                            <br />\
                            “Heartiste is easily the biggest American\
                            intellectual of the last 100 years or so,  and\
                            has more impact on the lives of men than anyone\
                            else.” — <a href="http://www.rooshvforum.com/post-\
                            743165.html#pid743165" target="_blank">Samseau</a>\
                            <br />\
                            <br />\
                            “8=====&gt;" — <a href="http://heartiste.wordpre\
                            ss.com/2014/08/29/what-to-do-when-a-girl-scolds-\
                            you/" target="_blank">Heartiste</a><br />\
                            <br />\
                            ##<br />\
                            <br />\
                            If you held a survey in this corner of the web\
                            and asked guys their favorite game blog,\
                            <a href="http://heartiste.wordpress.com/"\
                            target="_blank">Heartiste</a> would win a\
                            landslide. I''d definitely vote for him.<br />\
                            <br />\
                            There''s lots of good that can be said about\
                            Heartiste—he''s an interesting stylist,  he has\
                            an exceptional eye for detail,  he hasn''t\
                            junked up his site with banner ads and popovers—\
                            but\
                            for my money,  what''s most appealing is that he\
                            seems to genuinely love chasing and bedding women.\
                            <br /> \
                            <br /> \
                            For whatever reason,  that''s not a given among\
                            game bloggers,  even those who\
                            (judging by their stories) are probably more\
                            prolific in their snatch-getting than Heartiste.\
                            But if I''m going to take my game cues from\
                            somebody,  I''m not that interested in how many\
                            girls he gets. I wanna know how much pleasure\
                            he gets out of those girls,  and I think it''s\
                            clear that for Heartiste,  the answer to\
                            that question is "a lot."<br />\
                            <br />\
'
book.add_item(intro)

# Book Spine
book.spine = ['cover', intro]

# Table of Contents
book.toc = (epub.Link('intro.xhtml', 'Introduction', 'intro'),
            (epub.Section('Languages'),
             (intro))
            )

# create epub file
epub.write_epub('roissy.epub',  book, {})
