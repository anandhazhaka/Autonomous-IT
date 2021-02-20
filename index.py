import boto3
import json
from flask import Flask, request, render_template
app = Flask(__name__,template_folder='templates')
@app.route('/', methods =["GET", "POST"])
def hello():
    if request.method == "POST":
        with open("D:/anandh/create.json") as f:
            data = json.load(f)
        data['Parameters']['KeyName']['Default'] = request.form.get("Keypair")
        data['Parameters']['DBUser']['Default'] = request.form.get("Dbuser")
        data['Parameters']['DBPassword']['Default'] = request.form.get("Dbpass")
        data['Parameters']['DBRootPassword']['Default'] = request.form.get("Dbroot")
        data['Parameters']['InstanceType']['Default'] = request.form.get("Itype")
        # print(data['Parameters']['KeyName']['Default'])
        client = boto3.client('cloudformation',
            region_name = 'ap-south-1',
            aws_access_key_id='AKIAX4ZLTVKXCSRV3X74',
            aws_secret_access_key='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')
        response = client.create_stack(
            StackName="anandh",
            TemplateBody=json.dumps(data),
            DisableRollback=False,
        )
    return render_template("index.html")
if __name__ == '__main__':
    app.run()



