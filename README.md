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
- Na jednom z testovacích souborů ([chess](datasets/chess.dat), [connect](datasets/connect.dat)) vygenerujte četné vzory
  a vypočtěte Support.
- Z vygenerovaných četných vzorů vypište pravidla a jejich Confidence.

## Cvičení 2: Hierarchické aglomerativní shlukování

### Implementace algoritmu **(2 body)**

Vytvořte vlastní implementaci algoritmu, který načte data a pro vybranou [datovou sadu](datasets/data_clustering)
provede shlukování.

- Cílem bude implementovat dvě varianty aglomerativního shlukování a to **single** a **complete** linkage.
- Obě metody vychází z matice vzdáleností - počítejte s **Manhattan** a **Euclidean** vzdáleností.
- Cílem bude provést shlukování, které se zastaví buď při vhodné příležitosti (dosažení požadovaného počtu shluků), nebo
  po kompletním shlukování.
    - Při kompletním shlukování “sestupte” po dendrogramu shluků a nalezněte daný počet shluků.
- Výsledek shlukování vizualizujte pomocí bodového grafu.

### Preprocesing a cosinova vzdálenost **(1 bod)**

Tato část úkolu je zaměřena na otestování chování **Cosine** vzdálenosti pro ukázková data.

- Rozšiřte váš algoritmus o další typ vzdálenosti - **Cosine** vzdálenost (nepodobnost).
- Vyberte si jeden vstupní soubor a pro něj připravte dvě předzpracované verze - normalizování do rozsahu <0,1>,
  standardizace (průměr roven 0 a standardní odchylka 1).
- Proveďte shlukování a vizualizujte výsledky pro vybranou datovou sadu a její dvě verze po předzpracování.
- Zamyslete se nad výsledkem a rozdílem oproti první předešlým vzdálenostem.

## Cvičení 3 - Shlukování Sklearn

Úkolem cvičení je prozkoumat a použít shlukovací metody z knihovny Sklearn pro datovou
sadu [Red wine quality](datasets/data_clustering/winequality-red.csv). K dispozici je šablona, kde je připraveno načtení
dat, vizualizace a základní předzpracování dat. Úkolem je vyzkoušet si různé možnnosti předzpracování dat a následně
použít vybranou metodu shlukování. Náslendě je potřeba výsledky vizualizovat a popsat jednotlivé shluky. V druhé části
je třeba si vyzkoušet Gini Index a Entropii jako další metriku pro vyhodnocení kvality shlukování (na základě atributu
kvality vína). Nebo si zkusit Mahalanobis vzdálenost pro vyhodnocení kvality shlukování.

## Cvičení 4 - Redukce dimenze

Cílem cvičení je vyzkoušet možnosti redukce dimenze a ověřit schopnost metod redukovat šum v datech. Využít SVD roklad a
prozkoumat chybu rekonstrukce matice. Dalším úkolem je použití metod PCA a TSNE pro vytvoření 2D vizualizace dat.je
použití metod PCA a TSNE pro vytvoření 2D vizualizace dat.

[BAR datasets](datasets/bars_datasets) - 10 000 obrázků 8x8 uložených jako 64 bajtů v textovém formátu, některé datové
sady obsahují určitou úroveň šumu v jednotlivých obrázcích.

## Cvičení 5 - Rozhodovací strom

### Implementujte algoritmus pro sestrojení rozhodovacího stromu. **(2b)**

Načtěte [dataset pro klasifikaci](datasets/data_classification) (využijte hlavně
dataset [sep.csv](datasets/data_classification/sep.csv), [nonsep.csv](datasets/data_classification/nonsep.csv) a
[iris.csv](datasets/data_classification/iris.csv)). Použijte rozdělení dat na trénovací a testovací sadu pro vyhodnocení
kvality klasifikačního algoritmu. **Vytvořte vaší implementaci rozhodovacího stromu.** Jakého skóre dosáhl rozhodovací
strom při validaci?

### Overfitting a underfitting

Otestuje vliv parametru maximální hloubky rozhodovacího stromu na trénovací a testovací přesnost. **(1b)**

Využijte dataset s reálnou [datovou sadou Titanic](datasets/data_classification/titanic.csv) - klasifikace, která byla
předzpracovaná do číselné podoby
viz [notebook](https://homel.vsb.cz/~pro0199/files/su_cv5_titanic_classification_preprocess.ipynb).
Proveďte vyhodnocení trénovací a testovací přesnosti bez omezení maximální hloubky i při nastavení parametru maximální
hloubky z intervalu <1, 15>. Dochází v tomto případě k efektům zvaných _overfitting_ nebo _underfitting_?
