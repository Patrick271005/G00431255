import pytest
def user_payload(equipment_id=2, student_id="STAB1234",description="Describe", priority=2,):
    return{"equipment_id":equipment_id, "student_id":student_id, "description":description, "priority":priority,}

def test_create_user_returns_201(client): 
    response=client.post("/api/requests",json=user_payload())
    assert response.status_code==201
    data=response.json()
    assert data["id"]==1
    assert data["description" == "Describe"]

def test_get_users(client):
    client.post("/api/requests", json=user_payload())
    response=client.get("/api/requests")
    assert response.status_code==200
    assert len(response.json()) ==1
    assert response.json()[0]["student_id"] ==["STAB1234"]

@pytest.mark.parametrize ("bad_sid",["stab1234","StAb123","STAB12345"],)
def test_invalid_student_id(client,bad_sid):
    response=client.post("/api/requests",json=user_payload(student_id=bad_sid))
    assert response.status_code ==422


    
