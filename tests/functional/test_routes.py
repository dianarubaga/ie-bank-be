from iebank_api import app
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Italy'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'John Doe'
    assert data['currency'] == '€'
    assert data['country'] == 'Italy'


def test_update_account_and_verify_content(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<id>' endpoint is used to update an account (PUT)
    THEN check that the response is valid and contains the updated account details
    """
    # Step 1: Create an account to update
    create_response = testing_client.post('/accounts', json={
        'name': 'Lucy Van Pelt',
        'currency': '$',
        'country': 'USA'
    })
    assert create_response.status_code == 200  # Ensure the account creation was successful
    
    # Extract the account ID from the response (assuming the response contains the account's ID)
    account_id = create_response.get_json().get('id')
    
    # Step 2: Update the account's name
    update_response = testing_client.put(f'/accounts/{account_id}', json={
        'name': 'Lucy Updated',
        'currency': '$',
        'country': 'USA'
    })
    assert update_response.status_code == 200  # Ensure the update was successful
    
    # Step 3: Verify the response contains the updated data
    updated_data = update_response.get_json()
    assert updated_data['name'] == 'Lucy Updated'
    assert updated_data['currency'] == '$'
    assert updated_data['country'] == 'USA'

def test_home_page(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid (200 OK)
    """
    response = testing_client.get('/')
    assert response.status_code == 200  # Check if the home page loads successfully