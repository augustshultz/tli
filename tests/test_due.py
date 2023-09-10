from datetime import date

from tli.models import Due

sample_due = {
    "recurring": False,
    "string": "today",
    "date": "2021-03-29"
}
sample_due_missing_recurring = {
    "string": "today",
    "date": "2021-03-29"
}


def test_create_due_from_dictionary_sets_recurring():
    due = Due(**sample_due)
    assert not due.recurring


def test_create_due_from_dictionary_defaults_recurring_when_elided():
    due = Due(**sample_due_missing_recurring)
    assert not due.recurring


def test_create_due_from_dictionary_sets_string():
    due = Due(**sample_due)
    assert due.string == 'today'


def test_create_due_from_dictionary_sets_date():
    due = Due(**sample_due)
    assert due.date == date(2021, 3, 29)


def test_due_string():
    due = Due(**sample_due)
    assert str(due) == 'today'
