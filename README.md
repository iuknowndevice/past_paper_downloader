# 📄 PMT Past Paper Downloader

A Python script that bulk downloads past papers from [Physics & Maths Tutor](https://www.physicsandmathstutor.com/). Instead of clicking every paper one by one, this script scrapes the page and downloads everything automatically into organised folders.

By default it downloads Edexcel A-level Maths and Physics papers, but you can grab **any subject or spec** just by changing the URLs.

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

Papers will be saved into an `Edexcel_Papers/` folder, organised by subject.

---

## ⚙️ Customising for any subject

Open `download_papers.py` and edit the `PAGES` list at the top:

```python
PAGES = [
    ("Maths_AS",   "https://www.physicsandmathstutor.com/maths-revision/a-level-edexcel/papers-as/"),
    ("Maths_A2",   "https://www.physicsandmathstutor.com/maths-revision/a-level-edexcel/papers/"),
    ("Physics_AS", "https://www.physicsandmathstutor.com/physics-revision/a-level-edexcel/papers-as/"),
    ("Physics_A2", "https://www.physicsandmathstutor.com/physics-revision/a-level-edexcel/papers/"),
]
```

Replace any of the URLs with a PMT past papers page for your subject. The label (e.g. `"Maths_AS"`) becomes the folder name — name it whatever you like.

For example, to download AQA A-level Biology:
```python
PAGES = [
    ("Biology_AQA", "https://www.physicsandmathstutor.com/past-papers/a-level-biology/"),
]
```

---

## 📁 Output structure

```
Edexcel_Papers/
├── Maths_AS/
│   ├── June 2023 QP.pdf
│   ├── June 2023 MS.pdf
│   └── ...
├── Maths_A2/
├── Physics_AS/
└── Physics_A2/
```

---

## 📝 Notes

- The script skips files that have already been downloaded, so it's safe to re-run
- Only downloads PDFs hosted on PMT (ignores external links to other sites)
- Adds a small delay between downloads to avoid hammering the server

---

## 🛠️ Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
