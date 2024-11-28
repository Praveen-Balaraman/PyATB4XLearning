import allure
import pytest
import requests
@allure.title("API")

def test_create_booking_postivie():
    #URL
    #BASE PATH
    #FULL URL = URL+ BASEPATH
    #HEADER
    #BODY OR PAYLOAD
    #AUTHORIZATION NO
    base_url="https://restful-booker.herokuapp.com"
    base_path="/booking"
    URL=base_url+base_path
    headers= {"Content-Type": "application/json"}
    payload={
      "firstname" : "Jim",
      "lastname" : "Brown",
      "totalprice" : 111,
      "depositpaid" : True,
      "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
             },
             "additionalneeds": "Breakfast"
             }
    response =requests.post(url=URL,verify= False,headers=headers, json=payload)
    assert response.status_code == 200
    print(response.json())
    response_data=response.json()

    booking_id=response_data["bookingid"]
    print(booking_id)
    assert booking_id is not None
    assert type(booking_id) == int
    assert booking_id>0

    first_name=response_data["booking"]["firstname"]
    assert first_name== "Jim"

def test_create_booking_negative():
    #URL
    #BASE PATH
    #FULL URL = URL+ BASEPATH
    #HEADER
    #BODY OR PAYLOAD
    #AUTHORIZATION NO
    base_url="https://restful-booker.herokuapp.com"
    base_path="/booking"
    URL=base_url+base_path
    headers= {"Content-Type": "application/json"}
    payload={}
    response =requests.post(url=URL,verify= False,headers=headers, json=payload)
    print(response.status_code)
    assert response.status_code == 500
    print(response.json())
    response_data=response.json()


