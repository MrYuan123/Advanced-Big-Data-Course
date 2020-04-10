
def parser(input):
    output = []
    output.append(input);
    output.append(input["planCostShares"])
    output.append(input["linkedPlanServices"][0])
    output.append(input["linkedPlanServices"][0]["linkedService"])
    output.append(input["linkedPlanServices"][0]["planserviceCostShares"])
    output.append(input["linkedPlanServices"][1])
    output.append(input["linkedPlanServices"][1]["linkedService"])
    output.append(input["linkedPlanServices"][1]["planserviceCostShares"])

    return output


def modification(input, id, key, value):
    if input["objectId"] == id:
        input[key] = value
        return input

    if input["planCostShares"]['objectId'] == id:
        input["planCostShares"][key] = value
        return input

    if input["linkedPlanServices"][0]['objectId'] == id:
        input["linkedPlanServices"][0][key] = value
        return input

    if input["linkedPlanServices"][0]["linkedService"]['objectId'] == id:
        input["linkedPlanServices"][0]["linkedService"][key] = value
        return input

    if input["linkedPlanServices"][0]["planserviceCostShares"]['objectId'] == id:
        input["linkedPlanServices"][0]["planserviceCostShares"][key] = value
        return input

    if input["linkedPlanServices"][1]['objectId'] == id:
        input["linkedPlanServices"][1][key] = value
        return input

    if input["linkedPlanServices"][1]["linkedService"]['objectId'] == id:
        input["linkedPlanServices"][1]["linkedService"][key] = value
        return input

    if input["linkedPlanServices"][1]["planserviceCostShares"]['objectId'] == id:
        input["linkedPlanServices"][1]["planserviceCostShares"][key] = value
        return input

    return input


def findDict(input, id):
    print(input["objectId"])
    if input["objectId"] == id:
        return input

    if input["planCostShares"]['objectId'] == id:
        return input["planCostShares"]

    if input["linkedPlanServices"][0]['objectId'] == id:
        return input["linkedPlanServices"][0]

    if input["linkedPlanServices"][0]["linkedService"]['objectId'] == id:
        return input["linkedPlanServices"][0]["linkedService"]

    if input["linkedPlanServices"][0]["planserviceCostShares"]['objectId'] == id:
        return  input["linkedPlanServices"][0]["planserviceCostShares"]

    if input["linkedPlanServices"][1]['objectId'] == id: return input["linkedPlanServices"][1]

    if input["linkedPlanServices"][1]["linkedService"]['objectId'] == id:
        return input["linkedPlanServices"][1]["linkedService"]

    if input["linkedPlanServices"][1]["planserviceCostShares"]['objectId'] == id:
        return input["linkedPlanServices"][1]["planserviceCostShares"]

    return {}
