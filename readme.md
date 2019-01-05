# laravel-ai
<img src="data/laravel-terminator.png" height=256>

Scrape subsets of github repositories for use in a Artificial Intelligence models.

## Installation
First, make sure you have anaconda installed. Then
```
git clone git@github.com:ajthinking/laravel-ai.git
cd laravel-ai
conda env create
conda activate laravel-ai
source activate
python src/examples/migration-analysis/01_scrape.py
```

## Todo
- [ ] Deploy more scrapers
- [ ] Transform 'data/raw' into 'data/processed/transformer-x'
- [ ] Find online storage for harvested dumps (33K files -> 83,8 MB )

## License
MIT