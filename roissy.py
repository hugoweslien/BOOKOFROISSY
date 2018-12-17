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
f2.content ='<h2>The Fundamental Premise</h2>\
<p>Eggs are expensive, \
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

f3 = epub.EpubHtml(title='double standards',
                   file_name='double_standards.xhtml',
                   lang='en')
f3.content='<h2>Double Standards</h2><p>You hear it all the time from \
people who are getting\
shafted by reality.  &#8220;It&#8217;s so UNFAIR that guys get to do\
X with impunity while girls doing X suffer social stigma.&#8221;  They\
think by bitching like this and attempting to shame those who\
would live in harmony with double standards they can alter people&#8217;s\
behavior into something more to their liking (i.e.,  a non-status driven,\
non-materialistic,  non-craven utopia of perfect loving LTRs where no one\
left out and no one gets dumped and everyone\
as a soulmate and enough positive life-affirming experiences to share\
with their yenta friends in recipe-swapping blogs devoted to covering\
the fascinating minutiae of their funny,  exciting,  sexy,  touching, \
poignant,\
growth-oriented lives.)</p>\
<p>Then there are those who,  when called out\
on their inconsistencies,  deploy a swarm of sophistry intended to obfuscate\
and deny the existence of double standards because they are beneficiaries\
of them.  Acknowledging these truths would mean coming to terms with\
the fact that they,  like everyone else,  have at their core\
an animal nature.</p>\
<p>Fuck that noize.  The truth of the matter\
is that double standards are necessary if you want to be\
halfway competent in your dealings with men and women.  As the\
<a target="_blank" href="http://www.amazon.com/Winning-Through-Intimidation\
-Robert-Ringer/dp/0449207862/ref=sr_1_6/102-3180284-9010533?ie=UTF8&amp;s=\
books&amp;qid=1176423704&amp;sr=1-6">author</a> of &#8220;Looking Out for\
#1&#8221; and &#8220;Winning Through\
Intimidation&#8221; wrote:</p>\
<p>If you deny reality it will automatically work against\
you.*</p>\
<p>Double standards are fixed features of life as a sexually\
reproducing social organism.  The modern career woman is miserable because she\
is constantly locking horns with men who won&#8217;t value her for\
her career achievement as much as for her hourglass figure and\
bedroom skills,  while these same men admire and respect career dominance\
by other men.  Her refusal to come to grips with this\
essential double standard explains why so many hard-charging women have turned\
their backs on their own femininity and lost the art of\
female coquettishness and submissiveness.  Alpha men have responded by fucking\
and leaving these domineering gender impostors for cute waitresses.\
Betas have responded\
in their own way &#8212; by assuming the doormat position and\
giving these feminists *exactly* what they claim they want.</p> <p>The same\
goes for sluts.  A man who sleeps with many women gets\
high fives from his buddies and sexual interest from girls who\
can&#8217;t help their burning loins.  But girls who sleep around are\
socially ostracized,  used by men and shunned by women.  It has\
always been and it will always be as long as a\
woman has 400 eggs to a man&#8217;s nearly infinite number of\
sperm.  Parents will treat their sons and daughters differently \
when dispensing\
advice on how to deal with the opposite sex and all\
the harpies with their multiple humanities degrees shrieking equalist\
platitudes to\
the high heavens will never change this.  It&#8217;s one thing to\
bloviate from a comfy tenured perch while your lesbian lover sucks\
ben wa balls out of your cooch from under the desk;\
it&#8217;s quite another to entrust the welfare of your children with\
the twisted lies of the Bitterati.</p>\
<p>*pretty girls have some leeway\
with this rule. (at least for a while. heh.)</p>\
<p>A handy pocket guide to the most common double standards:</p>\
<p>male slut = lothario<br />\
female slut = desperate</p>\
<p>male CEO = alpha<br />\
female CEO = bitch</p>\
<p>male model = silly<br />\
female model = alpha</p>\
<p>male nerd = loser<br />\
female nerd = cute</p>\
<p>young male death = statistic<br />\
young female death = tragedy</p>\
<p>male nurse = beta<br />\
female nurse = agreeable</p>\
<p>male stripper = clown<br />\
female stripper = desirable</p>\
<p>male sports star = role model<br />\
female sports star = butch</p>'

f4 = epub.EpubHtml(title='latest baumeister paper support ch concept of the\
                   market',
                   file_name='latest_baumeister.xhtml',
                   lang='en')
f4.content="<h2>Latest Baumeister Paper Support CH Concept Of The Sexual\
Market</h2>"

f5 = epub.EpubHtml(title='this is your life',
                   file_name='this_is_your_life.xhtml',
                   lang='en')
f5.content='<h2>This Is Your Life</h2><p>Common American Man,\
this is how your life will unfold.\
You will start with dreams,  big dreams.  You will believe you are\
ordained for exceptionalism.  You will reluctantly abandon your dreams\
as the years pass and reality inexorably descends upon you like a choking\
shroud of grit.  That reality looks like this &#8212;</p>\
<p>You will get older,  uglier,  and fatter with each year.  Soon you will\
notice young women no longer take your flirtations seriously.  Your sloth\
and social detachment will worsen until people don&#8217;t even bother to\
be polite around you.  You will gradually lower your standards in what you\
want in a girl until desperation pushes you to marry a dumpy oinker well\
past her prime.  You will rut with her once a week,  then once a month,\
then holidays only.  You will relieve yourself drearily masturbating in the\
middle of the night by the cold flickering light of your computer monitor\
while that bloated seacow who doesn&#8217;t give a shit for your desires\
snores in the bed you can no longer get a good night&#8217;s sleep in.\
Your one shred of solace will come from knowing your depreciating asset\
(AKA wife) will have as few options as you do virtually guaranteeing lifelong\
fidelity.  Eventually you will have a couple of ungrateful snotty kids and\
your free time and discretionary cash will be completely obliterated.  You\
will squander whatever morsels of opportunity come your way as you settle into\
an achingly dull job paying the median wage dutifully punching the clock as a\
faceless cog in the corporate machine greasing the soul-soaked gears of the\
global marketplace with your bitter bloody tears.  You will silently mourn\
your impotent,  shriveled manhood as the established order extracts the last\
penny of tribute from your broken spirit.  You will numb the pain with alcohol\
,\
untold hours vegging in front of the TV,  and leveling your character in\
World of Warcraft.  Hours,  days,  months,  years will slip away.  Then,\
one lonely quiet cloudy day sitting in your well-worn easy chair,\
you&#8217;ll contemplate the arc of your life.  And you&#8217;ll feel\
the gnawing grip of emptiness as the crushing weight of what a barren\
nothingness your existence proved to be presses down on you.\
Barely comprehending,  you&#8217;ll shudder.  And then,  finally,  the\
Grim Reaper will steal your last breath and you will disappear from the\
world as if you had never been here and when they bury you no one will\
really notice and no one will really care because in your whole life you\
never never never,  not even once,  stepped off the hamster wheel and did\
anything courageous or interesting or different.</p>\
<p>And it will be too late when you realize that the chains clasped to\
your ankles and wrists were unlocked all along and you were always\
free to go.</p> <p align="center">~Fin~ </p>'\

f6 = epub.EpubHtml(title='arnie',
                   file_name='arnie.xhtml',
                   lang='en')
f6.content='<h2>Arnie</h2><p>Lex was a ruggedly handsome man,\
mid-40s,  and in shape\
from near daily yoga and martial arts classes. He was fidgety and frenetically\
hyperverbal and rarely came up for breath once he got rolling on a story\
drawn from his illustrious past and present lifestyle. And what stories! He\
ran a business in the recreation industry which put him in contact with a\
steady stream of young European girls. This contact often led to intimacy.\
Many patrons of his business would regale you with tales of \
witnessing Lex whisk\
some new 22 year old Polish hottie back to his quarters for a night\
of debauchery,  only to do it again the next night with a new\
girl.</p>\
<p>The four of us sat around the\
restaurant table swapping war stories from the field. Lex&#8217;s\
tomcat career was long and fruitful,  but an undercurrent of melancholic\
nostalgia buttressed\
the impression that he had let one or two &#8220;quality girls\
&#8221; get away. He seemed,  in a way,  a\
traitor to his contentment &#8212; a victim of chance and his compulsions\
. Lex made a passing comment,  barely noticed in the cavalcade of sex\
stories if you weren&#8217;t paying attention,  that &#8220\
;it was getting harder out there&#8221; and he needed to\
adjust accordingly.</p>\
<p><img data-attachment-id\
="2804" data-permalink="https://heartiste.wordpress.com\
/2009/04/16/arnie/img_2043b/" data-orig\
-file="https://heartiste.files.wordpress.com/2009\
/04/img_2043b.jpg?w=500&#038;h\
=375" data-orig-size="1600, 1200" data\
-comments-opened="1" data-image-meta="{&quot\
;aperture&quot;:&quot;2.8&quot;, &\
quot;credit&quot;:&quot;&quot;, &quot;camera\
&quot;:&quot;Canon PowerShot SD600&quot;, &quot;\
caption&quot;:&quot;&quot;, &quot;created_timestamp&quot\
;:&quot;1236464336&quot;, &quot;copyright&quot;:&\
quot;&quot;, &quot;focal_length&quot;:&quot;5\
.8&quot;, &quot;iso&quot;:&quot;\
0&quot;, &quot;shutter_speed&quot;:&quot;0\
.016666666666667&quot;, &quot;title&quot;:&quot;&\
quot;}" data-image-title="backstage at the met opera"\
data-image-description="" data-medium-file="https://\
heartiste.files.wordpress.com/2009/04/img_2043b.\
jpg?w=500&#038;h=375?w=\
300" data-large-file="https://heartiste.files.\
wordpress.com/2009/04/img_2043b.jpg?w=\
500&#038;h=375?w=500" class="\
size-full wp-image-2804 alignnone" title="backstage at\
the met opera" src="https://heartiste.files.wordpress.\
com/2009/04/img_2043b.jpg?w=500&#\
038;h=375" alt="backstage at the met opera"\
width="500" height="375" srcset="https://heartiste.\
files.wordpress.com/2009/04/img_2043b.jpg?\
w=500&amp;h=375 500w,  https://heartiste\
.files.wordpress.com/2009/04/img_2043b.jpg\
?w=1000&amp;h=750 1000w,  https://\
heartiste.files.wordpress.com/2009/04/img_2043b.\
jpg?w=150&amp;h=113 150w,  https\
://heartiste.files.wordpress.com/2009/04/img_2043b\
.jpg?w=300&amp;h=225 300w,\
https://heartiste.files.wordpress.com/2009/04/\
img_2043b.jpg?w=768&amp;h=576 768w\
" sizes="(max-width: 500px) 100vw,  500px" /></\
p>\
<p>Zeets admired the unapologetically masculine lifestyle Lex chose for\
himself. Marriage,  kids,  social approval,  clock punching and clock ticking\
? Fuck that noise. Lex lived on his own terms,  in hock\
to no one but himself. Zeets playfully encouraged Lex&#8217;s\
telling of his numerous conquests and the game he runs on women in the\
big city. Lex was especially fond of &#8220;fruit stand game\
&#8221; where he would casually sidle up to a girl (Lex\
banged chicks of all ages,  as long as they were younger than him\
) and guess what meal she was going to cook judging by the veggies\
she had in her basket. Since Lex was a competent cook,  this\
banter would often segue into him inviting her over for dinner.</p>\
\
<p>Trent,  the fourth and youngest man at the table,\
also approved of Lex&#8217;s playboy adventures,  but his approval\
carried more weight. Trent was a one woman kind of guy,  always\
strapped into a long term relationship that lasted for years and eager to get\
back into one on the rare occasions he was single. Trent was no\
herb; he had the tools and the skill to seduce many women if\
he wanted,  so his relatively monogamous existence was all the more \
intriguing.</\
p>\
<p>Outside of the restaurant we parted,  and Lex\
declined our offer to go to the bar for drinks and carousing. He\
was on his way back home to make a thousand calls. Lex could\
hardly focus on anything for long &#8212; his ADHD was legendary &#\
8212; and he barely stopped moving as we bro-slapped hands goodbye\
.</p>\
<p>Around 1AM back at Trent&#8217;\
s apartment,  as we were about to step inside,  an older man\
,  late 40s or early 50s,  with a paunch and one shirttail of\
his light blue button down poking out of his jeans,  greeted us with\
a weary but friendly expression. He introduced himself as Arnie and said he\
had been Trent&#8217;s neighbor for five years. Trent nodded\
his head knowingly as if he recognized Arnie,  but later told us in\
private he had never seen the guy. He probably had,  but it\
didn&#8217;t register.</p>\
<p>Arnie was\
an affable bloke,  and we stood outside in the mild air leaning against\
stair railings under the diffuse glow of the city lights for fifteen\
minutes talking\
guy stuff. We learned Arnie was never married,  lived alone,  and\
worked in a blue collar hands-on job,  and that it was\
clear to me that he possessed the basic intelligence to work white collar if\
he so chose. He had lived in the city his whole life and\
his apartment was rent controlled. There was no chance he would leave,\
despite the landlord working hard to force out his tenants by \
passively ignoring repairs\
that needed to be done.</p>\
<p>Arnie relished our\
company,  that much I could tell. He asked us if we were\
planning to go out somewhere again that night. Trent mentioned the bar where\
he bartended and Arnie made a frown,  explaining that that bar was too\
&#8220;hoity-toity&#8221; for him; he preferred\
down to earth establishments hanging &#8220;with the boys&#8221;.\
We laughed,  because Trent&#8217;s bar is not really snobby\
,  especially not for this city. We began turning our heads and shoulders\
toward the door and told Arnie we were going to call it a night\
. Arnie looked disappointed. &#8220;Well,  another time,  then\
.&#8221; He nodded at Trent. &#8220;Maybe I&#\
8217;ll meet you over at your bar sometime.&#8221; There\
was a hint of overeagerness in his gravelly voice.</p>\
<p\
>As we stepped inside to leave Arnie behind in the streetlight-misted\
night,  the door swung behind us with a slow creak. When it\
thumped closed,  it echoed heavily in my ears.</p>'

f7 = epub.EpubHtml(title='men with options',
                   file_name='men_with_options.xhtml',
                   lang='en')
f7.content='<h2>Men With Options</h2>'

f8 = epub.EpubHtml(title='what do women want? a master',
                   file_name='what_do_women_want_a_master.xhtml',
                   lang='en')
f8.content='<h2>What Women Want? A Master</h2><p>A reader asked if \
                   there were any books I could recommend that\
                   explored the psychology of women. I suggested &#8220;Story\
                   of O&#8221; and &#8220;9 1/2 Weeks&#8221;. (The latter\
                   was originally a book which is much better than the movie\
                   version.)</p>\
<p>There is a maxim among the pick-up community that if you want to know\
what women want it&#8217;s better to watch what they do than listen to what\
they say. Very true. However,  if you are going to listen to what a\
woman says for clues about her innermost desires,  or read what she\
writes,  you would do well to pay attention to what a woman says TURNS\
HER ON. Not what she says she wants in a hypothetical husband or boyfriend\
but what she specifically describes that got her horny and hungry for loving\
penetration. Any editorial commentary about the ideal man can be safely\
ignored.</p>\
<p>The two books above,  both written by women and featuring very beautiful\
female protagonists,  are wide-open windows to the id of women&#8217;s\
sexual natures. What we find there is shocking to most,  dispiriting to some,\
and unsurprising to a few. Women reading these books will, \
                   despite themselves,\
become uncomfortably aroused. Men will discover ancient stirrings within\
themselves they may have thought civilization and a PC academic indoctrination\
stamped out.</p> <p>The beatings and brandings the women in the books suffer,\
provoke,  and then eagerly anticipate in turn are distractions from the main\
message,  which is that the self-confidence and exquisitely suffocating\
domination of the male characters caused the women to fall so helplessly\
in love with them that the men could do anything,  make any demand,  and\
the women would happily go along just to keep their love. Some men can\
handle this awesome power,  some can&#8217;t. The man in 9 1/2 Weeks was\
consumed by his power as much as his lover,  and it got the better of\
him.</p>\
<p>These books,  taken together with the real world observations of men\
who actually live lives like those of the men in the books,  tell us what\
women want.</p>\
<p>They want a man who takes charge.</p>\
<p>A master.</p>\
    <p>Adopt the attitude of the master,  and women will revert to their\
    naturally submissive essence faster and more profoundly than you can\
    scarcely imagine,  and no amount of feminist propaganda,  insulating\
    credentials,  or careerist ladder climbing will stand in the way of\
    their joyous,  even relieving,  surrender to your intoxicating dominance\
    and confidence.</p>'

f9 = epub.EpubHtml(title='the ideal lover',
file_name='the_ideal_lover.xhtml',
lang='en')
f9.content='<h2>The Ideal Lover Can Never Be The Great Boyfriend</h2><p>\
Men are burdened with a duality. We feel impelled to commit to\
a chaste woman but we will happily sleep around with raging sluts. Women,\
too,  are creatures of duality. They relish the emotional connection with\
the great boyfriend who dotes on them and pampers them but they succumb\
helplessly to their raw sexuality with the ideal lover. The god of\
biomechanics is,  if nothing else,  a practical joker.</p>\
<p>There are very few men who embody both the great boyfriend and the ideal\
lover in equal measure. In fact,  my experience in the trenches of modern\
decadence leads me to conclude there are NO men like this. 50/50 internal\
power sharing between lover and supporter,  manifestly expressed in perfect\
synchronicity with a woman&#8217;s unspoken needs for the one or the other\
masculine archetype,  is the myth of &#8220;the One&#8221; perpetuated by\
the feminist grievance industry to keep women unsatisfied and constantly\
searching. The truth is that most men,  by innate character,  lean one way,\
and a few men of purity wholly abandon their soul&#8217;s struggle and\
jettison one archetype to fully embrace its opposite.</p>\
<p>How do you know if you are closer in character to the ideal lover or\
to the great boyfriend? To answer this for yourself,  consider the following\
scenarios,  and then decide if they accurately describe how you would behave\
in your own life.</p>\
<ul>\
<li>Holiday shopping (Kwanzaa not included)</li>\
</ul>\
<p>The great boyfriend thinks of the gifts he will buy others before he\
thinks of himself. His time shopping is spent with a gentle smile\
envisioning the look on his lover&#8217;s face when she sees what he\
bought for her.</p>\
<p>The ideal lover thinks of all the fantastic shit he will buy for\
himself before he thinks of others. His time shopping is spent with a\
joyous grin perusing the electronics section,  and only after he has\
sat in the massage chair at Brookstones for a while does he put in a\
token effort to find reasonably acceptable gifts for his girlfriend.</p>\
<ul>\
<li>Family</li>\
</ul>\
<p>The great boyfriend showers affection on his family. He is especially\
affectionate with little nieces and nephews.</p>\
<p>The ideal lover is either fighting or drinking with his family. He\
is the first to teach his little nephew how to flip the bird and what\
it means.</p>\
<ul>\
<li>Sex</li>\
</ul>\
<p>The great boyfriend is a master of foreplay and delaying his own\
gratification. He is a slow and steady lovemaker. The look of surrender on\
his woman&#8217;s face during orgasm brings him almost as much pleasure as\
his own climax. Sex is often preceded by the lighting of scented candles and\
the playing of soft jazz.</p>\
<p>The ideal lover is selfish in bed. He may eat his woman out for an\
eternity one night while hurting her anally another night,  slowly grind\
into her missionary style or jackhammer her like a rutting cape buffalo,\
but always know that everything he does sexually to her is in service to his\
penis. He will often not know nor care if she came,  and what usually precedes\
sex is a rough hand up her skirt.</p>\
<ul>\
<li>Compassion</li>\
</ul>\
<p>The great boyfriend will listen intently when his girl has had a bad day,\
careful not to brusquely offer any pointed suggestions to alleviate her\
sadness,  instead opting to massage her shoulders and make her some soup.</p>\
<p>The ideal lover will attempt to take his girl&#8217;s mind off her worries\
with hot sex. It will usually work.</p>\
<ul>\
<li>Values</li>\
</ul>\
<p>The great boyfriend appreciates his girlfriend&#8217;s values,\
and this is reflected in his mature respect for her political views,\
even when he disagrees.</p>\
<p>The ideal lover only cares for one value &#8212; his lover&#8217;s\
commitment to the righteousness of sexual abandon. He&#8217;s apolitical as\
far as she knows,  because he&#8217;s very good at mentally dismissing her\
silly political beliefs as the earnest naivete of an unworldly\
little girl.</p>\
<ul>\
<li>Compatibility</li>\
</ul>\
<p>The great boyfriend understands that much of what makes a relationship\
successful are shared goals and interests. He loves spending time with his\
lover doing things they both enjoy,  and he will put in the extra effort to\
learn about those things she likes to do but which he is either unfamiliar\
or uninterested. For instance,  if she likes tango dancing but he&#8217;d\
rather play pool,  he&#8217;ll spend a night or two attending tango\
classes with her and making her feel worth his sacrifice.</p>\
<p>The ideal lover understands that what makes a relationship successful is\
not spending too much time together. Quality over quantity,  and in his\
world the best measure of quality is how often intercourse is happening. He\
will occasionally treat his lover to romantic nights out,  but when she wants\
him to join her on <a href="https://heartiste.wordpress\
.com/2009/11/16/discovering-a-girls\
-soul-with-one-simple-question/" target="_blank\
">her trip to Antartica</a> he&#8217;ll stroke\
her cheek lovingly and tell her to have a good time by herself.</\
p>\
<p>These examples should give you an idea where on\
the testicular spectrum you fall. Are you a Latin lover or a loving\
partner? Like I said,  most men lean one way or the other\
,  a few embrace an extreme,  and only Master Casanovas balance their dual\
essence so evenly that their women are always breathlessly infatuated \
with them.</p\
>\
<p>The men who have <a href="https://\
heartiste.wordpress.com/2009/05/19/be-\
a-skittles-man/" target="_blank">complete command over their\
women</a> are the men who intuitively know when to disarm with\
the tender ministrations of the great boyfriend or the lustful\
recklessness of the ideal\
lover. When you are aware of this ever present immutable female desire for\
dualing male archetypes,  you will find it that much easier to direct a\
woman&#8217;s emotions,  like Mozart conducting a symphony. A\
woman&#8217;s loyalty is as much a function of your ability\
to seduce it out of her as it is of her character.</p>'

f10 = epub.EpubHtml(title='the sixteen commandments of poon',
file_name='the_sixteen_commandments_of_poon.xhtml',
lang='en')
f10.content='<h2>The Sixteen Commandments of Poon</h2><p><strong>I. Never\
say &#8216;I Love You&#8217; first</strong></p>\
<p>Women want to feel like they have to overcome obstacles to win\
a man&#8217;s heart. They crave the challenge of capturing the\
interest of a man who has other women competing for his attention,\
and eventually\
prevailing over his grudging reluctance to award his committed\
exclusivity. The man who gives\
his emotional world away too easily robs women of the\
satisfaction of earning his love\
. Though you may be in love with her,  don&#8217;t\
say it before she has said it. Show compassionate restraint for her need to\
struggle toward yin fulfillment. Inspire her to take the leap for you,  and\
she&#8217;ll return the favor a thousandfold.</p>\
<p\
><strong>II. Make her jealous</strong></p>\
<p\
>Flirt with other women in front of her. Do not dissuade other women\
from flirting with you. Women will never admit this but jealousy excites them.\
The thought of you turning on another woman will arouse her sexually. No girl\
wants a man that no other woman wants. The partner who harnesses the gale\
storm of jealousy controls the direction of the relationship.</p>\
<p><\
strong>III. You shall make your mission,  not your woman,  your\
priority</strong></p>\
<p>Forget all those romantic cliches of\
the leading man proclaiming his undying love for the woman who completes\
him. Despite\
whatever protestations to the contrary,  women do not want to be &#8220;\
The One&#8221; or the center of a man&#8217;s\
existence. They in fact want to subordinate themselves to a worthy man&#8217\
;s life purpose,  to help him achieve that purpose with their feminine support\
,  and to follow the path he lays out. You must respect a woman\
&#8217;s integrity and not lie to her that she is &#8220\
;your everything&#8221;. She is not your everything,  and if she\
is,  she will soon not be anymore.</p>\
<p><strong\
>IV. Don&#8217;t play by her rules</strong></\
p>\
<p>If you allow a woman to make the rules she\
will resent you with a seething contempt even a rapist cannot inspire.\
The strongest\
woman and the most strident feminist wants to be led by,  and to submit\
to,  a more powerful man. Polarity is the core of a healthy loving\
relationship. She does not want the prerogative to walk all over you with her\
capricious demands and mercurial moods. Her emotions are a hurricane,  her\
soul saboteur. Think of yourself as a bulwark against her tempest.\
When she grasps\
for a pillar to steady herself against the whipping winds or\
yearns for an authority\
figure to foil her worst instincts,  it is you who has to be there\
&#8230; strong,  solid,  unshakeable and immovable.</p>\
<p\
><strong>V. Adhere to the golden ratio</strong></p>\
\
<p>Give your woman 2/3 of everything she gives you.\
For every three calls or texts,  give her two back. Three declarations of\
love earn two in return. Three gifts; two nights out. Give her\
two displays of affection and stop until she has answered with three \
more. When\
she speaks,  you reply with fewer words. When she emotes,  you emote\
less. The idea behind the golden ratio is twofold &#8212; it establishes\
your greater value by making her chase you,  and it demonstrates that you have\
the self-restraint to avoid getting swept up in her personal dramas.\
Refraining\
from reciprocating everything she does for you in equal measure instills in\
her the proper\
attitude of belief in your higher status. In her deepest loins it is what\
she truly wants.</p>\
<p><strong>VI. Keep her\
guessing</strong></p>\
<p>True to their inscrutable natures,\
women ask questions they don&#8217;t really want direct answers to.\
Woe be the man who plays it straight &#8212; his fate is the\
suffering of the beta. Evade,  tease,  obfuscate. She thrives when she\
has to imagine what you&#8217;re thinking about her,  and withers\
when she knows exactly how you feel. A woman may want financial and family\
security,  but she does not want passion security. In the same manner,\
when she has displeased you,  punish swiftly,  but when she has done you\
right,  reward slowly. Reward her good behavior intermittently and\
unpredictably and she will\
never tire of working hard to please you.</p>\
<p><strong\
>VII. Always keep two in the kitty</strong></p>\
<\
p>Never allow yourself to be a &#8220;kept man&#8221\
;. A man with options is a man without need. It builds confidence and\
encourages boldness with women if there is another woman,  a safety net,  to\
catch you in case you slip and risk a breakup,  divorce,  or a\
lost prospect,  leading to loneliness and a grinding dry spell. A woman knows\
once she has slept with a man she has abdicated a measure of her power\
; when she has fallen in love with him she has surrendered nearly all of\
it. But love is ephemeral and with time she may rediscover her power and\
threaten to leave you. It is her final trump card. Withdrawing all her\
love and all her body in an instant will rend your soul if you are\
faced with contemplating the empty abyss alone. Knowing there is another\
you can turn\
to for affection will fortify your will and satisfy your manhood.</p>\
<\
p><strong>VIII. Say you&#8217;re sorry only when\
absolutely necessary</strong></p>\
<p>Do not say you&#\
8217;re sorry for every wrong thing you do. It is a posture\
of submission that no man should reflexively adopt,  no matter how alpha he is\
. Apologizing increases the demand for more apologies. She will come to\
expect your\
contrition,  like a cat expects its meal at a set time each day.\
And then your value will lower in her eyes. Instead,  if you have\
done something wrong,  you should acknowledge your guilt in a glancing\
way without resorting\
to the actual words &#8220;I&#8217;m sorry.&#8221\
; Pull the Bill Clinton maneuver and say &#8220;Mistakes were made&#\
8221; or tell her you &#8220;feel bad&#8221; about\
what you did. You are granted two freebie <em>&#8220;I\
&#8217;m sorry&#8221;</em>s for the life of\
your relationship; use them wisely.</p>\
<p><strong>IX\
. Connect with her emotions</strong></p>\
<p>Set yourself\
apart from other men and connect with a woman&#8217;s emotional landscape\
. Her mind is an alien world that requires deft navigation to\
reach your rendevous\
. Frolic in the surf of emotions rather than the arid desert of logic.\
Be playful. Employ all your senses. Describe in lush detail scenarios to set\
her heart afire. Give your feelings freedom to roam. ROAM. Yes,\
that is a good word. You&#8217;re not on a linear\
path with her. You are ROAMING all over,  taking her on an adventure\
. In this world,  there is no need to finish thoughts or draw conclusions\
. There is only need to EXPERIENCE. You&#8217;re grabbing her\
hand and running with her down an infinite,  labyrinthine alleyway\
with no end,\
laughing and letting your fingers glide on the cobblestone walls along\
the way.</p\
>\
<p><strong>X. Ignore her beauty</strong></p\
>\
<p>The man who trains his mind to subdue the reward centers\
of his brain when reflecting upon a beautiful female face will\
magically transform his interactions\
with women. His apprehension and self-consciousness will melt away,\
paving the\
path for more honest and self-possessed interactions with the\
objects of his desire\
. This is one reason why the greatest lotharios drown in more love than they\
can handle &#8212; through positive experiences with so many beautiful\
women they lose\
their awe of beauty and,  in turn,  their powerlessness under its spell.\
It will help you acquire the right frame of mind to stop using the words\
<em>hot,  cute,  gorgeous,  </em>or <em\
>beautiful </em>to describe girls who turn you on. Instead,\
say to yourself &#8220;she&#8217;s interesting&#8221;\
or &#8220;she might be worth getting to know&#8221;. Never\
compliment a girl on her looks,  especially not a girl you aren&#8217\
;t fucking. Turn off that part of your brain that wants to put\
them on pedestals. Further advanced training to reach this state of\
unawed Zen transcendence\
is to sleep with many MANY attractive women (try to avoid sleeping with a\
lot of ugly women if\
you don&#8217;t want to regress\
). Soon,  a Jedi lover you will be.</p>\
<p\
><strong>XI.  Be irrationally self-confident</strong></p>\
\
<p>No matter what your station in life,  stride through the world\
without apology or excuse. It does not matter if objectively you are not the\
best man a woman can get; what matters is that you think and act\
like you are. Women have a dog&#8217;s instinct for uncovering\
weakness in men; don&#8217;t make it easy for them.\
Self-confidence,  warranted or not,  triggers submissive emotional\
responses in women.\
Irrational self-confidence will get you more pussy than\
rational defeatism.</p>\
\
<p><strong>XII.  Maximize your strengths,  minimize your weaknesses</\
strong></p>\
<p>In the betterment of ourselves as men we\
attract women into our orbit. To accomplish this gravitational pull as\
painlessly and efficiently\
as possible,  you must identify your natural talents and shortcomings and\
parcel your efforts\
accordingly. If you are a gifted jokester,  don&#8217;t waste\
time and energy trying to raise your status in philosophical debate.\
If you write\
well but dance poorly,  don&#8217;t kill yourself trying to expand\
your manly influence on the dancefloor. Your goal should be to\
attract women effortlessly\
,  so play to your strengths no matter what they are; there is a\
groupie for every male endeavor. Except World of Warcraft.</p>\
<p\
><strong>XIII. Err on the side of too much boldness,  rather\
than too little</strong></p>\
<p>Touching a woman inappropriately\
on the first date will get you further with her than not touching her at\
all. Don&#8217;t let a woman&#8217;s faux\
indignation at your boldness sway you; they secretly love it when a\
man aggressively\
pursues what he wants and makes his sexual intentions known. You don&#8217\
;t have to be an asshole,  but if you have no choice,\
being an inconsiderate asshole beats being a polite beta,  every time.</p>\
\
<p><strong>XIV. Fuck her good</strong></p>\
\
<p>Fuck her like it&#8217;s your last fuck.\
And hers. Fuck her so good,  so hard,  so wantonly,  so\
profligately that she is left a quivering,  sparking mass of shaking\
flesh and sex\
fluids. Drain her of everything,  then drain her some more. Kiss her\
all over,  make love to her all night,  and hold her close in\
the morning. Own her body,  own her gratitude,  own her love.\
If you don&#8217;t know how,  learn to give her squirting\
orgasms.</p>\
<p><strong>XV. Maintain your state control\
</strong></p>\
<p>You are an oak tree. You will not be manipulated by\
crying,  yelling,  lying,  head games,  sexual withdrawal,  jealousy ploys,\
pity plays,  shit tests,  hot/cold/hot/cold,  disappearing\
acts,  or guilt trips. She will rain and thunder all around you and\
you will shelter her until her storm passes. She will not drag you into\
her chaos or uproot you. When you have mastery over yourself,  you will\
have mastery over her.</p>\
<p><strong>XVI.  Never be afraid to lose her</strong></p>\
<p>You must not fear. Fear is the love-killer.\
Fear is the ego-triumph that brings abject loneliness. You will face your\
fear. You will permit it to pass over and through you. And when\
your ego-fear is gone you will turn and face your lover,  and\
only your heart will remain. You will walk away from her when she has\
violated your integrity,  and you will let her walk when her heart is closed\
to you. She who can destroy you,  controls you. Don&#8217\
;t give her that power over yourself. Love yourself before you love her.</p>\
<p>***</p>\
<p>The closer you follow the letter of these commandments,  the easier\
you will find and keep real,  true unconditional love and happiness in\
your life\
.</p>\
<p>Best.</p>'

f11 = epub.EpubHtml(title='the fundamentals',
file_name='the_fundamentals.xhtml',
lang='en')
f11.content='<h2>The Fundamentals</h2><p>There is so much pickup information\
available now that\
it&#8217;s easy to lose sight of the fundamentals that govern sexual\
tension and attraction between men and women. When the information\
cascade overwhelms it begins to pull you away from what works,  and\
what has always worked for you\
. Consequently,  over-analysis can hinder your spiritual growth as\
a womanizer.\
That is why it is vital to step back every so often,  ignore the\
steady stream of advice,  and return to a few golden,  immutable laws of\
attraction that will never go out of style.</p>\
<p>The\
one fundamental to which I always return,  and has never failed to reward me\
as expected,  is this:</p>\
<p>Women cannot resist the\
aloof and indifferent man.</p>\
<p>Of all the compulsions hard\
-wired in a female&#8217;s hindbrain,  this one is etched\
deeper and more enduringly. Every woman,  to a greater or lesser degree,\
feels the burn of lust and the agony of love for a man who projects\
a &#8220;take it or leave it&#8221; attitude.</p\
>\
<p>Note that aloof and indifferent doesn&#8217;t mean\
haughty,  distant or uninterested. It means <em>disinterested.</em>\
It means that while you may love her and flatter her and soothe her and\
give her gifts,  underlying it all is an attitude that tells her &#8220\
;I can walk if necessary,  and find someone new.&#8221;</p\
>\
<p>It may seem counterproductive for a woman to respond so favorably\
to a man exhibiting this attitude,  but the evolution of human sociosexuality\
offers an\
explanation: an aloof man is indirectly advertising his skill at seducing\
women. Such\
a man will give a woman sons who will inherit his ladykiller genes. Conversely\
,  a man who gloms onto a woman may as well be holding a placard\
that says &#8220;My celibacy is nigh!&#8221;. He has no\
confidence that should his girlfriend or wife misbehave,  or leave him,\
he will\
be able to find another woman&#8217;s bossom for comfort.</p\
>\
<p>And really,  that&#8217;s what all this\
talk by women about valuing &#8220;confidence&#8221; in men means\
; what women are really saying is that they value men who could dump them\
on a whim and get with new women easily. Men who can do this\
are filled with the kind of confidence that turns women on.</p>\
<\
p>The aloof and indifferent attitude can be expressed reactively or\
proactively,  deliberately\
or passively. She senses it when other women flirt with you and you refuse\
to act ashamed for it. You don&#8217;t rub your desirability\
to competitor women in her face,  but neither do you downplay it.</p\
>\
<p>She senses it when she is the first to say &#\
8220;I love you&#8221;,  after many months of eager &#8212\
; but ultimately unfulfilled &#8212; anticipation on her part for you to say\
it first.</p>\
<p>She senses it when you occasionally pepper\
your relationship with unexplained absences.</p>\
<p>She senses it when\
you hang out with guy friends who are known players.</p>\
<p\
>She senses it when you drag your feet about going on expensive trips together\
.</p>\
<p>She senses it when you are <a href\
="https://heartiste.wordpress.com/2010/07/16/\
why-you-should-leave-after-sex/" target="_blank\
">the first to hop out of bed</a> after climax.</p\
>\
<p>She senses it when your exes are always bumping into you\
.</p>\
<p>She senses it when you announce that you don\
&#8217;t understand guys like her male friend who can only play video\
games when his girlfriend is not around to castigate him,  and when you then\
proudly and defiantly proclaim you value your &#8220;freedom and\
independence&#8221\
; too much to be like that guy.</p>\
<p>She senses it when a half-assed microwaved meal that you cooked for the\
both of you means more to her than a four course dinner\
slaved over for hours in the kitchen by a beta would mean to her.</\
p>\
<p>She senses it when you set the bar so low\
,  it becomes a challenge to disappoint her.</p>\
<p>The\
fundamentals. Be aloof. Be indifferent. Be loving.</p>\
<p\
>Do these three things and you will never be lacking for a woman&#\
8217;s eternally grateful love.</p>'

f12 = epub.EpubHtml(
    title='flattering words',
file_name='flattering_words.xhtml',
lang='en ')

f12.content='<h2>The Most Flattering Words You Can Hear From A Woman \
<p>Some of you naive souls may be thinking,  &#8220;\
Oh,  I know the answer! Me! Me! Look over here!&#\
8230;. &#8216;I love you&#8217;. Did I win?&#\
8221;</p>\
<p>No,  you did not. You LOSE\
,  madam. You get NOTHING. Good day to you.</p>\
<\
p>The answer is this: &#8220;How can you be such\
a jerk and so lovable at the same time?&#8221;</p>\
<\
p>Gentlemen,  if you hear that from a woman,  particularly a girlfriend\
or wife,  you will know you have penetrated her heart and mind to the\
soft,  chewy center of her hamster&#8217;s id,  which is\
one id level deeper than her own human id. You cannot possibly hear anything\
more flattering from a woman unless it&#8217;s a breathless demand to\
scour her cervical wall with your proud protuberance.</p>\
<p>&#8220\
;How is being called a jerk more flattering than just being\
called lovable?&#\
8221;</p>\
<p>Oh,  you silly,  anatomically ambiguous acculturated\
automaton. Don&#8217;t you know how to read girlcode? It\
&#8217;s like hieroglyphics,  except less understandable to the average man.\
When a girl calls you a jerk,  you have enflamed her vagina. When\
a girl calls you lovable,  you have palpitated her heart. When a girl\
calls you a jerk AND lovable,  you have made a slave of her.\
Recline in the pillow-soft comfort of your testicular allure,\
because from that\
point forward you can do no wrong.</p>'

f13 = epub.EpubHtml(title='love',
file_name='love.xhtml',
lang='en')
f13.content='<h2>Love</h2>'

c = epub.EpubHtml(title='chicks: their ways and workings',
file_name='chicks.xhtml',
lang='en')
c.content='<h2>Chicks: Their Ways and Workings</h2>'


c1 = epub.EpubHtml(title='where guys falter',
file_name='where_guys_falter.xhtml',
lang='en')
c1.content='<h2>Where Guys Falter</h2>\
<p>The best way to do well with women over the long haul\
is to think like them,  understand them,  and put yourself in their shoes\
.  The man who can empathize with a woman&#8217;s frustrations will\
know better how to make her happy.  All the great seducers of history co\
-opted to some degree the psychology and the courting tactics of women.  They\
used women&#8217;s pyschological weapons against them.</p>\
<p\
>This is why European men have a reputation for smoothness with the ladies &#\
8212; they spend more time than American men in the company of women,\
participating in activities and intellectual pursuits that appeal to women,\
learning about them.\
American men bemoan their dating hardships,  but spending all their free time\
watching sports\
,  drinking beer,  video gaming,  and golfing,  where no women are present\
,  only to take a flailing Saturday night stab at getting laid in overheated\
bar\
environments,  is not a good way to learn how to turn women on.</\
p>\
<p>The inexperience of many guys around women shows in their\
ham-fisted come-ons.  They often act so counter-productively that\
it&#8217;s a wonder any girls give it up to them at\
all.  Verbally gang tackling a group of girls at a bar is one example\
.  Which guy,  in a moment of reflection,  really believes that\
approaching two\
girls with five of his buddies in phalanx formation and swarming them\
like vultures over a carcass will win their affections?  Guys who\
don&#8217;t have\
the sack to approach women on their own should not advertise their weakness\
by storming\
in with a giant cock posse for battlefield support.  Two guys maximum.  If\
necessary,  hold off on waving the rest of the crew in until after the\
set has been warmed up in a non-threatening way.</p>\
<\
p>Guys also do not listen.  Well,  not in the way that\
women want to be listened to.  A guy should listen to a woman with\
the same intensity he listens to his buddies talk about football or\
German hookers.\
The focus that a nerd brings to tackling a coding problem is the same focus\
that a guy should have when listening to an attractive woman speak.  The trick\
is to do it with the distracted aloofness of someone not hanging on her every\
word.  It&#8217;s very alluring to a girl when a guy\
off-handedly recalls some inconspicuous detail he picked up about\
her while she was\
talking without looking like he worked hard to remember it.  It\
subconsciously says to\
her &#8220;This guy is not desperate,  but wow I must be\
making an impression because he remembers how I felt when I danced \
at my sister\
&#8217;s wedding.  We connect!&#8221;</p>\
<p\
>This isn&#8217;t meant as mealy-mouthed John Gray relationship\
pap; listening intently to a woman will give him all the information he needs\
to successfully seduce her.  Women reveal so much about themselves in\
conversation &#8212\
; they can&#8217;t help it because they are self-obsessed\
creatures by nature &#8212; but they only do it in subtle read-\
between-the-lines ways,  feminine ways,  that to the uninitiated man will pass\
right under his radar.  It&#8217;s a double curse\
that boobs and pretty eyes cloud his efforts to stay engaged with her words.</\
p>\
<p>To seduce women,  you must seduce yourself first.\
You are the guy who will be everything she needs.  How will you know\
what she needs?  Get inside her head.  Become her.</p>\
'


c2 = epub.EpubHtml(title='away from the comapny of women',
file_name='away_from_the_company_of_women.xhtml',
lang='en')
c2.content='<p><em>I am never in the company of men after 5.<br />\
</em>&#8211; Bertrand Morane</p>\
<p><em>After sex,  the company of women can be a drag.<br />\
</em>&#8211; Me</p>\
<p>I spend a lot of time with women. Either seducing them\
,  fucking them,  <a href="https://heartiste.wordpress.com\
/2009/06/04/is-lady-rain-in-\
this-porno/" target="_blank">fucking with them</a>,  listening \
to them,  scratching the napes of their necks,  or examining them like a \
disassembled timepiece. The purpose of such mingling goes deeper than \
enjoying the pleasure of \
their company. Books,  mentors,  a willingness to discard delusion and lies,  \
and a keen eye will aid a man in his divine quest to acquire as \
much sex and love as he can handle from beautiful women,  but no impetus \
to personal growth is as effective as direct interaction with the subject. \
Whether sex \
is or is not the goal,  being around women sharply flattens the learning curve\
. There may be a gene yet discovered which grants its possessor the \
innate ability \
to know how a woman ticks,  but if there is such a gene,  \
it is a neural algorithm that quickly decays from disuse. Even the \
best naturals \
had to <span style="text-decoration:line-through;">buck \
up and endure</span> spend glorious time around women before their Asmodeus-\
blessed gifts could find full expression.</p>\
<p>Given this reality\
,  some men might make the understandable mistake that their every \
waking moment should be \
with women or,  if no women are physically present,  with women in their \
thoughts. This would be a false extrapolation. Like a diligent \
scientist deep in \
the bowels of his flourescently dismal lab who has forgotten the \
feeling of the sun \
on his face,  a man who spends all his free time with women risks \
degeneration of his masculine core. Inhalation of the estrogenic fumes \
of too much distaff \
attention and his spirit becomes arthritic,  his testicular acuity \
blurs into maudlin mush. \
Perspective is lost.</p>\
<p>Men would do well to occasionally \
distance themselves from women and their petty intrigues,  and the best \
way to do \
this is not through solitude but in the company of other men,  reveling in \
hearty chest thumps,  metaphorical or real,  and swearing bloodstirring oaths \
to doctrines good \
and great that elude the grasp of women stuck in the mud of their uninspiring\
,  earthy practicality. And men,  unlike women,  are capable of their high \
drama without uttering a word.</p>\
<p>Let me cut to the chase: Women are mostly \
boring. Even,  maybe especially,  the brightest and most overeducated \
among them can \
induce cataract-like glazing of the eyes if given enough comfort and \
a sympathetic \
ear to unleash the menstrual force of their vaggy stream of consciousness. \
Disconnected from \
their bodies and sexuality,  their flirtations and flattery,  and their \
charm and whimsy\
,  women are incapable of seriously entertaining for any length of time \
greater than the \
duration from leer to spent urge any but the most desperately cloying of men. \
Sure there are exceptions &#8212; women of particularly engaging personalities \
and surprising fondness \
for the abstract &#8212; but these exceptions serve merely to remind a man \
of the depressing drabness of the mass of women with their meager,  \
provincial concerns\
.</p>\
<p>Don&#8217;t lose contact with the world of men\
. Their vigorous,  purposeful company is a refreshing tonic to the \
pedestrian prattle,  \
contrived machinations,  and histrionic solipsism of women.</p>\
'

c4 = epub.EpubHtml(title='the most misogynistic blog post \
                   on the internet',
file_name='misogynistic.xhtml',
lang='en')
c4.content='<h2>The Most Misogynistic Blog Post On The Internet</h2>\
<p>If people are going to accuse you of misogyny,  may as well enjoy the \
egotistic benefits of being a truth-telling misogynist.</p>\
<p>***</p>\
<p>Men move the discussion forward. Women swap recipes and beauty tips.</p>\
<p>Men debate. Women wheedle.</p>\
<p>Men confront. Women slander.</p>\
<p>Men act. Women plot.</p>\
<p>Men invent. Women benefit.</p>\
<p>Men are passionate. Women are passion parasites.</p>\
<p>Men cheat. Women betray.</p>\
<p>Men withdraw. Women shit test.</p>\
<p>Men kill. Women play let&#8217;s you and him fight.</p>\
<p>Men are emotionally distant. Women are emotionally manipulative.</p>\
<p>Men&#8217;s Achilles&#8217; heel is pride. Women&#8217;s Achilles&#8217; \
heel is vanity.</p>\
<p>Men die younger. Women live slower.</p>\
<p>Men think loftily. Women think grubbily.</p>\
<p>Men are expendable. Women are perishable.</p>\
<p>Men humiliate. Women shame.</p>\
<p>Men bluster. Women preen.</p>\
<p>Men break barriers. Women co-opt broken barriers.</p>\
<p>Men design. Women utilize.</p>\
<p>Men self-serve. Women self-delude.</p>\
<p>Men fuck. Women barter.</p>\
<p>Men are funny. Women are melodramatic.</p>\
<p>Men look at the sun. Women look in the mirror.</p>\
<p>Men sexualize. Women characterize.</p>\
<p>Men eat. Women indulge.</p>\
<p>Men aspire. Women inspire.</p>\
<p>Men love freely. Women love desperately.</p>\
<p>***</p>\
<p>This post is bitch bait. It&#8217;s been booby-trapped. We&#8217;ll \
see who trips it.</p>
'

c5 = epub.EpubHtml(title='why do conservatives sanctify women',
file_name='conservatives.xhtml',
lang='en')
c5.content='<h2>Why Do Conservatives Sanctify Women?</h2>\
<p>Reader LoboSolo sent me <a href="http://townhall.\
com/columnists/PaulGreenberg/2010/03/03/women_know?page\
=full&amp;comments=true" target="_blank">this article\
</a> by conservative writer Paul Greenberg extolling the\
&#8220;innate superiority\
&#8221; of women.</p>\
<blockquote><p>I&#\
8217;ve never been much of a believer in historical theories about\
the Indispensable\
Man. There may be some examples &#8212; Washington,  Lincoln,  Moses\
&#8212; but they are few. But the indispensable woman,  I believe\
in. Call it Greenberg&#8217;s Law: Women are the innately\
superior sex. My theory may not be backed by any scientific evidence,  but\
it&#8217;s something every man has surely felt. At least if\
he&#8217;s got a lick of sense. [&#8230;]</p\
>\
<p>When it comes to great truths,  each generation shouldn&#\
8217;t have to work them out by itself. They don&#8217\
;t have to be written down,  any more than the English constitution is\
. Every boy soon learns that women seem to know intuitively what the\
weaker male\
sex may grasp only by effort and education. Which is why it requires marriage\
and family to civilize the male animal. He needs a woman&#8217;\
s tutelage.</p></blockquote>\
<p>Greenberg tells a story,\
among others,  which purports to demonstrate unassailable female virtue:</p>\
<blockquote\
><p>Brighter boys learn the lesson of female superiority early; dimmer ones\
may never catch on. A story: It was homecoming weekend many years ago\
in Pine Bluff,  Ark.,  and a clump of us stood on Main Street\
waiting for the black college&#8217;s high-stepping marching band to\
come striding by,  drum major and majorettes and 76 trombones and all.</p\
>\
<p>A venturesome little boy in the group stepped off the curb\
to look way up the street &#8212; where the little girl on the\
Sunbeam Bread sign,  a local landmark,  still swings endlessly to and fro.\
Way in the distance,  the boy spotted the prancing majorettes\
throwing their batons high\
,  higher,  highest,  catching them on the beat. &#8220;Wow\
!&#8221; he exclaimed,  returning to report what he&#8217;d\
seen. His conclusion: &#8220;Girls have to know so many things\
!&#8221;</p></blockquote>\
<p>Lovely stories,  Mr.\
Greenberg. Now let me tell you a story.</p>\
<p>\
I&#8217;ve seen things you gullible chumps wouldn&#8217;t\
believe. Married women&#8217;s loins on fire off the rumpled sheets\
of my bed. A feminine Russian woman,  her buttocks turned in my direction\
,  sweetly asking me if I&#8217;d &#8220;like to\
do her in the ass&#8221; as her cell phone rings with the\
plaintive wail of her husband seeking her whereabouts. I&#8217;ve watched\
nipples harden in the dark near the cathedral gate,  and behind\
the rectory doors\
. I&#8217;ve lain with the most virtuous women you could imagine\
&#8212; caring women who &#8220;have to know so many things\
&#8221; and who give dollars to homeless bums and who tear up during\
sad scenes in the movies &#8212; who freely allowed my member to violate\
them in every conceivable way in their husband&#8217;s and boyfriend&#\
8217;s beds,  their writhing bodies,  ecstatic moans,  and gushing furrows\
testament to the lustful abandon with which they unshackled\
themselves of that other conservative virtue\
,  fidelity. I once counseled the most darling woman &#8212; a young\
woman so exquisitely gentle and winsome I&#8217;d dare any man not\
to fall instantly for her &#8212; to stop her flowing tears for our\
doomed affair and,  there on the sidewalk in midday,  to return to her\
husband at her apartment which was two blocks down the street;\
the husband who ,  through years of his toil and love,  put a roof\
over her underemployed\
head in one of the ritzier neighborhoods of the city. I have made love\
&#8212; God&#8217;s highest expression of devotion to His creation\
&#8212; with women in the company of small woodland creatures,\
scandalized roommates\
,  and children who were,  as best we dared,  out of earshot of\
our erotic rustlings. I have witnessed women,  caught in the snare\
of irrefutable\
evidence damning their supposed virtue,  lie with the effortlessness\
of a soulless sociopath.\
In the moment of release,  when we come closest to touching the Hand of\
God,  I have been instructed by a wondrously virtuous woman to &#8220;\
rape her&#8221; and to &#8220;do it like you mean\
it&#8221;. Her screams of howling joy &#8212; pain or pleasure\
I could not tell &#8212; to this day echo in my memories.\
And,  most enlightening of all,  I have seen wives and girlfriends,  their\
hearts once filled with seemingly endless and nourishing love,  cruelly\
turn on their daft\
former lovers with a vengeance unmatched by even a wronged God. Such as the\
time a sizzlingly sexy brunette whose mouth I was gracing with the\
metaphorical appendage of\
God&#8217;s divine love answered a phone call,  mid-oral\
delight,  from her ex-fiancee (who it should be noted was recovering\
from a mental breakdown) to thank him for purchasing a $5,\
000 Tempur-Pedic mattress delivered to her apartment two weeks earlier.\
Her thank\
you&#8217;s sounded surprisingly sincere for a woman whose free hand was\
simultaneously cradling the fleshy pod holding the life-giving seed\
of another man.</\
p>\
<p>All those moments will be lost in time,  Mr\
. Greenberg,  like tears in rain.</p>\
<p>What is\
it with conservatives and their willful blindness to the true\
nature of women? Pedestalization\
of the Other (and its many permutations,  c.f. &#8220\
;noble savage&#8221;,  &#8220;gaiaism&#8221;,  &#\
8220;diversity&#8221;,  and &#8220;na&#8217;\
vi&#8221;) is a sickening act of self-abasement; a\
desperate denial that one could possibly be right when one has been so badly\
wronged,  or that a wrongdoer could possibly be as bad as the facts\
attest. Perhaps those who engage in this sort of faith-based pedestalization\
of women are deathly afraid to confront the reality of female nature\
              because it\
would impose on their tidy worldview. Perhaps they need a savior,  in\
the form of women,  like of god,  to compartmentalize the darkness and\
symbolize something to aspire to. After all,  if women are just as\
bad as men,  where does that leave the sensitive man? Stuck now\
with double the responsibility to guard oneself against predation by\
              both sexes,  and\
to discard to the ash heap cherished notions of the fairer sex. Does\
this sound familiar? If you thought &#8220;beta&#8221;,\
you&#8217;d be right.</p>\
<p>Where\
conservatives sanctify women,  liberals demonize men. Not all\
              conservatives and not all\
liberals,  but enough of them that a valid generalization can be made.\
Whether sanctifying women or demonizing men,  the end result is the same:\
laws,  policies,  and cultural beliefs that are anti-male,  and\
which we in the West are soaking in today.</p>\
<p\
>I believe the conservative&#8217;s and liberal&#8217;\
s instincts toward women can be explained by contrasting the\
              peculiar life conditions of\
both:</p>\
<ul>\
<li>Conservatives,  having grown\
up in larger,  more intact families than liberals,  and being thus surrounded\
by more sisters,  aunts,  and female cousins on a daily basis,\
are loathe to imagine those female relatives could be the alpha cock-hungry\
animals inside that they really are. Liberals,  meanwhile,\
              hailing from broken\
homes and guided under the tutelage of man-hating single moms with a\
revolving bedroom door,  find it easier to grasp the amoral nature of women\
.</li>\
<li>Conservatives have less sexual experience with women than\
do liberals. I would not be surprised if it was discovered that liberal\
men lost their virginity at an earlier age than conservative men.\
              Nothing teaches\
like experience.</li>\
<li>Conservatives believe women are morally child\
-like compared to men,  that women are the weaker sex,  and\
so cannot be held accountable for their actions. Liberals,  who see white\
male oppression behind every human group difference,  are more\
              likely to individualize a\
woman&#8217;s bad actions and politicize a man&#8217;\
s bad actions.</li>\
<li>Conservatives are ashamed of their\
base desires. Thus,  they recoil at the thought that the women they\
desire might share the same debased thoughts that they do. Liberals,  by\
contrast,  are proud of their base desires. And so they are more\
accepting of the knowledge that women are as depraved as men.</li>\
<\
li>Religious conservatives fear sex for its power to distract from god. It\
is better for them that women are thought of as empty vessels incapable\
of making\
sex-based calculations in their decisions. Secular liberals love sex for\
its power\
to distract from considering the merits of any moral code. It is better for\
them that women are thought of as sex-possessed tankgrrls ready to\
rumble across\
the Vaginot Line of mind-body liberation.</li>\
<li>Conservatives\
invest more in the idea of family than do liberals. A wanton woman is\
a grave threat to that idea,  graver than even a wanton man,  for\
reasons clearly elucidated by evolutionary biology. Ergo,  women\
cannot possibly be as wanton\
as men.</li>\
<li>Conservative women are busier being pregnant and\
/or fatter than liberal women,  and are thus less frequently able to act\
wantonly. This may skew conservative men&#8217;s impressions of women to\
being something more positive than it really is.</li>\
<li>Conservatives\
by temperament are drawn to the beautiful. Liberals by temperament are\
drawn to the\
degraded. Conservatives have trouble tainting with dark knowledge the\
beauty of a woman in\
her prime. Liberals relish the thought that a beautiful young woman\
kwould wallow in\
the mud just as enthusiastically as they do.</li>\
</ul>\
<\
p>As a man who is drawn to both the beautiful and the degraded\
,  my aim is to act as a bridge between conservative men and liberal men\
,  holding the liberal&#8217;s hand tenderly to the conservative&#8217\
;s crotch. I shall bring understanding between the two mortal enemies,  and\
together we shall march into the nearest bar,  our minds fortified\
with the knowledge\
of women&#8217;s true natures and our hearts swollen with masculine conceit\
,  and lay waste to that place,  claiming battalions of pussy for our own\
. Without excuse,  without apology. Without god,  whether\
supernatural or political.</\
p>\
<p>Women are vile creatures at heart,  just as men\
are. An ugly truth,  Mr. Greenberg,  which even God can&#\
8217;t shield you from. Don&#8217;t let the batting eyelashes fool you.</p>\
'


c6 = epub.EpubHtml(title='heady pettiness',
file_name='heady_pettiness.xhtml',
lang='en')
c6.content='<h2>Heady Pettiness</h2>\
<p>I was with a girl shopping for assorted consumerist baubles. Technically\
,  she was shopping and I was providing color commentary. A man must learn\
to amuse himself to pull through these dreaded moments. In the middle of a\
well-delivered quip,  I noticed from the most distant corner of my eye\
a familiar jeans-covered ass. I studied the ass for a bit and\
the flow of hair down the back and realized it was one of my exes\
. She turned around and confirmed for me it was her.</p>\
<\
p>She didn&#8217;t see me. I watched her for\
a bit. The three years were not kind to her. Her body was\
still great but her face looked drawn,  eyes sad,  and was that an\
incipient turkey gullet? When I dated her she was a solid 8,  and\
sexy as hell. Now? A 7. Barely. In just three years\
she dropped a full point. I wondered if she had gone through an emotionally\
draining divorce in the time since I&#8217;d known her. She\
was at the store alone on a day in which most women are shopping with\
their partners.</p>\
<p>My time spent with her had been\
good. I held no ill will toward her. We departed not as exes\
,  but as former lovers,  blessedly free of bitterness or rancor. And yet\
,  when I saw my ex there in the store,  and mentally noted that\
the girl I was with was better looking than her,  a sadistic urge to\
flaunt my latest lover and parade her past my ex like a trophy float overcame\
me. I maneuvered myself and my female company into visual range of my ex\
. I refrained from looking over. I wanted the <a href="https\
://heartiste.wordpress.com/2007/10/15/bumping-\
into-exes/" target="_blank">bump in to feel natural</a\
>. (Had my lover been less attractive than my ex,  I would&#\
    8217;ve hid behind the clothes racks and rushed us out of the\
    store.)</p>\
<p>As I maneuvered closer to my ex\
through the aisles of clothes and kitchenware,  I placed my hands lovingly on\
various erogenous zones of my companion&#8217;s body. All while\
pretending not to notice my ex. I slid my hand down my lover\
&#8217;s back,  played with her hair,  and made sure\
to tell a joke so that she giggled girlishly within earshot of my ex\
. Unfortunately,  my ex didn&#8217;t notice. Either she\
was captivated by the 40% sale on hand towels,  or she was\
expertly avoiding acknowledging my presence. I doubted the latter,  \
because usually even\
the best actresses cannot hold it together with zen-like calm and serenity\
when bumping into an ex who left such an indelible impression on them.\
They give away their true feelings with a nearly imperceptible \
quiver in the shoulders\
,  or a nervous dart of the eyes.</p>\
<p>\
Had she forgotten me? Not possible. We dated too many months,\
and I&#8230; did things&#8230; with her that assured\
a memorial to me would forever be etched in her brain,  like a\
Vietnam Lovers Memorial of sex acts. Or maybe she didn&#8217;\
t recognize me? I *was* wearing a hat,  crisply turned\
down along the front brim.</p>\
<p>Nevertheless,  no\
matter how much I maneuvered,  I couldn&#8217;t needle my\
ex with my profound pettiness. She remained steadfastly\
unaware of my presence,\
flitting about the store like a hummingbird. What a wasted opportunity for a\
deliciously ego-massaging bump in.</p>\
<p>I told\
my girl about my ex being alone in the store,  and how I\
was trying to get the ex to see us. I also told her\
she was hotter than my ex. Instead of chastising me for my immaturity\
,  her eyes lit up with conspiratorial glee and she offered a strategy.</\
p>\
<p>&#8220;Ooh,  I&#8217;m\
curious. Which one is she? Let&#8217;s walk by\
her and I&#8217;ll stick my ass out for you to\
smack. Yay!&#8221;</p>\
<p>God bless women\
. Just when you are about to resign yourself to the thought that they\
are made of nothing but sugar and spice and everything nice,  you are\
reminded of the arsenic laced within.</p>\
<p>We left\
the store mission unaccomplished. I pondered for a second why I relished the\
thought of rubbing my happiness in the face of a sad,  possibly single\
ex for whom I had nothing but warm feelings. I had released the\
id monster from its hindbrain depths,  and danced a little jig with it\
.</p>\
<p>I guess it just feels too good.\
And I&#8217;ve no doubt she would&#8217;ve\
done the same had the shoe been on the other foot. Any woman\
would&#8217;ve done the same. But don&#8217;\
t bother asking them. They&#8217;ll deny deny deny.\
They&#8217;ve got an image to burnish,  you see.</\
p>\
<p><em>Note: As with many of my\
posts,  the chronology of this post has been altered to protect the innocent\
. Namely,  me.</em></p>
'

c7 = epub.EpubHtml(title='female dictionary',
file_name='female_dictionary.xhtml',
lang='en')
c7.content='\
<h2>Better Than Again: The Female Secret Code Decoder Dictionary</h2>\
<p>A wealth of experience with women will clue a man into the\
dissonance between a woman&#8217;s words and actions,  and gradually lead\
him to discover that the woman&#8217;s word is the exact inverse\
of what she wishes you to presuppose it is: not a verbal descriptive but\
rather a psychological misdirection to lull the unsuspecting,  including \
herself,  to cogitate on\
the opposite of what is,  in fact,  <a href="https://\
heartiste.wordpress.com/2008/09/09/better-than\
/" target="_blank">true</a>. Resist the temptation to blame a\
woman for her subterfuge because,  in another example of \
empirics catching up to folk\
wisdom,  <a href="http://www.nytimes.com/2009\
/01/25/magazine/25desire-t.html?_r=\
1&amp;pagewanted=all" target="_blank">science is revealing\
</a> that not even she is aware what currents ripple through her vagina\
.</p>\
<p>On that prologue,  here follows a handy dandy\
secret girl code decoder crib sheet. Though you have been weaned \
since toddlerhood,\
when your flaccid tot dong jutted out at a continual 90 degree angle to your\
raisins,  to believe the last in each series is to be aspired to,\
the truth is that,  if sexnlurv with the sexynlurvly hot babes is what you\
want,  then you are far better off being deemed the opposite by the fairer\
sex.</p>\
<p>douchey &gt;&gt;&gt;\
nice guy</p>\
<p>asshole &gt;&gt;&gt\
; sweet</p>\
<p>jerk &gt;&gt;&gt\
; cute</p>\
<p>bastard &gt;&gt;&gt\
; good man</p>\
<p>pig &gt;&gt;&\
gt; gentleman</p>\
<p>insane &gt;&gt;&\
gt; dependable</p>\
<p>jerk &gt; sexy &\
gt; hot &gt; cute &gt; sweet &gt; creep\
&gt; nice guy</p>\
<p>creeper &gt;\
creep &gt; stalker &gt; loser &gt; nice guy</\
p>\
<p>serial killer &gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;\
nice guy</p>\
<p>mass murderer &gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt; nice guy</p>\
<\
p>psychopathic hedge fund white collar criminal &gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;\
(*phew*) &gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt; nice guy</p>\
\
<p>nice guy &gt; pedophile (finally!)</p>\
<\
p>he makes me cry &gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt; he&#8217;s\
always there for me</p>\
<p>it&#8217;s\
so hard with him &gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt; yeah\
,  he&#8217;s a great guy</p>\
<p>\
freak &gt;&gt;&gt; attentive lover</p>\
<p\
>cheating bastard &gt;&gt;&gt; he treats me like a\
princess</p>\
<p>you don&#8217;t see what\
i see in him &gt;&gt;&gt; he&#8217;\
s the perfect man</p>\
<p>wiseass &gt;&gt\
;&gt; funny &gt;&gt;&gt; clown &gt;&\
gt;&gt; goofy &gt;&gt;&gt; quirky &gt\
;&gt;&gt; weird</p>\
<p>mysterious &gt\
;&gt;&gt; a good friend</p>\
<p>exciting\
&gt;&gt;&gt; easy to get along with</p>\
\
<p>i don&#8217;t know how much more i can\
take with him &gt;&gt;&gt; someday we&#8217;\
ll get married</p>\
<p>he always forgets our anniversaries &\
gt;&gt;&gt; he understands my needs</p>\
<p\
>pervert &gt;&gt;&gt; sensitive lover</p>\
<\
p>he screwed my best friend &gt;&gt;&gt; i\
screwed his best friend</p>\
<p>he gets me &gt\
;&gt;&gt; i get him</p>\
<p>fucking\
asshole arrogant son of a bitch motherfucking cocksucking pike of\
steaming shit filthy fucking bastard\
mama&#8217;s boy &gt;&gt;&gt; nice guy\
</p>\
<p>selfish lover &gt;&gt;&gt;\
eats me out</p>\
<p>who are you texting? &\
gt;&gt;&gt; i promise i&#8217;m not texting\
any other guys</p>\
<p>god that was such a turn\
-on &gt;&gt;&gt; i love you</p>\
\
<p>cocky bastard &gt;&gt;&gt; sweet guy</\
p>\
<p>i never know what he&#8217;s up\
to &gt;&gt;&gt; we go everywhere together</p>\
\
<p>lover &gt;&gt;&gt; husband</p>\
\
<p>is that a girl&#8217;s voice i hear in\
the background? &gt;&gt;&gt; thanks for letting me know\
what time you&#8217;ll be home</p>\
<p>\
you&#8217;re going to shit in front of me?! &gt\
;&gt;&gt; i&#8217;ll be out in a minute,  honey</p>\
'


c8 = epub.EpubHtml(title='womanese translator',
file_name='womanese_translator.xhtml',
lang='en')
c8.content='\
<h2>Womanese-to-English Translator</h2\
>\
<p>Online translator services are really helpful in a pinch when you\
&#8217;re overseas,  but what do you do when you&#8217\
;re talking with a woman who speaks your language? American women \
speak English\
,  at least syntactically and grammatically,  but the meanings of their \
words and sentences \
often mislead as much as inform. After all,  if women said what they \
meant and spoke clearly and honestly,  wining and dining them \
with all-expenses \
paid dates would be a thing of the past. You&#8217;d \
know within a few minutes whether she was going to put out for you or \
not. And if she was interested in sex,  you&#8217;d \
know exactly how to proceed to ensure it happened.</p>\
<p>\
So for those times when you actually care what a woman says to you &#\
8212; i.e.,  those times you&#8217;re talking with \
an attractive young babe you want to crotch smash &#8212; your life (\
and sanity) would be immeasurably improved if you had a Womanese-to-\
English translator at your instant disposal. Imagine \
the following conversation:</p>\
<\
p>YOU: Hi,  can I buy you a drink?</p>\
\
<p>HER: Sure!</p>\
<p>YOU: Cool\
.</p>\
<p>HER: Thanks. [drinks up,  eyes \
                 room,  alpha male pops up out of nowhere and \
                 she leaves with him\
                 ,  laughing all the way]</p>\
<p>YOU: fuck\
.</p>\
<p>Now this is how the above conversation would go \
if you had a Chateau Heartiste Womanese-to-English Translator on hand:</\
p>\
<p>YOU: Hi,  can I buy you a drink\
? [turns on W/E Translator,  patent pending]</p>\
<\
p>HER: Sure,  I won&#8217;t turn down a \
freebie,  but it will hurt your chances to have sex with me.</p\
>\
<p>YOU: Nah,  I changed my mind. I won\
&#8217;t buy you a drink.</p>\
<p>HER\
: So&#8230; you seem kind of interesting. New around here?</\
p>\
<p>See how your life would be so much better with \
the W/E Translator at your side? Here&#8217;s another \
sample conversation that many of you will encounter in the course of \
your pickup career\
:</p>\
<p>YOU: I collect walking sticks. Come,  \
let&#8217;s go to my place. I&#8217;ll \
show you my collection.</p>\
<p>HER: Ok,  but \
nothing&#8217;s going to happen tonight.</p>\
<p>\
YOU: [dejected face] oh,  ok. Well,  can I get \
your number?</p>\
<p>HER: [gives fake number]</\
p>\
<p>Feel like a lah-hooo-ser? You \
should. But you don&#8217;t need to ever feel that way \
again with the W/E Translator (patent pending,  internationally \
                               copyrighted)! How \
would the above conversation have turned out when run through the W/ET for \
accuracy?</p>\
<p>YOU: I collect walking sticks. Come\
,  let&#8217;s go to my place. I&#8217;\
ll show you my collection. [turns on W/ET]</p>\
\
<p>HER: Ok,  but nothing&#8217;s going to \
happen tonight if you give up trying.</p>\
<p>YOU: \
    [smug face] Don&#8217;t worry,  I won&#\
    8217;t.</p>\
<p>HER: [takes your \
         arm]</p>\
<p>Beautiful love,  with an assist from\
the W/E Translator. Can a price be put on such a product\
? It can&#8217;t,  but now you can have it for\
the low low price of $49.99,  an infinity dollars-minus\
-$49.99 savings! You&#8217;d be crazy to pass\
up this opportunity.</p>\
<p>More game-changing,  dick\
-wetting,  money-saving,  sanity-sparing magic,  courtesy of the\
W/ET:</p>\
<p><span style="text-decoration\
:underline;">Before W/E Translator</span></p>\
<p\
>YOU: [making bedroom move on your wife]</p>\
<p\
>HER: [turns over] I have a headache tonight. Maybe another\
time.</p>\
<p><span style="text-decoration:underline\
;">After W/E Translator</span></p>\
<p>YOU\
: [making bedroom move on your wife]</p>\
<p>HER\
: [turns over] Can&#8217;t do it. My vagina\
is still sore from fucking my boss.</p>\
<p><span style\
="text-decoration:underline;">Before W/E Translator</span></\
p>\
<p>HER: When are you going to dust the cat\
hair balls like I asked?</p>\
<p>YOU: Sorry,\
honey,  I forgot. I&#8217;ll get right to it.</\
p>\
<p>HER: Nevermind,  I already did it. You\
obviously don&#8217;t care.</p>\
<p>YOU:\
    What?! Of course I care about you! Where did this come from\
    ?</p>\
<p>HER: Just forget about it. I\
&#8217;ll be at the spa.</p>\
<p><span\
style="text-decoration:underline;">After W/E Translator</span\
></p>\
<p>HER: When are you going to stick up\
for yourself and say no to me?</p>\
<p>YOU:\
    So this is what you mean. I get it now.</p>\
\
<p>HER: My complaint about the cat hair balls is really a\
passive-aggressive taunt directed at your repulsive feeble betatude.</p>\
<p\
>YOU: It&#8217;s refreshing to know how you really feel\
instead of making me read between the lines.</p>\
<p>HER\
: I&#8217;ll be filing for divorce in less than a year\
.</p>\
<p>***</p>\
<p>Since I doubt your\
woman will stop talking anytime soon,  the W/E Translator is useful in\
every situation. Just read these typical obfuscating female words and\
watch them transform right\
before your eyes into distilled truth.</p>\
<p>HER: I\
don&#8217;t deserve you.</p>\
<p>W/\
ET: Treat me like shit if you want to get in my pants.</\
p>\
<p>HER: I&#8217;d rather not corrupt\
an innocent man.</p>\
<p>W/ET: Your inexperience\
with women is a turn-off.</p>\
<p>HER:\
    I&#8217;m not nearly as nice of a person as you\
    are.</p>\
<p>W/ET: I&#8217\
;m really nice to jerks,  but I won&#8217;t be\
nice to you.</p>\
<p>HER: I&#8217;\
m a bit too immature to appreciate a guy like you.</p>\
<\
p>W/ET: Call me in ten years after I&#8217\
;ve ridden the cock carousel and my looks have taken a hit.</p\
>\
<p>Act now,  and we&#8217;ll throw in\
the bonus W/E Nonverbal Translator! Just hold it up to visually record\
your girlfriend or wife,  and receive a verbal confirmation of her\
real state of\
mind.</p>\
<p>HER: [scarfs down ice cream]</\
p>\
<p>YOU: [activates W/ENT]</p>\
\
<p>W/ENT: &#8220;This ice cream is more\
exciting to me than your dick.&#8221;</p>\
<p>***</p\
>\
<p>HER: [parks her fat ass on a sofa to\
         watch The View]</p>\
<p>YOU: [point W\
         /ENT at her]</p>\
<p>W/ENT:\
    &#8220;I no longer feel motivated to please you because you are\
    an uninspiring beta herb.&#8221;</p>\
<p>Amazing stuff\
! And guess what? The W/ET even has a super secret algorithm\
that can tell which words women speak are truthful. That&#8217;s\
right,  it knows what needs translating,  and what doesn&#8217;t\
! When a woman says something unexpectedly candid,  the W/ET flashes a\
green light. That&#8217;s green light for &#8220;go\
to your nearest chapel and profess your belief in a higher being,  ESP,\
and Bigfoot&#8221;.</p>\
<p>HER: You&#8217\
;re too safe and predictable for me.</p>\
<p>W\
/ET: *green light*</p>\
<p>HER: You\
&#8217;re giving me too much power and I resent it.</p\
>\
<p>W/ET: *green light*</p>\
<\
p>HER: I wish you&#8217;d stop doing as I\
say because you logically figure it&#8217;s how to avoid a crushing\
break-up.</p>\
<p>W/ET: *green\
light*</p>\
<p>There&#8217;s even a setting\
that allows you to program the W/ET so that the closer a woman\
comes to speaking the unadulterated truth,  the brighter the green\
light shines in your\
face.</p>\
<p>HER: My vagina burns for violent sexual\
adventures with an emotionally opaque,  aloof badboy who makes me\
a little scared for\
my life.</p>\
<p>W/ET: *GREEN LIGHT\
GREEN LIGHT GREEN LIGHT*</p>\
<p>Sold yet? You should\
be! $49.99 will give you such a massive competitive advantage over\
every other man it&#8217;s a wonder this product isn&#8217\
;t ILLEGAL! Buy now before the divorce lawyers find a way to classify\
the W/E Translator as Schedule I contraband! (Operators and coping therapists\
                                              standing by.)</p>
'


c9 = epub.EpubHtml(title='top qualities',
file_name='top_qualities.xhtml',
lang='en')
c9.content='\
<h2>The Top Three Qualities That Make A Girl Good Girlfriend Material</h2>\
<p>There are many &#8220;tells&#8221; women have\
that,  unbeknownst to them,  signal to the men they are dating \
their worthiness\
as long-term investments. The tell number could very well be in the\
thousands,  and,  yes ladies,  we men are attuned to all of them\
,  in greater or lesser perspicacity,  and with conscious awareness \
or,  more often\
and more insidiously,  with subconscious awareness.</p>\
<p>But there\
&#8217;s value in narrowing the list to the top three tells,\
and clarifying them for the less experienced men (betas) so that they are\
armed with the foreknowledge to actively avoid those women who would \
make bad girlfriends or\
wives. An ounce of prevention is worth a pound of cuckoldry.</p>\
\
<p>So here they are: The top three girlfriend material qualities,\
in no particular order.</p>\
<p><strong>1. She\
exercised and ate healthily before she met you,  and she continues to do so\
after you start dating her seriously.</strong></p>\
<p>Marriage\
counselors and platitudinal couples therapists can stow their poppycock\
psychology aka feminist fantasy books.\
The biggest warning sign that a relationship is about to fail is the growing\
size of the woman. The fatter and more shapeless she gets,  the more her\
man&#8217;s eyes will wander,  his empathy will wither,  and\
his heart will shut down. A girl who has spent years cultivating\
good lifestyle\
habits that ensure she retains her slender,  hourglass figure for as\
long as possible\
is a girl who,  on a fundamental emotional level,  respects men&#8217\
;s needs and seeks to fulfill them. Feminists and assorted broken cunts don\
&#8217;t care about their appearance because they loathe male desire. That\
is why they are so unpleasant to be around for longer than it takes to\
deliver a hate-fueled hot jizz payload.</p>\
<p>A\
woman who works to stay as good-looking as she can within the constraints\
of her genetic endowment is signaling that she has a generous heart\
and a magnanimous\
soul. The care with which she comports herself will spill over into care for\
your well-being and support for your aspirations.</p>\
<p><\
strong>2. She rarely disparages her girl friends or snipes about their flaws\
behind their backs.</strong></p>\
<p>The girl who is\
forgiving of her friends&#8217; flaws,  who does not feel a compulsion\
to privately tear them down in order to lift herself up,  is a rare\
jewel indeed,  for the natural proclivity of The Woman™ is to backbite,\
snark and gossip about female competitors,  real and imagined,  until\
her ego tank\
is filled to brimming again. What care should men have about this\
peculiar trait\
of the unfairer sex? I&#8217;ll tell you. If she\
&#8217;s quick and all too enthusiastic to trash her friends in private\
,  she&#8217;ll be quick and all too enthusiastic to demean your\
manhood in the privacy of her mind. And once she&#8217;s\
gone down that road,  the mental demeaning begins its twisted\
manifestation into nagging and\
sex withdrawal. Unlike a man with a vendetta,  a judgmental bitch has a\
scattershot target designator; don&#8217;t be surprised if one day her\
gun of ingratitude is aimed directly at you.</p>\
<p>However\
,  expecting a girl to be nonjudgmental at all times is \
unrealistic. Women are\
born with the neural roadmap to gossip because it aids their sex in\
maximizing resources\
for their (eventual) families. But we can draw lines between women who\
occasionally indulge this instinct and women who wallow in it like a \
pig in mud\
. When you&#8217;re with your date,  is she constantly running\
down her supposed BFFs? Does her face light up when an opportunity \
presents to\
sneer about a friend&#8217;s recent nose job? Beware,  because\
you are staring at the dark heart of <a href="https://heartiste\
.wordpress.com/2012/02/01/the-evisceration-\
of-penelope-trunk/" target="_blank">borderline personality disorder</a\
> and unfettered narcissism,  the latter a characteristic that is\
particularly galling and self\
-immolating in women when taken to unhealthy extremes.</p>\
<p>\
A girl who is patient with and tolerant of her friends will extend the same\
to you. This then is an excellent foundation upon which to build a\
relationship\
that will have to,  necessarily due to the nature of two parties\
with competing\
reproductive goals,  navigate shoals in the future. A girl like this\
will also\
be more tolerant of your manly desire,  and,  instead of cutting down her\
competition,  will work on herself so that she can compete with the best of\
them for your love.</p>\
<p><strong>3. She\
has not had many past lovers,  and she is not a constitutional flirt who\
will invite the temptation of more lovers.</strong></p>\
<p>\
Lovefacts to make a feminist&#8217;s vagina explode angrily in a shower\
of dustballs: The more partners a woman has had,  the <a href\
="https://heartiste.wordpress.com/2010/09/16/\
why-sluts-make-bad-wives/" target="_blank">more\
likely she is to divorce you</a>. Sluts really are bad long-\
term prospects for men. They are great lays,  but they are bad ideas\
as girlfriends or wives. So be on the lookout today for <a href\
="https://heartiste.wordpress.com/2008/12/29/\
its-easy-to-identify-a-slut/" target="_blank\
">any and all slut tells</a> a girl will reveal in the\
course of dating her. It could save you a divorce theft tomorrow.</p\
>\
<p>But it&#8217;s not always easy to unearth\
a woman&#8217;s sordid past (rule of thumb: your working\
assumption should be that her past is more sordid than it is modest). So\
you have to rely on other,  more immediate cues of future\
unfaithful whorishness.\
That&#8217;s where a keen eye for her propensity to switch on\
a dime into flirt mode will serve you well. Constitutional flirts,  aka <\
a href="https://heartiste.wordpress.com/2010/07/\
15/shes-a-superflirt/" target="_blank">eternal ingenues</\
a>,  while fun in the beginning for their sexual promise and alluring \
coyness,\
can quickly become stressful headaches within the confines of a\
relationship. Watch for how\
effortlessly she can segue from poised girl into seductive flirt when\
other men are around\
. Does it come a little *too* naturally for her? Then you\
,  my friend,  are playing with vagina fire. A girl who loves to\
flirt,  and indulges frequently with or without you,  is a girl who is\
one private moment in the after hours office meeting room from cheating\
on you.</\
p>\
<p>Now,  personally,  I love flirty women. So\
walking the fine line between enjoying the company of flirts and suffering\
the crassness of\
flakes has presented challenges. Obviously,  I look for women who\
moderate their urges\
to flirt. A girl who generously throws off a flirty vibe that once in\
a blue moon time because she feels especially good about the way she looks,\
or because it&#8217;s her birthday,  is no trouble to dating\
stability. The girl who flirts with her girlfriend&#8217;s boyfriend on\
a random Wednesday night because,  oh,  she wants ALL the men&#8217\
;s attention,  and burgers are half price,  is a girl you should\
consider fucking and chucking after a few months pretending you&#8217;re into\
her that way.</p>\
<p>More importantly,  does she direct\
her flirting to me,  or to the world? Some girls just can&#\
8217;t get their attention whore fix without a large audience of men.\
Other girls,  the better ones,  are satisfied getting their ego fixes \
from their\
lovers alone. If a girl I am dating likes to flirt,  but she\
finds her outlet role playing Seductress Joan with me rather than\
sidling up like the\
town courtesan to every meathead with a hungry glare,  I bump her to the\
top of my LTR potential list.</p>\
<p>I hope this\
post is equally informative for the women reading as it is for the men.\
You ladies have a duty too,  if you want to capture the heart of\
a high value man,  and keep it:</p>\
<p><strong\
>Be fit.</strong></p>\
<p><strong>Be forgiving\
.</strong></p>\
<p><strong>Don&#8217;t\
be a foul slut.</strong></p>\
<p>If you think\
about it,  that&#8217;s not asking much compared to the grind\
that the average man has to endure to claim a single pussy as his own\
.</p>\
'


c10 = epub.EpubHtml(title='quality girl',
file_name='quality_girl.xhtml',
lang='en')
c10.content='\
<h2>Quality Girl</h2>\
<p>I&#8217;m often asked &#8220;What do\
you consider a quality girl?&#8221; This is a good question,  if\
by quality we mean a girl I&#8217;d be willing to date\
long term (&gt;3 months),  to invest more than the minimal amount\
of my time and energy,  and to feel secure,  if I were so\
inclined,  in committing myself exclusively without worry that she \
might spread her legs for\
any random guy who happens to catch her alone on an especially \
drunken night and\
says the right things about how good her forehead looks in the \
reflection of the\
beer bottle.</p>\
<p>Very few&#8230; and I\
mean VERY few&#8230; women in DC have met my exacting standards of\
quality. I&#8217;d estimate that of all the girls I&#\
8217;ve dated in this city less than 10% were worthy of my\
full attention. I&#8217;d hazard to guess that if all men\
held themselves to the same high standards I do and didn&#8217;t\
kowtow to the first chick who deigned to bless them with a crumb of affection\
there&#8217;d be universal agreement among DC men that my 10%\
figure is accurate. Maybe in flyover country the number of quality \
girls hits 25\
%. In Poland it is 80%. The times have changed and quality girls are\
no longer the norm.</p>\
<p>So what makes a quality\
girl? Well,  I know what *doesn&#8217;t* make\
a quality girl.</p>\
<ul>\
<li>She has cheated\
more than three times in her life,  or has cheated more than once on\
the same boyfriend.</li>\
<li>She forgets to say &#8220\
;thank you&#8221; when you buy her a drink. Buying her\
a second drink confirms her ingratitude.</li>\
<li>She dates around\
. Dating around &#8212; specifically,  seeing more than one person \
concurrently &#\
8212; is a prerogative of men only,  for reasons having to do with\
the greater leverage <a href="https://heartiste.wordpress.com/\
2007/11/14/dont-stop-thinking-about-the\
-next-girl/" target="_self">men need to arm themselves with\
</a> to compete in a dating market that is fundamentally tilted in favor\
of women. Any girl who makes a habit of dating more than one guy\
at a time,  especially if the parallel dating lasts longer than one month,\
in order to milk her options is a bad seed. In all my years\
of banging,  one soulsaving thing I&#8217;ve learned is to walk\
away from any girl who I&#8217;ve discovered is also dating other\
men. Even if I beat the competition and win her over,  it never\
ends well.</li>\
<li>She tells you she has a <\
a href="https://heartiste.wordpress.com/2008/07/\
01/boyfriend-destroyer/" target="_self">long distance boyfriend she loves\
</a>,  then proceeds to bang you anyway. A few months later,\
you see her groping a new guy,  and she&#8217;s still\
with her boyfriend. (That relationship is doomed.)</li>\
<li>\
Her default mode is sarcasm,  negativity,  coarseness,  \
and shamelessness.</li>\
\
<li>She spends twice as much time getting ready for a house party\
than she spends getting ready for a date with you.</li>\
<li\
>She can&#8217;t control her impulse to flirt with other men\
. Double minus points if she does this in your presence.</li>\
<\
li>She doesn&#8217;t seem nervous undressing in front of you\
the first time.</li>\
<li>She fucks you on a pretense\
of less than the sum total of an hour of conversation,  and calls you\
the next day worried that your condomless sex might have \
given her something. (\
    She&#8217;s been down this road before.)</li>\
<\
li>She is proud to be on the pill and considers her dependence\
on it a carte blanche slut sanctioner instead of a safety net \
affection fortifier\
.</li>\
<li>She is cavalier about casual sex.</li\
>\
</ul>\
<p>A quality girl does the opposite of\
all the above. She doesn&#8217;t cheat,  and if\
she does she has a plausible rationale. But she will still feel bad\
about it. She is generous when it is risky to be so.\
She is positive and lifts people up,  not pushes them down to lift\
herself up. She laughs at the absurdity and beauty of the world,\
but never at the expense of others. She is warm,  and this\
is something that can&#8217;t be taught. She says &#\
8220;I love you&#8221; early and often out of conviction\
,  not inquisition. She understands that her heart is more important than her\
pride.</p>\
<p>A high quality girl is good for\
standing by,  sticking with,  supporting always,  loving fully,\
    defending righteously\
,  and if the timing is right,  embracing for life to the exclusion\
    of all others. She is the type of girl who can enthrall you\
    with her words alone. She can make you smile over the phone.\
She can be far away but feel near. She is often discovered in\
the unlikeliest places,  and her magic is the energy that animates her pretty\
    face,  rather than the other way around.</p>\
<p>\
    Low quality girls are good for fucking,  a few laughs,  some funny\
    digicam pics,  and that&#8217;s it. Spare your hard\
    -earned manly capital &#8212; your time,  your resources,  your\
    protection,  your commitment,  your LOVE &#8212; for those few quality\
    girls you might meet if you&#8217;re lucky. And speaking\
    as a man who has seen,  heard and experienced enough to turn the\
    most naive optimist into a stone cold cynic,  if you do meet a girl like\
    that,  you would be a fool to pass her up. Her kind is going extinct.</p>\
'

c11 = epub.EpubHtml(title='slut id',
file_name='slut_id_xhtml',
lang='en')
c11.content='\
<h2>It''s Easy To Identify a Slut</h2>\
<p>Women seem to think that men are too thickheaded and inattentive to\
identify which of them are cockgobbling cumguzzling sluts. Or they prefer\
to believe their\
sly poses of innocence and white lies are good enough to keep men in the\
dark about their sexual histories. They would be wrong. The dirty\
little secret\
is out: Men have finely tuned straydar for slutty women because they are the\
ones more likely to cheat. Women <a href="http://www3.\
interscience.wiley.com/journal/118999174/abstract?CRETRY=1\
&amp;SRETRY=0" target="_blank">lie more about their\
sexual pasts</a> to men and to themselves,  or otherwise expend great\
effort covering it up,  because they know that men will downgrade them\
as potential\
long term mates if their sluttiness were revealed in all\
its jizz-spackled bukkaked\
glory.</p>\
<p>Here is a list of tramp tells:</\
p>\
<ul>\
<li>She broaches the subject of sex first\
.</li>\
</ul>\
<p>The more explicitly she talks about\
sex before you&#8217;ve banged her,  the likelier she has a\
storied slutty past.</p>\
<ul>\
<li>She suggests kinky\
sex acts.</li>\
</ul>\
<p>If you&#8217\
;ve been dating a short while and she eagerly implores you for public sex\
before the glow of bedroom missionary sex has worn off,  you&#8217;\
ve got a slut.</p>\
<ul>\
<li>She&#\
8217;s neurotic and disagreeable.</li>\
</ul>\
<p>\
Emotionally flighty girls are vaginally flighty girls. They are ruled\
by their vaginas.\
If she&#8217;s the gossipy,  backstabbing,  conniving sort who <\
a href="https://heartiste.wordpress.com/2008/10/\
22/sarcasm-is-unfeminine/" target="_blank">drips with sarcasm\
</a> and generally disdains everyone around her,  you can bet her black\
soul will seek sustenance on a carousel of cock.</p>\
<ul>\
\
<li>She frequently goes commando.</li>\
</ul>\
<p\
>Yeah,  as guys,  we think it&#8217;s hot when\
we slide our hands under our girlfriends&#8217; dresses during dinner in a\
fancy restaurant and discover a panty-less pussy waiting for us,  but what\
if you notice she&#8217;s sans underwear while you&#8217;\
re both shopping in Whole Foods? At a family picnic? In church?\
On a ferris wheel? In a glass elevator? You get the picture.</\
p>\
<ul>\
<li>She&#8217;s got that\
crazy,  hyper,  coked-up look in her eyes.</li>\
</\
ul>\
<p>Welcome to attention whore land! Chicks who can&#\
8217;t breathe without being the center of attention are chicks who are unable\
to control their craving for fresh cock. You want to be on the lookout\
for manic depressives and girls who can&#8217;t make it through a\
ten minute conversation without screeching in phony excitement.</p>\
<ul>\
<\
li>She shows a lot of cleavage all the time.</li>\
</\
ul>\
<p>No worries if she&#8217;s accentuating her\
tits on the first date to entice you,  but if she&#8217;\
s got those colliding death stars displayed for the world to admire\
every time you\
&#8217;re out with her,  you&#8217;ve got a\
woman on your hands who is addicted to advertising herself. And there will be\
buyers,  oh yes!</p>\
<ul>\
<li>She *\
really* seems to know what she&#8217;s doing in bed.</\
li>\
</ul>\
<p>Hey man,  nothing like getting a\
BJ from a chick who knows how to hit the underside with her tongue,\
but it does make you wonder how much dick it required for her to reach\
that level of professionalism.</p>\
<ul>\
<li>She has\
an impressive collection of vibrators and admits to wacking off to porn.</li>\
\
</ul>\
<p>She&#8217;s a high testosterone sex\
fiend who values sexual novelty more than pair bonding. This type of girl is\
a creature of her id. High T girls are easy to spot. Check\
for forearm hair,  narrow hips,  broad shoulders,  a penchant for cursing,\
a flat ass (adjusted for race),  career ambition,  and status whoring.</\
p>\
<ul>\
<li>She asks you how many women you\
&#8217;ve slept with or accuses you of being a player.</li\
>\
</ul>\
<p>One word: projection.</p>\
<\
ul>\
<li>She seems &#8220;hard&#8221;.</li\
>\
</ul>\
<p>If she&#8217;s got that\
tough,  tankgrrl aura about her,  like she&#8217;s been through\
dating hell and back,  and her cynicism is worse than yours,  you know\
she&#8217;s been used like a cheap whore.</p>\
<\
ul>\
<li>She&#8217;s incredibly circumspect or incredibly forthcoming\
about her past or sex in general.</li>\
</ul>\
<p\
>In the course of a few dates,  occasionally the conversation turns to past\
loves or sexual experiences,  or views on men and women and the dating scene\
. Normally,  these exchanges are blessedly brief and act as\
useful springboards for other\
topics,  but when she seems like she&#8217;s hiding something big\
you&#8217;ve got a right to be suspicious. Listen for tells\
that give the game away. Stuff like &#8220;Oh well,  we\
all have our skeletons&#8221;. Or &#8220;I&#8217;\
ve learned so much growing up.&#8221; Or &#8220;Men are\
pigs.&#8221; (The last one usually said by a record breaking slut\
.) Naturally,  you want to write off any girl as GF material who brags\
about her CRAZY and WILD college years. Believe me,  those years included more\
than college.</p>\
<ul>\
<li>She&#8217;\
s an artsy type.</li>\
</ul>\
<p>Or a\
lawyer. See: <a href="https://heartiste.wordpress.com\
/2008/09/17/how-to-handle-femmes-\
fatales-part-2a/" target="_blank">Eternal Ingenue</a>\
and <a href="https://heartiste.wordpress.com/2008/\
09/18/how-to-handle-femmes-fatales-part\
-3/" target="_blank">Amazonian Alpha</a>. The paradox of\
femininity is that it is often both the ultrafeminine and\
ultramasculine women who have racked\
up big numbers of men.</p>\
<ul>\
<li>She\
tells you about all the places she&#8217;s traveled.</li>\
\
</ul>\
<p>Yeah,  chicks love to travel,  but how\
many have put their dreams into action? If your date has been around the\
world twice with multiple stops in Rome,  Rio,  Vegas,  LA,  or\
some Appalachian backwater you can be sure she&#8217;s &#8220;\
traveled&#8221; straight into the crotch of an exotic local\
at every destination\
.</p>\
<ul>\
<li>She never has a break between\
men longer than one week.</li>\
</ul>\
<p>If\
she&#8217;s the type who can&#8217;t stand to\
be single and monkey swings from one man to the next,  sometimes with sperm\
-sharing overlap,  odds are high she&#8217;s a slut.</p>\
<ul>\
<li>You&#8217;re tapping her for the first time and\
she doesn&#8217;t remind you to put on a condom.</li\
>\
</ul>\
<p>We men have an excellent fallback system for\
flushing out the sluts. If we think you&#8217;ve been around\
,  we act as if we&#8217;re going to rawdog you,\
only to reach for the condom at the last possible second. If you haven\
&#8217;t reminded us to put one on during the long pre-\
penetration buildup,  and it looks like you&#8217;d have been OK\
taking our unwrapped meat,  we have all the evidence we need that you&#\
8217;re a skank.</p>\
<ul>\
<li>She\
never stops shit testing you.</li>\
</ul>\
<p>A\
girl who is constantly testing you for alpha congruency is a girl\
who would jump\
to another man the moment you betatize yourself. Worthy girls keep\
the shit testing\
to a bare minimum. Turn on your love light,  baby.</p>\
\
<ul>\
<li>She buys you a lot of gifts.</li\
>\
</ul>\
<p>I&#8217;m not sure why\
this is a leading indicator of sluttiness,  but in my experience it is.\
Especially if she showers you with little gifts early in the\
relationship. I open\
the floor to a discussion of theories for this particular observation.</p>\
<\
ul>\
<li>She&#8217;s OK with making out in\
bars.</li>\
</ul>\
<p>Self-explanatory.</p\
>\
<ul>\
<li>She lets you snort coke off her ass\
.</li>\
</ul>\
<p>Oh yeah,  big time slut\
.</p>\
<ul>\
<li>She&#8217;s black\
.</li>\
</ul>\
<p>Sorry,  folks,  hate to\
say it,  but going by my personal experience and what I&#8217;\
ve heard from friends,  black chicks seem to sleep around more. Don&#\
8217;t blame me,  I&#8217;m just the Deliverer Of\
Truths Best Left Unsaid But I&#8217;m Going To Say Anyhow.</\
p>\
<ul>\
<li>She has a lot of slutty friends\
.</li>\
</ul>\
<p>Ye shall know her by her\
support group.</p>\
<ul>\
<li>Her cunt is cavernous\
.</li>\
</ul>\
<p>Some of you wonder if this\
is an urban legend or a frat boy joke,  but it&#8217;\
s got a kernel of truth. If you feel big with most girls,\
but small with her (and she doesn&#8217;t have the excuse\
                    of being a seacow),  she has a stretched out pussy\
that has happily\
accommodated a parade of giant cocks. Why do you think Kegels are all the\
rage with the city slutterati? Chicks are onto the fact that their\
distended pussies\
betray their loose ways,  and anything to tighten up that love hole helps them\
hide their pecker pounded tracks. When I feel humongous with a girl,  I\
know she has a normal sized snatch that hasn&#8217;t been used\
like the town orifice. The more I feel like I&#8217;m\
ripping her insides to shreds,  the likelier I am to move her to the\
front of my cherished girlfriend queue.</p>\
<ul>\
<li>\
Your gut tells you she may be a slut.</li>\
</ul>\
\
<p>Always go with your gut. It will almost never lead you\
astray.</p>\
<p>****</p>\
<p>A lot of\
guys,  particularly artsy fartsy greater beta males whose agenda is to\
ingratiate themselves to\
women with a fawning act of white knighting nonjudgmentalism drivel,\
believe that it is\
wrong to categorize women by sluttiness,  let alone to disqualify\
them as relationship candidates\
based on how many hot loads to the face they took over the course of\
their sexually active lifetimes. &#8220;Don&#8217;t judge!&#\
8221; is the rallying cry of weak women and lickspittle betas and\
lesser alphas\
everywhere. Conveniently forgotten in this social stampede to shame\
male standards out of existence\
is the fact that judgement is inherent to human nature. The\
frontlines of judging\
eyes are everywhere. We all do it,  including those who judge others for\
exercising their judgement. If sluttiness were just another lifestyle\
choice with no implications,\
there would not be a stigma attached to the word,  nor a concerted effort\
to enforce compliance with the equalist world order by the guardians of\
female prerogative and\
pushers of beta male submission howling with inflamed passion at the\
injustice of men who\
dare to promote less promiscuous women at the expense of sluts for\
the best of\
their masculine love and attention.</p>\
<p><strong>Note:</\
strong> As a tactical matter,  it\
&#8217;s recommended to refrain\
from being judgemental of the sexual history of\
girls you are gaming. Naturally,\
you don&#8217;t want to\
deep six a budding romance before you\
&#8217;ve closed the deal.\
There will be plenty of time post\
-sex for you to take a measure\
of the girl&#8217;s\
sluttiness and screen her for lesser or greater\
commitment. I think this goes without\
saying,  but apparently there are some commenters\
who believe being completely nonjudgemental of anything\
a woman does is the mark of an\
alpha. In fact,  it&#\
8217;s just the opposite. Only\
alphas have the market value to mercilessly\
judge the women they choose to bring into\
their lives.</p>\
<p\
>Men subconsciously judge women&#8217;\
s sluttiness for eminently practical reasons,\
just as women judge men on a host\
of alpha benchmarks for similarly practical reasons\
. No moral equation required. &#8220\
;Slut&#8221; is,\
in fact,  a morally neutral term in\
the context of the sexual market,\
where a slutty girl is viewed,  justifiably\
,  desirably as an easy lay who\
will go all the way right away,\
and undesirably as a girlfriend or wife\
prospect in whom to invest precious resources.\
With the law and social institutions of\
the modern west arrayed against male interest as\
it hasn&#8217;t been in all of human history,  it is\
of critical importance that men get this part of choosing girls for <a href\
="https://heartiste.wordpress.com/2008/08/26/\
quality-girl/" target="_blank">long term investmest and wife and mother\
potential</a> down to a science. <a href="https://\
heartiste.wordpress.com/2008/03/11/mandatory-paternity\
-testing-has-arrived/" target="_blank">Mandatory paternity testing</\
a> will aid them in this,  and I predict such testing will seismically\
shift the playing field in a way we haven&#8217;t seen since\
the introduction of the pill and widespread use of the condom.\
While most married\
men are not soulkilled by cuckoldry,  it only takes a radical change at the\
margins to have a huge effect on the behaviors of the whole.</p>\
\
<p>For those of you new to the Wonderworks that is Poon,\
don&#8217;t bother bitching ineffectually like a wind-up Jezebel lezbot\
about &#8220;<a href="https://heartiste.wordpress.com/\
2007/04/13/double-standards/" target="_blank">double\
standards</a>&#8220;. They are a fact of deeply ingrained sex differences\
,  and aren&#8217;t going anywhere. No one said life was\
fair.</p>\
<p><strong>Maxim #41: The more\
experience you have with women,  the more you&#8217;ll know which\
women have experience with men.</strong></p>\
<p><strong>\
Corollary to #41: It is the inexperienced beta male who is most often\
in the dark about a woman&#8217;s sexual history and liable to\
be victimized by the cheating slut.</strong></p>\
<p>The\
<a href="http://www.physorg.com/news10824.html\
" target="_blank">median number of sex partners</a> for American\
women is 3(!). The average is 8.6. This means that there\
is a group of super slutty women,  let&#8217;s call them\
&#8220;girls who live in the big blue coastal cities and work in\
marketing or PR&#8221;,  who are shifting the average higher for all women\
. By these numbers,  it is fair to conclude that a woman who has\
had more than the median number of partners is a candidate for\
slut designation,\
and the higher her number the sluttier she is.</p>\
<p>\
0 lifetime partners: Sweet virginal manna. A bit weird,  but you&#\
8217;re confident you&#8217;ll break her in.<br />\
\
3 lifetime partners: Typical woman. Wife and mother of your\
children material.<\
br />\
10 lifetime partners: Above average. Proceed with caution.<br />\
\
15 lifetime partners: Well above average. Be dominant or she&#8217;\
ll cheat.<br />\
25 lifetime partners: A whole lot. Use her\
and lose her.<br />\
100 lifetime partners: Stopwatch material. You wonder\
how fast you can get her from &#8220;Hi&#8221; to\
&#8220;Spread your ass cheeks,  I&#8217;m going in\
&#8221;.</p>\
<p>I suspect that overall female sluttiness (\
    actual penis in vagina sluttiness,  not sluttiness as defined by\
    proxy fashion trends\
) has increased slightly over the past 40 years,  with the blue state city\
chicks fucking around more than ever and the red state religious girls\
fucking around less\
. It goes without saying that only the top 20% of men are enjoying\
the emergent slut bounty.</p>\
<p>What men think about sluts\
,  illustrated:</p>
'


c12 = epub.EpubHtml(title='jobs ',
file_name='jobs.xhtml',
lang='en')
c12.content='\
<h2>What a Girl''s Job Tells You</h2>\
<p>Here are my opinions of the sexual and relationship\
compatibilities of girls\
with the following jobs:</p>\
<p><strong>ADDENDUM:</strong\
><br />\
Some of the commenters mentioned I left interns and staffers off the\
list.  I count these girls as part of the hr/marketing/pr\
brigade except they are burdened with much bigger egos,\
self-righteousness,  and\
workaholic issues.  They all secretly want to hook up with an\
older powerful man\
.  They disdain artist types.<br />\
<em>SSR:  full erection\
(come on,  they&#8217;re all under 23. rigidity guaranteed\
 )<br />\
LTPR:  varies (are you a congressman? lock her\
               in. if not,  use her and lose her)</em></p\
>\
<p>It was an oversight by me to leave off saleswomen.\
See: Lawyer and HR/Marketing/PR.  Much depends on how well\
she does in sales.  Because sales is so inegalitarian in how the\
field dispenses\
its rewards,  you have to make a distinction between weekend\
warriors and the true\
success stories.  Is she a dilettante real estate agent?  She&#8217;\
ll be grounded and feminine.  Consider a long term investment in her.  Did\
she turn $250K in commissions as a pharm sales rep?  She&#8217\
;s just as alpha and ballcutting masculine as the BIGLAW lawyer.\
Just remember\
,  if she can compete with the most aggressive MEN and still come out on\
top,  her vagina is coated with radioactive juices.</p>\
<p>\
Note on lawyers:  Just because she may work for a non-profit doesn\
&#8217;t make her a kinder,  gentler woman.  In fact,\
some of the most cutthroat lawyers work at non-profits since\
those positions are\
in demand and in short supply.  Moralism and megalomania is\
never a good combination\
.</p>\
<p><strong>Lawyer</strong></p>\
<\
p>Amoral alpha males with vaginas.  Their yin is so deeply buried they\
spend all their free time (2 hours per week) fantasizing about a powerful\
dominant man releasing their inner woman.  This is your cue to ratchet up the\
assholery.  Outside of i-bankers and fashionistas,  you will not meet a\
more materialistic or status-conscious chick than a lawyer.  When she\
inevitably starts\
talking about what law school she attended and politicos she knows,\
put your finger\
up to her mouth and say <em>&#8220;shhh&#8230;\
stop.  from now on we will talk about happy things.  tell me only\
the good things that come to mind about your childhood.&#8221;</em>\
Most lawyer chicks have large clits which they use to pin you down on the\
bed.  Making love to a lawyer means facefucking her till she pukes a little\
.  The gods of karmic retribution will be pleased with this.  Lawyers\
are always\
fucking over everyone else so this is your chance to return\
the favor.  Proceed\
with great relish.<br />\
<em>Sexual Satisfaction Rating:  4/\
5th erection<br />\
Long Term Potential Rating:  don&#8217;t\
be a masochist</em></p>\
<p><strong>Human Resources\
/Marketing/Public Relations (99% of all women)</strong></p\
>\
<p>Since so many women work in these preposterous fields,  it\
is hard to say anything definitive about them as romantic partners.\
The only conclusions\
we can draw are that these women are people-persons (shocker!) and\
have ADD.  They could not sit still for a minute and reduce a fraction\
if their lives depended on it.  They are intuitive and fiercely catty,  but\
also practical.  In fact,  conventional wisdom to the contrary\
notwithstanding,  women are\
more practical than men.  Let her believe you think her job is important and\
she will spread her legs for you unbidden.<br />\
<em>Sexual\
Satisfaction Rating:  2/3rd erection<br />\
Long Term Potential Rating:\
    3/4 carat</em></p>\
<p><strong>\
Engineer (0.00001% of all women)</strong></p>\
<\
p>If there was ever an occupation created solely for the benefit of a\
man&#8217;s intellectual strengths,  engineering is it.  So right off\
the bat you know that any female engineer will be weird.  Not\
necessarily assertively\
masculine like the female lawyer,  but not typically feminine either.\
Female engineers are\
the Holy Grail of male nerddom.  Every nerdo anime fanboy\
with Dungeon Master on\
his resume dreams of meeting and falling in love with a cute nerdgirl WHO IS\
EXACTLY LIKE HIM so that his autistic social retardation doesn&#8217;t get\
pushed to the breaking point like it would with a normal girl.<br />\
\
Minus: fornication mysteriously happens in between lengthy dissertations\
on string theory.<br />\
Plus: she can assume sex positions within a millimeter of spec.<br />\
<em>Sexual Satisfaction Rating:  1/4th erection<br />\
Long\
Term Potential Rating:  5 carats</em></p>\
<p><strong\
>Elementary School Teacher</strong></p>\
<p>Pure gold.\
Put this girl on your short list for long term commitment.  What&#8217\
;s not to love about the elementary school teacher?  Cute,  thin (\
it&#8217;s a workout chasing kids all day),  ultra feminine\
,  nurturing,  selfless,  caring,  and most importantly blessedly\
    low maintenance due\
to the nature of her workplace environment sequestering her from the\
    attentions of men\
.  The best ones teach 1st through 5th grades.  Women who supervise daycare\
are too toddler-focused and will love the kids more than you.\
You will soon tire of her coo-ing at every baby you both\
pass by.  High school teachers are too stressed out from their job to\
properly service your manly needs at home.  Don&#8217;t bother\
with college professors unless you think foreplay is listening to an\
    earful of pomo\
feminist shrillness.<br />\
Bonus:  teachers don&#8217;t make\
much money so your financial status will always be higher,  guaranteeing a long\
and healthy relationship.<br />\
<em>Sexual Satisfaction Rating:  3\
/4th erection<br />\
Long Term Potential Rating:  hope diamond (\
she&#8217;s not gonna have much opportunity to cheat at work\
)</em></p>\
<p><strong>Nurse</strong></p\
>\
<p>See:  elementary school teacher.  One caveat &#8212\
; the nurse is secretly a status whore.  Patients lean on her all\
day for comfort and assistance so when she gets home she wants nothing more\
for herself than a high status alpha male to lean on.  That is\
why you will often see nurses pairing up with military officers,\
    stockbrokers,\
and executives.  The superfeminine gravitates to the supermasculine.\
    Surprisingly,  nurses and\
doctors rarely date &#8212; perhaps they look for a partner in whom\
they can escape the human suffering they deal with on the clock,  and\
not be reminded of it at home.<br />\
<em>Sexual\
Satisfaction Rating:  1/3rd erection (full erection if she wears the\
nurse outfit)<br />\
Long Term Potential Rating:  cubic zirconia (it\
&#8217;s fun to fool status whores)</em></p>\
<p><strong>Scientist</strong></p>\
<p>\
Hidden gem.  The female scientist is reserved,  taciturn,  introspective,  shy\
,  and when they put some effort into how they look,  cute &#\
8212; all wonderful traits for a woman to possess.  They ambitiously pursue\
abstract ideas,  not material goals or oneupsmanship,  so status\
                                             competition with them\
will be minimal.  They are smart in the way people like their smarties\
&#8212; inwardly directed as opposed to outwardly manipulative.  This is a\
result of their smarts being spread out over both brain hemispheres\
                                             rather than concentrated\
in just the right like most women.  The scientist&#8217;s\
natural creativity and systematizing impulse will express itself with\
                                        magnificent attention to detail in\
the bedroom.  You will never get a better&#8230; or more\
meticulous&#8230; blowjob.<br />\
Minus:  she is ultimately rational\
and will give you exactly six months to propose.  No stringing along this\
chick.<br />\
<em>Sexual Satisfaction Rating:  serviceable chubby<\
br />\
Long Term Potential Rating:  3 carats  (frumpy clothes and dorky\
competition encourage fidelity)</em></p>\
<p><strong>Stripper\
</strong></p>\
<p>Have you ever seen an unhappy\
man dating a stripper?  The novelty,  bragging rights,  and earthshattering sex\
are worth the drama.<br />\
<em>Sexual Satisfaction Rating:\
titanium rod<br />\
Long Term Potential Rating:  hide your valuables</\
em></p>\
<p><strong>Journalist</strong></p\
>\
<p>Don&#8217;t ask me why but for\
some reason these girls have absolutely no personal ethical code\
                                             whatsoever.  Which may\
be why the journalism profession is in such disarray today and trusted by no\
one.  The she-journo will fuck around remorselessly with a dashing embed\
while her fiancee waits loyally at home for her return.<br />\
<\
em>Sexual Satisfaction Rating:  3/4th erection<br />\
Long\
Term Potential Rating:  1/24 carat</em></p>\
<\
p><strong>Artist</strong></p>\
<p>Every man\
should experience at least once in his life the joy of dating an artist chick\
.  Painters,  photographers,  singers,  freelance fiction writers,\
                                             actresses&#8230;\
their exuberant lovemaking will spoil you for all other women.\
                                    Their beautiful romantic gestures\
will capture your heart.  Their craving for intimacy and their\
wellspring of empathy will\
draw you in.  And then right at the moment you fall deepest for her\
you will catch her one night frenching a half-shaven DJ at a seedy\
club.<br />\
<em>Sexual Satisfaction Rating:  titanium rod minus refractory\
period<br />\
Long Term Potential Rating:  cracker jack box ring</em\
></p>\
<p><strong>CEO</strong></p>\
<\
p>Are you fucking kidding me?<br />\
<em>Sexual Satisfaction\
Rating:  flaccid<br />\
Long Term Potential Rating:  why bother?</em\
></p>\
<p><strong>Waitress</strong></p>\
<\
p>That&#8217;s more like it.<br />\
<em\
>Sexual Satisfaction Rating:  7/8th erection<br />\
Long Term Potential\
Rating:  1/2 carat</em></p>\
<p><strong\
>Blogger</strong></p>\
<p>If she writes a confessional\
online diary,  expect her to be passive-aggressive,  petty,  moody,\
cruel,  untrustworthy,  vengeful,  and highly libidinous.  Make a sex tape as\
soon as it is feasible so you can use it as blackmail in the event\
of post-breakup threats to out your dirty laundry on her blog.<br\
/>\
<em>Sexual Satisfaction Rating:  N/A<br />\
Long\
Term Potential Rating:  N/A</em></p>\
<p>\
I hope it hasn&#8217;t escaped anyone&#8217;s notice\
that sexual satisfaction and long term potential are inversely related.</p>
'

c13 = epub.EpubHtml(title='friends',
file_name='friends.xhtml',
lang='en')
c13.content='\
<h2>Judging A Girl By The Friends She Keeps\
</h2>\
<p>When you start dating a girl,  you will\
get to meet her friends,  sometimes sooner,  sometimes later. But\
usually within\
the first couple of months you will have been introduced to\
nearly everyone she knows\
(locally),  especially if she really likes you. Pay close attention to the\
types of friends she has (if she has any),  for that will tell\
you a lot about her long term potential. Screening a girl for LTR worthiness\
based on the friendships she keeps is a powerful tool men have\
at their disposal\
,  and one you should not overlook.</p>\
<p>The following\
categories are ranked by LTR worthiness and chance of mental instability.</p>\
<\
p><span style="text-decoration:underline;"><strong>The Girl\
with No Friends</strong></span><br />\
LTR worthiness: Short but\
passionate fling<br />\
Chance of mental instability: Sleep with one eye open\
</p>\
<p>A girl with no friends likely has some personality\
defect that prevents her from forming bonds with people. Other\
girls regard her as\
a weirdo,  and not without justification. Men think her social\
isolation means she\
will be an easy lay. They are right. This kind of girl is\
starved for human connection with a man who &#8220;gets her&#8221\
;. Hit those buttons,  and you will enjoy a three month festival of zero\
-cost fornication. After a while,  though,  her weirdness will grate,\
and she will pull stunts that make you scratch your head in confusion. Girls\
with no friends are often brooding emo types,  or <a href="https\
://heartiste.wordpress.com/2011/07/15/cutter-\
lover/" target="_blank">cutters</a>,  and they may go batshit\
crazy if you dump them. Have a restraining order ready.</p>\
<\
p><span style="text-decoration:underline;"><strong>The Girl\
with No Close Friends,  Only Acquaintances</strong></span><br />\
LTR\
worthiness: Pump and dump<br />\
Chance of mental instability: Hope you\
like drama</p>\
<p>The classic attention whore. The girl\
with nothing but loose acquaintances who flit in and out of her\
life craves the\
attention of hundreds,  if not thousands,  of human beings. She is usually\
a hot chick with a swollen ego who initially attracts girls into her\
reality for\
friendship,  but who then drives them away with her insatiable\
appetite for social domination\
and ego stroking. She is a known blue ball queen who gets off stringing\
along beta orbiters in sexless perpetuity. She is simultaneously\
loved and loathed by her\
girlfriends,  who find her outrageous fun at parties,  but\
insufferable in more intimate\
settings. She is frequently bad-mouthed behind her back,  and she presents\
one of the few cases where girl friends will sympathize more with\
her male suitors\
and boyfriends than they will with her. She is a high infidelity risk,\
so proceed with caution. Best used as a sperm receptacle,  if you can\
get her to give it up (not an easy task unless you know how\
to expose her soft underbelly &#8212; fear of ostracization.)</p>\
\
<p><span style="text-decoration:underline;"><strong>\
The Girl with Only Family for Friends</strong></span><br />\
\
LTR worthiness: Perennial booty call<br />\
Chance of mental instability:\
Riddled with insecurities</p>\
<p>On paper,  a girl\
who only has her family for companionship may strike you as a good LTR\
prospect. You think: Ah,  she&#8217;s grounded,\
earthy,  family-oriented,  and shuns the nightlife. But you would\
be wrong. As any man who has married a &#8220;family\
-only&#8221; girl will tell you,  they are demanding,\
mule-headed,  socially awkward,  often obnoxious and full of themselves.\
Remember,  she&#8217;s had her family telling her how great\
she is her whole life,  with no unbiased opinion from outside\
                       sources checking\
her ego. She is,  in fact,  not much different than the\
girl with no friends,  except she has decided that leaning on her family\
for support and ego gratification is better than being alone.\
                       Other girls find\
her annoying at best,  and arrogantly repugnant at worst,  and that is\
why she must retreat to the comfortable confines of family for\
                       her social needs\
.</p>\
<p>The no-friends girl at least has\
the cutesy artist angle to work; the family-only girl has nothing\
to offer but an unjustified entitlement complex. She is the classic daddy&#\
8217;s slutty princess. The family girl instinctually knows this about herself\
,  and thus will nurse barely-concealed insecurities about her true worth,\
which she will take out on you,  making your life miserable. Double\
-plus negative: You&#8217;ve gotta deal with her parents\
,  brothers and sisters ALL THE TIME. Run away (after you&#\
8217;ve plundered her ass.)</p>\
<p><span style\
="text-decoration:underline;"><strong>The Girl with Only Guy\
Friends</strong></span><br />\
LTR worthiness:  Second string girlfriend\
<br />\
Chance of mental instability: High,  if you regard manipulation\
and tomboyishness as psychological disorders</p>\
<p>What do you\
get when you surround a girl with obsequious,  supplicating betas who want in\
her panties,  and remove all contact with catty girl friends who might steal\
the attention of those mewling betas? Yeah,  that&#8217;s\
right&#8230; a self-centered user. If the girl is\
cute,  you should always cast a jaundiced eye at her if her friends\
are all men. Odds are very good that most of those men&#\
8230; actually,  all of them&#8230; want to bang her\
(and she knows this). But they aren&#8217;t.\
Their job is to mingle in her glorious presence,  polishing her pedestal and\
generally turning her into a girl who expects men to roll out the red\
carpet for her. She is the classic cocktease. She loves the intimate emotional\
connection she gets from a close circle of male friends,  without having\
to give\
up her pussy to any of them or having to deal with competitor females.\
Now you may be the most alpha alpha male of all times,  and she\
may love you for it,  but once a girl has demonstrated by her friendship\
choices that she is a user,  there will come a time,  you can\
count on it,  that she will try to use you. It&#8217\
;s best to keep her in your second tier of lovers,  where her\
machinations won&#8217;t affect you with nearly as much import.</p\
>\
<p>Caveat: If she&#8217;s plain looking and\
has mostly male friends,  the upside of her having a well-developed sympathy\
for men&#8217;s peculiar challenges outweighs the downside of her having her\
ego stroked and her emotional needs met all the time by her male friends.\
All the better if most of her male friends are alphas themselves who are in\
relationships and who don&#8217;t spend inordinate time massaging her ego.\
But then why are you dating a plain-looking girl?</p>\
<\
p><span style="text-decoration:underline;"><strong>The Girl\
with Mostly Gay Guy Friends</strong></span><br />\
LTR worthiness:\
    One night stand<br />\
Chance of mental instability: She gets her own DSM edition</p>\
<p>Same as above,  except multiplied one thousand fold. A big\
unwritten story about the decline of the West is the deleterious\
impact trendy gay men\
have had on the egos of single urban Western SWPL women. If you can\
imagine it,  try to picture her as nothing more than a\
disembodied vaginal hole\
. It will help keep a healthy emotional distance. A few gay guy friends\
is perfectly fine. Ten of them,  to the exclusion of other groups of\
friends,  is a red flag.</p>\
<p><span style="\
text-decoration:underline;"><strong>The Girl with Only Girl Friends<\
strong></span><br />\
LTR potential: High,  if you like lavish\
weddings<br />\
Chance of mental instability: Not more than the average girl\
,  which is to say,  high</p>\
<p>The good\
news about the girl with only girl friends is that she is normal and feminine\
. She likes doing girly stuff,  and if you are a real man and\
not a spotted-ass nerd with a jones for a butt-kicking babe\
who solves math proofs in her downtime,  then you will appreciate\
being the boyfriend\
of this type of socially calibrated and psychologically\
balanced girl. There&#8217;\
s nothing wrong with dating a girl who,  you know,  ACTS LIKE A\
GIRL. Another plus: she doesn&#8217;t require the ministrations of\
hordes of beta male taintlickers to keep her from downward\
spiraling into depression.</p\
>\
<p>The bad news should be obvious: she has no concept\
of what men must endure in either the dating market or the social market in\
general. Thus,  her sympathy for men is nil,  and she comes across\
solipsistic and self-absorbed. But she will happily bend to the will of\
a strong man,  because she does not shun her female nature. She makes\
a great girlfriend; a wife,  though,  is an entirely different matter.\
That same group of supportive single girl friends who loved you as\
her boyfriend will\
tirelessly work to undermine your marriage should they themselves remain in\
the purgatory of singledom\
.</p>\
<p><span style="text-decoration:underline;"><\
strong>The Girl with Only Lesbian Friends</strong></span></p>\
\
<p>*Doesn&#8217;t exist in the state of nature.*</\
p>\
<p><span style="text-decoration:underline;"><strong\
>The Girl with a Mixed Group of Girl and Guy Friends</strong></\
span><br />\
LTR potential: Be careful,  your player days might be\
over with her!<br />\
Chance of mental instability: She makes most girls\
seem like candidates for institutionalization</p>\
<p>And here we have\
the ideal girl,  if LTRs are your thing. (Note: If same\
night lays are your thing,  she is NOT the ideal girl.) She\
is open-minded and humble enough to enjoy the company of a variety of\
friends with strong opinions,  she has enough femininity to relish\
time with girl friends\
,  and she has enough exposure to guy friends that she can\
sympathize with their\
concerns. Ideal scenario: her girl and guy friends are all in\
relationships of\
their own. This limits the cattiness and the beta orbiter supplication\
to a manageable\
level.</p>\
<p>A girl who maintains an attractive humility and\
who respects the wishes and the laments of men is a girl who is emotionally\
secure enough to not just tolerate,  but embrace,  the company of both girl\
friends and guy friends. She loves people for who they are,  and not\
for what they can do for her ego.</p>\
<p><span\
style="text-decoration:underline;"><strong>The Girl with One or\
Two Player Friends</strong></span><br />\
LTR potential: bimonthly tests\
for STDs,  OR GF material<br />\
Chance of mental instability: She\
&#8217;s not crazy,  she&#8217;s creative!</p>\
<p>If a girl spends a lot of time with either a Samantha\
-type slut or a Hitch-like player,  she&#8217;s\
got hang-ups about her sexuality and her dating market value worth. She\
wants to live vicariously through their exploits because she herself\
lives a rather modest life\
,  or she IS like them and enjoys being with people who live and think\
just as she does. If the former,  she might be redeemable with enough\
LTR game. If the latter,  there&#8217;s a good chance\
that eerie suspicion you had that she was getting pounded by another\
cock last Thursday\
was true.</p>\
<p>Major red flag: Double all her\
slut points if the time she spends with the player or the slut is over\
Sunday brunch at a tapas restaurant,  getting drunk on mimosas.</p>\
<\
p>***</p>\
<p>My hope with this post is to impress\
upon the male reader the importance of not only screening girls\
for LTR potential,\
but of winning over a girl&#8217;s friends,  man or woman\
,  if you intend to date her beyond the customary three weeks. While it\
appeals to a certain renegade male mindset to boff a girl and pay no heed\
to her extraneous social life,  it&#8217;s always better to have\
her friends on the inside of the tent pissing out,  than outside pissing in\
. Girls,  being the lemming sex,  rely more heavily than men do on\
the judgment of their friends&#8217; opinions about their boyfriends. If she\
is someone you could date for the long haul,  best to befriend her social\
circle eagerly. If nothing else,  you have neutralized any future\
sabotage. More\
likely,  you have made a new group of friends. And if your girlfriend\
is cool,  then the solid bet is that her friends are cool,  too\
.</p>\
'


c14 = epub.EpubHtml(title='age brackets',
file_name='age_brackets.xhtml',
lang='en')
c14.content='\
<h2>The Difficulty of Gaming Women by Age Bracket</h2>\
<\
p>The following observations apply to established adult men,\
post college years.\
Younger men still in college will find their success rate with\
women of various ages\
,  particularly older women (aka cougars),  highly variable.\
The rules for them\
will be different than the rules for older men.</p>\
<p><\
strong><span style="text-decoration:underline;">18 to 22 year\
olds</span></strong></p>\
<p>Hard to believe,\
but it is often easier to bed a very young woman than an older woman\
,  if you are an older man. This is because 20-40%\
of women are specifically attracted to older men. It is hard-wired in\
them,  and this hard-wiring can be reinforced by poor\
family upbringing resulting\
from divorce of parents or absentee fathers. Single moms are\
the greatest source of\
future generations of slutty daughters the world has ever known.</p>\
<p\
>Your goal is to identify which 18-21 year olds are amenable to\
being seduced by you. Since a majority will balk at the idea,  you\
should learn to quickly identify and NEXT! them. Thankfully,  most girls aren\
&#8217;t brazen cockteases,  and will make their lack of interest known\
early on. Beware,  though,  that a small minority of barely legal rapacious\
golddiggers will try to keep you on tenterhooks,  extracting\
your resources for little in\
return. A simple <a href="https://heartiste.wordpress.com\
/2008/09/16/how-to-handle-femmes-\
fatales/" target="_blank">preemptive qualification</a> should suffice to smoke\
them out.</p>\
<p>You can bang an 18-21\
year old surprisingly quickly because they have little ASD\
(anti-slut defense).\
This is because they do not have the long history of\
sluttiness common to older\
women which needs to be rationalized away by posturing as a paragon\
 of chaste virtue\
. A young woman simply won&#8217;t perceive sex with you as\
an admission of sluttiness. She is innocent to herself as well as to you\
. Plus,  actual slutty behavior has been defined down so that\
five partners today\
is equivalent to one partner thirty years ago.</p>\
<p>Caveat\
to the above: although you can get the bang with an 18-21\
year old very quickly,  you should not prime the path to banging with obvious\
signs of physical escalation. There is a high risk with very young women that\
escalating kino will be perceived as &#8220;pervy&#8221; or &#\
8220;creepy&#8221;. This means no PDA,  no &#8220;\
innocent&#8221; touching of her erogenous zones,  and no raunchy sex talk\
. You want to keep it on the superficial friend tip until she is in\
your place. Then you should escalate rapidly. You&#8217;d be\
amazed how fast the young woman sheds her clothes when the bang is in sight\
. Very little foreplay is required. The sex will be,  as you can\
imagine,  the <a href="https://heartiste.wordpress.com/\
2007/08/30/hotter-women-better-sex/" target\
="_blank">hottest you will ever have</a>.</p>\
<p\
>DO NOT EVER &#8220;DATE&#8221; an 18-21\
year old. Women under 23 don&#8217;t date,  they &#\
8220;hang out&#8221;. Anything that remotely smacks of a date &#\
8212; drinks at a lounge,  dinner for two,  day trips to a\
museum &#8212; will scare her off. The under-23 young woman\
cannot handle the &#8220;seriousness&#8221; of a dating context.\
This is the reality of modern America. &#8220;Dating&#8221;\
makes younger women think &#8220;no fun,  marriage,  kids,  pressure\
,  relationships,  stuff that older people do&#8221;. You need to be\
so chill that you&#8217;re barely motivated to do anything proactive with\
her. Instead,  &#8220;hang out&#8221; with her in\
a neutral context. Walks along window-browsing streets are good for this.\
So is meeting at a local park and talking while goofing off on the swings\
. You can take her to a coffee shop as long as you don&#\
8217;t buy anything.</p>\
<p>DON&#8217;\
T BE LAME. If a 19 year old (true story) offers you\
an E tab in a dark corner of a loud club at 1 am,\
don&#8217;t refuse her like some boring fuddy duddy. Either pop\
that baby and enjoy the ride,  or pretend to take it and throw it\
away when she&#8217;s not looking if you&#8217;re\
suspicious of the pill&#8217;s origins and purity. Push for a\
blowjob in the alley behind the club; plans to make future dates are a\
fool&#8217;s errand.</p>\
<p>DON&#8217\
;T BE HER DAD. Contrary to popular misconception,  most young women don\
&#8217;t want to date a father figure. They DO want to\
date a strong dominant man,  and older men bring that demeanor to the table\
. This is why it is better to dress youthfully (if you are in\
shape) rather than in a sharp suit and tie if it&#8217\
;s much younger women you want to meet. A notable minority of younger\
women love the business suit look,  but most of them,  especially the ones\
on the fence about dating older men,  would feel more\
comfortable if you projected\
an aura of youthfulness through your dress and attitude.</p>\
<p><\
strong><span style="text-decoration:underline;">23 to 27 year\
olds</span></strong></p>\
<p>Similar to the 18\
-22 year olds in terms of difficulty of picking up,  with some important\
differences. The 23-27 year old feels she is at her attractiveness peak\
,  despite her peak having passed a few years earlier. This is because she\
is surrounded by many more high status men than she was while in college (\
    or working at the Piggly Wiggly) who are expressing sexual interest in her\
. This social dynamic will work to inflate her ego beyond the bounds of her\
actual beauty ranking. Some consequences result from this.</p>\
<p>\
NEG HARDER. The 23-27 year old will require harder negging than any\
other age group of women,  even the hotter 18 year olds. She needs\
her ego punctured before her pussy will open for you.\
Remember that cherished maxim\
:</p>\
<p><strong>Maxim #23: The defensive crouch\
is where pussy tingles are born</strong>.</p>\
<p>DEFY\
EXPECTATIONS. She expects you to pay her way and play the role of earnest\
suitor. You can&#8217;t &#8220;hang out&#8221\
; with the 23-27 year old like you should with the 18-\
22 year old without staining yourself with the immaturity label,\
but you shouldn&#\
8217;t fall into her trap of arid,  sexless dating either. Arrange\
dates that are simple and logistically favorable. Never spend\
 more than two drinks&#\
8217; worth of money on her on a single date.</p>\
<\
p>DATE CONCURRENTLY. The 23-27 is,  arguably,  the most\
in-demand woman on the market. Various social factors account for this,\
which will be the subject of another post. Thus,  she will have the\
greatest self-regard. Despite your best game,  you may find yourself getting\
flaked on by a girl in this age range. A good defense is a\
solid offense,  so minimize the creep of neediness and\
desperation by dating many women\
at once. Do not feel guilt about fucking multiple women concurrently.</p>\
\
<p>THIS IS YOUR SWEET SPOT FOR GAME. No other woman will\
react as positively to hardcore game as the 23-27 year old. She\
and her sisters will be throwing meatballs at the middle of your lineup. Aim\
for the fences.</p>\
<p><strong><span style="text\
-decoration:underline;">28 to 30 year olds</span></strong></\
p>\
<p>Finally,  the female ego suffers chinks in its armor\
. She will try hard to cover these cracks,  but they&#8217;\
ll creep out here and there. 30 is a huge and depressing milestone for\
women,  but 29 is an even more depressing birthday. It is the &#\
8220;last hurrah&#8221;,  so to speak,  and the number taunts\
her daily with reminders of her impending obsolescence. A\
single girl who was dumped\
by her boyfriend and who has just turned 29 may be the easiest girl in\
the world to lay. You will still need to game her,  but the\
path to sex will be exhilaratingly fast and furious.</p>\
<p>\
28-30 year olds are a mixed bunch. Some are riding a wave\
of career and social success that has nowhere to go but down,  and their\
bloated egos reflect that. Others,  less conventionally\
successful,  are emotionally frazzled by\
the disappearing act of their heady youth and by\
the intractability of their singledom.\
You will find some of the cuntiest,  and sweetest,  girls in this age\
range.</p>\
<p>Same rules as the ones for 23-\
27 year olds apply to 28-30 year olds,  with the exception that\
negging should be tailored to the life success as well as the looks of the\
girl you are gaming. A 30 year old businesswoman is often harder to game\
than a 20 year old hipster. She will need subtle reminders that her beauty\
isn&#8217;t what it once was.</p>\
<p><\
strong><span style="text-decoration:underline;">31 to 34 year\
olds</span></strong></p>\
<p>In some ways,\
women in the 31-34 age range are the toughest broads to game.\
(By &#8220;toughest&#8221;,  it is meant &#8220;\
 most time consuming&#8221;.) It&#8217;s counterintuitive,  yes\
 ,  but there are factors at work besides\
 her declining beauty which mitigate against\
 the easy,  quick lay. For one,  it is obviously harder to\
 meet single 31-34 year old women than it is to meet single\
 younger women. Marriage is still a pussy-limiting force to contend with\
 for the inveterate womanizer,  but Chateau apprentices are hard\
  at work battling the\
 scourge of mating market disturbances caused by the grinding and\
  churning of the marriage\
 machine.</p>\
<p>But the bigger reason 31-34\
 year olds are harder to game than any other age group of women has\
 to do with the wicked nexus of entitlement and\
 self-preservation that occurs\
 at this age in women. When you combine a disproportionate\
sense of entitlement\
 fueled by years of feminism,  steady paychecks and\
 promotions,  and cheerleading <\
 a href="https://heartiste.wordpress.com/2009/04\
 /20/your-gay-doom/" target="_blank">gay\
 boyfriends</a> with suspicions of every man&#8217;s motives\
 and a terrible anxiety of being used for a\
  sexual fling sans marriage proposal\
 ,  you get a venom-spitting malevolent demoness on guard against anything she\
 might perceive as less than total subjugation to her craving for\
 incessant flattery and\
 princess pedestaling.</p>\
<p>Note that Chateau guests aren&#\
 8217;t necessarily complaining. A harder-to-game 33 year\
 old is kind of like getting bumped down from a Honda Civic rental but\
 driving off the lot with the consolation prize of a Ferrari.</p>\
\
 <p>Listen to any man who is good with women and they\
 will tell you the same thing:</p>\
<p>&#8220;\
 I have an easier time bedding and dating 23 year olds than I do\
 33 year olds.&#8221;</p>\
<p>This defies all\
 logic until you see it through the eyes of the hamster sweating its fluffy\
 ass off in a woman&#8217;s brain. (Poor little\
 creature must be pooped out by the mid-30s.) Sure,  a\
33 year old is not as hot as the 23 year old version of herself\
,  but her ASD is through the roof,  as is her self-conception\
as a hot marriage-worthy commodity. Many older women will tell themselves that\
their experience,  maturity,  accomplishments and financial stability mean\
they should be way more\
valuable to men seeking wives than some young babe on the take. Of course\
,  they have to tell themselves this because reality isn&#8217;t making\
it easy to believe.</p>\
<p>These are the kind of\
women who have sexual flings with college guys,  because they\
can psychologically box those\
men in as &#8220;purely for fun&#8221; adventures. But\
the men the 31-34 year old women really want are the older,\
established men who will give them a marriage proposal and a family. This is\
why it is counterintuitively harder to game the older woman who\
still retains a vestige\
of her youthful attractiveness: she wants and expects so much\
more than the younger\
woman.</p>\
<p>Game required: Strong body language,  masculine\
dominance,  sharp suits and shoes,  easy on the negs and palm reading,\
emphasis on the comfort stage,  lots of travel stories,\
disqualify yourself from sex\
on the first date,  <a href="https://heartiste.wordpress.\
com/2009/01/29/vulnerability-game/" target="_blank\
">vulnerability game</a>,  avoidance of the beta provider zone.</p>\
\
<p>In short,  if you can present yourself to her as different\
than the indistinguishable mass of sad schlumpy <a href="https://heartiste.\
wordpress.com/2010/05/19/beta-or-herb\
/" target="_blank">beta herbs</a> who are her typical choice\
in available men,  then you are guaranteed the lay. Just don&#8217\
;t expect to sleep with her on the first night. She will work\
hard to make your seduction as difficult and drawn out as possible.</p>\
\
<p>Note: DO NOT SPEAK OF THE YOUNGER WOMEN YOU DATE to\
an older woman. You will be tempted to do this to demonstrate your higher\
value,  but instead she will withdraw so fast into her ego-preserving turtle\
shell that no game will redeem the pickup. If the subject comes up,\
just tell her you&#8217;ve &#8220;dated many interesting women\
&#8221; and leave it at that.</p>\
<p><strong\
><span style="text-decoration:underline;">35 year olds</span\
></strong></p>\
<p>This age gets a special mention.\
Why? Because 35 is the year of formal female expiration. (Informal expiration\
can occur many years later,  depending on the woman&#8217;s\
genetic\
good luck.) At 35,  most women are over the hill.\
An\
unmarried woman at 35 is officially in crisis mode. Full meltdown will happen\
within\
the year if she isn&#8217;t hitched in that time.\
You\
do not want to be in the vicinity of a woman in full meltdown mode\
. Full meltdown is accompanied by the acquisition of a second\
cat,  alcoholism,\
cackling brunches of mimosas with equally pathetic Samantha wannabes,\
sloppy drunken one night stands\
with college age men which they will then rationalize as evidence\
of their enduring beauty\
,  and a laundry list of annoying personality tics and neuroses that\
would comfortably provide\
for the retirement plans of ten psychotherapists.</p>\
<p>Game required\
: &#8220;Hi&#8221;.</p>\
<p><strong><\
span style="text-decoration:underline;">36 to 38 year olds</\
span></strong></p>\
<p>She is at peace with her\
spinsterhood and her failure in the dating market. She will acquiesce\
easily and gratefully\
to sex with very little game,  as long as you don&#8217;\
t look like a grandpa. Her expectations are so low,  it will be\
a challenge to disappoint her.</p>\
<p>If you are prone\
to guilt,  you might feel it when you inevitably dump a woman in this\
age range. Don&#8217;t. Remind yourself that her past is\
littered with her insouciant dumping of many beta\
men before you. You are merely\
an alpha agent of righteous karma.</p>\
<p>A Chateau proprietor\
once dated a European 37 year old for a couple of months. She looked\
years younger than her age,  so the sex was fun and the time together\
was relaxed,  but everything was glazed with a tint of sadness. A vow\
was made never to go much above 30 again.  So far,  the vow\
remains unbroken.</p>\
<p><strong><span style="text-\
decoration:underline;">39+ year olds</span></strong></p>\
\
<p>No Chateau proprietor has experience dating or fucking women 39 years old\
or older,  so we cannot offer much advice for gaming women in this age\
range. Yes,  yes,  we can all hear you crying now.</p\
>
'




c15 = epub.EpubHtml(title='the wall',
file_name='the_wall.xhtml',
lang='en')
c15.content='\
<h2>The Wall</h2>\
<p><strong>the wall</strong> [thuh wawl] <\
em>-noun</em>: 1. a large,  immovable monolith of frightening\
and awesome power capable of threshing egos and rending souls,\
serving as a metaphorical\
stoppage point at the intersection between a woman&#8217;s declining\
 sexual attractiveness\
and her advancing years,  beyond which female sexual\
desirability disappears into the misty void\
.</p>\
<p><a href="http://www.futurepundit.\
com" target="_blank">FuturePundit</a> has a post up <\
a href="http://www.futurepundit.com/archives/006914.\
html" target="_blank">highlighting a scientific study</a> which concludes\
,  most depressingly,  that by age 30 only 12% of a woman&#\
8217;s eggs remain.</p>\
<blockquote><p>Tom Kelsey\
,  a Senior Research Fellow at the School of Computer Science at St Andrews,\
said,  &#8220;Previous models have looked at the decline in ovarian reserve\
,  but not at the dynamics of ovarian reserve from\
 conception onwards. Our model\
shows that for 95% of women,  by the age of 30 years,\
only 12% of their maximum ovarian reserve is present,  and by the age\
of 40 years only 3% remains.</p></blockquote>\
<p>\
This is a surprise even to me. I knew there was a significant dropoff\
in female fertility by age 30,  but I didn&#8217;t know\
it was this precipitous. I find this news depressing,  because\
female fertility and\
sexual attractiveness closely parallel; allowing for a few lag years\
for the outer shell\
to catch up to the inner biology,  the number of viable eggs a woman\
has remaining directly correlates with the number of years she has\
 left as a highly\
coveted product on the sexual market. That is,  when a woman has a\
full basket of eggs she is at her most beautiful. When she has dwindled\
to 50% eggs left,  she is desireable to only half the men she\
was capable of attracting for short and,  particularly,  long\
term relationships when she\
was at her beauty prime. And when she is down to 3% eggs\
at age 40,  she can only attract 3% of the men she used\
to attract for long term investment when she was peaking at,  typically,  age\
20. And what&#8217;s worse,  those 3% of men\
are the leftover omega dregs with no other options whom she turned\
down when she\
was a hotter commodity.</p>\
<p>Personally,  as a man\
who has no desire to have kids,  the number of remaining eggs a woman\
has left is of no concern to me other than as an abstract matter.\
But a woman&#8217;s beauty is of paramount concern to me,\
and as such it would happen that,  through the use of my infallible divining\
boner rod,  my very selective screening procedures against\
women showing signs of physical decay\
would necessitate that I avoid dating women with less than 50% eggs in their\
basket. So far,  this is how it has worked out,  and I\
&#8217;ve mostly game and a devilish smile to thank for that.</\
p>\
<p>This saddens me. Why? I will explain.\
Anything,  any uncontrollable force,  that strips beauty from the\
 world is my enemy\
. How much grander and pleasurable life if women stayed beautiful\
for 100 years instead\
of a precious 15 years? How much love would my heart shout at the\
world if the pool of beautiful women was every woman,\
everywhere,  forevermore,\
and not just a small sliver of women with power so fleeting it may as\
well be a curse than a blessing? Imagine this world,  and tell me\
then how you keep the demons of hate from lashing impudently and\
futilely against the\
natural order of things. I say fuck the natural order. Bring on the\
life and beauty extending tamperings of human ingenuity. Get off\
your knees,  you\
limp-noodled gaiaists and blithely stoic servants of religion,\
you philosophical naifs and\
self-deluded sophists. Turn the tables and bring your\
evolutionary inheritance to its\
knees,  if you dare.</p>\
<p>More evidence for the\
wall comes from a <a href="http://www.dailymail.co\
.uk/femail/article-1246576/You-CAN-old-\
overnight.html" target="_blank">Japanese study showing that there is a\
real &#8220;tipping point&#8221; in aging</a>,  or\
a &#8220;hitting the wall&#8221; effect,  where a woman\
&#8217;s natural biological ability to rejuvenate herself and stay toe to toe\
with the ravages of aging slips into freefall at age 35,  much younger than\
previously thought.</p>\
<blockquote><p>&#8216;While some measurements showed a gradual decline,\
cheek volume &#8211; one of the key factors in a youthful appearance &#\
8211; can drop off suddenly,  by as much as 35 per cent in\
a year, &#8217; he says.</p></blockquote>\\
<p\
>Naturally,  there are some women whose stress-inducing lives of stripping,\
smoking,  slutting,  and single motherhood age them much faster\
than their actual years\
. These are truly tragic cases,  for they have thrown away\
their most precious\
asset for instant gratification.</p>\\
<p>In other news,  the\
new HBO documentary &#8220;<a href="http://www.hbo.\
com/documentaries/youth-knows-no-pain/index.html\
" target="_blank">Youth Knows No Pain</a>&#8221; was\
pretty good. A number of the women interviewed were boldly honest\
about their declining\
sexual attractiveness,  and the reasons for why they went\
under the knife to &#\
8220;get a little work done&#8221;. One woman even noted that\
when her friends told her there are plenty of women who look good for their\
age,  like Sophia Loren,  she responded that Sophia Loren is just one woman\
out of millions who &#8220;don&#8217;t look so good\
when they get older&#8221;. Found: A woman with a grasp of\
basic statistical concepts. Alert the media!</p>\\
<p>Most of\
the women in the documentary looked like alien-eyed stretchy gumbo toys,  but\
a couple did actually look pretty good,  at least ten years younger than their\
ages. At some point,  the science is going to have to dispense with\
the scalpel and start rejuvenating under the hood,  fixing\
the problem at its source\
using stem cells or some other form of cellular manipulation. I can&#8217\
;t wait for matrix-like abortion mills to be constructed to help my\
harem stay young and sexy for as long as possible.</p>\
'


c16 = epub.EpubHtml(title='boredom',
file_name='boredom.xhtml',
lang='en')
c16.content='\
<h2>Time to Boredom</h2>\
<p>There are two\
reasons men get bored with women\
: Intellectual incompatibility and beauty incompatibility\
. The less mentally stimulating or\
aesthetically stimulating a woman is to\
\
a man,  the quicker he\
will grow bored with her and\
throw his worm\
back into the\
waters for nibbles from new fish\
. Which of these two factors\
\
controls a larger portion of a\
man&#8217;s interest\
? Beauty,\
clearly,  and\
especially so in the critical first\
few months,  but assuming a\
\
threshold for acceptable beauty is met\
intellectual attraction or lack thereof serves\
to capture a\
man&#8217\
;s interest beyond the three\
-month mark. If neither\
\
the beauty nor intellectual threshold of\
attraction is crossed,  a man\
will get bored\
after the first\
ejaculation. If both are met\
,  a man is susceptible to\
\
the woman&#8217;s\
ploys to entrap him into marriage\
.</p>\
\
<p\
>Beauty and intellectual compatibility are\
relative to the man&#8217\
;\
s dating market value.\
If the man is a 9\
,  he will need\
a woman\
who is a 9 or 10\
in beauty,  and no less\
than\
10 IQ points lower than\
his own,  if he is\
to avoid getting bored\
with her\
after a month or two.\
Although I&#8217;ve\
known\
plenty of people whose wit\
,  charm,  and humor belied\
their average IQs,\
I will\
use IQ in this post as\
a rough proxy for intellectual and\
personality\
compatibility. For purposes of\
discussion,  I&#8217;\
ll set aside the\
few exceptions\
where the IQ of the partners\
is equal but their interests are\
so\
contrary that boredom becomes a\
manifestation of despising the other person\
&#8217;s\
hobbies.</\
p>\
<p>What\
follows is a handy chart illustrating\
<\
strong>Time To Boredom\
</strong> for the average\
man (male dating\
                                                     value rank\
     = 5 on a scale\
     of 0 &#8211;\
     10 inclusive\
                                                     ) based on\
the two critical variables of female\
beauty and IQ. Note\
that\
Time To Boredom is a relative\
value that will,  on average\
,  occur\
much sooner for a\
high ranking man than it would\
for a low ranking man\
.\
It is conceivable,  in fact\
,  that a male 10 will\
get bored\
with every woman he\
meets within hours if he doesn\
&#8217;t have\
mistresses\
to take up the slack in\
his attention span,  while a\
male zero\
might take years to\
get bored of a female zero\
,  although in the latter\
case\
the boredom might be just as\
quickly forthcoming but given the dearth\
of options\
available to the male zero he will work hard to keep his boredom and disgust\
hidden from his ugly partner.</p>\
<p>Female IQ is measured\
against a male baseline of 100.</p>\
<p>Female Hotness            Female\
Time To Male<br />\
\
<span style="text-\
decoration:underline\
;">Rank </\
span> <span style="\
text-decoration:underline;">\
\
IQ </span> <span\
style="text-decoration:\
    underline;">Boredom\
</span\
><br />\
0                                   +-10\
points     1 nanosecond (Neural disgust\
                         registers\
                                                                  <br />\
before\
                         conscious awareness)<br />\
\
0                                   &gt;-10\
points\
same diff<br />\
0\
&gt;+10 points     same\
diff<\
br />\
1                                   +-\
10 points      1 millisecond (time\
                              to retinal burn)<br\
\
/>\
1                                   &gt;-10\
points      irrelevant<br />\
1\
&gt;+\
10 points     1 millisecond to boredom + annoyance<br />\
2                                   +-10 points\
1 second<br />\
2\
&gt;-10 points      1\
minute (male\
                                                                  inspired to<\
        br />\
ridicule the dummy\
        )<br />\
2                                   &\
gt\
;+10 points     1 minute\
(male inspired to<br\
 />\
ridicule the nerd\
                          )<\
br />\
3                                   +-10 points\
5 minutes (male tries to\
           find\
                                                                <br />\
redeeming\
           quality)<br />\
3\
&gt;-10 points\
3\
minutes (male fails at finding\
         <br />\
redeeming quality\
         )<br />\
\
3\
&gt;+10 points     6\
minutes (takes male extra minute\
         to<\
                                                                  br />\
realize\
         she&#8217;s\
         ugly thanks to her<br />\
impressive knowledge of<br />\
computer hardware)<br />\
4                                    +-10 points      1 hour \
(male wants same night lay\\
 )<br />\
4                                    &\
gt;-10 points      1/\
2 hour (male wants same \
        hour lay)<br />\
\
4                                    &gt;+10 points\
\
2 hours (males wants same\
         \
         night lay<br />\
\
\
\
         with talky talky chick\
         )<\
\
br />\
5                                    \
+-10 points\
5 weeks (\
    bloom off the\
         rose after<br />\
\
         third bang)<br />\
\
5                                    &gt;-10 points\
3 weeks (pillow talk excruciating\
         )<br />\
5                                    &\
gt;+10 points     4 weeks\
(male charmed,  then annoyed\
 , <br />\
by\
 chick&#8217;s\
 nerdiness)<br />\
6\
+-10 points      3 months (\
    best he&#8217;\
    s ever had, <\
    br />\
but still not\
    that good)<br />\
\
6                                    &gt;-10 points\
2 months (her hobby is\
          <a href="https\
          ://heartiste.wordpress.\
          com/2008/05\
          /30/flip-\
          cup-game/" target\
          ="_blank">beer pong\
          </a>)<br />\
\
6                                    &gt;+10 points\
2.5 months (emasculated\
            by her<br />\
\
            sharp tongue)<br />\
\
7                                    +-10 points      1 year\
(a beta&#8217;\
 s heaven)<br />\
\
7                                    &gt;-10 points\
9 months (tard kills boners\
          dead)<br />\
7\
&gt;+10 points     1\
.5 years (male inspired\
          by her, <br\
          />\
but relationship unstable)<\
br />\
8                                    +-10 points\
5 years (even a beta\
         will get tired<br\
         />\
of sex with same\
         hottie)<br />\
8\
&gt;-10 points      5\
years (she&#8217;\
       s too hot to care\
       <br />\
about tardness\
       )<br />\
8                                    &\
gt;+10 points     5 years\
(she&#8217;s\
 too hot to care<\
 br />\
about nerdiness)<\
br />\
9                                    +-10 points\
30 years (beta suffers seizure\
          from<br />\
constant\
          stream of endorphins)<br\\
/>\
9                                    &gt;-10\
points      30 years (she&#\
                      8217;s too hot\
                      to notice<br />\
\
                      tardness)<br />\
9\
&gt;+10 points     30\
years (she&#8217;\
       s too hot to notice\
       <br />\
much of anything except<br />\
how hot she is)<br />\
\
10                                 +-10 points      forever (\
    entered realm of unreality)<\
br />\
10                                 &gt;-\
10 points      forever + 1 (\
    tardness means she can&#\
    8217;t<br\
    />\
tell he&#8217\
    ;s a beta)<\
br />\
10                                 &gt;+\
10 points     forever -1 (\
    one day,  she uses\
    big word<br />\
\
    that renders him impotent)</\
p>\
<p>As\
you can see,  it is\
almost guaranteed that men of every\
status rank will grow bored with\
their girlfriends,  dates,  wives\
,  fuckbuddies without an external injection\
of groinal stimulation. There is\
only one way a man can\
delay Time To Boredom:</p>
'


c17 = epub.EpubHtml(title='quality vs qunatity',
file_name='quality_vs_quantity.xhtml',
lang='en')
c17.content='
<h2>Quality VS Quanity,  Formula Version</h2>
'

c18 = epub.EpubHtml(title='wrapped',
file_name='wrapped.xhtml',
lang='en')
c18.content='
<h2>Wrapped Around His Finger</h2>
'


















































# Book Spine

book.add_item(intro)
book.add_item(foundations)
book.add_item(f1)
book.add_item(f2)
book .add_item(f3)
book .add_item(f5)
book.add_item(f6)
book.add_item(f7)
book.add_item(f8)
book.add_item(f9)
book.add_item(f10)
book.add_item(f11)
book.add_item(f12)
book.add_item(f13)
book.spine = ['cover ', intro, foundations, f1, f2, f3, f4, f5 , f6, f7, f8,
              f9, f10, f11, f12 , f13]

# create epub file
epub.write_epub('roissy.epub', book, {})
