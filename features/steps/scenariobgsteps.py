from behave import *

@given(u'I launch browser')
def step_impl(context):
    assert True,"Tet Passed" #duplicates; in the same step definition file or the other step definition file

@when(u'I open application')
def step_impl(context):
    assert True,"Tet Passed"


@then(u'Enter valid username and password')
def step_impl(context):
    assert True,"Tet Passed"


@then(u'Click on login')
def step_impl(context):
    assert True,"Tet Passed"


@then(u'User must login to the My Account page')
def step_impl(context):
    assert True,"Tet Passed"


@when(u'navigate to search page')
def step_impl(context):
    assert True,"Tet Passed"


@then(u'search page should display')
def step_impl(context):
    assert True,"Tet Passed"


@when(u'navigate to advanced search page')
def step_impl(context):
    assert True,"Tet Passed"


@then(u'advanced search page should display')
def step_impl(context):
    assert True,"Tet Passed"
