from ebooklib import epub

# minimal metadata

book = epub.EpubBook()
book.set_identifier('258')
book.set_title('Core Game')
book.set_language('en')
book.add_author('Chateau Heartise')

book.set_cover("image.jpg", open('images.jpeg', 'rb').read())


# Chapters
# Introduction Chapter
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

# Foundation Chapter
foundations = epub.EpubHtml(title='Foundations', file_name='foundations.xhtml',
                            lang='en')
foundations.content='<span><strong>FOUNDATIONS</strong></span>'

# Endless Dating Chapter
f1 = epub.EpubHtml(title='Endless Dating', file_name='endless_dating.xhtml',
                            lang='en')
f1.content='<h2>Endless Dating</h2><p>How long is too long to stay in the \
dating game? The primary \
reason for the psychological unease and emotional instability of so many\
modern women and to a different extent modern men resides in the irresolvable\
tension between our ancient biological inheritance and the relatively recent\
emergence of the high-tech rootless world of unparalleled mate choice we now\
inhabit. </p>\
<p>It would shock most people if they were to be transported back in time\
to when humans lived in small tribes to see young girls having babies at\
14 and again at 14 years and 9.5 months.  There are subsistence cultures\
that behave this way today.  The bulk of our pre-history was spent in\
conditions like this so it is no wonder that our brains are having trouble\
coping with a radically different environment where childbirth is routinely\
put off until the mid-30s,  if at all,  and rejection by a woman no longer\
means banishment to the icy wastelands of celibate metadeath when a man need\
merely walk to the other side of a bar to try again.</p>\
<p>One consequence of this new paradigm is the absurd number of years spent\
in the dating circuit.</p>\
<p>Women are designed by nature to begin the next generation not much older\
than age 25.  Her risk of miscarriage or fetal abnormalities <a\
target="_blank" href="http://en.wikipedia.org/wiki/Fertility">increases</a>\
each year after that and exponentially so after 35.  Her body begins to\
wear down which affects how much energy she can devote to raising small\
children.  If she has not found a suitable mate by her late 20s she\
will begin to notice that those powerful feelings of infatuation she felt\
for crushes when she was younger,  perfectly created by evolution to bring\
a man and woman together to make babies,  now seem muted and foggy.  This\
in turn will sap the dating experience of the best things it has going\
for it &#8211; namely,  the spontaneity,  the euphoria,  the intense drive to\
connect &#8211; and leave behind a desiccated simulacra of dating that\
more closely resembles haggling over a business deal or suffering through\
a job interview.  Overthinking replaces lust.</p>\
<p>It is an embittering realization.</p>\
<p>Men,  too,  have had to adjust under the new system.\
Anthropologically-speaking,  it wasn&#8217;t so long ago that a man\
(or his immediate kin) blew his entire wad of hard-earned social and\
material capital wooing one or two women over the course of his\
natural lifespan.  In a pre-birth control age when the first\
deflowering blast inside a woman often meant conception followed by\
years of fatherhood there were limits on just how many female sex partners\
the average man could accumulate in a lifetime.  The rigorous experience\
of winning over and keeping the best quality woman he could afford and\
then providing for their kids soon thereafter meant that serial dating\
was not a typical feature of life.  Dating 40 or 50 different women in a\
year and jumping haphazardly in and out of 3-month mini-relationships is a\
peculiarity of modern life for which men are not optimized.  The energy\
requirement is enormous.  Men have adapted to this stressful cycle of\
meet-attract-close-keep by either settling and marrying the first girl that\
would have them (usually high school sweethearts who have not lived enough\
to acquire unrealistically picky standards) or by hardening themselves\
against the judgment of women and learning to play the numbers game.</p>\
<p>The game begat the player.</p>\
<p>In the gigantic atomized urban tribe of any big city playing the numbers\
is not the high risk strategy it once was for our distant male ancestors who\
were often locked out of any future matings when a pickup attempt went awry\
and the target or cockblock would run and tell the whole tribe what a loser\
he is.  Today,  the proximity of exes has very little impact on potential\
future conquests.  For men,  this has bought them virtually unlimited\
opportunity to get laid.  For women,  this has robbed them of one of their\
most potent weapons in ensuring that only the fittest males get access to\
their vaginas &#8212; the withering ostracization of their sexual rejection\
.</p>\
<p>On the flipside,  men have lost confidence in the fidelity of their\
chosen partners while women have gained unstigmatized sexual freedom\
allowing them to play the field until the perfect man finally arrives to\
sweep them off their feet.</p>\
<p>I do not think the current reality of endless dating can last.\
Something must give.  Either humans will evolve into different social\
animals capable of withstanding decades of hookups and fragmentary\
relationships without turning to the comforts of cats and internet porn,\
or those people who serially date and delay childbirth will not have enough\
kids and natural selection will remove them from the gene pool as a\
failed experiment.  Either way,  <a target="_blank"\
href="http://www.world-science.net/exclusives/070326_evolution.htm">change\
</a> is in the air.</p>'\

# The fundamental premise
f2 = epub.EpubHtml(title='The fundamental premise',
                   file_name='the_fundamental_premise',
                   lang='en')
f2.content ='<h2>The Fundamental Premise</h2><p>Eggs are expensive, \
sperm is cheap. Every psychological\
dynamic you see playing out in mass societies liberated from artificial\
constraints on the sexual market flows from this premise. This means,\
as a systemic matter,  women are coddled,  men are upbraided. Women are\
victims,  men are victimizers. Women need a leg up,  men need to man up.\
Women have advocacy groups,  men have equal opportunity violations.\
A woman subjected to the indignity of eavesdropping on a tame joke about\
dongles makes national news,  while the chilling fact that 95% of all\
workplace deaths are suffered by men barely pings the media\
consciousness.</p>\
<p>It is what it is,  and it will never change so long as humans are a\
sexually reproducing species. All the laws in the world can at best\
only paper over the very primal compulsion of people to value the\
life of the average woman more than the life of the average man,\
and sympathize accordingly. Railing against it is akin to shaking a\
fist at sunspots and gamma rays. It&#8217;s therefore folly or\
self-serving disingenuousness to act like there’s some moral high\
ground to stake out by imparting culpable agency to an indifferent,\
organically emergent biomechanical phenomenon. Rationalizing favoritism\
toward women as some sort of payback for male privilege,  or refusing\
to acknowledge this favoritism altogether,  is an example of the\
cognitive calisthenics and evasive sophistry most people will indulge\
to avoid grappling with the cold,  black void of an uncaring evolutionary\
replication machine.</p>\
<p>If you are a man,  know that the moment you were born the universe\
had it in for you. The deck was stacked. The deal was raw. Your\
expendability was programmed into your wet code before you gained\
self-awareness. The worldscape of genes can rebuild with the seed of\
one man should catastrophe strike,  but each woman lost is a lethal\
blow to the repopulation project.</p>\
<p>In sober moments free of maudlin introspection,  you will understand\
there is no other game to play save this one. This is why to live as a\
man is to TAKE what you want. Not to wait for it to be given to you.\
Because it will never be given. Not to anticipate the empathy of the\
overseers. Because they will never empathize. Not to expect the coddling\
of the crowd. Because they will never coddle. Not to assume the wagon\
circling of kindreds. Because they will never circle for you. You got\
 he short stick,  now what? Do you contemplate it and hope for a\
longer one? No.</p>\
<p>You sharpen it and jab it into the heart of every obstacle that\
sets itself in your way.</p>'\

    # Book Spine
book.add_item(intro)
book.add_item(foundations)
book.add_item(f1)
book.add_item(f2)
book.spine = ['cover', intro, foundations, f1, f2]

# create epub fil
epub.write_epub('roissy.epub',  book, {})
