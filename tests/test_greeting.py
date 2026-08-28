from src.greeting import greeting

def test_greeting_includes_name():
	assert greeting("Rahul") == "Hello, Rahul!"
