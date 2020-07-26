"""Using the `Template` class for templating."""

from string import Template

import pytest


def test_template_substitute() -> None:
    """Substitute placeholders in a template."""
    template = Template("${village}folk send $$10 to $cause")
    replacements = {"village": "Nottingham", "cause": "the ditch fund"}
    sentence = template.substitute(replacements)
    assert sentence == "Nottinghamfolk send $10 to the ditch fund"


def test_template_exception() -> None:
    """Conditions that raise exceptions."""
    template = Template("${village}folk send $$10 to $cause")
    pytest.raises(KeyError, template.substitute, village="Nottingham")

    template = Template("${village}folk send $10 to $cause")
    replacements = {"village": "Nottingham", "cause": "the ditch fund"}
    pytest.raises(ValueError, template.substitute, replacements)


def test_template_safe_substitute() -> None:
    """Substitute placeholders in a template, 'safely'."""
    template = Template("${village}folk send $10 to $cause")
    sentence = template.safe_substitute(village="Nottingham")
    assert sentence == "Nottinghamfolk send $10 to $cause"


def test_template_customise() -> None:
    """Customise template syntax."""

    class PercentTemplate(Template):
        """Customised template that uses `%` as placeholder delimiter."""

        delimiter = "%"

    template = PercentTemplate("%{village}folk send $10 to %{cause} 50%% of the time")
    sentence = template.substitute(village="Nottingham", cause="the ditch fund")
    assert sentence == "Nottinghamfolk send $10 to the ditch fund 50% of the time"
