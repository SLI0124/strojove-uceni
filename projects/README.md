# Informace k projektům

## Shlukování dat (15-30 bodů):

- Shlukovací analýza s popisem nalezených skupin záznamů pro vámi vybraný dataset, informujte mě o jeho výběru emailem.
- Součástí práce bude základní popis analyzované datové sady, krátká explorace, předzpracování dat, aplikace
  shlukovacích metod a **popis nalezených shluků**. Je možné doplnit o vizualizaci shluků ve 2D.
- Povinou částí je **závěrečné shrnutí** zajímavých poznatků.
- Formou vypracování je Jupyter Notebook s kódy a interpretací vizualizací nebo PDF report + zdrojové kódy.
- Odhadovaná náročnost pro projekt je 3-6 hodin. Tento odhad můžete použít jako vodítko pro rozsah analýzy. Každopádně
  čas se bude lišit podle vašich dovedností.
- Termín odevzdání projektu je **1. 12. 2024 (23:59)**, projekt odevzdáte nahráním na Dropbox.
- Zisk bodů při splnění nutných podmínek u dobrého projektu bude 15-22 bodů. Pro získání maximálního počtu bodů je
  nezbytné detailnější rozmyšlení a provedení všech kroků - preprocessing, výběr shlukovací metody včetně jejich
  parametrů
  a dobrý popis získaných shluků. V rámci hodnocení bude brán zřetel na analytický přístup.

### Nutné podmínky:

- Provedení 3 různých shlukování (kombinace odlišného předzpracování a shlukovací metody) a **popis nalezených shluků**.
- Využití alespoň 2 shlukovacích metod.

### Co v rámci shlukování zkoušet:

- preprocessing metody pro analyzované data,
- parametry shlukovací metody,
- výběr atributů pro shlukování - kompletní dataset, ruční výběr (dle vašich předpokladů z popisu konkrétního datasetu),
  výběr s využitím Feature
  selection ([SelectKBest s chi^2](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html)
  testem nebo [jiné](https://scikit-learn.org/stable/modules/feature_selection.html)).

Výběr dat:

- Pro nalezení datasetu, pro vaši analýzu a shlukování můžete
  použít [Kaggle](https://www.kaggle.com/), [UCI repository](https://archive.ics.uci.edu/ml/datasets.php) a
  další zdroje na internetu.
- Doporučená velikost datové sady je 1000+ záznamů a 10+ atributů.
- Z výběru jsou vyloučeny data ze cvičení a přednášky (Titanic, Country Data, Red wine quality) a také datasety ze ZSU (
  Credit Card Data, Audi used car listings, FIFA 2022, Social, gender and study data from secondary school students,
  Wine
  Dataset for Clustering).
- Při výběru je třeba zvážit vhodnost dat ke shlukování. Například datové sady s převahou binárních nebo kategoriálních
  atributů budou složitější na shlukování.

## Klasifikace dat (15-25 bodů):

## Implementace (15-25 bodů):