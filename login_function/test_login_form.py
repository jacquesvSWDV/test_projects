import pytest
from login_form import LoginForm


#a fresh form for each test
@pytest.fixture
def form(self):
    return LoginForm()

#setup the paramatrize test data for the email validation
@pytest.mark.parametrize("email", [
    "user@example.com",
    "balls@example.com",
    "NotAi@ai.com",
    "joebiden@thewhitehouse.com",
    "boejiden@theblackhouse.com",
    "yarrmematey@piratebay.com",
    "santaclaus@thenorthpole.org",
    "petergriffin@spoonerstreet.org",
    "teacher@teacherland.edu",
    "test@testing.com",
    "thepythonman@python.com",
    "notch@minecraft.net",
    "bartsimpson@bartsimpson.bart",
    "themoneyman@dollarbill.com",
    "gangster@crimedoer.com",
    "imhungry@food.com",
    "dev_team@startup.tech"
])
def test_valid_email(self, form, email):
    assert LoginForm.validate_email(form, email) == True

def test_invalid_email(self, form, email):
    assert LoginForm.validate_email(form, email) == False