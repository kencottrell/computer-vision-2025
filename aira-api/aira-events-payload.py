true = True  # expected payload for AiraFace below
false = False # expected spelling for AiraFace below 

aira_create_event_payload = {
  "action_type": "http",
  "name": "Kens_Test_Event",
  "enable": true,
  "group_list": [
    "All Person"
  ],
  "divice_groups":[
    "cdc97c86-5f06-4504-914e-87172af202c5"
  ],
  "temperature_trigger_rule": 0,
  "remarks": "This is a test from Kens VSCode python program",
  "specify_time": {
    "list": [
      {
        "start_time": 1704556800000,
        "end_time": 1705075200000
      }
    ]
  },
  "weekly_schedule": {
    "list": [
      {
        "day_of_week": 2,
        "hours_list": [8, 9]
      }
    ]
  },
  "https": true, "method": "GET", "user": "username", "pass": "password",  "host": "192.168.2.3", "port": 80, "data_type": "JSON",  "language": "en",
  "url": "/?aaa=##VerifiedTimeStamp##&bbb=##IsStranger##&", "custom_data": "", "note" : ""
 }

testPayload = {
    "uuid": "48508ca0-e2fb-4b07-8164-069287961b81",
    "name": "Test1",
    "action_type": "http",
    "enable": True,
    "group_list": [
      "All Visitor"
    ],
    "divice_groups": [
      "0"
    ],
    "temperature_trigger_rule": 0,
    "remarks": "240925",
    "specify_time": {
      "list": []
    },
    "weekly_schedule": {
      "list": []
    },
    "https": False,
    "method": "POST",
    "user": "Admin",
    "pass": "123456",
    "host": "127.0.0.1",
    "port": 80,
    "data_type": "JSON",
    "url": "/",
    "custom_data": "\"param1\":\"##VerifiedTimeStamp##\",\n\"param2\":\"##SourceDevice##\",",
    "note": "",
    "created_time": 1727285730497,
    "updated_time": 1727285730497
}

test_allPersonPayload = {

    "uuid": "5c6c0665-98a8-4207-8b93-09eab18dd56c",
    "name": "testAllPerson",
    "action_type": "http",
    "enable": True,
    "group_list": [
      "All Person"
    ],
    "divice_groups": [
      "0"
    ],
    "temperature_trigger_rule": 0,
    "remarks": "All Persons ",
    "specify_time": {
      "list": []
    },
    "weekly_schedule": {
      "list": []
    },
    "https": False,
    "method": "POST",
    "user": "Admin",
    "pass": "123456",
    "host": "127.0.0.1",
    "port": 80,
    "data_type": "JSON",
    "url": "/allPerson?\"ts\":\"##VerifiedTimeStamp##\",\n\"videoSrc\":\"##SourceDevice##\",\n\"stranerBool\":\"##IsStranger##\",\n\"personID\":\"##PersonId##\",",
    "custom_data": "\"ts\":\"##VerifiedTimeStamp##\",\n\"videoSrc\":\"##SourceDevice##\",\n\"stranerBool\":\"##IsStranger##\",\n\"personID\":\"##PersonId##\",",
    "note": "",
    "created_time": 1727292927371,
    "updated_time": 1727292927371
  }

test_allVisitorGroupPayload = {
    "uuid": "47de8b66-c4c7-4609-9e2f-e86059f66b7c",
    "name": "AllVisitorGrp",
    "action_type": "http",
    "enable": True,
    "group_list": [
      "All Visitor"
    ],
    "divice_groups": [
      "0"
    ],
    "temperature_trigger_rule": 0,
    "remarks": "All Visiotors",
    "specify_time": {
      "list": [
        {
          "start_time": 1727366400000,
          "end_time": 1730390400000
        }
      ]
    },
    "https": False,
    "method": "POST",
    "user": "Admin",
    "pass": "123456",
    "host": "127.0.0.1",
    "port": 80,
    "data_type": "JSON",
    "url": "/",
    "custom_data": "\"vts\":\"##VerifiedTimeStamp##\",\n\"vs\":\"##SourceDevice##\",\n\"strangerBool\":\"##IsStranger##\",\n\"group\":\"##Group##\",\n\"remarks\":\"##Remarks##\",",
    "note": "",
    "created_time": 1727293215716,
    "updated_time": 1727293215716
  }