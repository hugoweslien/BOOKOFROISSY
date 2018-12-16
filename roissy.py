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

# Book Spine
book.add_item(intro)
book.add_item(foundations)
book.add_item(f1)
book.add_item(f2)
book.add_item(f3)
book.add_item(f4)
book.add_item(f5)
book.add_item(f6)
book.add_item(f7)
book.add_item(f8)
book.add_item(f9)
book.add_item(f10)
book.add_item(f11)
book.add_item(f12)
book.add_item(f13)
book.spine = ['cover', intro, foundations, f1, f2, f3, f4, f5, f6,
              f7, f8, f9, f10, f11, f12, f13]

# create epub file
epub.write_epub('roissy.epub',  book, {})
