from src.app import handle_request


def test_handle_request_returns_greeting_for_known_path():
      status, body = handle_request("/greet?name=Rahul")
      assert status == 200
      assert body == "Hello, Rahul!"


def test_handle_request_uses_default_name_when_missing():
      status, body = handle_request("/greet")
      assert status == 200
      assert body == "Hello, World!"


def test_handle_request_returns_404_for_unknown_path():
      status, body = handle_request("/unknown")
      assert status == 404