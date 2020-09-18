#!/usr/bin/env python3
import os

from aws_cdk import core

from cdkworkshop.cdkworkshop_stack import CdkworkshopStack

REGION = os.getenv("CDK_DEFAULT_REGION", "eu-west-2")

app = core.App()
CdkworkshopStack(app, "cdkworkshop", env={"region": REGION})

app.synth()
