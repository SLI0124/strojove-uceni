Algoritmy I

    Na základě diskuse s ChatGPT o podobě projektu, jeho zadání, a rozsahu témat, jsem vytvořil seznam klíčových bodů, které
    podle mého názoru odrážejí podstatné aspekty, jež byste měli při práci zvážit. I když tento checklist přesně nekopíruje
    obsah přednášek a cvičení, považuji ho za užitečný základ pro strukturovaný přístup k projektu. Doporučuji zahrnout
    některé z těchto bodů do vaší analýzy a využít je jako vodítko pro zpracování úkolu.

    Petr Prokop (+ ChatGPT)

# Checklist pro projekt: Klasifikace dat

Použijte tento checklist jako osnovu při práci na projektu klasifikace dat. Každé téma zvažte ve vztahu k vašemu
datasetu a implementaci.

1. **Analýza a porozumění dat**

    - **Zdroj datové sady**: Odkud data pochází? Jaký je jejich kontext a praktický význam?=
    - **Popis atributů**: Identifikace jednotlivých atributů (numerické, kategoriální, textové).
    - **Identifikace cílové proměnné**: Co predikujete a jaký to má praktický dopad?
    - **Prozkoumání nevyváženosti tříd**: Jsou třídy vyvážené? Pokud ne, jak to ovlivní klasifikaci?
    - **Vizualizace závislostí**: Vztahy mezi atributy a cílovou proměnnou (např. korelace, scatter ploty, heatmapy).

2. **Předzpracování dat**

    - **Čištění dat**: Odstranění chybějících hodnot, outlierů a nekonzistentních dat.
    - **Normalizace/škálování**: Úprava numerických atributů (např. min-max scaling, standard scaling).
    - **Kódování kategoriálních dat**: Převod kategorií na číselné hodnoty (např. one-hot encoding).
    - **Feature engineering**: Vytvoření nových atributů nebo transformace stávajících.
    - **Redukce dimenze**: Použití metod jako PCA nebo selekce atributů pro zjednodušení modelu.
    - **Zpracování textových dat**: Převod textu na číselné reprezentace (např. TF-IDF, embeddingy).

3. **Rozdělení dat**

    - **Rozdělení na sady**: Rozdělení dat na trénovací, validační a testovací sady (např. 70-15-15).
    - **Krosvalidace**: Implementace k-fold nebo stratifikované krosvalidace.
    - **Zpracování časových řad**: Zajištění správného rozdělení, aby nedocházelo k úniku informací mezi sadami.

4. **Výběr klasifikátorů**

    - **Použití základních metod**: Implementace povinných algoritmů (např. DecisionTree a RandomForest).
    - **Testování dalších metod**: Vyzkoušení alespoň dvou dalších algoritmů (např. Logistic Regression, SVM, Gradient
      Boosting).
    - **Srovnání metod**: Porovnání jednoduchých a složitých modelů v kontextu vašeho datasetu.

5. **Optimalizace modelů**

    - **Ladění hyperparametrů**: Testování vlivu různých hodnot parametrů (např. hloubka stromu, počet stromů).
    - **Optimalizační metody**: Použití GridSearchCV, RandomizedSearchCV nebo pokročilých metod (např. Bayesian
      Optimization).
    - **Analýza výsledků**: Jak změny hyperparametrů ovlivňují výkon modelu?

6. **Výběr a hodnocení metrik**

    - **Výběr metrik**: Uveďte, které metriky používáte (např. accuracy, precision, recall, F1-score, ROC-AUC) a proč.
    - **Řešení nevyváženosti tříd**: Použití vážených metrik nebo PR-AUC pro dataset s nevyváženými třídami.
    - **Vizualizace metrik**: Prezentace výsledků pomocí confusion matrix, ROC křivek nebo dalších grafů.

7. **Interpretace modelů**

    - **Vysvětlení modelů**: Použití metod jako SHAP, LIME nebo feature importance.
    - **Identifikace důležitých atributů**: Jaké atributy měly největší vliv na predikce?
    - **Logická analýza výsledků**: Odpovídají výsledky modelu kontextu problému?

8. **Řešení problémů v datech**

    - **Nevyváženost tříd**: Testování SMOTE, oversamplingu nebo vážení tříd.
    - **Chybějící hodnoty**: Imputace nebo odstranění chybějících dat.
    - **Šum**: Jak model zvládá šum a nekonzistence v datech?

9. **Srovnání výsledků**

    - **Porovnání modelů**: Který model dosáhl nejlepších výsledků a proč?
    - **Analýza přeučení**: Vyhodnocení rozdílů mezi trénovací, validační a testovací sadou.
    - **Diskuze nad omezeními modelu**: Jaké problémy se objevily a jak by šly řešit?

10. **Prezentace výsledků**

    - **Struktura projektu**: Je výstup přehledný a obsahuje všechny důležité části?
    - **Vizualizace**: Jsou výsledky prezentovány srozumitelně (grafy, tabulky, popisky)?
    - **Kód a interpretace**: Je kód dobře okomentovaný a interpretace jasná?

11. **Aplikace modelu a doporučení**

    - **Praktická aplikace**: Jak by mohl být model nasazen v reálném světě?
    - **Návrhy na zlepšení**: Jaké další kroky by mohly zvýšit kvalitu modelu?
    - **Omezení projektu**: Jaká jsou možná omezení a rizika při použití modelu?

