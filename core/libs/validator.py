# HANDLE
# Data Type Validation: Ensure that the data is of the expected type (e.g., integer, string, boolean).
# Required Fields: Verify that all necessary fields are present and not empty.
# Enumerations: Ensure that the value of a field is one of a set of predefined values.
# Sanitization: Clean input data to prevent injection attacks (e.g., SQL injection, cross-site scripting).

# IGNORE
# Value Range: Check that numeric values fall within an acceptable range.
# String Length: Ensure that string data does not exceed a certain length or meet minimum length requirements.
# Format Validation: Validate that strings match a specific format, such as email addresses, phone numbers, or dates (regular expressions can be helpful here).
# Uniqueness: Check that certain fields (like usernames or emails) are unique and not already used in your database.
# Cross-Field Validation: Sometimes you need to validate data across multiple fields (e.g., ensuring start_date is before end_date).
# Custom Business Rules: Any other business-specific validation that your application requires.

class Validator:
    def isstring(self, obj):
        return type(obj) is str and obj.strip()
    
    # All method: add, get
    def all(self, data : dict, keys : set[str]):
        if not data or not keys.issubset(data):
            return False
        
        isvalid = {
            "htype": lambda value: self.isstring(value),
            "hash": lambda value: self.isstring(value),
            "phrase": lambda value: self.isstring(value)
        }

        for key in keys:
            if not isvalid[key]:
                return False
            
        return True