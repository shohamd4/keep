import pytest
from unittest.mock import patch
from keep.api.routes import alerts
from tests.conftest import PusherMock

@pytest.fixture
def pusher_mock():
    return PusherMock()

@patch('keep.api.routes.alerts.get_pusher_client')
def test_alert_dismiss_triggers_alert_update(mock_get_pusher_client, pusher_mock):
    # Arrange
    mock_get_pusher_client.return_value = pusher_mock
    tenant_id = 'test-tenant'
    alert_id = 'test-alert-id'
    email = 'user@example.com'
    class AuthEntity:
        def __init__(self):
            self.tenant_id = tenant_id
            self.email = email
    auth_entity = AuthEntity()
    # Patch the DB dismiss function to do nothing
    with patch('keep.api.routes.alerts.dismiss_error_alerts_db') as mock_db:
        mock_db.return_value = None
        # Act
        response = alerts.dismiss_error_alerts(
            request=type('obj', (object,), {'alert_id': alert_id})(),
            authenticated_entity=auth_entity
        )
    # Assert
    assert response["success"] is True
    assert any(
        event[1] == "alert_update" and event[2]["id"] == alert_id
        for event in pusher_mock.triggers
    ), "alert_update event was not triggered on dismiss" 