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
    create_response = testing_client.post('/accounts', json={
        'name': 'Lucy Van Pelt',
        'currency': '$',
        'country': 'USA'
    })
    assert create_response.status_code == 200  
    
    account_id = create_response.get_json().get('id')
    
    update_response = testing_client.put(f'/accounts/{account_id}', json={
        'name': 'Lucy Updated',
        'currency': '$',
        'country': 'USA'
    })
    assert update_response.status_code == 200 
    
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

def test_hello_world(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, World!'

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the account is created
    """
    response = testing_client.post('/accounts', json={
        'name': 'John Doe', 
        'currency': '$', 
        'country': 'USA'
    })
    assert response.status_code == 200
    account_data = response.get_json()
    assert account_data['name'] == 'John Doe'
    assert account_data['currency'] == '$'
    assert account_data['country'] == 'USA'

def test_get_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<id>' page is requested (GET)
    THEN check the response is valid and returns the correct account
    """
    # First create an account to retrieve
    response = testing_client.post('/accounts', json={
        'name': 'Jane Doe', 
        'currency': '€', 
        'country': 'France'
    })
    account_data = response.get_json()
    account_id = account_data['id']

    # Retrieve the account
    response = testing_client.get(f'/accounts/{account_id}')
    assert response.status_code == 200
    retrieved_account = response.get_json()
    assert retrieved_account['name'] == 'Jane Doe'
    assert retrieved_account['country'] == 'France'

def test_update_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<id>' page is updated (PUT)
    THEN check the account is updated correctly
    """
    # First create an account to update
    response = testing_client.post('/accounts', json={
        'name': 'John Doe', 
        'currency': '$', 
        'country': 'USA'
    })
    account_data = response.get_json()
    account_id = account_data['id']

    # Update the account
    update_response = testing_client.put(f'/accounts/{account_id}', json={
        'name': 'John Smith', 
        'country': 'Canada'
    })
    assert update_response.status_code == 200

    # Verify the update
    updated_account = update_response.get_json()
    assert updated_account['name'] == 'John Smith'
    assert updated_account['country'] == 'Canada'

def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<id>' page is deleted (DELETE)
    THEN check the account is deleted and cannot be retrieved
    """
    # First create an account to delete
    response = testing_client.post('/accounts', json={
        'name': 'Mark Johnson',
        'currency': '$',
        'country': 'UK'
    })
    assert response.status_code == 200  # Ensure account creation is successful
    account_data = response.get_json()
    account_id = account_data['id']
    
    # Delete the account
    delete_response = testing_client.delete(f'/accounts/{account_id}')
    assert delete_response.status_code == 200  # Ensure account deletion is successful
    
    # Verify that the account was deleted by checking it no longer exists
    get_response = testing_client.get(f'/accounts/{account_id}')
    assert get_response.status_code == 404  # Expect 404 Not Found after deletion
