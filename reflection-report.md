# Refleksjonsrapport - Programmering med KI

## 1. Gruppeinformasjon

**Gruppenavn:** StudyBuddy AI

**Gruppemedlemmer:**
- [Navn 1] - [Student-ID/E-post]
- [Navn 2] - [Student-ID/E-post]
- [Kine Pettersen] - [Student-ID/kinempettersen@gmail.com]

**Dato:** 04.12.2025

-- -

## 2. Utviklingsprosessen

### 2.1 Oversikt over prosjektet
Prosjektet StudyBuddy-AI realiserer kjerneverdien i applikasjonen: å transformere opplastet læringsstoff (PDF/DOCX) til personlige sammendrag, flashcards og quizer. Brukeren laster opp et dokument, backend trekker ut tekst, og en KI-tjeneste (primært Google Gemini, eventuelt OpenAI GPT-4) genererer læringsressurser som lagres i Firestore og vises i et interaktivt grensesnitt. Målet er å gi studenter en intuitiv og effektiv måte å bearbeide store mengder akademisk tekst på, slik at de lettere kan lære gjennom aktiv repetisjon og selvtesting. Prosjektet kombinerer teknologi, pedagogikk og KI for å redusere tiden fra rått fagstoff til strukturert, anvendbart læringsmateriale, og demonstrerer samtidig en praktisk og etisk bruk av generativ KI i høyere utdanning.

### 2.2 Arbeidsmetodikk
Arbeidet ble organisert etter en lettversjon av Agile-metodikk, med korte iterasjoner og tydelige delmål basert på akseptansekriteriene (AC 2.1–2.5).

I oppstartsfasen ønsket gruppen å utforske hvordan Gemini kunne brukes direkte i Visual Studio Code (VSC), slik at alle fikk en praktisk forståelse av KI-integrasjonen før prosjektet tok form. Gruppen besto av medlemmer med ulik bakgrunn: noen hadde programmeringserfaring, andre var helt nye. Dette ga en variert læringsdynamikk og stilte krav til tilpasning i arbeidsmetodikken.

Det ble avholdt et oppstartsmøte hvor gruppen opprettet en Jira-side for oppgavefordeling og fremdriftskontroll. Verktøyet ble lite brukt, og all kommunikasjon og koordinering ble derfor flyttet til Microsoft Teams, som fungerte bedre. Her hadde vi ukentlige møter, fordelte oppgaver, diskuterte fremdrift og satte mål for neste periode.

For å sikre læring for alle besluttet vi at hvert medlem skulle delta i alle deler av prosessen – planlegging, koding, testing og dokumentasjon. Dette styrket forståelsen av helheten og forbedret samarbeid og kommunikasjon.

Gruppen startet med fire medlemmer, men i uke 45 valgte Sara å avslutte deltakelsen fordi arbeidsform og tempo ikke passet hennes preferanser. Resten av gruppen fordelte ansvar basert på styrker: Birgitte bidro med struktur, kritiske spørsmål og detaljfokus, Hamdi hadde teknisk erfaring og var spesielt god på å lese og rette kodefeil, mens Kine, som var helt ny i programmering, brukte prosjektet til å lære gjennom aktiv deltakelse.

Samarbeidsverktøy: Vi brukte VSC til utvikling, GitHub til versjonskontroll og pull requests med kodegjennomgang, og Teams til kommunikasjon, møter og avklaringer.

KI var en sentral støtte gjennom hele utviklingsprosessen. Gemini-integrasjonen i VSC ble brukt til å kommunisere med agenter, gjennomføre idémyldring og få forslag til kodeforbedringer. Dette var særlig nyttig i tidlige faser, der vi testet ulike tilnærminger og løste tekniske utfordringer fortløpende. I tillegg brukte vi ChatGPT, spesielt til feilsøking og tolkning av feilmeldinger. ChatGPT forklarte feilmeldingene, foreslo løsninger og hjalp oss å forstå hvorfor koden ikke fungerte som forventet. Kombinasjonen av Gemini og ChatGPT ga både idéutvikling, teknisk støtte og læring underveis.

### 2.3 Teknologi og verktøy
[Liste over de viktigste teknologiene og verktøyene dere brukte]
- Frontend: [f.eks. NextJS, HTML/CSS]
- Backend: [f.eks. Python/FastAPI]
- Database: [f.eks. Supabase, MongoDB, PostgreSQL]
- KI-verktøy: [f.eks. Claude Code, Gemini CLI, GPT-5 Codex]
- Andre verktøy: [f.eks. VS Code, BMAD etc]

### 2.4 Utviklingsfaser
[Beskriv de ulike fasene i utviklingen]

**Fase 1: Planlegging**
- [Hva gjorde dere i denne fasen?]
- [Hvordan brukte dere KI her? Husk å lagre promptene deres! Inkluder ALLE stegene dere gjorde.]

**Fase 2: Utvikling**
- [Hva gjorde dere i denne fasen?]
- [Hvordan brukte dere KI her? Husk å lagre promptene deres! Inkluder ALLE stegene dere gjorde.]

-- -

## 3. Utfordringer og løsninger

### 3.1 Tekniske utfordringer
[Beskriv 2-3 konkrete tekniske problemer dere møtte]

**Utfordring 1: [Tittel]**
- Problem: [Beskriv problemet]
- Løsning: [Hvordan løste dere det?]
- KI sin rolle: [Hvordan hjalp eller hindret KI dere?]

**Utfordring 2: [Tittel]**
- Problem: [Beskriv problemet]
- Løsning: [Hvordan løste dere det?]
- KI sin rolle: [Hvordan hjalp eller hindret KI dere?]

### 3.2 Samarbeidsutfordringer
En sentral samarbeidsutfordring var ulikt erfaringsnivå innen programmering. Noen hadde tidligere erfaring, andre var helt nye. Dette krevde ekstra tålmodighet og støtte, spesielt i de tekniske fasene. For å sikre læringsutbytte for alle fikk hvert medlem prøve seg på flere deler av prosessen – koding, testing og dokumentasjon – slik at alle fikk en helhetlig systemforståelse.

Kommunikasjonen ble tidlig flyttet fra Jira til Microsoft Teams, som fungerte bedre som samarbeidsverktøy. Teams ble brukt til ukentlige møter, deling av kode og løpende avklaringer. Dette ga bedre kontinuitet og færre misforståelser.

Da Sara valgte å trekke seg i uke 45 på grunn av ulik oppfatning av tempo og arbeidsmetode, oppsto behov for omstrukturering. Oppgaver som tidligere var fordelt på fire personer måtte omprioriteres, og ansvar og roller ble tydeliggjort på nytt. Arbeidsplanen ble justert, og de gjenværende medlemmene fordelte oppgavene mer strategisk etter kompetanse og kapasitet. Omstillingen ga økt arbeidsmengde på kort sikt, men styrket samarbeidet og ansvarsbevisstheten. Det ble lagt vekt på godt arbeidsmiljø og åpen kommunikasjon, slik at alle følte seg trygge på egne oppgaver og bidrag.

Når det gjelder samarbeid med lærere og undervisningsopplegg, møtte vi flere utfordringer. Læreboken som skulle brukes i faget ble aldri ferdigstilt, og flere kapitler som skulle publiseres fortløpende kom aldri. Dette skapte usikkerhet om forventet faglig innhold og gjorde det vanskelig å følge pensum.

Det ble etter hvert lagt ut en tidsplan for prosjektfasene, men denne ble ikke fulgt i undervisningen. Forsinkelser gjorde at faglig innhold i forelesningene ikke stemte med progresjonen i prosjektet. Dette gjorde det uklart hva vi skulle prioritere, og vi opplevde å komme bakpå tidlig fordi planlegging, utvikling og KI-integrasjon ikke var koordinert med undervisningen.

Vi erfarte også at det ville vært enklere å følge undervisningen dersom forelesningene hadde vært forhåndsinnspilt. Da kunne vi tilpasset læringen bedre til egen tid og unngått tekniske problemer knyttet til lærernes bruk av KI i sanntid. Forelesningene de siste 4–5 ukene, som omhandlet prosjektet og praktisk KI-bruk, kom for sent. Gruppen hadde da allerede startet prosjektet uten full forståelse av krav, læringsmål og verktøy. Mange opplevde også “beer-game”-delen av undervisningen som forvirrende og lite relevant for prosjektet, noe som økte uklarheten.

Når det gjelder oppfølging, opplevde vi gjentatte utfordringer med å få kontakt med lærere. Avtalte veiledningsmøter ble ikke alltid gjennomført, og det var tidvis vanskelig å få svar på spørsmål eller booke nye møter. Dette gjorde at mye av læringen og problemløsningen måtte håndteres internt i gruppen eller ved hjelp av KI-verktøy. Til tross for dette ble samarbeidet internt styrket. Vi ble mer selvstendige og lærte å finne løsninger på egen hånd. Samtidig viste erfaringen hvor viktig tydelig struktur, tilgjengelig veiledning og stabile læringsressurser er for at nettbaserte prosjekter skal fungere godt.

### 3.3 KI-spesifikke utfordringer
[Problemer spesifikt knyttet til bruk av KI]
- [f.eks. Feil kode fra KI, misforståelser, inkonsistent kvalitet]
- [Hvordan håndterte dere disse?]

## 4. Kritisk vurdering av KI sin påvirkning

### 4.1 Fordeler med KI-assistanse
KI bidro til å øke effektiviteten i utviklingsprosessen. Gemini ble integrert i Visual Studio Code og brukt til å generere kodeforslag, forklare logikk og strukturere funksjoner, noe som reduserte tid brukt på research og manuell feilsøking. ChatGPT supplerte dette, særlig ved tolkning av feilmeldinger og forklaring av årsaker til feil. Begge verktøy ble brukt aktivt i idémyldring, der vi testet ulike løsninger for arkitektur, funksjonalitet og brukerflyt. Hvert medlem brukte KI på sin måte – til å forbedre kode, forstå struktur eller utforske alternativer. Dette førte til raskere fremdrift og en mer dynamisk prosess, der KI fungerte som problemløser og idégenerator.


Læring og forståelse
For medlemmer med mindre programmeringserfaring fungerte KI som et personlig læringsverktøy. Ved å stille spørsmål til Gemini og ChatGPT fikk de raskt forklaringer på begreper, syntaks og funksjonslogikk, noe som styrket forståelsen og gjorde det enklere å delta i tekniske diskusjoner. KI ble brukt til å utforske konsepter, rette feil og forbedre kode. For mer erfarne medlemmer ble KI et verktøy for å validere ideer og heve kvaliteten på løsninger.

Kvalitet på koden
KI-verktøyene bidro også til en mer strukturert og robust kodebase. Gemini foreslo forbedringer innen lesbarhet, feilhåndtering og optimalisering, og hjalp med å oppdage svakheter tidlig i utviklingsløpet. ChatGPT bidro med alternative løsninger og bedre forståelse av feilmeldinger, som ofte førte til forbedrede implementasjoner. Denne kombinasjonen gjorde at koden gradvis ble mer stabil og at gruppen opparbeidet seg bedre forståelse av beste praksis innen utvikling.

### 4.2 Begrensninger og ulemper
Kvalitet og pålitelighet
Selv om KI-verktøyene ga rask fremdrift, var kvaliteten på svarene ikke alltid pålitelig. Spesielt ved bruk av Gemini opplevde vi at koden til tider inneholdt syntaksfeil, utdaterte biblioteker eller manglende forståelse av sammenhengen i prosjektet. Dette krevde ekstra tid til manuell feilsøking og testing. I noen tilfeller foreslo KI løsninger som virket logiske, men som senere viste seg å være teknisk uegnede. Dette understreker behovet for menneskelig kontroll og kritisk vurdering av KI-generert innhold.

Avhengighet og forståelse
I starten stolte vi for mye på KI uten å reflektere nok over resultatene. Kode ble tatt videre uten grundig vurdering, og vi oppdaget i etterkant at enkelte løsninger var feil eller lite hensiktsmessige. I tillegg ble ikke promptene lagret systematisk, noe som gjorde det vanskelig å spore hva som var gjort og hvorfor.
Dette ble en viktig læring. Etter de første fasene innførte vi en mer strukturert praksis: vi lagret alle KI-prompter, dokumenterte svar og ba Gemini lage korte sammendrag fra hver fase. Dermed gikk vi fra å bruke KI som et “hurtigverktøy” til å bruke det som en integrert lærings- og dokumentasjonsressurs.

Kreativitet og problemløsning
KI-forslagene var ofte konvensjonelle og ikke nødvendigvis innovative. Gruppen måtte derfor aktivt utfordre forslagene for å tenke utover standardløsninger. Det ble viktig å bruke KI som støtte, ikke som erstatning for egen refleksjon og problemløsning.

### 4.3 Sammenligning: Med og uten KI
KI hadde stor betydning for hvordan gruppen kunne gjennomføre prosjektet uten inngående kunnskap om alle verktøyene. Med støtte fra Gemini og ChatGPT kunne vi skrive, forstå og rette kode uten å kunne alle kommandoer, syntaksregler og bibliotekreferanser. KI forklarte løpende hva koden gjorde og foreslo forbedringer, slik at vi kunne fokusere mer på struktur og funksjonalitet.

På backend-siden gjorde KI FastAPI- og Firestore-integrasjon mer håndterlig. Gemini hjalp med å skrive grunnleggende funksjoner og filvalidering, mens ChatGPT forklarte feilmeldinger og hvordan de kunne rettes. På frontend ble det enklere å bygge et funksjonelt og visuelt grensesnitt uten inngående kjennskap til HTML, CSS og JavaScript. KI foreslo kode for interaktive elementer som flashcards og quizer og forklarte koblingen mot databasen.

Uten KI-støtte ville læringskurven vært brattere, men den tekniske forståelsen dypere. Vi måtte brukt betydelig mer tid på grunnleggende konsepter, biblioteker, syntaks og feilhåndtering. Med den tilgjengelige tiden ville det vært lite realistisk å oppnå samme funksjonalitet og kvalitet. Prosjektet ville trolig hatt lavere funksjonalitet, men høyere faglig dybde. Med KI fikk vi et mer komplett og visuelt ferdig produkt, selv om deler av koden ble forstått på et mer overordnet nivå.


### 4.4 Samlet vurdering
KI har totalt sett hatt en tydelig positiv innvirkning på prosjektet. Uten KI ville det vært svært krevende å gjennomføre et så teknisk komplekst prosjekt innenfor tidsrammen. Gemini og ChatGPT gjorde det mulig å bygge funksjonell kode, løse problemer raskt og forstå komplekse prosesser uten inngående forkunnskap i alle språk og rammeverk.

Samtidig viste erfaringen at KI ikke kan erstatte menneskelig forståelse og kritisk tenkning. De første fasene illustrerte hvor lett det er å stole for mye på KI. Etter hvert ble bruken mer strukturert: vi lagret prompter, dokumenterte forslag og kvalitetssikret koden fortløpende. Overgangen fra ukritisk til målrettet bruk er en av de viktigste læringene.

Vi vurderer KI som en netto positiv faktor: den ga høyere produktivitet, bedre struktur og et mer komplett sluttprodukt enn det som realistisk kunne vært oppnådd uten KI. Samtidig tydeliggjorde prosjektet at KI bør brukes som samarbeidspartner – ikke som erstatning for egen kunnskap.


## 5. Etiske implikasjoner

### 5.1 Ansvar og eierskap
Når KI-verktøy som Gemini og ChatGPT bidrar i kodeutvikling, oppstår spørsmålet om ansvar og eierskap. KI genererer kode basert på treningsdata og mønstre, og det kan være vanskelig å vurdere hvor originalt resultatet er. Dette reiser spørsmål om opphavsrett: kan man si at koden fullt ut er laget av studentene når deler er foreslått av KI?

Vi mener at ansvaret for koden alltid ligger hos utvikleren, også når KI har bidratt. KI er et støtteverktøy, ikke en selvstendig skaper. Forslag fra KI må vurderes kritisk, testes og tilpasses før de tas i bruk. Slik ivaretas både kvalitet og faglig eierskap.

Samtidig er grensen mellom menneskelig og KI-generert innhold ikke alltid tydelig. I praksis blir eierskapet et samspill mellom menneskelig arbeid, teknologisk støtte og systemkunnskap. Etisk sett mener vi likevel at vi som studenter har det endelige ansvaret for funksjonalitet, kvalitet og konsekvenser av koden som implementeres.


### 5.2 Transparens
I dette prosjektet har vi vært åpne om bruken av Gemini og ChatGPT. Vi har dokumentert hvilke deler av koden som var foreslått av KI, og lagret prompter og svar i egne filer. Dette ga bedre oversikt, læring og kvalitetssikring, og gjorde det enklere å skille mellom egen innsats og KI-generert innhold.

Vi mener transparens er avgjørende for å opprettholde tillit mellom studenter, lærere og brukere. Hvis KI-bruk holdes skjult, kan det skape tvil om hvor mye av arbeidet som faktisk er studentens eget, og undergrave læringsmål der metode og forståelse er like viktige som sluttresultatet.

Samtidig kan det i arbeidslivet være lite praktisk å dokumentere hvert enkelt KI-forslag. Likevel mener vi at i akademiske prosjekter bør graden av KI-assistanse synliggjøres tydelig, av hensyn til etikk, faglig integritet og troverdighet.


### 5.3 Påvirkning på læring og kompetanse
Erfaringene våre viser at KI har stort potensial som læringsstøtte, men at bruken må balanseres. KI gjorde det mulig å jobbe effektivt med avanserte verktøy uten at alle hadde tung teknisk bakgrunn. Gemini og ChatGPT forklarte begreper, løste kodefeil og gjorde komplekse prosesser mer tilgjengelige, noe som ga raskere læringskurve og økt mestringsfølelse.

Samtidig kan KI redusere behovet for aktiv problemløsning. Når man får raske svar og ferdige kodeforslag, kan den dype forståelsen av logikk og struktur svekkes. Dette opplevde vi særlig i starten, da mye arbeid ble gjort av KI uten tilstrekkelig refleksjon. Etter hvert begynte vi å bruke KI mer som veileder enn som “automatisert problemløser”.

Generelt ser vi at KI i utdanning har både pedagogisk og etisk betydning. Den kan gi umiddelbar støtte i fag som programmering, språk og rapportskriving, men også skape risiko for passiv læring. Utfordringen fremover blir å bruke KI til aktiv læring, refleksjon og forståelse – ikke som snarvei til ferdige svar. Vår erfaring tilsier at KI fungerer best som en digital mentor som støtter studentenes egen tankeprosess, ikke erstatter den.


### 5.4 Arbeidsmarkedet
Generativ KI endrer allerede arbeidslivet i IT-sektoren. Oppgaver som koding, feilsøking og dokumentasjon kan delvis automatiseres gjennom verktøy som Gemini og ChatGPT. Utviklere blir ikke overflødige, men kompetansebehovet endres. Det blir viktigere å forstå, validere og forbedre KI-generert kode enn å kunne alt fra bunnen av.

Prosjektet vårt illustrerer hvordan KI kan senke terskelen for å delta i tekniske prosjekter. Selv de uten programmeringserfaring kunne bidra fordi KI forklarte og skrev kode. I arbeidslivet kan dette gi mer tverrfaglig samarbeid, der ulike fagbakgrunner deltar i utviklingsprosesser.

Samtidig øker kravet til kritisk tenkning, analytisk forståelse og evnen til å kommunisere presist med KI-verktøy. Utviklerrollen kan i større grad bli å fungere som KI-veileder og kvalitetssikrer. Fremtidens utviklere må kombinere teknologisk innsikt med refleksjon, kontroll og ansvarsfølelse.

Vi tror ikke KI vil erstatte utviklere, men endre hva det vil si å være utvikler. Evnen til å samarbeide med intelligente systemer, forstå begrensningene deres og bruke dem strategisk, blir sentral i et mer KI-drevet arbeidsmarked.

### 5.5 Datasikkerhet og personvern
Bruk av KI-verktøy reiser viktige spørsmål om datasikkerhet og personvern. Når man deler kode, tekst eller dokumenter med eksterne KI-tjenester, sendes data til servere utenfor egen kontroll. Dette innebærer risiko for lagring, analyse og bruk til videre modelltrening.

I dette prosjektet var vi bevisste på å ikke dele sensitiv eller identifiserbar informasjon med Gemini eller ChatGPT. Dokumenter og prompter inneholdt kun teknisk og faglig innhold uten persondata.

Likevel er det lett å undervurdere datasikkerhet når man bruker KI. Mange brukere vet lite om hvordan data behandles, og hvilke rettigheter de har. Det finnes heller ikke alltid tydelige grenser for hvordan leverandører bruker innsendte data til modellforbedring. Dette viser behovet for kritisk bevissthet og kunnskap hos studenter og utviklere.

Etisk sett ligger personvernansvaret hos brukeren, også når data sendes til tredjepart. I akademiske og profesjonelle sammenhenger bør man følge prinsippet om “data minimization” – kun dele det som er nødvendig for å få et relevant svar.

Vi mener utdanningsinstitusjoner og utviklingsmiljøer bør etablere klare retningslinjer for sikker bruk av KI, inkludert transparens, datalagring og bruk av tredjepartstjenester. Dette er viktig for å sikre at innovasjon og læring skjer på en trygg og etisk måte.


## 6. Teknologiske implikasjoner

### 6.1 Kodekvalitet og vedlikehold
- Hvordan påvirker KI-generert kode langsiktig vedlikehold?
- Er KI-kode like forståelig som menneskeskrevet kode?
- Utfordringer med å debugge KI-generert kode

### 6.2 Standarder og beste praksis
- Følger KI alltid beste praksis og industristandarder?
- Eksempler på hvor KI foreslo utdaterte eller dårlige løsninger
- Viktigheten av å validere KI sine forslag

### 6.3 Fremtidig utvikling
- Hvordan tror dere KI vil påvirke programvareutvikling fremover?
- Hvilke ferdigheter blir viktigere for utviklere?
- Deres anbefalinger for hvordan man bør bruke KI i utviklingsprosesser

-- -

## 7. Konklusjon og læring

### 7.1 Viktigste lærdommer
[Liste de 3-5 viktigste tingene dere lærte gjennom prosjektet]
1. [Lærdom 1]
2. [Lærdom 2]
3. [Lærdom 3]

### 7.2 Hva ville dere gjort annerledes?
[Reflekter over hva dere ville endret hvis dere skulle startet på nytt]
- [Tekniske valg]
- [Bruk av KI]
- [Samarbeid og organisering]

### 7.3 Anbefalinger
[Deres anbefalinger til andre studenter som skal bruke KI i utvikling]
- [Råd om effektiv bruk av KI]
- [Fallgruver å unngå]
- [Beste praksis dere oppdaget]

Basert på erfaringene fra prosjektet anbefaler vi at studenter som skal bruke KI i programmeringsprosjekter har et bevisst og strukturert forhold til verktøyene. KI gir best resultat når den brukes målrettet og kritisk.

Råd om effektiv bruk av KI:
- Bruk KI som samtalepartner og veileder, ikke som automatisk kodegenerator. Still spørsmål, be om forklaringer, og be KI utdype hvorfor en løsning fungerer.
- Vær presis i promptene. Jo tydeligere problemet beskrives, desto mer relevante svar.
- Kombiner gjerne flere KI-verktøy, for eksempel Gemini til kodeutvikling og ChatGPT til feilsøking og konseptforklaringer.
- Dokumenter bruken. Lagre prompter og svar underveis for å kunne spore hvilke forslag som ble brukt.


Fallgruver å unngå:
- Ikke stol blindt på kodeforslag. Selv små feil kan gi logiske problemer eller sikkerhetsbrudd. Test og forstå hva koden gjør.
- Unngå å bruke KI som erstatning for egen læring. Reflekter over prosessen, ikke bare resultatet.
- Vær forsiktig med hva du deler. Ikke legg inn sensitiv informasjon, passord eller nøkkelfiler i promptene.


Beste praksis:
- Start prosjektet med felles retningslinjer for hvordan gruppen skal bruke KI – når, til hva og hvordan det skal dokumenteres.
- Bruk KI aktivt i brainstorming og idéutvikling for å utforske alternativer før dere velger retning.
- Når KI genererer kode, be også om forklaringer linje for linje for å øke læringsverdien.
- Sørg for at minst én i gruppen kvalitetssikrer alle forslag før de implementeres.


Oppsummert mener vi at nøkkelen til vellykket KI-bruk er balansen mellom effektivitet og forståelse. Når KI brukes bevisst, som støtte og ikke som erstatning, kan den både styrke læringsprosessen og øke kvaliteten på sluttproduktet.

### 7.4 Personlig refleksjon (individuelt)

**[Navn på gruppemedlem 1]:**
[Personlig refleksjon over egen læring og utvikling]

**[Navn på gruppemedlem 2]:**
[Personlig refleksjon over egen læring og utvikling]

**[Kine]:**
Som nybegynner uten tidligere erfaring med koding har dette prosjektet vært både utfordrende og svært lærerikt. I starten opplevde jeg usikkerhet rundt mange tekniske begreper og verktøy, men bruken av KI – spesielt Gemini sammen med VSC og ChatGPT – gjorde det mulig for meg å forstå og lære i mitt eget tempo. KI hjalp meg med å oversette teknisk kode til forståelige forklaringer og gjorde det mulig å prøve, feile og lære underveis.

Samtidig har prosjektet vist meg hvor avgjørende godt samarbeid er i et gruppeprosjekt. I begynnelsen oppsto det noen utfordringer med at enkelte gruppemedlemmer ikke møtte forberedt til møtene, og at avtalte møtetider ble endret på kort varsel. I en allerede travel hverdag ble det tydelig hvor viktig det er å holde avtaler og ta ansvar for gruppens fremdrift. Et gruppeprosjekt med flere deltakere krever at alle er dedikerte – når én gjør et valg, påvirker det alle. Denne erfaringen har lært meg mye om både struktur, kommunikasjon og respekt for andres tid.

Det skal også nevnes at jeg har fått mye hjelp og støtte fra Birgitte og Hamdi, som har vært utrolig fleksible, tålmodige og hjelpsomme gjennom hele prosessen. Det har vært rom for å stille spørsmål og prøve seg frem selvom om man er usikker, det har alltid vært rom for å stille spørsmål, og vi har i flere møter jobbet sammen i VSC ved deling av skjerm for å lære. 

Selv om jeg har lært mye og fått bedre forståelse for hvordan programmering og KI fungerer, ser jeg fortsatt på meg selv som en nybegynner, bare med litt mer kunnskap enn før. Jeg har fortsatt ikke forstått alt, men nå vet jeg hvor jeg skal begynne for å lære mer. Programmering har alltid vært litt høytsvevede og gresk, og det at jeg når kan sitte i VSC og promte er gøy. 

Gjennom dette prosjektet har jeg ikke bare lært om programmering og KI, men også om samarbeid, ansvar og hvordan man kan vokse i møte med utfordringer. Erfaringen har gitt meg en ny forståelse av hvor mye man kan oppnå når man kombinerer teknologi, samarbeid og læringsvilje.

-- -

## 8. Vedlegg (valgfritt)

- Skjermbilder av applikasjonen
- Lenke til GitHub repository
- Annen relevant dokumentasjon

-- -

**Ordantall:** [Ca. antall ord]

**Forventet lengde:** 3000-5000 ord (avhengig av gruppestørrelse og prosjektets kompleksitet)