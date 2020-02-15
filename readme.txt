This is an introductory tutorial shows how one can run a simple flask app with templates. 
It also deploys the app on GCP.

Do NOT forget to include:
- "venv" inside ".gitignore" to prevent pushing virtual environment to remote repo
- "requirements.txt"

After executing "python main3.py", you need to delete the contents of the table "book"; otherwise you receive an error.
> login to your postgresql DB
> delete from book;

Note you need to upgrade the dependencies in rquirements.txt
pip install -r requirements-to-freeze.txt --upgrade
pip freeze > requirements.txt




