# Strojové učení

Cílem předmětu je poskytnout posluchači detailní přehled o postupech a metodách v oblasti strojového učení. Od
explorační analýzy dat, přes hledání podobnosti, porovnání objektů až po hledání klasifikačních modelů. Studenti budou
mít šanci si jednotlivé metody implementovat i vyzkoušet nad umělými i reálnými daty a zhodnotit dosažené výsledky,
které se naučí i správně odprezentovat.

Odkaz na stránku [předmětu](https://homel.vsb.cz/~pla06/) s přednáškami a
na [cvičení](https://homel.vsb.cz/~pro0199/su.html).

# Cvičení

## Cvičení 1:  Hledání vzorů a generování pravidel

Úkolem cvičení bude implementace algoritmu Apriori/ProjectedEnumerationTree pro dolování vzorů. Jednotlivé úkoly pro
cvičení:

- Vygenerujte všechny kombinace bez opakování o délce 3 z 6 možných.
- Na jednom z testovacích souborů (chess, connect) vygenerujte četné vzory a vypočtěte Support.
- Z vygenerovaných četných vzorů vypište pravidla a jejich Confidence.

## Cvičení 2: Hierarchické aglomerativní shlukování

### Implementace algoritmu (2 body)

Vytvořte vlastní implementaci algoritmu, který načte data a pro vybranou datovou sadu provede shlukování.

- Cílem bude implementovat dvě varianty aglomerativního shlukování a to single a complete linkage.
- Obě metody vychází z matice vzdáleností - počítejte s Manhattan a Euclidean vzdáleností.
- Cílem bude provést shlukování, které se zastaví buď při vhodné příležitosti (dosažení požadovaného počtu shluků), nebo
  po kompletním shlukování.
    - Při kompletním shlukování “sestupte” po dendrogramu shluků a nalezněte daný počet shluků.
- Výsledek shlukování vizualizujte pomocí bodového grafu.

### Preprocesing a cosinova vzdálenost (1 bod)

Tato část úkolu je zaměřena na otestování chování Cosine vzdálenosti pro ukázková data.

- Rozšiřte váš algoritmus o další typ vzdálenosti - Cosine vzdálenost (nepodobnost).
- Vyberte si jeden vstupní soubor a pro něj připravte dvě předzpracované verze - normalizování do rozsahu <0,1>,
  standardizace (průměr roven 0 a standardní odchylka 1).
- Proveďte shlukování a vizualizujte výsledky pro vybranou datovou sadu a její dvě verze po předzpracování.
- Zamyslete se nad výsledkem a rozdílem oproti první předešlým vzdálenostem.

