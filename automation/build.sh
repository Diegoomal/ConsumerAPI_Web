conda deactivate

conda env create -n web-ebeer-env -f ./env.yml

conda activate web-ebeer-env

pytest -s

streamlit run src/app.py