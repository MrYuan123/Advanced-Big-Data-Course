json_schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "planCostShares",
    "linkedPlanServices",
    "_org",
    "objectId",
    "objectType",
    "planType",
    "creationDate"
  ],
  "properties": {
    "planCostShares": {
      "$id": "#/properties/planCostShares",
      "type": "object",
      "title": "The Plancostshares Schema",
      "required": [
        "deductible",
        "_org",
        "copay",
        "objectId",
        "objectType"
      ],
      "properties": {
        "deductible": {
          "$id": "#/properties/planCostShares/properties/deductible",
          "type": "integer",
          "title": "The Deductible Schema",
          "default": 0,
          "examples": [
            2000
          ]
        },
        "_org": {
          "$id": "#/properties/planCostShares/properties/_org",
          "type": "string",
          "title": "The _org Schema",
          "default": "",
          "examples": [
            "example.com"
          ],
          "pattern": "^(.*)$"
        },
        "copay": {
          "$id": "#/properties/planCostShares/properties/copay",
          "type": "integer",
          "title": "The Copay Schema",
          "default": 0,
          "examples": [
            23
          ]
        },
        "objectId": {
          "$id": "#/properties/planCostShares/properties/objectId",
          "type": "string",
          "title": "The Objectid Schema",
          "default": "",
          "examples": [
            "1234vxc2324sdf-501"
          ],
          "pattern": "^(.*)$"
        },
        "objectType": {
          "$id": "#/properties/planCostShares/properties/objectType",
          "type": "string",
          "title": "The Objecttype Schema",
          "default": "",
          "examples": [
            "membercostshare"
          ],
          "pattern": "^(.*)$"
        }
      }
    },
    "linkedPlanServices": {
      "$id": "#/properties/linkedPlanServices",
      "type": "array",
      "title": "The Linkedplanservices Schema",
      "items": {
        "$id": "#/properties/linkedPlanServices/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "linkedService",
          "planserviceCostShares",
          "_org",
          "objectId",
          "objectType"
        ],
        "properties": {
          "linkedService": {
            "$id": "#/properties/linkedPlanServices/items/properties/linkedService",
            "type": "object",
            "title": "The Linkedservice Schema",
            "required": [
              "_org",
              "objectId",
              "objectType",
              "name"
            ],
            "properties": {
              "_org": {
                "$id": "#/properties/linkedPlanServices/items/properties/linkedService/properties/_org",
                "type": "string",
                "title": "The _org Schema",
                "default": "",
                "examples": [
                  "example.com"
                ],
                "pattern": "^(.*)$"
              },
              "objectId": {
                "$id": "#/properties/linkedPlanServices/items/properties/linkedService/properties/objectId",
                "type": "string",
                "title": "The Objectid Schema",
                "default": "",
                "examples": [
                  "1234520xvc30asdf-502"
                ],
                "pattern": "^(.*)$"
              },
              "objectType": {
                "$id": "#/properties/linkedPlanServices/items/properties/linkedService/properties/objectType",
                "type": "string",
                "title": "The Objecttype Schema",
                "default": "",
                "examples": [
                  "service"
                ],
                "pattern": "^(.*)$"
              },
              "name": {
                "$id": "#/properties/linkedPlanServices/items/properties/linkedService/properties/name",
                "type": "string",
                "title": "The Name Schema",
                "default": "",
                "examples": [
                  "Yearly physical"
                ],
                "pattern": "^(.*)$"
              }
            }
          },
          "planserviceCostShares": {
            "$id": "#/properties/linkedPlanServices/items/properties/planserviceCostShares",
            "type": "object",
            "title": "The Planservicecostshares Schema",
            "required": [
              "deductible",
              "_org",
              "copay",
              "objectId",
              "objectType"
            ],
            "properties": {
              "deductible": {
                "$id": "#/properties/linkedPlanServices/items/properties/planserviceCostShares/properties/deductible",
                "type": "integer",
                "title": "The Deductible Schema",
                "default": 0,
                "examples": [
                  10
                ]
              },
              "_org": {
                "$id": "#/properties/linkedPlanServices/items/properties/planserviceCostShares/properties/_org",
                "type": "string",
                "title": "The _org Schema",
                "default": "",
                "examples": [
                  "example.com"
                ],
                "pattern": "^(.*)$"
              },
              "copay": {
                "$id": "#/properties/linkedPlanServices/items/properties/planserviceCostShares/properties/copay",
                "type": "integer",
                "title": "The Copay Schema",
                "default": 0,
                "examples": [
                  0
                ]
              },
              "objectId": {
                "$id": "#/properties/linkedPlanServices/items/properties/planserviceCostShares/properties/objectId",
                "type": "string",
                "title": "The Objectid Schema",
                "default": "",
                "examples": [
                  "1234512xvc1314asdfs-503"
                ],
                "pattern": "^(.*)$"
              },
              "objectType": {
                "$id": "#/properties/linkedPlanServices/items/properties/planserviceCostShares/properties/objectType",
                "type": "string",
                "title": "The Objecttype Schema",
                "default": "",
                "examples": [
                  "membercostshare"
                ],
                "pattern": "^(.*)$"
              }
            }
          },
          "_org": {
            "$id": "#/properties/linkedPlanServices/items/properties/_org",
            "type": "string",
            "title": "The _org Schema",
            "default": "",
            "examples": [
              "example.com"
            ],
            "pattern": "^(.*)$"
          },
          "objectId": {
            "$id": "#/properties/linkedPlanServices/items/properties/objectId",
            "type": "string",
            "title": "The Objectid Schema",
            "default": "",
            "examples": [
              "27283xvx9asdff-504"
            ],
            "pattern": "^(.*)$"
          },
          "objectType": {
            "$id": "#/properties/linkedPlanServices/items/properties/objectType",
            "type": "string",
            "title": "The Objecttype Schema",
            "default": "",
            "examples": [
              "planservice"
            ],
            "pattern": "^(.*)$"
          }
        }
      }
    },
    "_org": {
      "$id": "#/properties/_org",
      "type": "string",
      "title": "The _org Schema",
      "default": "",
      "examples": [
        "example.com"
      ],
      "pattern": "^(.*)$"
    },
    "objectId": {
      "$id": "#/properties/objectId",
      "type": "string",
      "title": "The Objectid Schema",
      "default": "",
      "examples": [
        "12xvxc345ssdsds-508"
      ],
      "pattern": "^(.*)$"
    },
    "objectType": {
      "$id": "#/properties/objectType",
      "type": "string",
      "title": "The Objecttype Schema",
      "default": "",
      "examples": [
        "plan"
      ],
      "pattern": "^(.*)$"
    },
    "planType": {
      "$id": "#/properties/planType",
      "type": "string",
      "title": "The Plantype Schema",
      "default": "",
      "examples": [
        "inNetwork"
      ],
      "pattern": "^(.*)$"
    },
    "creationDate": {
      "$id": "#/properties/creationDate",
      "type": "string",
      "title": "The Creationdate Schema",
      "default": "",
      "examples": [
        "12-12-2017"
      ],
      "pattern": "^(.*)$"
    }
  }
}

json_content = {
	"planCostShares": {
		"deductible": 2000,
		"_org": "example.com",
		"copay": 23,
		"objectId": "1234vxc2324sdf-501",
		"objectType": "membercostshare"

	},
	"linkedPlanServices": [{
		"linkedService": {
			"_org": "example.com",
			"objectId": "1234520xvc30asdf-502dsdsdsd",
			"objectType": "service",
			"name": "Yearly physical"
		},
		"planserviceCostShares": {
			"deductible": 10,
			"_org": "example.com",
			"copay": 0,
			"objectId": "1234512xvc1314asdfs-503dsdsdsds",
			"objectType": "membercostshare"
		},
		"_org": "example.com",
		"objectId": "27283xvx9asdff-504sdsdsds",
		"objectType": "planservice"
	}, {
		"linkedService": {
			"_org": "example.com",
			"objectId": "1234520xvc30sfs-505",
			"objectType": "service",
			"name": "well baby"
		},
		"planserviceCostShares": {
			"deductible": 10,
			"_org": "example.com",
			"copay": 175,
			"objectId": "1234512xvc1314sdfsd-506",
			"objectType": "membercostshare"
		},

		"_org": "example.com",

		"objectId": "27283xvx9sdf-507",
		"objectType": "planservice"
	}],

	"_org": "example.com",
	"objectId": "12xvxc345ssdsds-508",
	"objectType": "plan",
	"planType": "inNetwork",
	"creationDate": "12-12-2017"
}