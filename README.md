# powercon

Steps for running in local (requires python3. I used python 3.9.7)
1. Clone the repository
2. Open terminal inside the root directory of the local repository folder
3. Create a virtualenv and activate it.
4. Run `pip install -r requirements.txt` to install all the requirements
5. Run `uvicorn main:app --reload` to start the server.


# Training the model. 
1. Modify `train.py` if any changes are to be made to the model
1. Run `python train.py` to train the model. it creates two files `finalized_model.sav` and `type_encoder.pkl`


Steps to deploy in heroku
1. Either fork this repository or create your own Github repository
2. Make sure that all the required files are commited to github repo
3. Create an account in Heroku and create an app
4. in the deploy section, select github and search for your repo
5. select the branch to be deploy and click deploy branch.
6. Heroku installs all the dependies and deploys the build
7. Heroku starts the server according to the instructions in `Procfile`


# Testing the endpoint
1. Using postman or insomnia send a post request to `base_url/api/predict`
2. If running in local `base_url = localhost:8000`.
3. If running from heroku,`base_url = https://your_app_name.herokuapp.com`
4. The body of the post request should be of json format. The following is the sample body
`{
	"typ" : "Metal",
	"sales": 12345,
	"employees" : 123454,
	"plant_area" : 12345566,
	"prod_level" : 216484321,
	"prod_hours" : 24763432
}`
