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

- Řešení klasifikační úlohy pro vámi vybraný dataset.
- Každý projekt musí obsahovat popis datové sady a krátký přehled atributů, se kterými budete pracovat.
- Postupně popište kroky vaší klasifikační úlohy:
    1. Popiště způsob (případně způsoby) předzpracování dat.
    2. Popiště a zdůvodněte jak budete hodnotit vaše klasifikátory.
    3. Vyzkoušejte alespoň 4 klasifikační metody (povinně použijte **DecisionTree** a **RandomForest**, výběr dalších 2
       metod je na vás). U každého z klasifikátorů se zaměřte na jeho parametry, proveďte experimenty s různým
       nastavením parametrů a popište jaký vliv měly parametry na vámi sledovanou úspešnost klasifikátoru (textově, v
       tabulce, v grafu).
- Čemu se věnovat (bude záležet na povaze vašeho datasetu): krosvalidace, výběr optimálních parametrů modelu, výběr
  atributů, řešení nevyváženosti tříd, atd.
- Jeden projekt věnující se klasifikaci dat jste už zpracovávali, očekávám, že zkusíte posunout úroveň projektu.
  Jako podpůrný materiál pro zadání si můžete prohlénout “checklist“.
- Povinou částí je **závěrečné shrnutí**, kde porovnáte dosažené výsledky.
- Formou vypracování je Jupyter Notebook s kódy a interpretací vizualizací nebo PDF report + zdrojové kódy.
  Odhadovaná náročnost pro projekt je 3-6 hodin. Tento odhad můžete použít jako vodítko pro velikost analýzy.
  Každopádně čas se bude lišit podle vašich dovedností.
  Termín odevzdání projektu je **12. 1. 2025**, projekt odevzdáte nahráním na Dropbox. V rámci zkouškového období budou
  vypsány termíny pro ústní obhajobu tohoto projektu.

Výběr dat:

- Pro nalezení datasetu můžete
  použít [Kaggle](https://www.kaggle.com/), [UCI repository](https://archive.ics.uci.edu/ml/datasets.php) a další zdroje
  na internetu.
- Doporučená velikost datové sady je 1000+ záznamů a 10+ atributů.
- Z výběru jsou vyloučeny data ze cvičení a přednášky (Titanic, Country Data, Red wine quality) a také datasety ze ZSU (
  Credit Card Customers, Adult, Heart Failure Prediction Dataset, KDD Cup 99, UNSW_NB15, Bank Marketing Data Set).

Deadline klasifikace 12. 1. 2025

## Implementace (15-25 bodů):

- Účelem toho projektu je vytvořit vlastní implementaci vybraného algoritmu např. z přednášky a prokázat tak znalost
  dané metody.
- Vybranou metodu mi nahlaste e-mailem.
- Použijte programovací jazyk dle vašeho výběru.
- Součástí implementace bude i ukázka použití vaší implementace. Tzn. například při implementaci neuronových sítí
  vytvoříte skript, kde nad ukázkovými daty (např. Iris nebo Titanic) budete využívat váš algoritmus.
- Pokud to bude možné, tak se srovnejte s implementací z dostupné knihovny. Porovnejte dosažené skóre, čas výpočtu,
  apod. Není důležité mít efektivnější implementaci, než tu z knihovny, ale musíte si uvědomit, která část vaší
  implementace není efektivní a tušit, jak by se případně dala zrychlit.
- Termín odevzdání projektu je 12. 1. 2025, projekt odevzdáte nahráním na Dropbox. V rámci zkouškového období budou
  vypsány termíny pro ústní obhajobu tohoto projektu.

### Návrhy algoritmů k implementaci:

- Random Forest
- Neural Network
- AdaBoost
- Naive Bayes
- DBSCAN
- CLARANS
- OPTICS
- BIRCH
- a další …
