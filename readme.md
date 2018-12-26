# laravel-ai
<img src="data/laravel-terminator.png" height=256>

This repository supplies tools to analyze the Laravel community's implementation practices for Artificial Inteligence research. That includes:

* Github scrape module
* Pytorch Dataset
* Pytorch Dataloader
* Example analysis

## Installation
* install anaconda
* install pygithub
* install pytorch
* copy Env.Example.py to Env.py and set your GITHUB_ACCESS_TOKEN
* run main.py

## Todo
- [x] Make a Env class
- [x] Make a Print class
- [x] Make 'main' into 'analysis-x'
- [x] Move everything to a src folder
- [x] Rename 'scraped' to 'data/raw'
- [x] Code example Transformer-X
- [ ] Deploy more scrapers
- [ ] Transform 'data/raw' into 'data/processed/transformer-x'
- [ ] Find online storage for harvested dumps (33K files -> 83,8 MB )

## License
MIT and optionally [pay what you want](https://andersjurisoo.com/laravel-ai/pay-what-you-want) (Allows me to keep hosting the dataset on AWS).