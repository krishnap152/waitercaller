MOCK_USERS = [{'email': 'test@example.com',
               'salt': "pKV6n5wOwz+6gF2AfBFjK0SSqL4=",
               'hashed': 'b20fedbd6cba89523c1dbbc91d248284073d913b39480a07115df7394b0656271e3631044435cd9e3e36012cb965dfa561e15c0ca1b5f1d544eeb0cda855d63f'
                }]

class MockDBHelper:
    def get_user(self,email):
        user = [x for x in MOCK_USERS if x.get("email") == email]
        if user:
            return user[0]
        return None
    
    def add_user(self, email, salt, hashed):
        print("email",email)
        print("salt: ",salt)
        print("hashed: ",hashed)
        MOCK_USERS.append({"email":email,"salt":salt,"hashed":hashed})
        print(MOCK_USERS)

    
