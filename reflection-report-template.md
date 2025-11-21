# Refleksjonsrapport - Programmering med KI

## 1. Gruppeinformasjon

**Gruppenavn:** [Navn på gruppen]

**Gruppemedlemmer:**
- [Navn 1] - [Student-ID/E-post]
- [Navn 2] - [Student-ID/E-post]
- [Navn 3] - [Student-ID/E-post]

**Dato:** 16.11.2025

-- -

## 2. Utviklingsprosessen

### 2.1 Oversikt over prosjektet
Prosjektet StudyBuddy-AI realiserer kjerneverdien i applikasjonen: å transformere opplastet læringsstoff (PDF/DOCX) til personlige sammendrag, flashcards og quizer. Brukeren laster opp et dokument, backend trekker ut tekst, og en KI-tjeneste (primært Google Gemini, eventuelt OpenAI GPT-4) genererer læringsressurser som lagres i Firestore og vises i et interaktivt grensesnitt. Målet er å gi studenter en intuitiv og effektiv måte å bearbeide store mengder akademisk tekst på, slik at de lettere kan lære gjennom aktiv repetisjon og selvtesting. Prosjektet kombinerer teknologi, pedagogikk og KI for å redusere tiden fra rått fagstoff til strukturert, anvendbart læringsmateriale, og demonstrerer samtidig en praktisk og etisk bruk av generativ KI i høyere utdanning.

### 2.2 Arbeidsmetodikk
Arbeidet ble organisert etter en lettversjon av Agile-metodikk, med korte iterasjoner og tydelige delmål basert på akseptansekriteriene (AC 2.1–2.5).

I oppstartsfasen ønsket gruppen først å utforske hvordan Gemini kunne brukes direkte i Visual Studio Code (VSC). Målet var at alle skulle få en praktisk forståelse av hvordan KI-integrasjonen fungerte i utviklingsmiljøet før selve prosjektet tok form. Gruppen besto av medlemmer med ulik bakgrunn: noen hadde tidligere erfaring fra programmeringsfag, mens andre var helt nye i faget. Dette ga prosjektet en variert læringsdynamikk og krevde tilpasning i arbeidsmetodikken.

Det ble avholdt et oppstartsmøte hvor gruppen opprettet en side i Jira for oppgavefordeling og fremdriftskontroll. Etter kort tid erfarte vi at verktøyet ble lite brukt, og valgte derfor å flytte all kommunikasjon og koordinering til Microsoft Teams, som fungerte bedre for gruppens behov. Vi har siden hatt ukentlige møter hvor vi har fordelt oppgaver, diskutert fremdrift og satt mål for neste periode.

Ettersom gruppen hadde ulikt erfaringsnivå, oppsto det tidlig en utfordring med å finne riktig arbeidsflyt. For å sikre mest mulig læring for alle, besluttet vi at hvert medlem skulle delta i alle deler av utviklingsprosessen – fra planlegging og koding til testing og dokumentasjon. Dette bidro til økt forståelse av helheten i prosjektet, og samtidig bedre samarbeid og kommunikasjon.

Gruppen startet med fire medlemmer, men i uke 45 valgte Sara å avslutte deltakelsen da arbeidsmetoden og tempoet ikke passet hennes preferanser. Resten av gruppen fortsatte prosjektet og fordelte ansvar basert på styrker: Birgitte bidro med struktur, kritiske spørsmål og sterk detaljfokus, Hamdi hadde teknisk erfaring og var særlig god til å lese og rette kodefeil, mens Kine, som var helt ny i programmering, brukte prosessen til å lære gjennom aktiv deltakelse, prøving og feiling.

Samarbeidsverktøy: Vi brukte VS Code til utvikling, GitHub til versjonskontroll og pull requests med kodegjennomgang, og Teams til kommunikasjon, møter og avklaringer.

KI ble brukt som en sentral støtte gjennom hele utviklingsprosessen. Vi benyttet Gemini-integrasjonen i Visual Studio Code aktivt for å kommunisere med agenter, gjennomføre idémyldring og få forslag til kodeforbedringer. Dette var særlig nyttig i tidlige faser, hvor vi testet ulike tilnærminger og løste tekniske utfordringer i sanntid. Ved siden av dette brukte vi også ChatGPT som en støttespiller, spesielt ved feilsøking og tolkning av feilmeldinger. ChatGPT viste seg å være et effektivt verktøy for å forklare hva feilmeldingene betydde, foreslå mulige løsninger og hjelpe oss å forstå hvorfor koden ikke fungerte som forventet. Kombinasjonen av Gemini og ChatGPT ga oss dermed både idéutvikling, teknisk støtte og læring underveis.

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
En av de største samarbeidsutfordringene i prosjektet var at gruppemedlemmene hadde forskjellig erfaringsnivå innen programmering. Noen hadde tidligere erfaring med utviklingsprosjekter, mens andre var helt nye i faget. Dette skapte et behov for ekstra tålmodighet og gjensidig støtte i gruppen, spesielt i de tekniske fasene av arbeidet. For å sikre læringsutbytte for alle, ble det besluttet at hvert medlem skulle få prøve seg på flere deler av prosessen – fra koding til testing og dokumentasjon – slik at alle fikk en helhetlig forståelse av systemet.

Kommunikasjonen ble tidlig flyttet fra Jira til Microsoft Teams, ettersom det viste seg å være et mer effektivt og naturlig samarbeidsverktøy for gruppen. Teams ble brukt til ukentlige møter, deling av kode og løpende avklaringer. Dette bidro til bedre kontinuitet og færre misforståelser i prosjektet.

En annen utfordring oppsto da ett av gruppemedlemmene, Sara, valgte å trekke seg i uke 45. Hennes avgjørelse var knyttet til ulik oppfatning av tempo og arbeidsmetode. Resten av gruppen valgte å fortsette samarbeidet og fordelte ansvaret mer tydelig for å sikre fremdrift. Samtidig ble det lagt vekt på å ivareta et godt arbeidsmiljø og åpen kommunikasjon, slik at alle følte seg trygge på egne oppgaver og bidrag.

### 3.3 KI-spesifikke utfordringer
[Problemer spesifikt knyttet til bruk av KI]
- [f.eks. Feil kode fra KI, misforståelser, inkonsistent kvalitet]
- [Hvordan håndterte dere disse?]

-- -

## 4. Kritisk vurdering av KI sin påvirkning

### 4.1 Fordeler med KI-assistanse
Effektivitet og produktivitet
Bruken av KI bidro betydelig til å øke effektiviteten i utviklingsprosessen. Gemini ble integrert i Visual Studio Code og brukt til å generere kodeforslag, forklare logikk og strukturere funksjoner, noe som reduserte tiden som normalt går med til research og manuell feilsøking. ChatGPT ble brukt som et supplement, særlig for å tolke feilmeldinger og forklare årsaker til feil på en forståelig måte.
Begge verktøyene ble også brukt aktivt i brainstorming-prosesser, hvor gruppen diskuterte og testet ulike løsninger på arkitektur, funksjonalitet og brukerflyt. Hvert medlem brukte KI på sin måte – noen for å forbedre eksisterende kode, andre for å forstå og bygge videre på det som allerede var utviklet. Dette førte til raskere fremdrift og en mer dynamisk utviklingsprosess, der KI fungerte som både problemløser og katalysator for nye ideer.

Læring og forståelse
For gruppemedlemmer med mindre programmeringserfaring fungerte KI som et personlig læringsverktøy. Ved å stille spørsmål direkte til Gemini eller ChatGPT underveis i arbeidet, fikk de raskt forklaringer på begreper, syntaks og funksjonslogikk, noe som styrket forståelsen og evnen til å delta aktivt i tekniske diskusjoner. KI ble brukt både til å utforske konsepter, rette feil og forbedre koden, noe som gjorde læringsprosessen kontinuerlig og praktisk. For mer erfarne medlemmer ble KI et redskap for å validere ideer og forbedre kvaliteten på eksisterende løsninger.

Kvalitet på koden
KI-verktøyene bidro også til en mer strukturert og robust kodebase. Gemini foreslo forbedringer innen lesbarhet, feilhåndtering og optimalisering, og hjalp med å oppdage svakheter tidlig i utviklingsløpet. ChatGPT bidro med alternative løsninger og bedre forståelse av feilmeldinger, som ofte førte til forbedrede implementasjoner. Denne kombinasjonen gjorde at koden gradvis ble mer stabil og at gruppen opparbeidet seg bedre forståelse av beste praksis innen utvikling.

### 4.2 Begrensninger og ulemper
Kvalitet og pålitelighet
Selv om KI-verktøyene ga rask fremdrift, var kvaliteten på svarene ikke alltid pålitelig. Spesielt ved bruk av Gemini opplevde vi at koden til tider inneholdt syntaksfeil, utdaterte biblioteker eller manglende forståelse av sammenhengen i prosjektet. Dette krevde ekstra tid til manuell feilsøking og testing. In some cases, KI suggested solutions that seemed logical but later proved to be technically unsuitable. This emphasizes the need for human control and critical evaluation of KI-generated content.

Avhengighet og forståelse
En utfordring med å bruke KI så aktivt er faren for overavhengighet, særlig i oppstartsfasen. Da prosjektet startet, hadde gruppen begrenset erfaring med hvordan Gemini kunne brukes mest mulig effektivt i Visual Studio Code. Dette førte til at vi i begynnelsen stolte litt for mye på KI uten å reflektere kritisk over resultatene. Koden ble ofte tatt videre uten grundig vurdering, og vi oppdaget i etterkant at enkelte løsninger var feil eller lite hensiktsmessige.
Denne raske fremdriften i starten førte også til at promptene (instruksjonene vi ga til KI) ikke ble lagret systematisk, noe som gjorde det vanskelig å spore hva vi faktisk hadde gjort og hvorfor. Dette ble raskt en viktig læringserfaring. Etter de første fasene innførte vi en mer strukturert praksis der vi lagret alle KI-prompter i egne filer, dokumenterte svarene og ba Gemini partake korte sammendrager fra hver fase. Dette ga bedre oversikt, bedre læring og gjorde det enklere å forbedre samarbeidet mellom mennesker og KI.

Ved å innføre denne strukturen gikk gruppen fra å bruke KI som et “hurtigverktøy” til å bruke det som en integrert lærings- og dokumentasjonsressurs. Erfaringen viste hvor viktig det er å kombinere teknologisk støtte med refleksjon og kritisk tenkning for å bevare faglig forståelse og eierskap til prosjektet.

Kreativitet og problemløsning
Selv om KI ofte kom med nyttige forslag, kunne den også begrense kreativiteten. Løsningene var gjerne konvensjonelle og ikke nødvendigvis innovative. Dette gjorde at gruppen måtte utfordre KI-forslagene aktivt for å tenke utenfor de mest opplagte løsningene. Det ble derfor viktig å bruke KI som et støtteverktøy – ikke som en erstatning for egen refleksjon og problemløsningsevne.

### 4.3 Sammenligning: Med og uten KI
[Reflekter over hvordan prosjektet ville vært uten KI]
- Hva ville vært annerledes?
- Hvilke deler av prosjektet ville vært vanskeligere/lettere?
- Ville sluttresultatet vært bedre eller dårligere?

### 4.4 Samlet vurdering
[Konklusjon: Hvordan påvirket KI sluttresultatet totalt sett?]
- Var KI en netto positiv eller negativ faktor?
- Hva var den viktigste lærdommen om å bruke KI i utviklingsprosessen?

-- -

## 5. Etiske implikasjoner

### 5.1 Ansvar og eierskap
- Hvem er ansvarlig for koden når KI har bidratt?
- Hvordan sikrer man kvalitet når KI genererer kode?
- Diskuter spørsmål om opphavsrett og intellektuell eiendom

### 5.2 Transparens
- Bør det være transparent at KI er brukt?
- Hvordan dokumenterer man KI sin bidrag?
- Hva er konsekvensene av å ikke være åpen om KI-bruk?

### 5.3 Påvirkning på læring og kompetanse
- Hvordan påvirker KI-avhengighet fremtidig kompetanse?
- Hvilke ferdigheter risikerer man å ikke utvikle?
- Balanse mellom effektivitet og læring

### 5.4 Arbeidsmarkedet
- Hvordan kan utbredt KI-bruk påvirke fremtidige jobber i IT?
- Hvilke roller vil bli viktigere/mindre viktige?
- Deres refleksjoner om fremtidig karriere i en KI-drevet verden

### 5.5 Datasikkerhet og personvern
- Hvilke data delte dere med KI-verktøy?
- Potensielle risikoer ved å dele kode og data med KI
- Hvordan skal man tenke på sikkerhet når man bruker KI?

-- -

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

### 7.4 Personlig refleksjon (individuelt)

**[Navn på gruppemedlem 1]:**
[Personlig refleksjon over egen læring og utvikling]

**[Navn på gruppemedlem 2]:**
[Personlig refleksjon over egen læring og utvikling]

**[Navn på gruppemedlem 3]:**
[Personlig refleksjon over egen læring og utvikling]

-- -

## 8. Vedlegg (valgfritt)

- Skjermbilder av applikasjonen
- Lenke til GitHub repository
- Annen relevant dokumentasjon

-- -

**Ordantall:** [Ca. antall ord]

**Forventet lengde:** 3000-5000 ord (avhengig av gruppestørrelse og prosjektets kompleksitet)