from src.greeting import greeting

def test_greeting_includes_name():
	assert greeting("Rahul") == "Hello, Rahul!"


def test_greeting_uses_default_for_empty_name():
      assert greeting("") == "Hello, World!"
