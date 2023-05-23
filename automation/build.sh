echo "1) Conda environment"

conda deactivate

conda env create -n web-ebeer-env -f ./env.yml

conda activate web-ebeer-env

echo "2) LINT verify with Flak8"

flake8 . --count --statistics

flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

echo "3) Generating documentation"

pdoc src/ebeer -o docs

echo "4) Unity test with pytest"

pytest -s

echo "5) Run project"

streamlit run src/app.py