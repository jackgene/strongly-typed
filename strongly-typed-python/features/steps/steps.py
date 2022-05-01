import os
import os.path
import shutil
import subprocess

from behave import *
from behave.runner import Context


@given("the Python source `{python_source}`")
def step_impl(context: Context, python_source: str):
    if os.path.isfile("source.py"):
        os.remove("source.py")
    shutil.copyfile(f"../../src/{python_source}", "source.py")


@when("running `{type_check_command}`")
def step_impl(context: Context, type_check_command: str):
    context.process = subprocess.run(type_check_command, shell=True, capture_output=True)


@then("type-checking should {result}")
def step_impl(context: Context, result: str):
    proc: subprocess.CompletedProcess = context.process
    if result == "pass":
        stdout: str = proc.stdout.decode('utf-8')
        assert proc.returncode == 0, f"Expected to pass, but failed with: {stdout}"
    else:
        assert proc.returncode != 0, "Expected to fail, but passed\n"
