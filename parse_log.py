
import json

from Log import Log

with open('log.json', 'r') as file:

    json_objects = json.load(file)


data = {
    "logs": json_objects
}

# print(data)
list_log_objects = []

for index, log in enumerate(data["logs"]):
    print(f"log {index + 1}:")
    print("whatever:", log["EventTime"])
    log_obj = Log(
        log["EventTime"],
        log["Hostname"],
        log["Keywords"],
        log["EventType"],
        log["SeverityValue"],
        log["Severity"],
        log["EventID"],
        log["SourceName"],
        log["ProviderGuid"],
        log["Version"],
        log["Task"],
        log["OpcodeValue"],
        log["RecordNumber"],
        log["ProcessID"],
        log["ThreadID"],
        log["Channel"],
        log["Domain"],
        log["AccountName"],
        log["UserID"],
        log["AccountType"],
        log["Message"],
        log["Opcode"],
        log["EventReceivedTime"],
        log["SourceModuleName"],
        log["SourceModuleType"]
    )
    list_log_objects.append(log_obj)

for obj in list_log_objects:
    print(obj.EventTime)
    print(obj.Hostname)
    print(obj.Keywords)
    print(obj.EventType)
    print(obj.SeverityValue)
    # and so on . . .
    print()




