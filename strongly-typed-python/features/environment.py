import os

from behave.model import Examples, Feature, Row, Scenario, ScenarioOutline, Table
from behave.runner import Context
from behave.tag_expression import TagExpression


def before_all(_: Context):
    os.chdir("features/work_dir")


def before_feature(context: Context, feature: Feature):
    # TODO see if it's possible to get run tags without using protected members
    run_tags: TagExpression = context._runner.config.tags
    commands: list[str] = []
    if run_tags.check(["mypy"]):
        commands.append("mypy --disallow-any-generics --disallow-untyped-defs --disallow-untyped-calls .")
    if run_tags.check(["pyre"]):
        commands.append("pyre --strict")
    if run_tags.check(["pyright"]):
        commands.append("pyright")
    for untyped_scenario in feature.scenarios:
        outline: ScenarioOutline = untyped_scenario
        for untyped_examples in outline.examples:
            examples: Examples = untyped_examples
            table: Table = examples.table
            new_rows: list[Row] = []
            for old_row_untyped in table.rows:
                old_row: Row = old_row_untyped
                old_cells: list[str] = []
                for old_cell in old_row:
                    old_cells.append(old_cell)
                for command in commands:
                    new_row: Row = Row(
                        old_row.headings + ["Type Checker"],
                        old_cells + [command],
                        old_row.line,
                        old_row.comments
                    )
                    new_rows.append(new_row)
            examples.table = Table(
                headings=table.headings + ["Type Checker"],
                line=table.line,
                rows=new_rows
            )


def before_scenario(context: Context, scenario: Scenario):
    type_checker_tags = ["mypy", "pyre", "pyright"]
    # scenario.tags.remove(type_checker_tags)
    for tag in type_checker_tags:
        scenario.tags.remove(tag)
        if tag in scenario.steps[1].name:
            scenario.tags.append(tag)
