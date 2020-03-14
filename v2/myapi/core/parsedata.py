
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
