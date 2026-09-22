# AI Engineer Tanterv — 0-ról Architect szintig

Forrás: `GDE_AI_Engineer_Syllabus.pdf` (What You'll Learn szekció, 9-12. oldal) + Rolling Project (13. oldal).
Kiindulás: szoftverfejlesztői háttér, AI-ban kezdő. Tempó: ~10-15 óra/hét. Becsült teljes hossz: ~26 hét (~6 hónap).

Követés: ez a fájl az élő progress tracker. Minden blokk végén frissítjük az **Állapot** és **Dátum** mezőt, és rögzítjük a mérföldkő linkjét/jegyzetét.

Állapot jelölések: `⬜ nincs elkezdve` / `🔶 folyamatban` / `✅ kész`

---

## Szint-térkép

| Szint | Blokkok | Amit ez igazol |
|---|---|---|
| **Junior AI Engineer** | 0–6 | Érted az NLP/ML/LLM alapokat, tudsz RAG-ot és LLM API-t integrálni |
| **AI Engineer** | 7–11 | Production-grade komponenseket építesz: MCP, konténerizált szolgáltatás, agent loop |
| **Senior / Architect** | 12–16 | Multi-agent rendszert tervezel és skálázol, production deploy, megfigyelhetőség, biztonság — teljes rendszert vittél élesbe |

---

## Mentor-protokoll (minden jövőbeli session-höz)

1. Megnézem ezt a fájlt: hol tartunk, mi az aktuális blokk állapota.
2. Átnézzük az előző mérföldkő produktumát (kód, jegyzet, kérdések) — ha van mit reviewolni, konkrét visszajelzést adok.
3. Rövid, tömör elméleti bevezető az aktuális blokk témájához (nem szöveg-fal, hanem a lényeg).
4. Kapsz egy konkrét, gyakorlati feladatot ("Kész kritérium" alapján).
5. Session végén frissítem ezt a fájlt: állapot, dátum, megjegyzés.

---

## Blokk 0 — Python & eszköz-refresher (1 hét)

**Cél:** környezet és eszközlánc gyorstalpaló, mivel van SW háttered — csak a hiányzó darabok.
**Témák:** venv/uv, csomagkezelés, git workflow, alap Docker fogalmak (később mélyítjük), Jupyter.
**Mérföldkő:** helyi dev környezet felállítva (Python 3.11+, venv, git repo a projekthez).
**Kész kritérium:** tudsz egy Python scriptet futtatni izolált környezetben, van git repód a kurzus projekthez.
**Állapot:** ✅ kész | **Dátum:** 2026-07-08

## Blokk 1 — NLP alapok (2 hét)

**Témák:** szövegelőfeldolgozás (tokenizáció, stopword, lemmatizáció), Word Embeddings (Word2Vec, GloVe, FastText), NER (spaCy, HuggingFace), szövegklasszifikáció, mondat-hasonlóság (SBERT, USE).
**Mérföldkő:** kis NER + klasszifikációs pipeline egy nyílt datasetten (pl. hírek vagy vélemények).
**Kész kritérium:** el tudod magyarázni embedding vs. one-hot különbséget, és van futó pipeline-od kimenettel.
**Állapot:** ✅ kész | **Dátum:** 2026-07-21 — elmélyítés lezárva mind a 4 témában. (4) NER+klasszifikáció rotten_tomatoes adaton: NER kisbetűs neveken is jól működött (kontextus > nagybetűzés), klasszifikációnál önállóan debuggolt két valós hibát (import mellékhatás duplikált kimenetet okozott; nem kevert dataset torz/homogén teszthalmazt adott, hamis 1.0 pontossággal) — végső, hiteles eredmény: 78% kiegyensúlyozott adaton

## Blokk 2 — Advanced NLP + RAG (2 hét)

**Témák:** RAG architektúra, vektor embeddingek, vektor adatbázisok, KNN vektor-keresés, alap RAG pipeline (FAISS/HuggingFace), dokumentum-Q&A / tudásalapú chatbot.
**Mérföldkő (Phase 1 projekt indul):** működő RAG demo saját dokumentumokon (document Q&A).
**Kész kritérium:** a RAG demo helyes választ ad egy nem-triviális kérdésre a saját dokumentumaidból.
**Állapot:** ✅ kész | **Dátum:** 2026-07-23 — teljes pipeline felépítve: .txt dokumentum → SBERT embedding → FAISS IndexFlatL2 retrieval → extractive QA (transformers). Önállóan debuggolt egy valós FAISS+transformers SIGSEGV library-ütközést (Apple Silicon, megoldás: KMP_DUPLICATE_LIB_OK + OMP_NUM_THREADS env varok). Mélyen megértett korlátok: (1) top-1 retrieval nem mindig a tartalmilag legjobb, (2) QA confidence score span-határ bizonyosságot mér, nem tartalmi helyességet, (3) naiv kontextus-összefűzés nem javít, mert extractive QA nem tud szintetizálni — ez indokolja a Blokk 6-os áttérést generatív LLM-re

## Blokk 3 — ML alapok (2 hét)

**Témák:** felügyelt vs. felügyelet nélküli tanulás, lineáris/logisztikus regresszió, döntési fák, Random Forest, XGBoost, deep learning és megerősítéses tanulás áttekintés, kiértékelési metrikák (accuracy, precision, recall, F1, AUC), cross-validation, hiperparaméter-tuning (GridSearchCV, Optuna).
**Mérföldkő:** egy klasszikus ML modell betanítva + kiértékelve, hiperparaméter-tuning legalább egy modellen.
**Kész kritérium:** meg tudod indokolni metrikaválasztást a konkrét problémára, és van reprodukálható eredményed.
**Állapot:** ✅ kész | **Dátum:** 2026-07-24 — diabetes datasetten 3 modell összehasonlítva reprodukálható (random_state) RMSE-vel: LinearRegression 53.37, hangolt Ridge (GridSearchCV, alpha keresési tartomány számított) 53.01, RandomForestRegressor 54.23 — mindig a kisebb/lineáris modell nyert, jó lecke hogy "fancyabb" modell nem mindig jobb kis adaton. Metrika-indoklás (RMSE vs accuracy) megértve. Felügyelet nélküli tanulás: KMeans + make_blobs, 98/100 pont helyesen csoportosítva címkék nélkül, vizualizálva matplotlib-bal. Fa-alapú modellek (döntési fa, Random Forest, XGBoost) fogalmilag tisztázva.

## Blokk 4 — GenAI Topics (1 hét)

**Témák:** GPU alapok, CUDA/NVIDIA driverek, Whisper (speech-to-text), multimodális modellek és képfeldolgozás.
**Mérföldkő:** kis demo — hang átirat Whisperrel, vagy egyszerű multimodális (kép+szöveg) lekérdezés.
**Kész kritérium:** érted mikor kell GPU, és futtattál legalább egy multimodális/audio modellt.
**Állapot:** ✅ kész | **Dátum:** 2026-08-06 — Whisper (tiny modell) audio átirat sikeresen lefuttatva saját QuickTime-mal rögzített felvételen. Valós hiba megoldva: a tiny modell svédnek ismerte fel a magyar beszédet, `language="hu"` paraméterrel explicit javítva. GPU/CUDA/MPS elmélet tisztázva, CPU vs GPU döntési szempont helyesen megfogalmazva. Bónusz: multimodális kép+szöveg demo is lefutott (`visual-question-answering` pipeline saját képen, helyes, rangsorolt válaszokkal).

## Blokk 5 — Bevezetés az LLM-ekbe (1 hét)

**Témák:** transformer/attention/decoder-only architektúra alapjai, pretraining vs. fine-tuning, modellcsaládok (GPT, Claude, LLaMA, Mistral/Falcon/Cohere említés szinten).
**Mérföldkő:** rövid írásos összefoglaló (saját szavaiddal) arról, hogyan generál egy decoder-only LLM egy tokent.
**Kész kritérium:** el tudod magyarázni egy junior kollégának az attention lényegét analógiával.
**Állapot:** ✅ kész | **Dátum:** 2026-08-06 — saját szavakkal helyesen leírta az autoregresszív, tokenenkénti generálást, és önállóan alkotott "zsúfolt parti" analógiát az attention-re (mondat=parti, szavak=vendégek, generált token=aki eldönti kire figyeljen). Pretraining vs fine-tuning és a fő modellcsaládok (GPT/Claude/LLaMA/Mistral/Falcon/Cohere) érintőlegesen átbeszélve.

## Blokk 6 — LLM Integration (2 hét)

**Témák:** Open WebUI, OpenAI API, Anthropic Claude API, AWS Bedrock (multi-model, auth, cost, latency), llama.cpp (lokális futtatás, kvantálás), LangChain/LangGraph áttekintés, tiszta Python integráció, LiteLLM (model-agnosztikus API).
**Mérföldkő (Phase 1 projekt folytatás):** AI-powered microservice — LLM integrálva, input/output kezelve, hibakezeléssel.
**Kész kritérium:** a microservice legalább 2 különböző LLM providerrel működik (pl. OpenAI + Claude, LiteLLM-en át).
**Állapot:** ✅ kész | **Dátum:** 2026-08-10 — LiteLLM-en át 2 provider működik: Anthropic Claude (API kulccsal) és helyi Llama modell Ollama-n át (llama.cpp témát is lefedi, ingyenes — OpenAI kihagyva fizetés hiányában, pl. helyettesítve). Útközben megoldva: API kulcs biztonságos kezelése (2. alkalommal is véletlen kulcs-beillesztés a chatbe, azonnal revoke-olva), PyCharm run-config env var beállítás, OpenAI billing hiba felismerése. Try/except hibakezelés hozzáadva és mindkét ág (siker/hiba) tesztelve.

*→ Ezzel a Phase 1 (Foundation Build) projekt lezárva. Junior AI Engineer szint elérve.*

## Blokk 7 — Claude Code / Engineering Workflows (1 hét)

**Témák:** kódgenerálás, debug, refaktor; nagy kódbázis kontextuskezelés; teszt-generálás és validáció; tool use; prompt-vezérelt fejlesztés; iteratív prototípuskészítés; beépítés a dev workflow-ba.
**Mérföldkő:** egy meglévő (akár saját) kódbázis-részlet refaktorálása és tesztlefedettség növelése AI-asszisztált workflow-val.
**Kész kritérium:** dokumentált előtte/utána diff + teszt eredmények.
**Állapot:** ✅ kész | **Dátum:** 2026-08-10 — a Blokk 3 diabetes scriptje refaktorálva (lineáris kódból 4 tesztelhető függvény: load_data, train_tuned_ridge, train_random_forest, evaluate), holt kód törölve. 2 unit teszt írva (unittest, önállóan), egy paraméterezhető mock-modell osztállyal (jó DRY-ösztön), mindkettő PASSED. Tanulság: mindig commitolj refaktor előtt, hogy legyen tiszta git diff.

## Blokk 8 — Prompt Engineering (1,5 hét)

**Témák:** prompt management, alapelvek (instruction following, temperature, top-p, role prompting), Chain-of-Thought és ReAct minták, few-shot vs. zero-shot, prompt kiértékelés és iteráció.
**Mérföldkő:** egy konkrét feladatra (pl. RAG válaszminőség) prompt-iteráció mérhető javulással (előtte/utána metrika).
**Kész kritérium:** van dokumentált prompt-verziótörténeted és mérőszámod a javulásra.
**Állapot:** ✅ kész | **Dátum:** 2026-08-10 — Blokk 2 RAG projekt visszavéve, extractive QA lecserélve valódi LLM hívásra (LiteLLM + ollama/llama3.2). Mérés: trükkös kérdés (digital tablet vs e-reader indoklás összekeverhető) 5x lefuttatva. V1 (naiv prompt): 1/5 helyes (20%) — modell hajlamos letagadni a meglévő választ. V2 (direktebb, "ne tagadd le a választ, ne adj extra magyarázatot"): 5/5 helyes (100%). Tiszta, dokumentált, mérhető javulás.

## Blokk 9 — Applied LLM Engineering (2 hét)

**Témák:** modell-desztilláció, MCP szerver/kliens architektúra (queueing, scheduling, inference management / strukturált kérések, retry, output handling), "vibe coding" példák.
**Mérföldkő (Phase 2 projekt indul):** az AI microservice becsomagolva MCP kliens-szerver struktúrába, queueing + retry támogatással.
**Kész kritérium:** a rendszer túlél egy szimulált hibát (retry működik), és strukturált választ ad.
**Állapot:** ✅ | **Dátum:** 2026-08-25

*Megjegyzés:* MCP szerver/kliens (FastMCP) felépítve, a Block 8-as RAG+LLM logikát (`answer_it`) importálja sys.path-bővítéssel. Retry exponenciális backoff-fal tesztelve szimulált hibával (érvénytelen modellnév → 3 retry 1s/2s/4s késleltetéssel, majd graceful fail). Strukturált válasz: `AnswerResult` dataclass (`answer`, `success`, `attempts`), végigvezetve `generate_answer` → `answer_it` → MCP tool → kliens láncon. Tanulságos hibák útközben: modul/osztály névütközés importnál, MCP kliens oldali `CallToolResult.data` rekonstrukció (ehhez visszatérési típus-annotáció kell a tool függvényen), és a legfontosabb — `@dataclass` és kézzel írt `__init__` együtt nem működik, a mezőket class-szintű típusannotációként kell megadni, nem saját konstruktorban.

## Blokk 10 — Infrastructure and Deployment (2 hét)

**Témák:** Docker konténerizáció, API kiszolgálás FastAPI/Flask-kal, inference skálázás, GPU erőforrás-menedzsment, monitoring/logging (LangFuse, OpenTelemetry), model serving vLLM-mel.
**Mérföldkő:** a projekt Dockerizálva, FastAPI mögött fut, alap logging/monitoring bekötve.
**Kész kritérium:** `docker run` egy paranccsal elindítja a teljes szolgáltatást, és van látható log/metrika kimenet.
**Állapot:** ✅ | **Dátum:** 2026-09-07

*Megjegyzés:* A `document_mcp` RAG-logika (Blokk 9-es extra gyakorlat) FastAPI mögé kötve (`/ask` POST endpoint, Pydantic request model). Dockerizálva: `Dockerfile` + `.dockerignore`, `docker build` + `docker run -p 8000:8000` egy paranccsal elindítja. Valós hibák útközben: (1) csomagon belüli relatív importok (`from document_results import ...`) elromlanak, ha a modult csomagként (`document_mcp.api:app`) indítod — abszolút importra kellett váltani; (2) relatív fájl-útvonal (`clean_code.pdf`) a futtatás helyétől függött, `os.path.dirname(__file__)`-alapú abszolút útvonalra javítva; (3) konténerből a host gépen futó Ollama nem érhető el `localhost`-on — Docker Desktop `host.docker.internal` DNS-neve + `OLLAMA_API_BASE` env változó oldotta meg, hogy helyi és konténeres futtatás is működjön. Logging: `print` helyett `logging` modul, kérdésenként log a sikerességről, próbálkozás-számról és válaszidőről — konténerben is látható. Külön megbeszélve: Ollama-t nem a konténerbe sütjük bele (image-méret, egy-folyamat-per-konténer elv) — docker-compose-os, két-konténeres (app+ollama) verzió jövőbeli bővítési lehetőségként megjegyezve.

## Blokk 11 — Advanced AI Topics (1,5 hét)

**Témák:** aszinkron feldolgozás, resiliency (hibakezelés, retry, séma-validáció), context engineering, progressive disclosure, agent skills.
**Mérföldkő:** a szolgáltatás átalakítva async-ra, séma-validáció bekötve (pl. Pydantic).
**Kész kritérium:** terheléses mini-teszt mutatja az async előnyét a szinkron verzióhoz képest.
**Állapot:** ✅ | **Dátum:** 2026-09-09

*Megjegyzés:* A document_mcp RAG-szolgáltatás async-ra alakítva: `litellm.acompletion` + `await`, retry-backoff `asyncio.sleep`-pel (nem blokkoló), végigvezetve `async_answer_question` → `async_answer_it` → FastAPI `/ask` és MCP tool láncon, a szinkron verzió is megtartva összehasonlításhoz (`/ask` sync, `/ask-async` async). Séma-validáció: Pydantic `Field(min_length=..., max_length=...)` a kérés- és válasz-modelleken (tanulság: kimeneti/generált mezőre nem érdemes felső hosszkorlátot tenni, mert valós adatot törhet el). Terheléses mini-teszt: `ThreadPoolExecutor` + `requests`, 5 egyidejű kérés — sync 8.74s, async 6.95s (~20% gyorsabb). Reális, tanulságos eredmény: a különbség valós, de nem drámai, mert a helyi Ollama backend maga is korlátozottan párhuzamosít — az async a saját FastAPI rétegen javít, nem varázsolja el a downstream szűk keresztmetszetet. Útközbeni hibák: Docker build extrém lelassulása (CUDA-s torch függőségek Linuxon) — megoldva `[tool.uv.sources]` + explicit `torch` direkt függőségként való felvételével (a forrás-átirányítás csak direkt függőségre hat); `ThreadPoolExecutor.submit(fn(arg))` vs `submit(fn, arg)` különbség (előbbi azonnal, szinkron hívja meg a függvényt a főszálon, ami hibás).

## Blokk 12 — AI Agents (2,5 hét)

**Témák:** kontextuskezelés, chatbot fejlesztés, history management, agent design patternek (agent loop vs. DAG), tervezés/döntéshozatal (tool use, memória, célok), implementációs minták (LangChain Agents, ReAct, Finite State Agents), runtime menedzsment és költségvonzat, multi-agent architektúrák CrewAI-jal.
**Mérföldkő (Phase 2 projekt folytatás):** valódi agentic ReAct loop tool use-zal + egy multi-agent (CrewAI) proof-of-concept.
**Kész kritérium:** az agent legalább 2 eszközt (tool) tud önállóan kiválasztani és használni egy összetett feladatban.
**Állapot:** ✅ | **Dátum:** 2026-09-22

*Megjegyzés:* ReAct agent loop LiteLLM function callinggal: 2 eszköz (`calculate` — biztonságos, korlátozott `eval()`; `answer_it` — a document_mcp RAG). A modell (előbb llama3.2, majd qwen2.5:14b) helyesen, önállóan választott a két eszköz között kérdés típusa alapján. Valós, dokumentált limitáció: Ollama-n keresztül a `tool_choice="auto"` gyakorlatilag mindig tool-hívásra kényszerít, ha `tools` jelen van a kérésben — még akkor is, ha a modell már megkapta a tool-eredményt a historyban. Diagnosztizálva: `messages` tartalom kiíratásával igazolva, hogy a history helyes volt, a hívás nélküli teszt igazolta, hogy a `tools` paraména jelenléte maga a probléma. Megoldás: kétfázisú hívás — csak az első körben `tools`-szal, utána anélkül, hogy kikényszerítsük a végső szöveges választ (max. 1 tool-hívás/kör, tudatos kompromisszum, nem hiba). `for...else` Python-szintaxis bevezetve a "nem sikerült lezárni N próbálkozás alatt" eset kezelésére. Multi-agent CrewAI proof-of-concept: 3 agent (Product Manager → Software Engineer → Code Reviewer) szekvenciális `Crew`-ban, `Task context=[...]` lánccal, egy "gyógyszer-emlékeztető" feature-ön. Valódi emergens érték: a Reviewer agent ténylegesen releváns hibákat/hiányosságokat talált (kód-duplikáció, hiányzó validáció, hiányzó docstring) és érdemben jobb, refaktorált kódot adott vissza.

*→ Ezzel a Phase 2 (Workflow Integration) projekt lezárva. AI Engineer szint elérve.*

## Blokk 13 — Model Reasoning (1 hét)

**Témák:** reasoning vs. pattern completion, induktív/deduktív/abduktív módok, multi-hop reasoning, tool use a reasoning kiterjesztésére, kiértékelési módszerek (TruthfulQA, BBH, GSM8K).
**Mérföldkő:** saját reasoning-kiértékelés futtatása az agentedre egy publikus benchmark alcsoportján.
**Kész kritérium:** van számszerű reasoning-pontszámod és tudod értelmezni a hibás eseteket.
**Állapot:** ⬜ | **Dátum:** —

## Blokk 14 — From Code to Production (2,5 hét)

**Témák:** end-to-end LLM automatizációs alkalmazás, egyedi MCP kliens/szerver + n8n workflow integráció, valós deployment (CI/CD, verziózás, failover), etika/compliance/biztonság AI rendszerekben.
**Mérföldkő (Phase 3 projekt):** CI/CD pipeline, failover terv, monitoring, compliance-checklist a teljes rendszerhez.
**Kész kritérium:** egy commit push automatikusan deployol, van rollback/failover terv leírva, és monitoring dashboard mutatja az élő státuszt.
**Állapot:** ⬜ | **Dátum:** —

*→ Ezzel a Phase 3 (Production Deployment) projekt lezárva.*

## Blokk 15 — Capstone Review & Portfólió (1 hét)

**Cél:** a teljes rendszer (Phase 1→3) egyben bemutatva: architektúra diagram, README, demo, ismert korlátok és skálázási terv.
**Kész kritérium:** el tudod adni 15 percben egy technikai interjún úgy, mint egy általad tervezett, épített és élesített production AI rendszert.
**Állapot:** ⬜ | **Dátum:** —

*→ **Architect szint elérve.***

---

## Jegyzetek / eltérések a tervhez képest

*(itt gyűjtjük session közben, ha módosítunk ütemezést, sorrendet, vagy extra témát viszünk be)*

- 2026-08-25: Blokk 9 lezárva, Phase 2 (Workflow Integration) projekt elindult. Következő session Blokk 10-zel (Infrastructure and Deployment) indul.
- 2026-08-25 (extra, kurzuson kívüli gyakorlat): valós tankönyv-RAG (Clean Code PDF) végigvitele Blokk 2+8+9 mintáira építve, önállóan: PDF-kinyerés (pypdf), szavas chunkolás átfedéssel, embedding+FAISS index modul-szintű egyszeri build (nem minden hívásnál), top-k retrieval, retry+backoff LLM válaszgenerálás strukturált (`DocumentResult`) kimenettel, MCP tool-ba csomagolva docstringgel — végig működő, tesztelt pipeline (`document_mcp` mappa). 2026-07-08: a blokkonkénti hét-becslések irányadók, nem határidők. Gergő inkább lassabban, szilárd alapokkal halad — ha egy blokk nem érzi elég biztosnak, ott maradunk, amíg nem az. Minőség > tempó, főleg az alapozó blokkoknál.
- 2026-07-23: Blokk 0-2 lezárva. Következő session: Blokk 3 (ML alapok) indítása.
- 2026-08-10: Blokk 0-6 mind lezárva, Phase 1 Rolling Project kész → **Junior AI Engineer szint elérve**. Következő session: Blokk 7 (Claude Code / Engineering Workflows) indítása.
- 2026-09-07: Blokk 10 lezárva (FastAPI + Docker + logging a document_mcp RAG-ra). Következő session Blokk 11-gyel (Advanced AI Topics: async, resiliency, context engineering) indul.
- 2026-09-09: Blokk 11 lezárva (async átalakítás, séma-validáció, terheléses mini-teszt). Ezzel az **AI Engineer szint** blokkjai (7-11) mind lezárva. Következő session Blokk 12-vel (AI Agents — agentic ReAct loop, multi-agent CrewAI) indul, ez a Phase 2 Rolling Project folytatása.
- 2026-09-22: Blokk 12 lezárva (ReAct agent loop 2 eszközzel, CrewAI 3-agentes dev-csapat PoC). Ezzel a **Phase 2 Rolling Project lezárva, AI Engineer szint elérve** (a szint-térkép szerint blokk 7-11 volt AI Engineer, de a Phase 2 projekt ténylegesen blokk 12-vel zárul). Következő session Blokk 13-mal (Model Reasoning) indul, ez már a Senior/Architect szintű blokkok (12-16) második tagja.
