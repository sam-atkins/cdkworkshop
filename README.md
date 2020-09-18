# AWS CDK Workshop

- [AWS CDK Workshop](#aws-cdk-workshop)
  - [Setup](#setup)
  - [Development](#development)
  - [Welcome to your CDK Python project!](#welcome-to-your-cdk-python-project)
  - [Useful commands](#useful-commands)

Learning some CDK by following this [workshop](https://cdkworkshop.com/)

## Setup

Follow the workshop instructions to get the following setup:

- AWS CLI
- AWS Account and User (make a note of the profile name)
- Node.js

Create a Python 3 virtualenv and install the requirements

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Add an `.env` at project root level with the following variable and add the AWS region e.g.

```
CDK_DEFAULT_REGION=eu-west-2
```

## Development

```bash
# activate the venv
source venv/bin/activate

# use the correct version of NPM
nvm use

# any cdk commands need to include the profile option along with the profile name
# if you have more than one AWS profile and don't want to use the default
cdk bootstrap --profile {profileName}
```

##  Welcome to your CDK Python project!

(The docs below are created as part of the `cdk init sample-app --language python` command)

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (`cdkworkshop_stack`)
which contains an Amazon SQS queue that is subscribed to an Amazon SNS topic.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .env directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
