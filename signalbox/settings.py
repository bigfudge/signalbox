try:
    from statistics import median_low, mean, stdev
except ImportError:
    from simplestats import median_low, mean, stdev


SCORESHEET_FUNCTION_NAMES = "sum mean min max stdev median".split(" ")

SCORESHEET_FUNCTION_LOOKUP = {
    'min': lambda x: round(min(x), 0),
    'max': lambda x: round(max(x), 0),
    'sum': sum,
    'mean': mean,
    'stdev': stdev,
    'median': lambda x: round(median_low(x), 0),
}

DATE_INPUT_FORMATS = ('%d/%m/%Y', )

DATETIME_INPUT_FORMATS = ('%d/%m/%Y %H:%M', )


# SIGNALBOX
USER_PROFILE_FIELDS = [
    # this is the list of possible fields in the user profile
    # list in the order in which they should appear in the form
    # note, you can't simply add fields here - they must also be
    # defined on the UserProfile model.
    'landline',
    'mobile',
    'site',
    'address_1',
    'address_2',
    'address_3',
    'county',
    'postcode',
]

# See also DEFAULT_USER_PROFILE_FIELDS in configurable_settings.py


OB_DATA_TYPES = [
    ('external_id', "External reference number, e.g. a Twilio SID"),
    ('attempt', "Attempt"),
    ('reminder', "Reminder"),
    ('success', "Success"),
    ('failure', "Failure"),
    ('created', "Created"),
    ('timeshift', "Timeshift"),
]


REPLY_DATA_TYPES = [
    ('incorrect_response', "incorrect_response"),
    ('question_error', "an error occured answering question with variablename"),
]


OB_DATA_TYPES_DICT = dict(OB_DATA_TYPES)

STATUS_CHOICES_DICT = {
    0: "pending",
    -2: "email sent, response pending",
    -3: "due, awaiting completion",
    -1: "in progress",
    -4: "redirected to external service",
    1: "complete",
    -99: "failed",
    -999: "missing",
}

STATUS_CHOICES = sorted(zip(list(STATUS_CHOICES_DICT.keys()), list(STATUS_CHOICES_DICT.values())), reverse=True)


SMS_STATUSCODES = {
    'd': ('delivered', True),
    'f': ('failed', False),
    'e': ('error', False),
    'j': ('', False),
    'u': ('', False)
}

TITLE_CHOICES = [(i, i) for i in ['', 'Mr', 'Mrs', 'Ms', 'Miss', 'Dr', 'Prof', 'Rev']]

QUESTION_TEXT_HELP_TEXT = """
The text displayed for this question.
<a href="#" onClick="$('.questiontexthelp').show();$(this).hide();return false;">
Syntax help</a>
<div class="questiontexthelp hide">
As part of instruction questions it's now possible to
include variables representing summary scores (ScoreSheets) attached to
the Asker, or previous question responses.

This is done by including Django template syntax in the `text` attribute
of the question.

Summary scores can be accessed as: `{{scores.<scoresheetname>.score}}`
and computation messages as `{{scores.<scoresheetname>.message}}`.

Previous answers can be displayed using `{{answers.<variable_name>}}`.

Standard Django template logic can also be used with these variables,
for example `{% if scores.<scoresheetname>.score %}Show something else
{% endif %}`.
</div>"""



#  TODO XXX FIXME see
# http://django-reversion.readthedocs.org/en/latest/api.html

from django.conf import settings
if settings.USE_VERSIONING:
    from reversion import revisions
    create_revision = lambda x: None #revisions.create_revision
else:
    create_revision = lambda x: None

