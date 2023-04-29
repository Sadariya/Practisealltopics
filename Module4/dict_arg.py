'''def getdata(data):
    print("ID:",data['stid'])
    print("Name:",data['stnm'])
    print("Subject:",data['stsub'])


dict1 = {'stid':101,'stnm':'Mitesh','stsub':'Python'}

getdata(dict1) #dict argument
'''
list1 =[
    {
        "id": 1,
        "created": "2023-03-27T11:17:24Z",
        "event_name": "Society Party",
        "event_time": "2023-03-29",
        "event_information": "This is Event update Block",
        "comments": "This is Event comment"
    },
    {
        "id": 2,
        "created": "2023-03-27T11:17:24Z",
        "event_name": "Society Party",
        "event_time": "2023-03-29",
        "event_information": "event_information",
        "comments": "This is Event comment"
    },
    {
        "id": 3,
        "created": "2023-03-27T11:17:24Z",
        "event_name": "Diwali celebrations",
        "event_time": "2023-03-22",
        "event_information": "This is Diwali Festival",
        "comments": "This is more information about celebrations"
    },
    {
        "id": 4,
        "created": "2023-04-04T05:23:41.605315Z",
        "event_name": "Testing",
        "event_time": "2023-03-04",
        "event_information": "Testing from iOS",
        "comments": "TOPS Tech event"
    },
    {
        "id": 5,
        "created": "2023-04-05T02:53:02.890012Z",
        "event_name": "Party Time",
        "event_time": "2023-04-05",
        "event_information": "This is Party Event",
        "comments": "This is for fresher Party"
    },
    {
        "id": 6,
        "created": "2023-04-05T02:53:02.890012Z",
        "event_name": "Party Time",
        "event_time": "2023-04-05",
        "event_information": "This is Party Event",
        "comments": "This is for fresher Party"
    },
    {
        "id": 7,
        "created": "2023-04-05T03:21:11.379028Z",
        "event_name": "HTTP POST",
        "event_time": "2023-04-05",
        "event_information": "This is POST Method testing",
        "comments": "Good Evening!"
    },
    {
        "id": 8,
        "created": "2023-04-05T03:21:11.379028Z",
        "event_name": "Testing….",
        "event_time": "2023-09-05",
        "event_information": "Testing…",
        "comments": "Testing…."
    },
    {
        "id": 9,
        "created": "2023-04-05T03:21:11.379028Z",
        "event_name": "Sanket’ Birthday Party",
        "event_time": "2023-12-05",
        "event_information": "Alpha One Ahmedabad",
        "comments": "Only for students"
    },
    {
        "id": 10,
        "created": "2023-04-06T06:05:52.681552Z",
        "event_name": "Annual Function",
        "event_time": "2023-02-02",
        "event_information": "Rajkot Indira circle",
        "comments": "Open invitation"
    },
    {
        "id": 11,
        "created": "2023-04-06T06:05:52.681552Z",
        "event_name": "Annual Function",
        "event_time": "2023-02-02",
        "event_information": "Rajkot Indira circle",
        "comments": "Open invitation"
    },
    {
        "id": 12,
        "created": "2023-04-06T06:05:52.681552Z",
        "event_name": "Annual Function",
        "event_time": "2023-02-02",
        "event_information": "Rajkot Indira circle",
        "comments": "Open invitation"
    },
    {
        "id": 13,
        "created": "2023-04-06T06:05:52.681552Z",
        "event_name": "Annual function",
        "event_time": "2023-02-02",
        "event_information": "Indira circle",
        "comments": "Open invitation"
    },
    {
        "id": 14,
        "created": "2023-04-06T06:05:52.681552Z",
        "event_name": "birthday celebration",
        "event_time": "2023-07-16",
        "event_information": "wankaner",
        "comments": "open invitation"
    },
    {
        "id": 15,
        "created": "2023-04-06T06:05:52.681552Z",
        "event_name": "marriage",
        "event_time": "2023-04-13",
        "event_information": "Morbi",
        "comments": "Dress code complsary"
    },
    {
        "id": 16,
        "created": "2023-04-06T06:05:52.681552Z",
        "event_name": "Fun day",
        "event_time": "2023-04-10",
        "event_information": "solo",
        "comments": "red t-tishirt"
    },
    {
        "id": 17,
        "created": "2023-04-08T04:43:46.464612Z",
        "event_name": "Diwali function",
        "event_time": "2023-10-27",
        "event_information": "chopda poojan",
        "comments": "only family mambers"
    },
    {
        "id": 18,
        "created": "2023-04-08T04:43:46.464612Z",
        "event_name": "Diwali function",
        "event_time": "2023-10-27",
        "event_information": "chopda poojan",
        "comments": "only family mambers"
    },
    {
        "id": 19,
        "created": "2023-04-08T04:43:46.464612Z",
        "event_name": "janmanstmi",
        "event_time": "2015-05-06",
        "event_information": "white Kurt’s",
        "comments": "only student"
    }
]
def getdata(data):

    for i in data :
            print("ID:",i['id'])
            print("Time:",i['created'])
            print("event_name:",i['event_name'])
            print("event_time:",i['event_time'])
            print("event_information:",i['event_information'])
            print("comments:",i['comments'])


getdata(list1) #dict argument