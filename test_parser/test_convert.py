import xmltodict, json
import pprint

pp = pprint.PrettyPrinter()

string_xml = open("api_music.xml").read()

parser = xmltodict.parse(string_xml)

rezult = json.dumps(parser)

media = json.loads(rezult)

# CONST = media['music']['Artists']['artist']
# i=0

# while True:
#     try:
#         print(CONST[i]['name'])
#         print(CONST[i]['age'])
#         print(CONST[i]['sex'])
#         print(CONST[i]['month_listeners'])
#         print('-' * 20)
#     except IndexError as e:
#         break
#     while True:
#         try:
#             print(CONST[i]['singles']['songs']['song'][j]['name'])
#             print(CONST[i]['singles']['songs']['song'][j]['duration'])
#             print(CONST[i]['singles']['songs']['song'][j]['listeners'])
#             print("-"*20)
#         except IndexError as e:
#             pass

    # print('-' * 20)
    # print(CONST[0]['albums']['album']['name'])
    # for z in range(4):
    #     print(CONST[0]['albums']['album']['songs']['song'][z]['name'])
    #     print(CONST[0]['albums']['album']['songs']['song'][z]['duration'])
    #     print(CONST[0]['albums']['album']['songs']['song'][z]['listeners'])
    #     print('-' * 20)
        # print(media['music']['Artists']['artist'][0]['albums']['album'])
