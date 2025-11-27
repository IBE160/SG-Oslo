Refleksjonsrapport - Programmering med KI 

1. Gruppeinformasjon 

Gruppenavn: [SG-Oslo] 

Gruppemedlemmer: 

Birgitte Bellsund - [201583/birgitte.bellsund@himolde.no] 

Hamdi Abdi Mohamed - [Student-ID/hamdi.a.mohamed@himolde.no] 

Kine Marie Pettersen - [Student-ID/kine.m.pettersen@himolde.no] 

 

Dato: 16.11.2025 

 

2. Utviklingsprosessen 

2.1 Oversikt over prosjektet 

Prosjektet StudyBuddy-AI realiserer kjerneverdien i applikasjonen: å transformere opplastet læringsstoff (PDF/DOCX) til personlige sammendrag, flashcards og quizer. Brukeren laster opp et dokument, backend trekker ut tekst, og en KI-tjeneste (primært Google Gemini, eventuelt OpenAI GPT-4) genererer læringsressurser som lagres i Firestore og vises i et interaktivt grensesnitt. Målet er å gi studenter en intuitiv og effektiv måte å bearbeide store mengder akademisk tekst på, slik at de lettere kan lære gjennom aktiv repetisjon og selvtesting. Prosjektet kombinerer teknologi, pedagogikk og KI for å redusere tiden fra rått fagstoff til strukturert, anvendbart læringsmateriale, og demonstrerer samtidig en praktisk og etisk bruk av generativ KI i høyere utdanning. 

2.2 Arbeidsmetodikk 

Arbeidet ble organisert etter en lettversjon av Agile-metodikk, med korte iterasjoner og tydelige delmål basert på akseptansekriteriene (AC 2.1–2.5). 

I oppstartsfasen ønsket gruppen først å utforske hvordan Gemini kunne brukes direkte i Visual Studio Code (VSC). Målet var at alle skulle få en praktisk forståelse av hvordan KI-integrasjonen fungerte i utviklingsmiljøet før selve prosjektet tok form. Gruppen besto av medlemmer med ulik bakgrunn: noen hadde tidligere erfaring fra programmeringsfag, mens andre var helt nye i faget. Dette ga prosjektet en variert læringsdynamikk og krevde tilpasning i arbeidsmetodikken. 

Det ble avholdt et oppstartsmøte hvor gruppen opprettet en side i Jira for oppgavefordeling og fremdriftskontroll. Etter kort tid erfarte vi at verktøyet ble lite brukt, og valgte derfor å flytte all kommunikasjon og koordinering til Microsoft Teams, som fungerte bedre for gruppens behov. Vi har siden hatt ukentlige møter hvor vi har fordelt oppgaver, diskutert fremdrift og satt mål for neste periode. 

Ettersom gruppen hadde ulikt erfaringsnivå, oppsto det tidlig en utfordring med å finne riktig arbeidsflyt. For å sikre mest mulig læring for alle, besluttet vi at hvert medlem skulle delta i alle deler av utviklingsprosessen – fra planlegging og koding til testing og dokumentasjon. Dette bidro til økt forståelse av helheten i prosjektet, og samtidig bedre samarbeid og kommunikasjon. 

Gruppen startet med fire medlemmer, men i uke 45 valgte Sara å avslutte deltakelsen da arbeidsmetoden og tempoet ikke passet hennes preferanser. Resten av gruppen fortsatte prosjektet og fordelte ansvar basert på styrker: Birgitte bidro med struktur, kritiske spørsmål og sterk detaljfokus, Hamdi hadde teknisk erfaring og var særlig god til å lese og rette kodefeil, mens Kine, som var helt ny i programmering, brukte prosessen til å lære gjennom aktiv deltakelse, prøving og feiling. 

Samarbeidsverktøy: Vi brukte VS Code til utvikling, GitHub til versjonskontroll og pull requests med kodegjennomgang, og Teams til kommunikasjon, møter og avklaringer. 

KI ble brukt som en sentral støtte gjennom hele utviklingsprosessen. Vi benyttet Gemini-integrasjonen i Visual Studio Code aktivt for å kommunisere med agenter, gjennomføre idémyldring og få forslag til kodeforbedringer. Dette var særlig nyttig i tidlige faser, hvor vi testet ulike tilnærminger og løste tekniske utfordringer i sanntid. Ved siden av dette brukte vi også ChatGPT som en støttespiller, spesielt ved feilsøking og tolkning av feilmeldinger. ChatGPT viste seg å være et effektivt verktøy for å forklare hva feilmeldingene betydde, foreslå mulige løsninger og hjelpe oss å forstå hvorfor koden ikke fungerte som forventet. Kombinasjonen av Gemini og ChatGPT ga oss dermed både idéutvikling, teknisk støtte og læring underveis. 

2.3 Teknologi og verktøy 

For denne appen har vi tatt i bruk følgende teknologi og verktøy: 

Frontend: React (Vite), TypeScript, Material-UI:  

Backend: Node.js/Express.js (API Gateway, Brukerdata) 

AI Service: Python/FastAPI 

KI-verktøy: Google Gemini API, Google Cloud AI 

Database: PostgreSQL, S3-objektlagring 

DevOps: Docker, Kubernetes, GitHub Actions 

2.4 Utviklingsfaser 

[Beskriv de ulike fasene i utviklingen] 

Fase 1: Planlegging 

I denne fasentok vi i bruk BMADs agent for å brainstorme med SCAMPER-metoden for å komme frem til nye funskjoner og forbedringer for StudyBuddy. Disse forbedringene fokuserte blant annet på en smartere måte å organisere generert læringsmateriale(quiz, sammendrag, flashcards), økt brukerengasjement og en enklere systemarkitektur. De mest relevante resultatene fra brainstormingen var et AI-drevet Topic Map som automatisk strukturerer læringsmateriale. Videre kom vi frem til micro-læring med korte og fleksible økter i tillegg til lengre økter. Et annet resultat fra brainstormingen var å introdusere skylagring hos bruker istedenfor intern applagring, noe som reduserer kompleksitet og ekstra arbeid og kostnad ift lagring av materiale. I tillegg kom vi frem til en omvendt arbeidsflyt der AI først kartlegger brukerens mål før en skreddersydd studieplan blir laget. Disse forslagene bidro til å skape en mer adaptiv, effektiv og personlig læringsopplevelse i StudyBuddy AI. 

[Hvordan brukte dere KI her? Husk å lagre promptene deres! Inkluder ALLE stegene dere gjorde.] 

Fase 2: Utvikling 

Arbeidet startet med å synkronisere det lokale repositoriet med main-grenen og identifisere "Install frontend dependencies" som neste steg i arbeidsflyten. Et innledende forsøk på npm install feilet i frontend-mappen grunnet manglende package.json, noe som ble løst ved å opprette en midlertidig fil med basisavhengigheter for å fullføre installasjonen. Etter vellykket installasjon ble de midlertidige filene umiddelbart fjernet igjen. 

Deretter ble fokuset flyttet til å etablere en ny React-applikasjon i mappen new-frontend ved bruk av create-react-app. Gjennom hele prosessen ble statusfilen bmm-workflow-status.md kontinuerlig oppdatert for å reflektere fullføringen av fasen og angi det neste logiske steget: å starte utviklingsserveren for den nyopprettede frontend-applikasjonen. Til slutt ble alle endringer, inkludert den komplette frontend-applikasjonen, committet til repositoriet. 

 

[Hva gjorde dere i denne fasen?] 

[Hvordan brukte dere KI her? Husk å lagre promptene deres! Inkluder ALLE stegene dere gjorde.] 

 

3. Utfordringer og løsninger 

3.1 Tekniske utfordringer 

[Beskriv 2-3 konkrete tekniske problemer dere møtte] 

Utfordring 1: Grense på gemini cli 

Problem: Maksimumskvoten for Gemini CLI ble nådd, noe som medførte stopp i bruk til neste dag. Dette skjedde etter intensiv bruk og ga en feilmelding om at kvoten var oppbrukt. Brukeren måtte vente i 24 timer for å få tilgang til en full økt igjen.  

Løsning: Det var ingen rask løsning – man må vente ut perioden før tilgang blir gjenopprettet. Alternativt kan det søkes om økt kvote via Gemini dashboard, men dette er ikke aktuelt for de fleste dagligbrukere.  

KI sin rolle: Kunstig intelligens hjelper her med å informere om kvotegrenser og gir beskjed om ventetid, men stanset videre arbeid. Ingen proaktiv assistanse for å omgå grensen eller få bedre ressursutnyttelse, kun standard beskjed om å vente. 

 

Utfordring 2: [Tester feiler] 

Problem: En eller flere tester mislyktes fordi API-nøkkelen manglet eller var plassert feil. Dette førte til mislykket autentisering og stoppet videre testing.   

Løsning: Problemet ble løst ved å spørre eksterne KI-chatboter. Svaret var at API-nøkkelen måtte ligge i riktig mappe eller .env-fil, for eksempel i en .gemini-mappe med en tilhørende .env-fil, eller legges inn som en miljøvariabel for at Gemini CLI skal fungere korrekt.   

KI sin rolle: Gemini CLI ga ikke en klar årsak til feilene eller konkrete løsningsforslag. I stedet ble mye tid brukt på feilsøking i CLI. Det var mer effektivt å få direkte svar og løsninger fra eksterne AI-chatboter, som ga nyttige tips om korrekt plassering av nøkkelen og feilkildene. 

 

Utfordring 3: [Gemin CLI bekrefteles loop] 

Problem: Noen ganger satte gemini seg i en loop der gemini utfører en oppgave og vil at bruker skal bekrefte med [yes/y]. Når man bekrefter dette blir svaret satt i en kø og gemini bare går uten at oppgaven blir utført. Selv når jeg avbryter og prøver igjen løser det seg ikke.  

Løsning: Bruke gemini chatbot for å høre hva som er problemet og få en kommando som gjr at gemini ikke trenger en ekstra bekreftelse fra bruker. Eksempelvis brukte vi denne kommandoen 

KI sin rolle: [Hvordan hjalp eller hindret KI dere?] 

 

Utfordring 4: [Tittel] 

Problem: [Beskriv problemet] 

Løsning: [Hvordan løste dere det?] 

KI sin rolle: [Hvordan hjalp eller hindret KI dere?] 

 

3.2 Samarbeidsutfordringer 

En av de største samarbeidsutfordringene i prosjektet var at gruppemedlemmene hadde forskjellig erfaringsnivå innen programmering. Noen hadde tidligere erfaring med utviklingsprosjekter, mens andre var helt nye i faget. Dette skapte et behov for ekstra tålmodighet og gjensidig støtte i gruppen, spesielt i de tekniske fasene av arbeidet. For å sikre læringsutbytte for alle, ble det besluttet at hvert medlem skulle få prøve seg på flere deler av prosessen – fra koding til testing og dokumentasjon – slik at alle fikk en helhetlig forståelse av systemet. 

Kommunikasjonen ble tidlig flyttet fra Jira til Microsoft Teams, ettersom det viste seg å være et mer effektivt og naturlig samarbeidsverktøy for gruppen. Teams ble brukt til ukentlige møter, deling av kode og løpende avklaringer. Dette bidro til bedre kontinuitet og færre misforståelser i prosjektet. 

En annen utfordring oppsto da ett av gruppemedlemmene, Sara, valgte å trekke seg i uke 45. Hennes avgjørelse var knyttet til ulik oppfatning av tempo og arbeidsmetode. Resten av gruppen valgte å fortsette samarbeidet og fordelte ansvaret mer tydelig for å sikre fremdrift. Samtidig ble det lagt vekt på å ivareta et godt arbeidsmiljø og åpen kommunikasjon, slik at alle følte seg trygge på egne oppgaver og bidrag. 

3.3 KI-spesifikke utfordringer 

[Problemer spesifikt knyttet til bruk av KI] 

[f.eks. Feil kode fra KI, misforståelser, inkonsistent kvalitet] 

[Hvordan håndterte dere disse?] 

 

4. Kritisk vurdering av KI sin påvirkning 

4.1 Fordeler med KI-assistanse 

Effektiv bruk av KI gjorde utviklingsprosessen både raskere og mer produktiv. Gemini i Visual Studio Code ble brukt til kodeforslag, forklaring av logikk og strukturering av funksjoner, mens ChatGPT særlig hjalp med å tolke feilmeldinger og forklare årsaker til feil. KI-verktøyene ble også brukt aktivt i brainstorming om arkitektur, funksjonalitet og brukerflyt, og hvert gruppemedlem brukte dem ulikt – enten for å forbedre kode eller for å forstå og bygge videre på eksisterende løsninger, noe som ga raskere fremdrift og en mer dynamisk prosess. 

For de med mindre programmeringserfaring fungerte KI som et personlig læringsverktøy, med raske forklaringer på begreper, syntaks og funksjonslogikk som gjorde det enklere å delta i tekniske diskusjoner. Mer erfarne utviklere brukte KI til å validere ideer og forbedre kvaliteten på løsningene. Samlet ga dette en mer strukturert og robust kodebase, der Gemini foreslo forbedringer i lesbarhet, feilhåndtering og optimalisering, mens ChatGPT bidro med alternative løsninger og bedre forståelse av feilmeldinger, slik at koden gradvis ble mer stabil og gruppen styrket forståelsen av beste praksis. 

 

4.2 Begrensninger og ulemper 

KI-verktøyene ga rask fremdrift, men kvaliteten på svarene var ikke alltid pålitelig, og forslag inneholdt av og til syntaksfeil, utdaterte biblioteker eller løsninger som senere viste seg teknisk uegnede. Dette krevde ekstra manuell feilsøking og understreket behovet for menneskelig kontroll og kritisk vurdering. I starten ble KI brukt så aktivt at gruppen ble for avhengig, stolte for mye på svarene og vurderte ikke koden grundig nok, noe som førte til feil og lite hensiktsmessige løsninger. 

Mangelen på struktur i begynnelsen gjorde også at promptene ikke ble lagret systematisk, slik at det var vanskelig å spore hva gruppen hadde gjort og hvorfor. Etter hvert innførte de en mer bevisst praksis der alle KI-prompter ble lagret i egne filer, svarene dokumentert, og Gemini ble brukt til korte sammendrag fra hver fase, noe som ga bedre oversikt, læring og samspill mellom mennesker og KI. Gruppen gikk dermed fra å bruke KI som et rent “hurtigverktøy” til å se det som en integrert lærings- og dokumentasjonsressurs, samtidig som de erfarte at KI kan begrense kreativiteten hvis forslagene ikke utfordres aktivt, og derfor må brukes som støtte – ikke som erstatning for egen refleksjon og problemløsningsevne. 

 

4.3 Sammenligning: Med og uten KI 

[Reflekter over hvordan prosjektet ville vært uten KI] 

Hva ville vært annerledes? Hva ville vært annerledes? 

Hvilke deler av prosjektet ville vært vanskeligere/lettere? 

Ville sluttresultatet vært bedre eller dårligere? 

 

Roller: Det ville vært behov for mennesker i rollene som utvikler, analytiker, produkteier og flere. I stedet for et team på tre personer, ville man hatt flere ganger så mange involverte, noe som ville krevd betydelig mer koordinering, kommunikasjon og planlegging.  Det ville nok ført til mer komplekse prosesser og hyppigere møter for å holde ting på rett spor. 

Dokumentasjon: Alle dokumenter ville ha blitt produsert manuelt av de ulike rollene i prosjektet, noe som kan være tidkrevende og variere i kvalitet.  Flere personer i teamet øker naturlig risikoen for menneskelige feil, og det ville vært mer tid brukt på feilsøking og synkronisering mellom teammedlemmer. 

 Uten KI kunne prosjektet hatt et tettere fokus på brukerens ønsker, kanskje med mer nytenkning og innovasjon, siden gruppen måtte stole mer på egne ideer og refleksjoner. Til slutt, uten KI ville prosjektgruppen hatt større kontroll over hele prosessen og trolig lært mer om utviklingsfasene gjennom manuell håndtering. 

 

 

Hvilke deler av prosjektet ville vært vanskeligere/lettere? 

Det ville nok vært lettere å  

Ville sluttresultatet vært bedre eller dårligere? 

4.4 Samlet vurdering 

[Konklusjon: Hvordan påvirket KI sluttresultatet totalt sett?] 

Var KI en netto positiv eller negativ faktor? 

Hva var den viktigste lærdommen om å bruke KI i utviklingsprosessen? 

 

5. Etiske implikasjoner 

5.1 Ansvar og eierskap 

Hvem er ansvarlig for koden når KI har bidratt? 

Den ansvarlige for koden når KI har bidratt er fremdeles de som har generert koden. I dette tilfellet er det vi som har kommandert KI til å generere kode for oss som er ansvarlige for hele prosjektet. 

Hvordan sikrer man kvalitet når KI genererer kode? 

Man kan sikre koden ved å for å gjennomgå koden og teste den før launch, samt vedlikeholde den og sørge for å forebygge, stoppe og ordne opp i bugs og problemer og sikkerhetsrelaterte feil og brudd.  

Diskuter spørsmål om opphavsrett og intellektuell eiendom 

I utgangspunktet vil det igjen være  

5.2 Transparens 

Bør det være transparent at KI er brukt? 

Det bør definitivt være transparent at KI er brukt. Når man tar i bruk KI pålegges man et ansvar for hva som blir generert. Videre skaper en åpenhet om hvordan man jobber tillitt hos brukere.  

Hvordan dokumenterer man KI sin bidrag? 

Hva er konsekvensene av å ikke være åpen om KI-bruk? 

5.3 Påvirkning på læring og kompetanse 

Hvordan påvirker KI-avhengighet fremtidig kompetanse? 

Hvilke ferdigheter risikerer man å ikke utvikle? 

Balanse mellom effektivitet og læring 

5.4 Arbeidsmarkedet 

Hvordan kan utbredt KI-bruk påvirke fremtidige jobber i IT? Utbredt KI-bruk kan gjøre at enkelte oppgaver og roller innenfor IT blir automatisert og erstattet av KI. 

Hvilke roller vil bli viktigere/mindre viktige? Roller som har å gjøre med ren koding, sortering og oppbygging av arkitektur vil bli mindre relevant, mens det vil bli viktigere med en innsikt i og evnen til å følge opp hele prosessen. Videre vil roller som krever mer soft skills og gode interpersonlige ferdigheter fremdeles være relevante. Dette vil for eksempel bety roller der man har personalansvar, der man samarbeider med klienter eller på tvers av team.  

Deres refleksjoner om fremtidig karriere i en KI-drevet verden:  

5.5 Datasikkerhet og personvern 

Hvilke data delte dere med KI-verktøy? 

Potensielle risikoer ved å dele kode og data med KI 

Hvordan skal man tenke på sikkerhet når man bruker KI? 

 

6. Teknologiske implikasjoner 

6.1 Kodekvalitet og vedlikehold 

Hvordan påvirker KI-generert kode langsiktig vedlikehold? 

KI-generert kode vil trolig kreve mer dokumentasjon og sørge for at den bruker samme type standard som programmerere selv ville brukt (for eksempel ingen typiske code smells) 

Er KI-kode like forståelig som menneskeskrevet kode? 

KI-generert kode er ofte mindre intuitiv og vanskeligere å vedlikeholde enn menneskeskrevet kode, selv om den er funksjonell. Videre viser erfaring at utviklere har en tendens til å være mindre kritiske i sin gransking av KI-kode, da de mangler den naturlige ansvarsfølelsen eller eierskapet de har til egen kode. Dette skaper en risiko for at man lettere fraskriver seg ansvaret ved feil, ved å skylde på KI-verktøyet fremfor å ta eierskap for å ha godkjent og implementert koden i prosessen..  

Utfordringer med å debugge KI-generert kode 

Når man selv ikke har laget koden kan det være vanskelig å vite akkurat hvordan KI har tenkt og hvorfor det har blitt generert ulike løsninger. Dermed kan det også være vanskeligere å debugge den.  

6.2 Standarder og beste praksis 

Følger KI alltid beste praksis og industristandarder? 

Ikke nødvendigvis. KI utivkler seg langt raskere enn for eksempel lover og regler gjør. Dette kan føre til at KI kan produsere programvare og løsninger som ligger i gråsonen juridisk sett. 

Eksempler på hvor KI foreslo utdaterte eller dårlige løsninger 

Et eksempel på når KI foreslår utdaterte eller dårlige løsninger er når KI vurderer kandidater for en stilling basert på informasjon som inneholder skjevheter. Det er velkjent at KI kan forsterke eksisterende bias knyttet til kjønn, hudfarge, religion og liknende. Når slike skjevheter ligger til grunn for vurderingene, risikerer allerede utsatte grupper å bli utsatt for ytterligere diskriminering, noe som kan forsterke ulikhet og urettferdighet i rekrutteringsprosessen. 

Viktigheten av å validere KI sine forslag 

Det er svrt viktig å validere KI sine forslag av ulike grunner. For det første er det essensielt at man sjekker at KI generert kode ikke inneholder sikkerhetshull eller feil som kan føre til sikkerhetsbrudd. Videre kan man avdekke kvaliteten på koden som er generert og gjøre eventuelle forbedringer eller justeringer.  

6.3 Fremtidig utvikling 

Hvordan tror dere KI vil påvirke programvareutvikling fremover? 

Hvilke ferdigheter blir viktigere for utviklere? 

Deres anbefalinger for hvordan man bør bruke KI i utviklingsprosesser 

 

7. Konklusjon og læring 

7.1 Viktigste lærdommer 

[Liste de 3-5 viktigste tingene dere lærte gjennom prosjektet] 

[Lærdom 1] 

[Lærdom 2] 

[Lærdom 3] 

7.2 Hva ville dere gjort annerledes? 

[Reflekter over hva dere ville endret hvis dere skulle startet på nytt] 

[Tekniske valg] 

[Bruk av KI] 

[Samarbeid og organisering] 

7.3 Anbefalinger 

[Deres anbefalinger til andre studenter som skal bruke KI i utvikling] 

[Råd om effektiv bruk av KI] 

[Fallgruver å unngå] 

[Beste praksis dere oppdaget] 

7.4 Personlig refleksjon (individuelt) 

[Birgitte]:  

Det var utfordrende å vite hvor eksakt i fasene jeg var og hva som var neste steg. Da kunne jeg heller ikke lese meg mer opp på det for å virkelig forstå hvordan jeg kunne videreutvikle appen og få til enda bedre løsninger. Videre måtte jeg selv avgrense ift å lage nye brancher og det var utfordrende å vite hvor jeg skulle stoppe og lage ne ny branch. Videre var det litt frustrerende å gå igjennom alle fasene og se hvordan BMAD methoden virker i praksis og tenke at man kunne gått tilbake og utnyttet metoden i langt større grad og kunne strukturert teamarbeidet mye bedre. Tidsmessig derimot, var det utfordrende. Det var også vanskelig å forholde seg til organisering av faget ettersom vi først ble satt igang for å starte for oss selv, deretter fikk utdelt en plan over uker vi skulle være ferdig med ulike faser som i tillegg var i kontrast med forelesningene gitt. Ila disse forelesningene kom det frem en del som kunne vært fint å ta med seg i sitt eget prosjekt, men som dessverre kom sent ut i semesteret. Det var derimot spennende å kunne lage en app og følge AI som en veiviser og ekspert som utviklet alt det tekniske. Det hadde vært hensiktsmessig for meg med mer teknisk innsikt da jeg kunne ha styrt prosessen bedre enn det jeg gjorde.  
Det var synd med lite tilbakemelding fra lærer og fagassistenter, dette gjorde prosessen mer rotete og uoversiktelig for meg da vi ikke hadde noen som kunne ta en titt på prosjektet og styre oss inn på riktig retning. Logging er vanskelig. Noen løsninger kom på plass etterpå. Men vi bruker mange eksterne AI; gemini, perplexity og chatgpt. Veldig mye logg arbeid ift å se hvordan de har hjulpet. 

 

[Navn på gruppemedlem 2]: [Personlig refleksjon over egen læring og utvikling] 

[Navn på gruppemedlem 3]: [Personlig refleksjon over egen læring og utvikling] 

 

8. Vedlegg (valgfritt) 

Skjermbilder av applikasjonen 

Lenke til GitHub repository 

Annen relevant dokumentasjon 

 

Ordantall: [Ca. antall ord] 

Forventet lengde: 3000-5000 ord (avhengig av gruppestørrelse og prosjektets kompleksitet) 

 