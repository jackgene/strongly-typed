import os

from behave.model import Examples, Feature, Row, ScenarioOutline, Table
from behave.runner import Context


def before_all(_: Context):
    os.chdir("features/work_dir")


def before_feature(_: Context, feature: Feature):
    commands: list[str] = [
        "mypy --disallow-any-generics --disallow-untyped-defs --disallow-untyped-calls .",
        "pyre --strict",
        "pyright",
    ]
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
