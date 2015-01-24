# -*- coding: utf-8 -*-

"""
Static data
"""

# Based on https://github.com/tarr11/Webmail-Domains and
# http://stackoverflow.com/questions/3823320/how-do-i-identify-a-webmail-service-from-an-email-address
# filtering out domains in urlblacklist that are without an MX record (the blacklist is from 2013)
webmail_domains = set([
    '123india.com',
    '163.net',
    '21centuryoutdoors.com',
    '24kt.com',
    '2bmail.co.uk',
    '2ndmail.com',
    '37.com',
    '44magnum.com',
    '4x4chevy.com',
    '4x4ford.com',
    '4x4jeep.com',
    '4x4ram.com',
    '5star.net',
    '7metasearch.com',
    'aaronsmail.com',
    'abbysmail.com',
    'abominablesnowman.com',
    'abv.bg',
    'acegroup.cc',
    'acemail.com',
    'acmemail.net',
    'acoolemail.com',
    'adamsmail.com',
    'address.com',
    'adiva.net',
    'affection.org',
    'africa-1.com',
    'africa1.net',
    'afterburners.com',
    'alabama1.com',
    'alansmail.com',
    'alberta1.com',
    'albertacam.com',
    'alexsmail.com',
    'algeria.com',
    'alien-adopt.com',
    'alienaa.com',
    'allansmail.com',
    'allensmail.com',
    'allhell.com',
    'alohastate.net',
    'alongcomesmary.com',
    'alove-in.com',
    'alsmail.com',
    'altern.org',
    'alwaysright.net',
    'amaterialgirl.com',
    'ambitious1.com',
    'americansportfishing.com',
    'amuro.net',
    'amysmail.com',
    'ananzi.co.za',
    'andrewsmail.com',
    'angelfire.com',
    'angrykid.net',
    'animalhouse.com',
    'animenation.com',
    'annsmail.com',
    'anonymous.to',
    'another.com',
    'aol.com',
    'apexmail.com',
    'aprilfools.net',
    'aprilsmail.com',
    'aquarius1.com',
    'arabia.com',
    'arach.net.au',
    'arave.net',
    'arctic.net',
    'aries1.com',
    'arizona1.com',
    'arkansas1.com',
    'artlovers.com',
    'artordie.com',
    'asia-1.com',
    'asia1.net',
    'asianoffice.com',
    'asiansonly.net',
    'asianwired.com',
    'aspemail.com',
    'asphaltangel.com',
    'atgratis.com',
    'atlanticcity1.com',
    'att.net',
    'attentionslut.com',
    'au.com',
    'ausi.com',
    'aussiemail.com.au',
    'australia.edu',
    'australia1.com',
    'axoskate.com',
    'backpackers.com',
    'bad-ass.net',
    'bagan.net.mm',
    'ballsy.net',
    'bangladesh.com',
    'bannertown.net',
    'barracudas.com',
    'barrhead.com',
    'baseball-fan.com',
    'baseballcrazy.com',
    'baseballforever.net',
    'basketball-fan.com',
    'basketballcrazy.com',
    'bassangler.net',
    'baystreetcanada.com',
    'beaverstate.net',
    'beehives.net',
    'beer.com',
    'beijingoffice.com',
    'bensmail.com',
    'berlinoffice.com',
    'berniesmail.com',
    'bestkeptsecrets.com',
    'bigcitylights.com',
    'bigdark.com',
    'bigfoot.com',
    'biggerbadder.com',
    'bigmailbox.com',
    'bigsteel.com',
    'billrules.com',
    'billysmail.com',
    'bird-lovers.com',
    'blackknights.com',
    'blacktopbandit.com',
    'blazemail.com',
    'blowinupthespot.com',
    'bluejeansforever.com',
    'boardbitch.com',
    'boardermail.com',
    'bobcatsrule.com',
    'bobsmail.com',
    'bolt.com',
    'bombdiggity.com',
    'bonnag.com',
    'bonnyville.com',
    'booklover.com',
    'boringwork.com',
    'borntodrive.com',
    'bostonoffice.com',
    'boxfrog.com',
    'brainery.com',
    'brandysmail.com',
    'breakthru.com',
    'brentsmail.com',
    'brettsmail.com',
    'briansmail.com',
    'brightlights.com',
    'bringingit.com',
    'britishcolumbia1.com',
    'brookesmail.com',
    'brunosmail.com',
    'buckeyestate.net',
    'buffalo1.com',
    'bugcrazy.com',
    'bulldogsrule.com',
    'bullsrule.com',
    'buyersusa.com',
    'byke.com',
    'c3.hu',
    'c4.com',
    'california1.com',
    'californiadreaming.com',
    'cameranews.com',
    'cameronsmail.com',
    'campbellriver.com',
    'campusunlimited.com',
    'canada1.com',
    'canadafishing.com',
    'canadaspeakersbureau.com',
    'canadiansportfishing.com',
    'canadianunity.com',
    'cancer1.com',
    'candycanelane.com',
    'candycanes.com',
    'capricorn1.com',
    'captainhook.com',
    'caramail.com',
    'careerbuildermail.com',
    'carlsmail.com',
    'carolinesmail.com',
    'carolsmail.com',
    'carolynsmail.com',
    'carscarscars.com',
    'cartoonsrock.com',
    'casablancaresort.com',
    'cashette.com',
    'cat-lover.com',
    'catcrazy.com',
    'cathednet.wa.edu.au',
    'catholic.org',
    'celtic.com',
    'centennialstate.com',
    'centralpets.com',
    'certifiedmail.com',
    'chadsmail.com',
    'charliesmail.com',
    'charlottetown.com',
    'charlottetown1.com',
    'charter.net',
    'chartermi.net',
    'chat.ru',
    'cheapdirt.org',
    'checkeredflags.com',
    'cheery.com',
    'chek.com',
    'chev.com',
    'chevrolet1.com',
    'chickmail.com',
    'chocolatenuts.com',
    'chooselife.com',
    'christian.net',
    'christiesmail.com',
    'christysmail.com',
    'chromerim.com',
    'chucksmail.com',
    'cidadeinternet.com.br',
    'cindysmail.com',
    'cityjewelry.com',
    'cityperformance.com',
    'claresholm.com',
    'clarksmail.com',
    'clickclass.com',
    'cliffsmail.com',
    'closedparty.com',
    'cmpnetmail.com',
    'coldmail.com',
    'college2100.com',
    'collegemail.com',
    'colorado1.com',
    'columbus1.com',
    'comcast.net',
    'comicmail.com',
    'comingoutproud.com',
    'communityconnect.com',
    'compleatangler.com',
    'comprendemail.com',
    'computermail.com',
    'computermail.net',
    'conanfan.com',
    'condonews.com',
    'conk.com',
    'connecticut1.com',
    'constitutionstate.com',
    'contractplayer.com',
    'cookingpro.com',
    'coolgoose.com',
    'coollist.com',
    'corestyle.net',
    'coreysmail.com',
    'cornhuskerstate.com',
    'cosmicconscious.com',
    'cougarsrule.com',
    'countrycooking.com',
    'countrygal.com',
    'countryguy.com',
    'covad.net',
    'cowboysrule.com',
    'cox.net',
    'coyotestate.com',
    'craigsmail.com',
    'currentmail.com',
    'curtissmail.com',
    'cwebmail.com',
    'cybercafemaui.com',
    'cybergrrl.com',
    'd-gen.net',
    'd4mail.com',
    'dalesmail.com',
    'danielsmail.com',
    'dansmail.com',
    'darkcastle.com',
    'darrensmail.com',
    'davesmail.com',
    'dazedandconfused.net',
    'dbzmail.com',
    'dcemail.com',
    'dealingwithit.com',
    'deansmail.com',
    'defiantchild.com',
    'delaware1.com',
    'deseretmail.com',
    'determinado.net',
    'detroit1.com',
    'detroitusa.com',
    'deuceswild.com',
    'diamondsforever.com',
    'diamondstate.net',
    'didamail.com',
    'digitalaudit.com',
    'digitalmail.com',
    'digitalmusicnation.com',
    'dipsydoo.com',
    'dir.bg',
    'directbox.com',
    'disconnectedyouth.com',
    'dispostable.com',
    'dodge1.com',
    'dogcrazy.com',
    'donnasmail.com',
    'donsmail.com',
    'doramail.com',
    'douglassmail.com',
    'draytonvalley.com',
    'dreammasters.com',
    'ducksrule.com',
    'duffers.com',
    'dwp.net',
    'dylansmail.com',
    'e-mailanywhere.com',
    'e-mol.com',
    'earthlink.com',
    'earthlink.net',
    'easyspace.com',
    'easywoodworking.com',
    'echoes.net',
    'ecompare.com',
    'ecuador.com',
    'edsmail.com',
    'edtn.com',
    'edwinsmail.com',
    'elismail.com',
    'elvisforever.com',
    'email.com',
    'email.it',
    'email.ro',
    'emailaccount.com',
    'emailaddresses.com',
    'emailit.com',
    'emailman.com',
    'emailsupport.com',
    'emailvista.com',
    'emich.edu',
    'emilysmail.com',
    'empirestate.net',
    'emsergipe.com',
    'endlesssummers.com',
    'entrepreneurmag.com',
    'epals.com',
    'eresmas.com',
    'ericsmail.com',
    'eriksmail.com',
    'erinsmail.com',
    'eudoramail.com',
    'europe-1.com',
    'evansmail.com',
    'evergreens.net',
    'evergreenstate.com',
    'everymail.net',
    'everyone.net',
    'evil1.com',
    'excite.com',
    'exclusivemail.co.za',
    'executivemail.co.za',
    'extreme1.com',
    'extrememoves.com',
    'extremerides.com',
    'eye.ch',
    'ezrs.com',
    'ezwebmailer.com',
    'ezzemail.com',
    'facebook.com',
    'fadmail.com',
    'falher.com',
    'fantasticyou.com',
    'fastermail.com',
    'fastmail.ca',
    'fastmail.fm',
    'fearlessfemale.com',
    'fetchmail.co.uk',
    'findmemail.com',
    'finestservice.com',
    'firehousemail.com',
    'firemail.de',
    'firestar.com.au',
    'fishhooks.com',
    'fishingforever.com',
    'fishrods.com',
    'flairmail.com',
    'flashmail.com',
    'florida1.com',
    'floydmail.com',
    'floydsmail.com',
    'footballpunk.com',
    'ford1.com',
    'forgottenrealms.com',
    'fortsaskatchewan.com',
    'fortunecity.com',
    'forum.dk',
    'foryoureyesonly.com',
    'france-mail.com',
    'francemel.com',
    'francemel.fr',
    'franklinsmail.com',
    'franksmail.com',
    'fransmail.com',
    'fredsmail.com',
    'free.fr',
    'freemail.de',
    'freemail.gr',
    'freemail.org.mk',
    'freemailguide.com',
    'freenet.de',
    'freetown.com',
    'freewebemail.com',
    'friendlyplaces.com',
    'frontierjustice.com',
    'funinthesun.com',
    'funjokes.net',
    'funkids.net',
    'funnymail.com',
    'fusemail.com',
    'fx.ro',
    'gaiaonline.com',
    'gailsmail.com',
    'gambling1.com',
    'gamespotmail.com',
    'ganjabud.com',
    'garysmail.com',
    'gatorsrule.com',
    'gearjamming.com',
    'geecities.com',
    'gemini1.com',
    'georgesmail.com',
    'georgia1.com',
    'getjiggywithit.com',
    'getmedieval.net',
    'gigileung.org',
    'ginasmail.com',
    'gingersmail.com',
    'girl4god.com',
    'girlchamps.com',
    'girlstorm.com',
    'girouxville.com',
    'glamlife.com',
    'glay.org',
    'global.net.au',
    'glossy.com',
    'gmail.com',
    'gmx.com',
    'gmx.de',
    'gmx.net',
    'gnarlyman.com',
    'go.com',
    'gobands.com',
    'gobuggy.com',
    'gobugs.com',
    'gochev.com',
    'gochevrolet.com',
    'gochevs.com',
    'gochevy.com',
    'gocondos.com',
    'gocop.com',
    'gocops.com',
    'godeep.com',
    'godscountrycanada.com',
    'godscountryusa.com',
    'gofords.com',
    'gohalloween.com',
    'goingaroundincircles.com',
    'goingwild.net',
    'gojewels.com',
    'gojokes.com',
    'golfcrazy.com',
    'golfgod.net',
    'golfingcanada.com',
    'golfingusa.com',
    'gonewiththewind.com',
    'goodjewelry.com',
    'goodnewsmail.com',
    'goodoleboy.net',
    'goodperfume.com',
    'goodperfumes.com',
    'goodwatches.com',
    'goofyfooters.com',
    'google.com',
    'googlemail.com',
    'gopaintings.com',
    'gopolice.com',
    'gordonsmail.com',
    'gosantaclaus.com',
    'goshdamn.com',
    'gospeakers.com',
    'gotitdown.com',
    'gotobugs.com',
    'gotrespect.com',
    'govalentines.com',
    'govalentinesday.com',
    'gowatches.com',
    'graffiti.net',
    'grandcanyonstate.net',
    'grandecache.com',
    'grandeprairie.com',
    'grandslams.com',
    'granites.net',
    'greatlakestate.com',
    'greenflags.com',
    'gregsmail.com',
    'grlmail.com',
    'groovy-baby.com',
    'gthangs.com',
    'guerillamail.com',
    'guysmail.com',
    'guyzrule.com',
    'habeascorpus.com',
    'halifax1.com',
    'halsmail.com',
    'hanginthere.net',
    'hanksmail.com',
    'hanmail.net',
    'happiest.com',
    'happy1.com',
    'hardnews.com',
    'hartford1.com',
    'haulinass.net',
    'haveagoodday.org',
    'hawaii1.com',
    'hawkeyes.net',
    'heartofgold.com',
    'heathersmail.com',
    'heavyhitters.com',
    'heavyweights.com',
    'hello.net.au',
    'hellorhighwater.com',
    'hermajesty.com',
    'highperformanceusa.com',
    'highriver.com',
    'highschoolclub.com',
    'highveldmail.co.za',
    'hitthebeach.com',
    'hiyadoin.com',
    'hkg.net',
    'hockeycrazy.com',
    'hogsrule.com',
    'holiday1.com',
    'holidaynews.com',
    'hollywoodusa.com',
    'homemail.co.za',
    'honduras.com',
    'hongkong.com',
    'hoodwinker.com',
    'hoodwinkers.com',
    'hoofmail.com',
    'hotdang.com',
    'hotmac.com',
    'hotmail.co.il',
    'hotmail.com',
    'hotmail.fr',
    'hotmail.it',
    'hotmail.kz',
    'hotpros.com',
    'hotvoice.com',
    'howardsmail.com',
    'howlermonkey.net',
    'howsweetitis.com',
    'hushmail.com',
    'huskiesrule.com',
    'hyderabad.com',
    'i-mail.com.au',
    'iamabitch.com',
    'iamplatinum.com',
    'iamwaycool.com',
    'ibest.com.br',
    'icloud.com',
    'icq.com',
    'icqmail.com',
    'id-base.net',
    'idaho1.com',
    'idigjesus.com',
    'ig.com.br',
    'iinet.net.au',
    'ikickass.net',
    'illinois1.com',
    'ilovecats.com',
    'ilovecountry.com',
    'iloveelvis.com',
    'ilovehorses.com',
    'ilovenewyork.net',
    'ilovenewyorknewyork.com',
    'iloverocknroll.com',
    'imstyling.com',
    'in-box.net',
    'in2jesus.com',
    'iname.com',
    'inbox.com',
    'incomparable.com',
    'incredimail.com',
    'indiana1.com',
    'indiansrule.com',
    'indiatimes.com',
    'indocities.com',
    'indy500racing.com',
    'innisfail.com',
    'inode.at',
    'interfold.com',
    'interia.pl',
    'iol.pt',
    'iowa1.com',
    'iplayhard.org',
    'iqemail.com',
    'irresistiblecharm.com',
    'iservejesus.com',
    'isleuthmail.com',
    'itchyfinger.net',
    'itds-consulting.com',
    'itsgoodtobeme.com',
    'itsgoodtogo.com',
    'ivillage.com',
    'iwalkthetalk.com',
    'iwon.com',
    'jacobsmail.com',
    'jahoopa.com',
    'jakesmail.com',
    'janesmail.com',
    'jansmail.com',
    'jasonsmail.com',
    'jdsmail.com',
    'jeffsmail.com',
    'jennifersmail.com',
    'jennyrules.com',
    'jerrysmail.com',
    'jessicasmail.com',
    'jesusandme.net',
    'jesussaves.net',
    'jewelrynews.com',
    'jillsmail.com',
    'jimsmail.com',
    'jmail.co.jp',
    'joannasmail.com',
    'joansmail.com',
    'joesmail.com',
    'johnnysmail.com',
    'johnsmail.com',
    'jokesfinder.com',
    'jonsmail.com',
    'joy-joy-joy.com',
    'joysmail.com',
    'jps.net',
    'judysmail.com',
    'junglemate.com',
    'juno.com',
    'justawildguess.com',
    'justicemail.com',
    'justinsmail.com',
    'kansas1.com',
    'karensmail.com',
    'kataweb.it',
    'katchup.co.nz',
    'katesmail.com',
    'kathysmail.com',
    'kebi.com',
    'keepitsmooth.com',
    'kellismail.com',
    'kellysmail.com',
    'kensmail.com',
    'kentucky1.com',
    'keromail.com',
    'kevinsmail.com',
    'keystonestate.net',
    'killermoves.net',
    'kittymail.com',
    'korea.com',
    'kristysmail.com',
    'kswildcat.com',
    'la.com',
    'landofenchantment.net',
    'landoflakes.net',
    'largebeauty.com',
    'larrysmail.com',
    'lastwomanstanding.com',
    'lasvegasusa.com',
    'latinmail.com',
    'laurensmail.com',
    'leesmail.com',
    'leo-1.com',
    'lesserslavelake.com',
    'letsblow.com',
    'letsride.com',
    'letsrock.com',
    'letsrock.net',
    'libero.it',
    'libertysurf.fr',
    'libra1.com',
    'lightspeed.net',
    'lindsaysmail.com',
    'linuxfreemail.com',
    'linuxmail.org',
    'live.com',
    'livetolove.net',
    'livetorace.com',
    'lloydminster.com',
    'lloydsmail.com',
    'loadmail.com',
    'locos.com',
    'locoseek.com',
    'loismail.com',
    'lonestars.net',
    'lonestarstate.com',
    'longhornmail.com',
    'lorismail.com',
    'losemynumber.com',
    'lostcontinent.com',
    'louisesmail.com',
    'louisiana1.com',
    'lovableme.com',
    'lovefootball.com',
    'lovemail.com',
    'lovemyhusband.com',
    'ltunas.inf.cu',
    'ludicrous.com',
    'lukesmail.com',
    'lycos.co.uk',
    'lycos.com',
    'lycos.de',
    'lycos.es',
    'lycos.fr',
    'lycos.nl',
    'm321.com',
    'mac.com',
    'macbox.com',
    'macsrbetter.com',
    'macwild.com',
    'maggiesmail.com',
    'magicmail.co.za',
    'magicspells.com',
    'magicwands.com',
    'magnolias.net',
    'mail-center.com',
    'mail.bg',
    'mail.com',
    'mail.lv',
    'mail.md',
    'mail.ru',
    'mail15.com',
    'mail2web.com',
    'mail2world.com',
    'mail4u.com.mm',
    'mailandnews.com',
    'mailasia.com',
    'mailblocks.com',
    'mailbox.co.za',
    'mailbox.sk',
    'mailcenter.cc',
    'mailcity.com',
    'mailexcite.com',
    'mailinator.com',
    'mailmgr.co.uk',
    'mailpanda.com',
    'mailplanet.net',
    'mailpride.com',
    'mailsnare.net',
    'mailstart.com',
    'mailstartplus.com',
    'mailtag.com',
    'mailwire.com',
    'maine1.com',
    'makinghay.com',
    'maltesemail.com',
    'mamaro.net',
    'mancity.net',
    'mandalay.net.mm',
    'maneater.com',
    'manitoba1.com',
    'mapleleaf.net',
    'marchmail.com',
    'marciasmail.com',
    'marcsmail.com',
    'mariasmail.com',
    'marksmail.com',
    'martinsmail.com',
    'maryland1.com',
    'marysmail.com',
    'massachusetts1.com',
    'matthewsmail.com',
    'mattsmail.com',
    'mauimail.com',
    'maxichat.com',
    'me.com',
    'medicinehat.com',
    'medsite.com',
    'meetic.fr',
    'megapoint.com',
    'melaniesmail.com',
    'meowmail.com',
    'merawalaemail.com',
    'merseymail.com',
    'michaelsmail.com',
    'michigan1.com',
    'midastouch.com',
    'midnightmagic.com',
    'mighty.co.za',
    'mikesmail.com',
    'millionairemail.com',
    'mindspring.com',
    'minneapolis1.com',
    'minnesota1.com',
    'mississippi1.com',
    'missouri1.com',
    'mixmail.com',
    'mochamail.com',
    'mochamomma.com',
    'montana1.com',
    'moonpuppies.com',
    'moonraker.com',
    'morgansmail.com',
    'morocco.com',
    'moscowoffice.com',
    'mountaineersrule.com',
    'movielovers.com',
    'moviesbymail.com',
    'msgto.com',
    'msn.com',
    'mts.net',
    'mustanggt.com',
    'mustgofishing.com',
    'mutantcity.com',
    'mutantfamily.com',
    'mutantlife.com',
    'mutantmind.com',
    'mutantpeople.com',
    'mutantplanet.com',
    'mutantworld.com',
    'mymail.com.au',
    'mynra.com',
    'myownemail.com',
    'mypad.com',
    'mypersonalemail.com',
    'myplace.com',
    'myrealbox.com',
    'myway.com',
    'n2mail.com',
    'naseej.com',
    'nashville1.com',
    'nashvilleusa.com',
    'nathansmail.com',
    'naturalstate.net',
    'naui.net',
    'navegalia.com',
    'neatasapin.net',
    'nebraska1.com',
    'nepal.com',
    'netaddress.com',
    'netcom.com',
    'netcourrier.com',
    'netfirms.com',
    'netnoir.net',
    'netpoint.com.br',
    'netroamer.com',
    'netscape.com',
    'netster.com',
    'netzero.com',
    'nevada1.com',
    'neverneverland.com',
    'neversaynever.com',
    'newbrunswick1.com',
    'newfoundland1.com',
    'newhampshire1.com',
    'newjersey1.com',
    'newlearn.com',
    'newmail.com',
    'newmexico1.com',
    'neworleans1.com',
    'newsboysmail.com',
    'newyearbaby.com',
    'newyearsbabies.com',
    'newyearsbaby.com',
    'newyork1.com',
    'newyorkcity.com',
    'newyorkoffice.com',
    'newzealand.com',
    'nexus.hu',
    'nexxmail.com',
    'nicaragua.com',
    'nice2meetu.org',
    'nicksmail.com',
    'nigelsmail.com',
    'nimail.com',
    'nj.com',
    'noahsmail.com',
    'nohands.org',
    'nohometraining.com',
    'nolansmail.com',
    'norikomail.com',
    'northamerica1.com',
    'northcarolina1.com',
    'northdakota1.com',
    'northernalberta.com',
    'northstarstate.com',
    'nothankstoyou.com',
    'novascotia1.com',
    'ntscan.com',
    'numail.co.uk',
    'nunavut1.com',
    'nuukiemail.com',
    'nz11.com',
    'occultmail.com',
    'oddpost.com',
    'offmyrocker.net',
    'ofir.dk',
    'oh-baby.net',
    'oh-behave.com',
    'ohio1.com',
    'ohmigod.com',
    'oklahoma1.com',
    'olddominionstate.com',
    'ondiscute.com',
    'onebox.com',
    'onemain.com',
    'online.ie',
    'onlinecommunity.com',
    'ontario1.com',
    'ontariogovernment.com',
    'operamail.com',
    'optonline.net',
    'optusnet.com.au',
    'orcon.net.nz',
    'oregon1.com',
    'ottawa1.com',
    'outdoorlore.com',
    'outdoorsamerica.com',
    'outdoorscanada.com',
    'outgun.com',
    'outlook.com',
    'pakistanmail.com',
    'palmettos.com',
    'palmettostate.com',
    'pamsmail.com',
    'pandamail.net',
    'parisoffice.com',
    'parkersmail.com',
    'passport.com',
    'passport.net',
    'patsmail.com',
    'paulsmail.com',
    'pconnections.net',
    'pcparty.com',
    'peaceriver.com',
    'peacerivercountry.com',
    'peaceseeker.com',
    'pennsylvania1.com',
    'people.it',
    'peoplepc.com',
    'performancecity.com',
    'perrysmail.com',
    'petesmail.com',
    'phat.co.nz',
    'philadelphia1.com',
    'philsmail.com',
    'phone.net',
    'pinchercreek.com',
    'pinetreestate.com',
    'pinoymail.com',
    'pipeline.com',
    'pirategold.com',
    'pisces1.com',
    'plaincrazy.com',
    'planetaccess.com',
    'planetearthinter.net',
    'platoon.com',
    'pobox.com',
    'pochta.ru',
    'pokemon.com',
    'polka.co.za',
    'ponoka.com',
    'pop.com.br',
    'popaccount.com',
    'popmail.com',
    'post.cz',
    'post.sk',
    'postmark.net',
    'postmaster.co.uk',
    'pousa.com',
    'powellriver.com',
    'princeedwardisland1.com',
    'privateers.com',
    'proangling.com',
    'probemail.com',
    'prontomail.com',
    'proudandfree.com',
    'provide.net',
    'prowalleye.com',
    'psychedout.net',
    'puertorico.com',
    'pullingyourleg.com',
    'purpleturtle.com',
    'qmail.com',
    'quadruplet.com',
    'quebec1.com',
    'quebeccity1.com',
    'quickhosts.com',
    'quintuplet.com',
    'quios.com',
    'racing1.com',
    'radbabe.com',
    'radguy.com',
    'radio1000.com',
    'ragingbull.com',
    'rainydaygirl.com',
    'rambler.ru',
    'ramsrule.net',
    'rarepaintings.com',
    'ratt-n-roll.com',
    'ravemail.co.za',
    'raven-mail.com',
    'ravetime.com',
    'raysmail.com',
    'realradiomail.com',
    'recipexperience.com',
    'recycler.com',
    'redheadandproud.com',
    'redheadsrock.com',
    'rediff.com',
    'rediffmail.com',
    'redlightbandit.com',
    'reedsmail.com',
    'regina1.com',
    'registeredsite.com',
    'reneesmail.com',
    'reno1.com',
    'respublica.fr',
    'returnreceipt.com',
    'rexsmail.com',
    'rhodeisland1.com',
    'richmondhill.com',
    'richsmail.com',
    'riderettes.com',
    'rileysmail.com',
    'robinsmail.com',
    'robsmail.com',
    'rock.com',
    'rock1.com',
    'rocketmail.com',
    'rocketsrule.com',
    'rockme.com',
    'rockymountainhouse.com',
    'rodeodriveusa.com',
    'rodsmail.com',
    'ronsmail.com',
    'roosh.com',
    'route1.net',
    'rsnmail.com',
    'runbox.com',
    'runningtheshow.com',
    'russia.com',
    'ryansmail.com',
    's-mail.com',
    'sacbeemail.com',
    'safe-mail.net',
    'sagittarius1.com',
    'saintmail.net',
    'samilan.com',
    'samsmail.com',
    'santasmail.net',
    'sarahsmail.com',
    'sarasmail.com',
    'saskatchewan1.com',
    'sawasdee.com',
    'scalawags.com',
    'scamartists.com',
    'scandalous.com',
    'scaryperson.com',
    'schizo.com',
    'scorpio1.com',
    'scotland.com',
    'scotsmen.com',
    'scottsmail.com',
    'seattlelab.com',
    'sesa.net',
    'sessionboy.com',
    'sethsmail.com',
    'sexjunkie.net',
    'seznam.cz',
    'shadango.com',
    'shaw.ca',
    'shivermetimbers.org',
    'shoutmail.com',
    'shredded.com',
    'sicktricks.net',
    'sidsmail.com',
    'sify.com',
    'silverslipper.com',
    'silverslippers.com',
    'silverspurs.com',
    'simonsmail.com',
    'sinnerandsaint.com',
    'skicrazy.com',
    'skios.es',
    'skyblog.com',
    'skynet.be',
    'slamdunks.com',
    'slowpoke.com',
    'smalltownhero.net',
    'snoopymail.com',
    'snowboardpunk.com',
    'snowcrazy.com',
    'soapsjunkie.com',
    'softhome.net',
    'sonicnetmail.com',
    'soonerstate.net',
    'sosick.net',
    'southafrica.com',
    'southamerica1.com',
    'southcarolina1.com',
    'southdakota1.com',
    'southernboy.net',
    'spacer.com',
    'spamgourmet.com',
    'spaznout.com',
    'speakerregistry.com',
    'special1.com',
    'speedcrazy.com',
    'speedwaycentral.com',
    'speedymail.net',
    'spl.at',
    'sports1.com',
    'sportscrazy.com',
    'sportshero.net',
    'spreadfirefox.com',
    'sprintmail.com',
    'sprynet.com',
    'stacysmail.com',
    'stalag13.com',
    'starmail.co.za',
    'start.com.au',
    'startmedia.com',
    'stbmail.com',
    'stephensmail.com',
    'stettler.com',
    'stevensmail.com',
    'stevesmail.com',
    'stewartsmail.com',
    'stickapin.com',
    'stjohns1.com',
    'stockcarcrazy.com',
    'stoned.com',
    'stonedage.com',
    'stopthepresses.com',
    'streetfreak.com',
    'streetrebel.com',
    'streetwarriors.com',
    'student.com',
    'sultanofbrunei.com',
    'suncrazy.com',
    'sunnygirl.net',
    'sunnysmail.com',
    'sunsetboulevardusa.com',
    'suntans.com',
    'superbucks.com',
    'superemail.com',
    'superettes.com',
    'superluck.com',
    'supernews.com',
    'superrides.com',
    'superwheel.com',
    'superwheels.com',
    'surfout.com',
    'surfy.net',
    'susansmail.com',
    'sweden.com',
    'swiftcurrent.com',
    'swiftdsl.com.au',
    'swiftel.com.au',
    'switchboardmail.com',
    'sydneyoffice.com',
    'sympatico.ca',
    'talk21.com',
    'talltale.com',
    'talltales.com',
    'taylorsmail.com',
    'tbwt.com',
    'tchatche.com',
    'techemail.com',
    'teddybearcrazy.com',
    'teenmusic.com',
    'tekmail.com',
    'telenet.be',
    'tenderhearted.com',
    'tenderlovingcare.com',
    'tennessee1.com',
    'tenniscrazy.com',
    'terra.com.br',
    'terrysmail.com',
    'texas1.com',
    'thai.com',
    'thatsdope.net',
    'thatweb.com',
    'the-n.com',
    'theagency.com',
    'thebaystate.com',
    'thecloser.net',
    'thecricket.co.za',
    'thedoghousemail.com',
    'thedorm.com',
    'thefishinghole.com',
    'thegemstate.com',
    'theglobe.com',
    'thegolf.co.za',
    'thegrid.net',
    'thegrrl.com',
    'thegrrls.com',
    'theheadoffice.com',
    'thejetsetter.com',
    'themail.com',
    'theoceanstate.net',
    'theovaloffice.com',
    'thepeachstate.com',
    'thepolice.com',
    'theprofessor.org',
    'thepub.co.za',
    'therugby.co.za',
    'thespecialists.com',
    'thestockmarket.com',
    'thestrip.com',
    'thesunshinestate.net',
    'thesupernatural.com',
    'thetwilightzone.com',
    'thewildanimal.com',
    'thewildgirls.com',
    'thewildwest.com',
    'thinkweird.com',
    'thirdage.com',
    'thumbhead.com',
    'timothysmail.com',
    'timsmail.com',
    'tiscali.it',
    'tmicha.net',
    'toast.com',
    'toddsmail.com',
    'tomsmail.com',
    'tonysmail.com',
    'too-cool.net',
    'too-smart.com',
    'toowicked.com',
    'totalperformance.com',
    'totalrides.com',
    'toughbitch.net',
    'tougherthanyou.com',
    'tpg.com.au',
    'tracysmail.com',
    'trashflash.com',
    'trashmail.net',
    'triviafreak.com',
    'trojansrule.com',
    'troubledlife.com',
    'troysmail.com',
    'truckcity.com',
    'truckstrucks.com',
    'truthmail.com',
    'turbosport.com',
    'turkey.com',
    'twitchcity.com',
    'ucky.com',
    'ucs.com.tw',
    'uk2.net',
    'ukraine.com',
    'uni.de',
    'unicum.de',
    'unitedstates1.com',
    'unitycanada.com',
    'uol.com.br',
    'ureach.com',
    'usa.com',
    'usa.net',
    'usaroute66.com',
    'usroute66.com',
    'uswestmail.net',
    'utah1.com',
    'uymail.com',
    'vaingirl.com',
    'valise.com',
    'vcmail.com',
    'vermont1.com',
    'vfemail.net',
    'vickysmail.com',
    'virgilio.it',
    'virginia1.com',
    'virginriver.com',
    'virgo1.com',
    'virtualstudy.com',
    'voila.fr',
    'volunteerstate.com',
    'vorras.net',
    'wahhh.com',
    'walla.com',
    'walleyeangler.com',
    'wallstreetusa.com',
    'wallstreetview.com',
    'waltersmail.com',
    'wapicode.com',
    'warlocks.com',
    'washington1.com',
    'washingtondc1.com',
    'wassupwitdat.com',
    'watchmail.com',
    'waveshredder.com',
    'waynesmail.com',
    'wazhappenin.com',
    'wcox.com',
    'web2mail.com',
    'webbasedemail.com',
    'webemail.com',
    'webmail.co.za',
    'webmail.com.tw',
    'websurfer.co.za',
    'webtopmail.com',
    'weedmonkey.com',
    'weekonline.com',
    'weezee.com',
    'westchestergov.com',
    'westlock.com',
    'westmail.net',
    'westnet.com.au',
    'westvirginia1.com',
    'wetaskiwin.com',
    'whatupdog.org',
    'whitehorse1.com',
    'whiteknights.com',
    'whitelightning.com',
    'whiz-kid.net',
    'wiggedout.net',
    'wildgang.com',
    'wildgardener.com',
    'wildinthecity.com',
    'wildmale.com',
    'wildwildwest.com',
    'wisconsin1.com',
    'witty.org',
    'women.com',
    'wongfaye.com',
    'workmail.co.za',
    'worldemail.com',
    'wowmail.com',
    'www2000.net',
    'www4mail.org',
    'wyn.net',
    'wyoming1.com',
    'x-er.com',
    'x-mail.net',
    'x-sport.co.il',
    'xmail.net',
    'ya.com',
    'yachtemail.com',
    'yahoo.co.in',
    'yahoo.co.uk',
    'yahoo.com',
    'yahoo.com.br',
    'yahoo.es',
    'yahoomail.com',
    'yandex.ru',
    'yap.com.au',
    'yawmail.com',
    'yebox.com',
    'yellowknife1.com',
    'ymail.com',
    'yopmail.com',
    'youonlyliveonce.com',
    'youpy.fr',
    'yourmail.cc',
    'yukon1.com',
    'yyhmail.com',
    'ziplip.com',
    'zipmail.com',
    'zoho.com',
    'zxmail.com',
    'zzn.com',
    ])


country_codes = [
    ("AF", u"Afghanistan"),
    ("AX", u"Åland Islands"),
    ("AL", u"Albania"),
    ("DZ", u"Algeria"),
    ("AS", u"American Samoa"),
    ("AD", u"Andorra"),
    ("AO", u"Angola"),
    ("AI", u"Anguilla"),
    ("AQ", u"Antarctica"),
    ("AG", u"Antigua and Barbuda"),
    ("AR", u"Argentina"),
    ("AM", u"Armenia"),
    ("AW", u"Aruba"),
    ("AU", u"Australia"),
    ("AT", u"Austria"),
    ("AZ", u"Azerbaijan"),
    ("BS", u"Bahamas"),
    ("BH", u"Bahrain"),
    ("BD", u"Bangladesh"),
    ("BB", u"Barbados"),
    ("BY", u"Belarus"),
    ("BE", u"Belgium"),
    ("BZ", u"Belize"),
    ("BJ", u"Benin"),
    ("BM", u"Bermuda"),
    ("BT", u"Bhutan"),
    ("BO", u"Bolivia, Plurinational State of"),
    ("BQ", u"Bonaire, Sint Eustatius and Saba"),
    ("BA", u"Bosnia and Herzegovina"),
    ("BW", u"Botswana"),
    ("BV", u"Bouvet Island"),
    ("BR", u"Brazil"),
    ("IO", u"British Indian Ocean Territory"),
    ("BN", u"Brunei Darussalam"),
    ("BG", u"Bulgaria"),
    ("BF", u"Burkina Faso"),
    ("BI", u"Burundi"),
    ("KH", u"Cambodia"),
    ("CM", u"Cameroon"),
    ("CA", u"Canada"),
    ("CV", u"Cape Verde"),
    ("KY", u"Cayman Islands"),
    ("CF", u"Central African Republic"),
    ("TD", u"Chad"),
    ("CL", u"Chile"),
    ("CN", u"China"),
    ("CX", u"Christmas Island"),
    ("CC", u"Cocos (Keeling) Islands"),
    ("CO", u"Colombia"),
    ("KM", u"Comoros"),
    ("CG", u"Congo"),
    ("CD", u"Congo, the Democratic Republic of the"),
    ("CK", u"Cook Islands"),
    ("CR", u"Costa Rica"),
    ("CI", u"Côte d'Ivoire"),
    ("HR", u"Croatia"),
    ("CU", u"Cuba"),
    ("CW", u"Curaçao"),
    ("CY", u"Cyprus"),
    ("CZ", u"Czech Republic"),
    ("DK", u"Denmark"),
    ("DJ", u"Djibouti"),
    ("DM", u"Dominica"),
    ("DO", u"Dominican Republic"),
    ("EC", u"Ecuador"),
    ("EG", u"Egypt"),
    ("SV", u"El Salvador"),
    ("GQ", u"Equatorial Guinea"),
    ("ER", u"Eritrea"),
    ("EE", u"Estonia"),
    ("ET", u"Ethiopia"),
    ("FK", u"Falkland Islands (Malvinas)"),
    ("FO", u"Faroe Islands"),
    ("FJ", u"Fiji"),
    ("FI", u"Finland"),
    ("FR", u"France"),
    ("GF", u"French Guiana"),
    ("PF", u"French Polynesia"),
    ("TF", u"French Southern Territories"),
    ("GA", u"Gabon"),
    ("GM", u"Gambia"),
    ("GE", u"Georgia"),
    ("DE", u"Germany"),
    ("GH", u"Ghana"),
    ("GI", u"Gibraltar"),
    ("GR", u"Greece"),
    ("GL", u"Greenland"),
    ("GD", u"Grenada"),
    ("GP", u"Guadeloupe"),
    ("GU", u"Guam"),
    ("GT", u"Guatemala"),
    ("GG", u"Guernsey"),
    ("GN", u"Guinea"),
    ("GW", u"Guinea-Bissau"),
    ("GY", u"Guyana"),
    ("HT", u"Haiti"),
    ("HM", u"Heard Island and McDonald Islands"),
    ("VA", u"Holy See (Vatican City State)"),
    ("HN", u"Honduras"),
    ("HK", u"Hong Kong"),
    ("HU", u"Hungary"),
    ("IS", u"Iceland"),
    ("IN", u"India"),
    ("ID", u"Indonesia"),
    ("IR", u"Iran, Islamic Republic of"),
    ("IQ", u"Iraq"),
    ("IE", u"Ireland"),
    ("IM", u"Isle of Man"),
    ("IL", u"Israel"),
    ("IT", u"Italy"),
    ("JM", u"Jamaica"),
    ("JP", u"Japan"),
    ("JE", u"Jersey"),
    ("JO", u"Jordan"),
    ("KZ", u"Kazakhstan"),
    ("KE", u"Kenya"),
    ("KI", u"Kiribati"),
    ("KP", u"Korea, North"),
    ("KR", u"Korea, South"),
    ("KW", u"Kuwait"),
    ("KG", u"Kyrgyzstan"),
    ("LA", u"Lao People's Democratic Republic"),
    ("LV", u"Latvia"),
    ("LB", u"Lebanon"),
    ("LS", u"Lesotho"),
    ("LR", u"Liberia"),
    ("LY", u"Libya"),
    ("LI", u"Liechtenstein"),
    ("LT", u"Lithuania"),
    ("LU", u"Luxembourg"),
    ("MO", u"Macao"),
    ("MK", u"Macedonia, the former Yugoslav Republic of"),
    ("MG", u"Madagascar"),
    ("MW", u"Malawi"),
    ("MY", u"Malaysia"),
    ("MV", u"Maldives"),
    ("ML", u"Mali"),
    ("MT", u"Malta"),
    ("MH", u"Marshall Islands"),
    ("MQ", u"Martinique"),
    ("MR", u"Mauritania"),
    ("MU", u"Mauritius"),
    ("YT", u"Mayotte"),
    ("MX", u"Mexico"),
    ("FM", u"Micronesia, Federated States of"),
    ("MD", u"Moldova, Republic of"),
    ("MC", u"Monaco"),
    ("MN", u"Mongolia"),
    ("ME", u"Montenegro"),
    ("MS", u"Montserrat"),
    ("MA", u"Morocco"),
    ("MZ", u"Mozambique"),
    ("MM", u"Myanmar"),
    ("NA", u"Namibia"),
    ("NR", u"Nauru"),
    ("NP", u"Nepal"),
    ("NL", u"Netherlands"),
    ("NC", u"New Caledonia"),
    ("NZ", u"New Zealand"),
    ("NI", u"Nicaragua"),
    ("NE", u"Niger"),
    ("NG", u"Nigeria"),
    ("NU", u"Niue"),
    ("NF", u"Norfolk Island"),
    ("MP", u"Northern Mariana Islands"),
    ("NO", u"Norway"),
    ("OM", u"Oman"),
    ("PK", u"Pakistan"),
    ("PW", u"Palau"),
    ("PS", u"Palestinian Territory, Occupied"),
    ("PA", u"Panama"),
    ("PG", u"Papua New Guinea"),
    ("PY", u"Paraguay"),
    ("PE", u"Peru"),
    ("PH", u"Philippines"),
    ("PN", u"Pitcairn"),
    ("PL", u"Poland"),
    ("PT", u"Portugal"),
    ("PR", u"Puerto Rico"),
    ("QA", u"Qatar"),
    ("RE", u"Réunion"),
    ("RO", u"Romania"),
    ("RU", u"Russian Federation"),
    ("RW", u"Rwanda"),
    ("BL", u"Saint Barthélemy"),
    ("SH", u"Saint Helena, Ascension and Tristan da Cunha"),
    ("KN", u"Saint Kitts and Nevis"),
    ("LC", u"Saint Lucia"),
    ("MF", u"Saint Martin (French part)"),
    ("PM", u"Saint Pierre and Miquelon"),
    ("VC", u"Saint Vincent and the Grenadines"),
    ("WS", u"Samoa"),
    ("SM", u"San Marino"),
    ("ST", u"Sao Tome and Principe"),
    ("SA", u"Saudi Arabia"),
    ("SN", u"Senegal"),
    ("RS", u"Serbia"),
    ("SC", u"Seychelles"),
    ("SL", u"Sierra Leone"),
    ("SG", u"Singapore"),
    ("SX", u"Sint Maarten (Dutch part)"),
    ("SK", u"Slovakia"),
    ("SI", u"Slovenia"),
    ("SB", u"Solomon Islands"),
    ("SO", u"Somalia"),
    ("ZA", u"South Africa"),
    ("GS", u"South Georgia and the South Sandwich Islands"),
    ("SS", u"South Sudan"),
    ("ES", u"Spain"),
    ("LK", u"Sri Lanka"),
    ("SD", u"Sudan"),
    ("SR", u"Suriname"),
    ("SJ", u"Svalbard and Jan Mayen"),
    ("SZ", u"Swaziland"),
    ("SE", u"Sweden"),
    ("CH", u"Switzerland"),
    ("SY", u"Syrian Arab Republic"),
    ("TW", u"Taiwan, Province of China"),
    ("TJ", u"Tajikistan"),
    ("TZ", u"Tanzania, United Republic of"),
    ("TH", u"Thailand"),
    ("TL", u"Timor-Leste"),
    ("TG", u"Togo"),
    ("TK", u"Tokelau"),
    ("TO", u"Tonga"),
    ("TT", u"Trinidad and Tobago"),
    ("TN", u"Tunisia"),
    ("TR", u"Turkey"),
    ("TM", u"Turkmenistan"),
    ("TC", u"Turks and Caicos Islands"),
    ("TV", u"Tuvalu"),
    ("UG", u"Uganda"),
    ("UA", u"Ukraine"),
    ("AE", u"United Arab Emirates"),
    ("GB", u"United Kingdom"),
    ("US", u"United States"),
    ("UM", u"United States Minor Outlying Islands"),
    ("UY", u"Uruguay"),
    ("UZ", u"Uzbekistan"),
    ("VU", u"Vanuatu"),
    ("VE", u"Venezuela, Bolivarian Republic of"),
    ("VN", u"Viet Nam"),
    ("VG", u"Virgin Islands, British"),
    ("VI", u"Virgin Islands, U.S."),
    ("WF", u"Wallis and Futuna"),
    ("EH", u"Western Sahara"),
    ("YE", u"Yemen"),
    ("ZM", u"Zambia"),
    ("ZW", u"Zimbabwe"),
]
