# Refleksjonsrapport - Programmering med KI

## 1. Gruppeinformasjon

**Gruppenavn:** [Navn på gruppen]

**Gruppemedlemmer:**
- Birgitte Bellsund - 201583/birgitte.bellsund@himolde.no 
- Hamdi Abdi Mohamed - Student-ID/hamdi.a.mohamed@himolde.no
- Kine Marie Pettersen - Student-ID/kine.m.pettersen@himolde.no

**Dato:** 16.11.2025

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
For denne appen har vi tatt i bruk følgende teknologi og verktøy: 
- Frontend: React (Vite), TypeScript, Material-UI:  
- Backend: Node.js/Express.js (API Gateway, Brukerdata) 
- AI Service: Python/FastAPI 
- KI-verktøy: Google Gemini API, Google Cloud AI
- Database: PostgreSQL, S3-objektlagring 
- DevOps: Docker, Kubernetes, GitHub Actions 

### 2.4 Utviklingsfaser
[Beskriv de ulike fasene i utviklingen]

**Fase 1: Planlegging**
I denne fasen tok vi i bruk BMADs agent for å brainstorme med SCAMPER-metoden for å komme frem til nye funskjoner og forbedringer for StudyBuddy. Disse forbedringene fokuserte blant annet på en smartere måte å organisere generert læringsmateriale(quiz, sammendrag, flashcards), økt brukerengasjement og en enklere systemarkitektur. De mest relevante resultatene fra brainstormingen var et AI-drevet Topic Map som automatisk strukturerer læringsmateriale. Videre kom vi frem til micro-læring med korte og fleksible økter i tillegg til lengre økter. Et annet resultat fra brainstormingen besto i å introdusere skylagring hos bruker istedenfor intern applagring, noe som reduserer kompleksitet og ekstra arbeid og kostnad ift lagring av materiale. I tillegg kom vi frem til en omvendt arbeidsflyt der AI først kartlegger brukerens mål før en skreddersydd studieplan blir laget. Disse forslagene bidro til å skape en mer adaptiv, effektiv og personlig læringsopplevelse i StudyBuddy AI. 

**Fase 2: Utvikling**
I utviklingsfasen startet arbeidet med å synkronisere det lokale repositoriet med main-grenen og identifisere "Install frontend dependencies" som neste steg i arbeidsflyten. Et innledende forsøk på npm install feilet i frontend-mappen grunnet manglende package.json, noe som ble løst ved å opprette en midlertidig fil med basisavhengigheter for å fullføre installasjonen. Etter vellykket installasjon ble de midlertidige filene umiddelbart fjernet igjen. 

Deretter ble fokuset flyttet til å etablere en ny React-applikasjon i mappen new-frontend ved bruk av create-react-app. Gjennom hele prosessen ble statusfilen bmm-workflow-status.md kontinuerlig oppdatert for å reflektere fullføringen av fasen og angi det neste logiske steget: å starte utviklingsserveren for den nyopprettede frontend-applikasjonen. Til slutt ble alle endringer, inkludert den komplette frontend-applikasjonen, committet til repositoriet. 

-- -

## 3. Utfordringer og løsninger

### 3.1 Tekniske utfordringer
[Beskriv 2-3 konkrete tekniske problemer dere møtte]

**Utfordring 1: [Grense på Gemini CLI ]**
- Problem: Maksimumskvoten for Gemini CLI ble nådd, noe som medførte stopp i bruk til neste dag. Dette skjedde etter intensiv bruk og ga en feilmelding om at kvoten var oppbrukt. Vi måtte vente i 24 timer for å få tilgang til en full økt igjen.  
- Løsning: Det var ingen rask løsning – vi måtte vente ut perioden før tilgangen ble gjenopprettet.  
- KI sin rolle: KI hjalp med å informere om kvotegrenser og ga beskjed om ventetid, men videre arbeid ble stanset og det ble ikke gitt noe assistanse ift å omgå grensen eller få bedre ressursutnyttelse, kun standard beskjed om å vente. 

**Utfordring 2: [Tester feiler]**
- Problem: En eller flere tester mislyktes fordi API-nøkkelen manglet eller var plassert feil. Dette førte til mislykket autentisering og stoppet videre testing.   
- Løsning: Problemet ble løst ved å spørre eksterne KI-chatboter. Svaret var at API-nøkkelen måtte ligge i riktig mappe eller .env-fil, for eksempel i en .gemini-mappe med en tilhørende .env-fil, eller legges inn som en miljøvariabel for at Gemini CLI skal fungere korrekt.  
- KI sin rolle: Det var en dårlig løsning å prøve å forstå gjennom Gemini CLI sine svar hva som var årsak til feilene eller konkrete løsningsforslag. I stedet var det langt mer effektivt å få direkte svar og løsninger fra eksterne AI-chatboter, som ga nyttige tips om korrekt plassering av nøkkelen og feilkildene og som løste problemet. 

**Utfordring 3: [Gemin CLI bekrefteles loop]**
- Problem: Noen ganger satte gemini seg fast i en loop der gemini utfører en oppgave og vil at bruker skal bekrefte med [yes/y]. Når man bekrefter dette blir svaret satt i en kø og gemini bare går uten at oppgaven blir utført. Selv når man avbryter og prøver igjen løser det seg ikke.    
- øsning: Bruke gemini chatbot for å høre hva som er problemet og få en kommando som gjør at gemini ikke trenger en ekstra bekreftelse fra bruker. 
- KI sin rolle:  

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

-- -

## 4. Kritisk vurdering av KI sin påvirkning

### 4.1 Fordeler med KI-assistanse
KI bidro til å øke effektiviteten i utviklingsprosessen. Gemini ble integrert i Visual Studio Code og brukt til å generere kodeforslag, forklare logikk og strukturere funksjoner, noe som reduserte tid brukt på research og manuell feilsøking. ChatGPT supplerte dette, særlig ved tolkning av feilmeldinger og forklaring av årsaker til feil. Begge verktøy ble brukt aktivt i idémyldring, der vi testet ulike løsninger for arkitektur, funksjonalitet og brukerflyt. Hvert medlem brukte KI på sin måte – til å forbedre kode, forstå struktur eller utforske alternativer. Dette førte til raskere fremdrift og en mer dynamisk prosess, der KI fungerte som problemløser og idégenerator.

Læring og forståelse For medlemmer med mindre programmeringserfaring fungerte KI som et personlig læringsverktøy. Ved å stille spørsmål til Gemini og ChatGPT fikk de raskt forklaringer på begreper, syntaks og funksjonslogikk, noe som styrket forståelsen og gjorde det enklere å delta i tekniske diskusjoner. KI ble brukt til å utforske konsepter, rette feil og forbedre kode. For mer erfarne medlemmer ble KI et verktøy for å validere ideer og heve kvaliteten på løsninger.

Kvalitet på koden KI-verktøyene bidro også til en mer strukturert og robust kodebase. Gemini foreslo forbedringer innen lesbarhet, feilhåndtering og optimalisering, og hjalp med å oppdage svakheter tidlig i utviklingsløpet. ChatGPT bidro med alternative løsninger og bedre forståelse av feilmeldinger, som ofte førte til forbedrede implementasjoner. Denne kombinasjonen gjorde at koden gradvis ble mer stabil og at gruppen opparbeidet seg bedre forståelse av beste praksis innen utvikling.

### 4.2 Begrensninger og ulemper
Kvalitet og pålitelighet Selv om KI-verktøyene ga rask fremdrift, var kvaliteten på svarene ikke alltid pålitelig. Spesielt ved bruk av Gemini opplevde vi at koden til tider inneholdt syntaksfeil, utdaterte biblioteker eller manglende forståelse av sammenhengen i prosjektet. Dette krevde ekstra tid til manuell feilsøking og testing. I noen tilfeller foreslo KI løsninger som virket logiske, men som senere viste seg å være teknisk uegnede. Dette understreker behovet for menneskelig kontroll og kritisk vurdering av KI-generert innhold.

Avhengighet og forståelse I starten stolte vi for mye på KI uten å reflektere nok over resultatene. Kode ble tatt videre uten grundig vurdering, og vi oppdaget i etterkant at enkelte løsninger var feil eller lite hensiktsmessige. I tillegg ble ikke promptene lagret systematisk, noe som gjorde det vanskelig å spore hva som var gjort og hvorfor. Dette ble en viktig læring. Etter de første fasene innførte vi en mer strukturert praksis: vi lagret alle KI-prompter, dokumenterte svar og ba Gemini lage korte sammendrag fra hver fase. Dermed gikk vi fra å bruke KI som et “hurtigverktøy” til å bruke det som en integrert lærings- og dokumentasjonsressurs.

Kreativitet og problemløsning KI-forslagene var ofte konvensjonelle og ikke nødvendigvis innovative. Gruppen måtte derfor aktivt utfordre forslagene for å tenke utover standardløsninger. Det ble viktig å bruke KI som støtte, ikke som erstatning for egen refleksjon og problemløsning.

### 4.3 Sammenligning: Med og uten KI
KI hadde stor betydning for hvordan gruppen kunne gjennomføre prosjektet uten inngående kunnskap om alle verktøyene. Med støtte fra Gemini og ChatGPT kunne vi skrive, forstå og rette kode uten å kunne alle kommandoer, syntaksregler og bibliotekreferanser. KI forklarte løpende hva koden gjorde og foreslo forbedringer, slik at vi kunne fokusere mer på struktur og funksjonalitet.

På backend-siden gjorde KI FastAPI- og Firestore-integrasjon mer håndterlig. Gemini hjalp med å skrive grunnleggende funksjoner og filvalidering, mens ChatGPT forklarte feilmeldinger og hvordan de kunne rettes. På frontend ble det enklere å bygge et funksjonelt og visuelt grensesnitt uten inngående kjennskap til HTML, CSS og JavaScript. KI foreslo kode for interaktive elementer som flashcards og quizer og forklarte koblingen mot databasen.

Uten KI-støtte ville læringskurven vært brattere, men med en dypere teknisk forståelsen og en mer inngående forståelse av de ulike fasene i utviklingen. Vi måtte brukt betydelig mer tid på grunnleggende konsepter, biblioteker, syntaks, dokumentasjon og feilhåndtering. Med den tilgjengelige tiden ville det vært lite realistisk å oppnå samme funksjonalitet og kvalitet. Prosjektet ville trolig hatt lavere funksjonalitet, men høyere faglig dybde. Med KI fikk vi et mer komplett og visuelt ferdig produkt, selv om deler av koden ble forstått på et mer overordnet nivå.


### 4.4 Samlet vurdering
KI har totalt sett hatt en tydelig positiv innvirkning på prosjektet. Uten KI ville det vært svært krevende å gjennomføre et så teknisk komplekst prosjekt innenfor tidsrammen. Gemini og ChatGPT gjorde det mulig å bygge funksjonell kode, løse problemer raskt og forstå komplekse prosesser uten inngående forkunnskap i alle språk og rammeverk.

Samtidig viste erfaringen at KI ikke kan erstatte menneskelig forståelse, kritisk tenkning og kreativitet. De første fasene illustrerte hvor lett det er å stole for mye på KI. Etter hvert ble bruken mer strukturert: vi lagret prompter, dokumenterte forslag og kvalitetssikret koden fortløpende. Overgangen fra ukritisk til målrettet bruk er en av de viktigste læringene.

Vi vurderer KI som en netto positiv faktor: den ga høyere produktivitet, bedre struktur og et mer komplett sluttprodukt enn det som realistisk kunne vært oppnådd uten KI. Samtidig tydeliggjorde prosjektet at KI bør brukes som samarbeidspartner og som et kraftig verktøy – ikke som erstatning for egen kunnskap og kreativitet.

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
  - KI-generert kode vil trolig kreve mer dokumentasjon og sørge for at den bruker samme type standard som programmerere selv ville brukt (for eksempel ingen typiske code smells) 
- Er KI-kode like forståelig som menneskeskrevet kode?
  - KI-generert kode er ofte mindre intuitiv og vanskeligere å vedlikeholde enn menneskeskrevet kode, selv om den er funksjonell. Videre kan det tenkes at utviklere har en tendens til å være mindre kritiske i sin gransking av KI-kode, da de mangler den naturlige ansvarsfølelsen eller eierskapet de har til egen kode. Dette skaper en risiko for at man lettere fraskriver seg ansvaret ved feil, ved å skylde på KI-verktøyet fremfor å ta eierskap for å ha godkjent og implementert koden i prosessen.  
- Utfordringer med å debugge KI-generert kode
  - Når man selv ikke har laget koden kan det være vanskelig å vite akkurat hvordan KI har tenkt og hvorfor det har blitt generert ulike løsninger. Dermed kan det også være vanskeligere å debugge den.  

### 6.2 Standarder og beste praksis
- Følger KI alltid beste praksis og industristandarder?
  - Ikke nødvendigvis. KI utivkler seg langt raskere enn for eksempel lover og regler gjør. Dette kan føre til at KI kan produsere programvare og løsninger som ligger i gråsonen juridisk sett. 
- Eksempler på hvor KI foreslo utdaterte eller dårlige løsninger:
  - Et eksempel på når KI foreslår utdaterte eller dårlige løsninger er når KI vurderer kandidater for en stilling basert på informasjon som inneholder skjevheter. Det er velkjent at KI kan forsterke eksisterende bias knyttet til kjønn, hudfarge, religion og liknende. Når slike skjevheter ligger til grunn for vurderingene, risikerer allerede utsatte grupper å bli utsatt for ytterligere diskriminering, noe som kan forsterke ulikhet og urettferdighet i rekrutteringsprosessen.   
- Viktigheten av å validere KI sine forslag
  - Det er svært viktig å validere KI sine forslag av ulike grunner. For det første er det essensielt at man sjekker at KI generert kode ikke inneholder sikkerhetshull eller feil som kan føre til sikkerhetsbrudd. Videre kan man avdekke quality på koden som er generert og gjøre eventuelle forbedringer eller justeringer. 

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
  - Bruk KI som samtalepartner og veileder, ikke som automatisk kodegenerator. Still spørsmål, be om forklaringer, og be KI utdype hvorfor en løsning fungerer.
    Vær presis i promptene. Jo tydeligere problemet beskrives, desto mer relevante svar.
    Kombiner gjerne flere KI-verktøy, for eksempel Gemini til kodeutvikling og ChatGPT til feilsøking og konseptforklaringer.
    Dokumenter bruken. Lagre prompter og svar underveis for å kunne spore hvilke forslag som ble brukt.
- [Fallgruver å unngå]
  - Ikke stol blindt på kodeforslag. Selv små feil kan gi logiske problemer eller sikkerhetsbrudd. Test og forstå hva koden gjør.
    Unngå å bruke KI som erstatning for egen læring. Reflekter over prosessen, ikke bare resultatet.
    Vær forsiktig med hva du deler. Ikke legg inn sensitiv informasjon, passord eller nøkkelfiler i promptene.
- [Beste praksis dere oppdaget]
  - Start prosjektet med felles retningslinjer for hvordan gruppen skal bruke KI – når, til hva og hvordan det skal dokumenteres.
    Bruk KI aktivt i brainstorming og idéutvikling for å utforske alternativer før dere velger retning.
    Når KI genererer kode, be også om forklaringer linje for linje for å øke læringsverdien.
    Sørg for at minst én i gruppen kvalitetssikrer alle forslag før de implementeres.

- Oppsummert mener vi at nøkkelen til vellykket KI-bruk er balansen mellom effektivitet og forståelse. Når KI brukes bevisst, som støtte og ikke som erstatning, kan den både styrke læringsprosessen og øke kvaliteten på sluttproduktet.

### 7.4 Personlig refleksjon (individuelt)

**[Birgitte]:**
På den positive siden har det vært svært spennende og lærerikt å utvikle en app fra start til slutt, med AI som en veiviser som håndterte det tekniske. Det var også tilfredsstillende å se og ta i bruk det ferdige produktet. I tillegg var det svært nyttig og lærerikt å komplementere Gemini CLI med bruken av eksterne AI-verktøy som Gemini, Perplexity og ChatGPT, som ga gode og som regel brukbare løsninger og var gode “sparringspartnere”. Det har også vært svært nyttig å lære hvordan Github fungerer i praksis og hvordan man jobber i brancher. 

På den negative siden var det utfordrende å vite nøyaktig hvor jeg befant meg i BMAD-fasene og hva som var neste steg. Det tok tid å lære hvordan jeg begynte igjen etter å ah avsluttet siste work session/work flows. Videre fant jeg det utfordrende å vite hvor jeg skulle avslutte brancher og hvor jeg skulle starte på nye. Det føles også litt frustrerende at både github og BMAD metoden kunne vært utnyttet langt bedre for samarbeid og en teamstruktur dersom teamet hadde hatt god nok kunnskap om dette ved starten av prosjektet. Organiseringen av faget skapte også utfordringer, med motstridende tidsplaner mot forelesningene og sen informasjon om hvordan vi kunne ha strukturert prosjektet. Andre ulemper for dette prosjektet inkluderte lite tilbakemelding fra lærere og assistenter.  

Til slutt vil jeg trekke frem hvor fascinerende og samtidig litt skremmende KI-utviklingen har blitt i 2025, med et enormt potensial og kraft. KI kan vise seg som et uvurderlig verktøy som komplementerer, ikke overtar, menneskelig kreativitet, innovasjon og problemløsning i prosjekter, slik som app-utvikling der det håndterer tekniske oppgaver effektivt. På den negative siden er det skummelt å tenke på at KI kan og vil overta roller som potensielt begrenser vår egen evne til kreativ tenkning og selvstendig utvikling, noe som understreker behovet for å behandle det som et støttende element snarere enn en erstatning. 

**[Navn på gruppemedlem 2]:**
[Personlig refleksjon over egen læring og utvikling]

**[Kine]:**
Som nybegynner uten tidligere erfaring med koding har dette prosjektet vært både utfordrende og svært lærerikt. I starten opplevde jeg usikkerhet rundt mange tekniske begreper og verktøy, men bruken av KI – spesielt Gemini sammen med VSC og ChatGPT – gjorde det mulig for meg å forstå og lære i mitt eget tempo. KI hjalp meg med å oversette teknisk kode til forståelige forklaringer og gjorde det mulig å prøve, feile og lære underveis.

Samtidig har prosjektet vist meg hvor avgjørende godt samarbeid er i et gruppeprosjekt. I begynnelsen oppsto det noen utfordringer med at enkelte gruppemedlemmer ikke møtte forberedt til møtene, og at avtalte møtetider ble endret på kort varsel. I en allerede travel hverdag ble det tydelig hvor viktig det er å holde avtaler og ta ansvar for gruppens fremdrift. Et gruppeprosjekt med flere deltakere krever at alle er dedikerte – når én gjør et valg, påvirker det alle. Denne erfaringen har lært meg mye om både struktur, kommunikasjon og respekt for andres tid.

Det skal også nevnes at jeg har fått mye hjelp og støtte fra Birgitte og Hamdi, som har vært utrolig fleksible, tålmodige og hjelpsomme gjennom hele prosessen. Det har vært rom for å stille spørsmål og prøve seg frem selvom om man er usikker, det har alltid vært rom for å stille spørsmål, og vi har i flere møter jobbet sammen i VSC ved deling av skjerm for å lære.

Selv om jeg har lært mye og fått bedre forståelse for hvordan programmering og KI fungerer, ser jeg fortsatt på meg selv som en nybegynner, bare med litt mer kunnskap enn før. Jeg har fortsatt ikke forstått alt, men nå vet jeg hvor jeg skal begynne for å lære mer. Programmering har alltid vært litt høytsvevede og gresk, og det at jeg når kan sitte i VSC og promte er gøy.

Gjennom dette prosjektet har jeg ikke bare lært om programmering og KI, men også om samarbeid, ansvar og hvordan man kan vokse i møte med utfordringer. Erfaringen har gitt meg en ny forståelse av hvor mye man kan oppnå når man kombinerer teknologi, samarbeid og læringsvilje.

## 8. Vedlegg (valgfritt)

- Skjermbilder av applikasjonen
- Lenke til GitHub repository
- Annen relevant dokumentasjon

-- -

**Ordantall:** [Ca. antall ord]

**Forventet lengde:** 3000-5000 ord (avhengig av gruppestørrelse og prosjektets kompleksitet)