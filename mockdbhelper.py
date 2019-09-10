import datetime
MOCK_USERS = [{'email': 'test@example.com',
               'salt': "pKV6n5wOwz+6gF2AfBFjK0SSqL4=",
               'hashed': 'b20fedbd6cba89523c1dbbc91d248284073d913b39480a07115df7394b0656271e3631044435cd9e3e36012cb965dfa561e15c0ca1b5f1d544eeb0cda855d63f'
                }]
MOCK_TABLES = [{"_id": "1","number": "1", "owner": "test@example.com", "url":"mockurl"}]

MOCK_REQUESTS = [{"_id":"1","table_number":"1","table_id":"1","time":datetime.datetime.now()}]

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

    def add_table(self,number,owner):
        MOCK_TABLES.append({"_id": str(number),"number": number,"owner": owner})
        return number
    
    def update_table(self,_id,url):
        for table in MOCK_TABLES:
            if table.get("_id") == _id:
                table["url"] = url
                break
    
    def get_tables(self,owner_id):
        return MOCK_TABLES
    
    def delete_table(self,table_id):
        for i, table in enumerate(MOCK_TABLES):
            if table.get("_id") == table_id:
                del MOCK_TABLES[i]
            break

    def get_requests(self,owner_id,):
        return MOCK_REQUESTS

    def delete_request(self,request_id):
        for i, request in enumerate(MOCK_REQUESTS):
            if request.get("_id") == request_id:
                del MOCK_REQUESTS[i]
                break

    


    
