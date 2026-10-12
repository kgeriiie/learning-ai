# Blokk 13 — Reasoning kiértékelés (GSM8K)

Modell: qwen2.5:14b (Ollama, lokális), a Blokk 12-es ReAct agent (`calculate` + `answer_it` tool-okkal).
Minta: GSM8K `test` split első 10 kérdése.

## Nyers eredmény

**Score: 70.0%** (7/10 helyes az automatikus kiértékelő szerint)

## Hibás esetek

1. **Wendi csirkéi** — agent kinyert válasz: 3.0, hivatalos: 20.0
2. **Kylar poharai** — agent kinyert válasz: 16.0, hivatalos: 64.0
3. **Carla letöltése** — agent kinyert válasz: 200.0, hivatalos: 160.0

## Elemzés

Az 1. és 2. eset **nem valódi reasoning-hiba**: az agent szöveges válasza mindkétszer tartalmazta a helyes végeredményt, de a mondat **később** még említett egy másik számot (pl. "20 chickens", "16 glasses"), és az egyszerű "vedd az utolsó számot a szövegből" regex-heurisztika ezt a hibás, később szereplő számot nyerte ki helyette. Ez a kiértékelő módszer (extraction logika) korlátja, nem az agent hibája.

A 3. eset **valódi reasoning-hiba**: az agent helyesen vezette le lépésről lépésre a részeredményeket (40+20+100=160 perc), de a végső összegzésben önellentmondásba került, és egy másik (helytelen) számot mondott végeredményként.

## Korrigált (valós) pontszám

**90.0%** (9/10) — ha a kinyerési hibákat (1. és 2. eset) kijavítjuk, és csak a ténylegesen téves reasoninget (3. eset) számoljuk hibának.

## Tanulság

A nyers automatikus pontszám **alábecsülte** a modell valódi képességét, mert a kiértékelő harness (a regex-alapú válasz-kinyerés) maga is hibaforrás — nem csak a mért jelenség (a modell reasoningje) hibázhat, hanem az azt mérő eszköz is. Ez egy valós, gyakori csapda LLM-kiértékelésnél: a mérőmódszer korlátait könnyű összekeverni a mért rendszer korlátaival.
