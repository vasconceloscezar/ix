/**
 * @generated SignedSource<<1649b76e79cb37ccd1bfc169eee173e7>>
 * @lightSyntaxTransform
 * @nogrep
 */

/* eslint-disable */

'use strict';

var node = (function(){
var v0 = [
  {
    "defaultValue": null,
    "kind": "LocalArgument",
    "name": "id"
  }
],
v1 = [
  {
    "alias": null,
    "args": [
      {
        "kind": "Variable",
        "name": "id",
        "variableName": "id"
      }
    ],
    "concreteType": "TaskType",
    "kind": "LinkedField",
    "name": "task",
    "plural": false,
    "selections": [
      {
        "alias": null,
        "args": null,
        "kind": "ScalarField",
        "name": "id",
        "storageKey": null
      },
      {
        "alias": null,
        "args": null,
        "kind": "ScalarField",
        "name": "isComplete",
        "storageKey": null
      },
      {
        "alias": null,
        "args": null,
        "kind": "ScalarField",
        "name": "completeAt",
        "storageKey": null
      },
      {
        "alias": null,
        "args": null,
        "concreteType": "GoalType",
        "kind": "LinkedField",
        "name": "goals",
        "plural": true,
        "selections": [
          {
            "alias": null,
            "args": null,
            "kind": "ScalarField",
            "name": "description",
            "storageKey": null
          },
          {
            "alias": null,
            "args": null,
            "kind": "ScalarField",
            "name": "complete",
            "storageKey": null
          }
        ],
        "storageKey": null
      }
    ],
    "storageKey": null
  }
];
return {
  "fragment": {
    "argumentDefinitions": (v0/*: any*/),
    "kind": "Fragment",
    "metadata": null,
    "name": "contexts_task_Query",
    "selections": (v1/*: any*/),
    "type": "Query",
    "abstractKey": null
  },
  "kind": "Request",
  "operation": {
    "argumentDefinitions": (v0/*: any*/),
    "kind": "Operation",
    "name": "contexts_task_Query",
    "selections": (v1/*: any*/)
  },
  "params": {
    "cacheID": "c0f86426550089152b13eca99e465356",
    "id": null,
    "metadata": {},
    "name": "contexts_task_Query",
    "operationKind": "query",
    "text": "query contexts_task_Query(\n  $id: ID!\n) {\n  task(id: $id) {\n    id\n    isComplete\n    completeAt\n    goals {\n      description\n      complete\n    }\n  }\n}\n"
  }
};
})();

node.hash = "7fcf897c6707d5a1e82f90ad7fe40d62";

module.exports = node;
