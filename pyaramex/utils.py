from pydantic import ValidationError


def validate_payload(func):
    def wrapper(self, payload):
        try:
            payload = func(self, payload)
        except ValidationError as e:
            return e.errors()
        
        return payload
    
    return wrapper
