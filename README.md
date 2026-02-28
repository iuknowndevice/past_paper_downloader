# 📄 PMT Past Paper Downloader

A Python script that bulk downloads past papers from [Physics & Maths Tutor](https://www.physicsandmathstutor.com/). Instead of clicking every paper one by one, this script scrapes the page and downloads everything automatically into organised folders.

By default it downloads Edexcel A-level Maths papers, but you can grab **any subject or spec** just by changing the URLs.

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install requests beautifulsoup4
```

### 2. Run the script
```bash
python download_papers.py
```

Papers will be saved into a `Past_Papers/` folder, organised by subject.

---

## ⚙️ Customising for any subject

Open `download_papers.py` and edit the `PAGES` list at the top:

```python
PAGES = [
    ("Edexcel_Maths_AS", "https://www.physicsandmathstutor.com/maths-revision/a-level-edexcel/papers-as/"),
    ("Edexcel_Maths_A2", "https://www.physicsandmathstutor.com/maths-revision/a-level-edexcel/papers/"),
]
```

Each entry is a `("folder_name", "url")` pair. The folder name is what the downloaded papers will be saved under — name it whatever you like. Just navigate to your subject's past papers page on PMT and paste the URL in.

For example, to download Edexcel A-level Physics:
```python
PAGES = [
    ("Edexcel_Physics_AS_Paper1", "https://www.physicsandmathstutor.com/past-papers/a-level-physics/edexcel-paper-1-as/"),
    ("Edexcel_Physics_AS_Paper2", "https://www.physicsandmathstutor.com/past-papers/a-level-physics/edexcel-paper-2-as/"),
    ("Edexcel_Physics_A2_Paper1", "https://www.physicsandmathstutor.com/past-papers/a-level-physics/edexcel-paper-1/"),
    ("Edexcel_Physics_A2_Paper2", "https://www.physicsandmathstutor.com/past-papers/a-level-physics/edexcel-paper-2/"),
    ("Edexcel_Physics_A2_Paper3", "https://www.physicsandmathstutor.com/past-papers/a-level-physics/edexcel-paper-3/"),
]
```

> **Note:** Some subjects on PMT split papers across multiple pages (e.g. Physics has a separate page per paper). Just add each page as its own entry.

---

## 📁 Output structure

```
Past_Papers/
├── Edexcel_Maths_AS/
│   ├── June 2023 QP.pdf
│   ├── June 2023 MS.pdf
│   └── ...
└── Edexcel_Maths_A2/
    └── ...
```

---

## 📝 Notes

- Already-downloaded files are skipped, so it's safe to re-run
- Only downloads PDFs hosted on PMT (ignores external links to other sites)
- Adds a small delay between downloads to be respectful to the server

---

## 🛠️ Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
